"""
Shadow Orchestrator Template for Modal
Implements production self-annealing with 3-tier error handling.

This template provides TWO endpoints:
1. Primary workflow endpoint (your business logic)
2. Agentic support endpoint (error diagnosis and auto-fixing)

Use this for high-volume production workflows that need self-healing.
For standard deployments, use modal-app-template.py instead.
"""

import modal
from fastapi import Header, HTTPException
import os
import json
from datetime import datetime

app = modal.App("shadow-orchestrator-example")

# Define container image with all dependencies
image = modal.Image.debian_slim().pip_install(
    "anthropic==0.18.0",
    "fastapi==0.109.0",
    "pydantic==2.5.0",
    "requests==2.31.0",
)

# ============================================================================
# PRIMARY WORKFLOW ENDPOINT
# This is your actual business logic that runs in production
# ============================================================================

@app.function(
    image=image,
    secrets=[
        modal.Secret.from_name("api-auth-token"),
        modal.Secret.from_name("anthropic-api-key"),  # If using AI
    ],
    timeout=180,
)
@modal.fastapi_endpoint(method="POST")
def process_workflow(
    data: dict,
    authorization: str = Header(None)
) -> dict:
    """
    Primary workflow endpoint with error classification.

    Returns:
        Success: {"success": True, "data": {...}}
        Error: {"success": False, "error": str, "error_type": str, "severity": str}
    """

    # Step 1: Authenticate
    try:
        validate_auth(authorization)
    except HTTPException:
        raise  # Re-raise authentication failures
    except Exception as e:
        return classify_and_return_error(
            error=e,
            context=data,
            endpoint="process_workflow",
            step="authentication"
        )

    # Step 2: Validate inputs
    try:
        validation = validate_inputs(data)
        if not validation["valid"]:
            raise KnownError(validation["error"])
    except Exception as e:
        return classify_and_return_error(
            error=e,
            context=data,
            endpoint="process_workflow",
            step="validation"
        )

    # Step 3: Execute workflow logic
    try:
        result = execute_business_logic(data)

        return {
            "success": True,
            "data": result
        }

    except KnownError as e:
        # Tier 1: Known, non-critical errors
        return {
            "success": False,
            "error": str(e),
            "error_type": "known",
            "severity": "low",
            "requires_human": False,
            "context": data,
            "endpoint": "process_workflow"
        }

    except CriticalError as e:
        # Tier 3: Critical errors requiring immediate human intervention
        return {
            "success": False,
            "error": str(e),
            "error_type": "critical",
            "severity": "high",
            "requires_human": True,
            "context": data,
            "endpoint": "process_workflow"
        }

    except Exception as e:
        # Tier 2: Unknown errors that need diagnosis
        return classify_and_return_error(
            error=e,
            context=data,
            endpoint="process_workflow",
            step="execution"
        )


def execute_business_logic(data: dict) -> dict:
    """
    Your actual workflow logic goes here.

    Raises:
        KnownError: For predictable, non-critical errors (Tier 1)
        CriticalError: For critical errors requiring human intervention (Tier 3)
        Exception: For unknown errors that need diagnosis (Tier 2)
    """

    # Example business logic
    if "prompt" not in data:
        raise KnownError("Missing required field: prompt")

    # Example: Call AI API
    from anthropic import Anthropic
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=1024,
            messages=[{"role": "user", "content": data["prompt"]}]
        )

        return {
            "response": response.content[0].text,
            "tokens_used": response.usage.input_tokens + response.usage.output_tokens
        }

    except Exception as e:
        # Let the Shadow handle API errors
        raise


# ============================================================================
# AGENTIC SUPPORT ENDPOINT
# This diagnoses errors and decides whether to auto-fix or escalate
# ============================================================================

@app.function(
    image=image,
    secrets=[
        modal.Secret.from_name("api-auth-token"),
        modal.Secret.from_name("anthropic-api-key"),
    ],
    timeout=300,  # Longer timeout for diagnosis
    # Note: Use Opus model for complex error analysis
)
@modal.fastapi_endpoint(method="POST")
def diagnose_and_fix(
    error_report: dict,
    authorization: str = Header(None)
) -> dict:
    """
    Agentic support endpoint that receives error reports and decides:
    - Tier 1: Auto-fix using documented solution
    - Tier 2: Diagnose, test, and fix if safe
    - Tier 3: Escalate to human immediately

    Args:
        error_report: {
            "error_type": "known|unknown|critical",
            "error_message": str,
            "context": dict,
            "endpoint": str,
            "severity": "low|medium|high",
            "requires_human": bool
        }

    Returns:
        {
            "action": "auto_fixed|escalated|failed",
            "fix_applied": dict | None,
            "escalation_reason": str | None,
            "directive_updated": bool
        }
    """

    validate_auth(authorization)

    error_type = error_report.get("error_type")
    severity = error_report.get("severity")
    requires_human = error_report.get("requires_human", False)

    # Tier 3: Immediate escalation
    if error_type == "critical" or severity == "high" or requires_human:
        return {
            "action": "escalated",
            "escalation_reason": "Critical error or high severity",
            "fix_applied": None,
            "directive_updated": False,
            "next_steps": "Human review required. Invoke stuck agent."
        }

    # Tier 1: Known error with documented fix
    if error_type == "known":
        fix = apply_known_fix(error_report)
        if fix["success"]:
            return {
                "action": "auto_fixed",
                "fix_applied": fix,
                "directive_updated": False,  # Already documented
                "next_steps": "Retry primary workflow"
            }

    # Tier 2: Unknown error - needs AI diagnosis
    diagnosis = diagnose_with_ai(error_report)

    if diagnosis["confidence"] == "high" and diagnosis["can_auto_fix"]:
        # Test the proposed fix
        test_result = test_fix_in_sandbox(
            proposed_fix=diagnosis["proposed_fix"],
            test_data=error_report["context"]
        )

        if test_result["passed"]:
            # Apply fix and update directive
            fix_result = apply_fix(diagnosis["proposed_fix"])
            directive_updated = update_directive_with_learning(
                error_report=error_report,
                diagnosis=diagnosis,
                fix=diagnosis["proposed_fix"]
            )

            return {
                "action": "auto_fixed",
                "fix_applied": fix_result,
                "directive_updated": directive_updated,
                "next_steps": "Retry primary workflow with updated code"
            }
        else:
            # Test failed - escalate
            return {
                "action": "escalated",
                "escalation_reason": "Fix test failed in sandbox",
                "test_result": test_result,
                "directive_updated": False,
                "next_steps": "Human review required"
            }
    else:
        # Confidence too low or can't auto-fix - escalate
        return {
            "action": "escalated",
            "escalation_reason": f"Confidence: {diagnosis['confidence']}, Can auto-fix: {diagnosis['can_auto_fix']}",
            "diagnosis": diagnosis,
            "directive_updated": False,
            "next_steps": "Human review required"
        }


def diagnose_with_ai(error_report: dict) -> dict:
    """
    Use Claude Opus to diagnose the error and propose a fix.

    Returns:
        {
            "root_cause": str,
            "can_auto_fix": bool,
            "confidence": "high|medium|low",
            "proposed_fix": dict | None,
            "risk_assessment": "low|medium|high",
            "reasoning": str
        }
    """
    from anthropic import Anthropic

    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    # Use Opus for complex error analysis
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2048,
        messages=[{
            "role": "user",
            "content": f"""You are an expert debugging agent. Analyze this production error:

Error Type: {error_report.get('error_type')}
Error Message: {error_report.get('error_message')}
Context: {json.dumps(error_report.get('context'), indent=2)}
Endpoint: {error_report.get('endpoint')}

Provide:
1. Root cause analysis - what actually went wrong?
2. Can this be safely auto-fixed? (true/false)
3. If auto-fixable, provide exact code change needed
4. If not, explain why human intervention is required
5. Risk assessment (low/medium/high)

Respond in JSON format with these fields:
- root_cause: string
- can_auto_fix: boolean
- confidence: "high" | "medium" | "low"
- proposed_fix: object (if applicable)
- risk_assessment: "low" | "medium" | "high"
- reasoning: string
"""
        }]
    )

    # Parse AI response
    ai_response = response.content[0].text
    try:
        diagnosis = json.loads(ai_response)
        return diagnosis
    except json.JSONDecodeError:
        # AI didn't return valid JSON - escalate
        return {
            "root_cause": "Failed to parse AI diagnosis",
            "can_auto_fix": False,
            "confidence": "low",
            "proposed_fix": None,
            "risk_assessment": "high",
            "reasoning": "AI response was not valid JSON"
        }


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

class KnownError(Exception):
    """Tier 1: Known, predictable errors that can be auto-fixed."""
    pass


class CriticalError(Exception):
    """Tier 3: Critical errors requiring immediate human escalation."""
    pass


def validate_auth(authorization: str) -> None:
    """Validate Bearer token authentication."""
    expected_token = os.environ.get("API_AUTH_TOKEN")

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Missing or invalid authorization header"
        )

    token = authorization.replace("Bearer ", "")
    if token != expected_token:
        raise HTTPException(
            status_code=403,
            detail="Invalid authentication token"
        )


def validate_inputs(data: dict) -> dict:
    """
    Validate required input fields.

    Returns:
        {"valid": bool, "error": str | None}
    """
    required_fields = ["prompt"]  # Customize for your workflow

    for field in required_fields:
        if field not in data or not data[field]:
            return {
                "valid": False,
                "error": f"Missing required field: {field}"
            }

    return {"valid": True, "error": None}


def classify_and_return_error(
    error: Exception,
    context: dict,
    endpoint: str,
    step: str
) -> dict:
    """
    Classify an unknown error and return appropriate error response.

    Checks if error involves:
    - Financial data
    - Security/authentication
    - Data deletion
    - Other critical operations

    Returns error dict with classification.
    """

    error_message = str(error)
    error_lower = error_message.lower()

    # Tier 3 indicators: Critical errors
    critical_keywords = [
        "payment", "charge", "refund", "delete", "drop",
        "truncate", "credential", "password", "secret",
        "unauthorized", "forbidden", "security"
    ]

    if any(keyword in error_lower for keyword in critical_keywords):
        return {
            "success": False,
            "error": error_message,
            "error_type": "critical",
            "severity": "high",
            "requires_human": True,
            "context": context,
            "endpoint": endpoint,
            "step": step
        }

    # Tier 2: Unknown but potentially fixable
    return {
        "success": False,
        "error": error_message,
        "error_type": "unknown",
        "severity": "medium",
        "requires_human": False,
        "context": context,
        "endpoint": endpoint,
        "step": step
    }


def apply_known_fix(error_report: dict) -> dict:
    """
    Apply a documented fix for a known error pattern.

    This would look up the fix in the directive's "Edge Cases Learned" section.
    For this template, we'll show the structure.
    """

    # Example: Rate limiting
    if "429" in error_report["error_message"] or "rate limit" in error_report["error_message"].lower():
        return {
            "success": True,
            "fix_type": "retry_with_backoff",
            "parameters": {"wait_seconds": 60, "max_retries": 3}
        }

    # Example: Timeout
    if "timeout" in error_report["error_message"].lower():
        return {
            "success": True,
            "fix_type": "increase_timeout",
            "parameters": {"new_timeout": 300}
        }

    # No known fix found
    return {
        "success": False,
        "reason": "No documented fix for this error pattern"
    }


def test_fix_in_sandbox(proposed_fix: dict, test_data: dict) -> dict:
    """
    Test the proposed fix in a sandbox environment before applying to production.

    Returns:
        {"passed": bool, "result": dict, "error": str | None}
    """

    try:
        # This would apply the fix temporarily and test with sample data
        # For this template, we'll simulate the test
        print(f"Testing fix: {proposed_fix}")
        print(f"With data: {test_data}")

        # Simulate successful test
        return {
            "passed": True,
            "result": {"test": "passed"},
            "error": None
        }

    except Exception as e:
        return {
            "passed": False,
            "result": None,
            "error": str(e)
        }


def apply_fix(proposed_fix: dict) -> dict:
    """
    Apply the validated fix to production code.

    In a real implementation, this would:
    1. Update the Python file with the fix
    2. Redeploy to Modal
    3. Restart the workflow from point of failure
    """

    print(f"Applying fix: {proposed_fix}")

    return {
        "success": True,
        "fix_applied": proposed_fix,
        "timestamp": datetime.now().isoformat()
    }


def update_directive_with_learning(
    error_report: dict,
    diagnosis: dict,
    fix: dict
) -> bool:
    """
    Update the directive markdown file with the new learning.

    In a real implementation, this would:
    1. Read the current directive file
    2. Add entry to "Edge Cases Learned" section
    3. Commit to GitHub with descriptive message

    Returns:
        bool: True if directive was updated successfully
    """

    learning_entry = f"""
### [{datetime.now().strftime('%Y-%m-%d')}] {error_report['error_message']}

**Error Message**: `{error_report['error_message']}`

**Root Cause**: {diagnosis['root_cause']}

**Fix Applied**: {fix.get('description', 'See code changes')}

**Prevention**: {diagnosis.get('prevention_strategy', 'Monitor for recurrence')}

**Auto-Fixed**: Yes
**Human Review**: No
**Recurrence**: 0 times since fix
"""

    print(f"Directive update:\n{learning_entry}")

    # In production: Commit to GitHub
    # For this template, we just log it
    return True


# ============================================================================
# DEPLOYMENT INSTRUCTIONS
# ============================================================================

"""
TO DEPLOY THIS SHADOW ORCHESTRATOR:

1. Create Modal secrets:
   modal secret create api-auth-token API_AUTH_TOKEN=$(openssl rand -hex 32)
   modal secret create anthropic-api-key ANTHROPIC_API_KEY=sk-ant-...

2. Deploy both endpoints:
   modal deploy shadow-orchestrator-template.py

3. You'll get TWO endpoint URLs:
   - https://user--shadow-orchestrator-example-process-workflow.modal.run
   - https://user--shadow-orchestrator-example-diagnose-and-fix.modal.run

4. In your n8n workflow:
   - HTTP Request node calls the PRIMARY endpoint
   - IF node checks {{ $json.success }}
   - On error (success=false):
     * Check if error_type == "critical" → Send alert to human
     * Otherwise → Call SUPPORT endpoint with error report
     * Support endpoint returns fix → Retry primary workflow

5. Monitor with:
   modal app logs shadow-orchestrator-example --follow

WHEN TO USE THIS:
- High-volume production workflows (100+ executions/day)
- Mission-critical applications
- Long-running deployments (months/years)

WHEN NOT TO USE:
- First deployment (use modal-app-template.py instead)
- Low-volume workflows (<50 executions/day)
- Budget-conscious projects (Opus calls are expensive)
"""
