"""
Shadow Orchestrator Modal Template
Production self-annealing endpoint with error classification and auto-fixing.

This template shows how to implement the Shadow Orchestrator pattern for
endpoints that can diagnose and fix their own errors in production.
"""

import modal
from fastapi import Header, HTTPException
import requests
import os
from datetime import datetime

app = modal.App("shadow-orchestrator-workflow")

# Define your dependencies
image = modal.Image.debian_slim().pip_install(
    "anthropic",
    "fastapi",
    "httpx"
)

# =============================================================================
# CUSTOM ERROR TYPES
# =============================================================================

class KnownError(Exception):
    """Non-critical error that can be auto-fixed by Agentic Support."""
    pass

class CriticalError(Exception):
    """Critical error that requires immediate human intervention."""
    pass


# =============================================================================
# PRIMARY ENDPOINT (Your Workflow Logic)
# =============================================================================

@app.function(
    image=image,
    secrets=[
        modal.Secret.from_name("anthropic-api-key"),
        modal.Secret.from_name("api-auth-token"),
        modal.Secret.from_name("agentic-support-url")  # URL to Agentic Support endpoint
    ],
    timeout=120,
)
@modal.fastapi_endpoint(method="POST")
def process_workflow(data: dict, authorization: str = Header(None)) -> dict:
    """
    Main workflow endpoint with Shadow Orchestrator error handling.

    Input: {"prompt": "Your input here", ...}
    Output: {"result": "Processed output", "status": "success"}
    """
    import anthropic

    # =========================================================================
    # AUTHENTICATION
    # =========================================================================
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

    # =========================================================================
    # MAIN WORKFLOW WITH ERROR CLASSIFICATION
    # =========================================================================
    try:
        # ---------------------------------------------------------------------
        # INPUT VALIDATION (use KnownError for validation failures)
        # ---------------------------------------------------------------------
        if not data.get("prompt"):
            raise KnownError("Missing required field: prompt")

        if len(data.get("prompt", "")) > 10000:
            raise KnownError("Prompt exceeds maximum length of 10000 characters")

        # ---------------------------------------------------------------------
        # YOUR WORKFLOW LOGIC HERE
        # ---------------------------------------------------------------------
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": data["prompt"]}],
            system="You are a helpful assistant."
        )

        result = message.content[0].text

        # Return success response
        return {
            "result": result,
            "status": "success",
            "timestamp": datetime.now().isoformat()
        }

    # =========================================================================
    # TIER 1: KNOWN ERRORS (Auto-Fix)
    # =========================================================================
    except KnownError as e:
        # Non-critical - send to Agentic Support for auto-fix
        support_url = os.environ.get("AGENTIC_SUPPORT_URL")

        try:
            requests.post(f"{support_url}/diagnose", json={
                "error_type": "known",
                "error_message": str(e),
                "context": data,
                "endpoint": "process_workflow",
                "severity": "low",
                "timestamp": datetime.now().isoformat()
            }, timeout=5)
        except:
            # If Agentic Support is down, just log and return error
            pass

        return {
            "status": "fixing",
            "message": "Error detected, auto-fixing in progress",
            "error": str(e),
            "retry_in_seconds": 30
        }

    # =========================================================================
    # TIER 2: API ERRORS (Diagnose & Decide)
    # =========================================================================
    except anthropic.APIError as e:
        # Check if it's a known API error pattern
        error_str = str(e).lower()

        if "rate_limit" in error_str or "429" in error_str:
            # Rate limiting - can be auto-fixed with retry logic
            raise KnownError(f"Rate limit exceeded: {e}")

        elif "timeout" in error_str or "timed out" in error_str:
            # Timeout - can be auto-fixed by increasing timeout
            raise KnownError(f"Request timeout: {e}")

        elif "authentication" in error_str or "401" in error_str:
            # Auth error - critical, needs human review
            raise CriticalError(f"Authentication failed: {e}")

        else:
            # Unknown API error - send to Agentic Support for diagnosis
            support_url = os.environ.get("AGENTIC_SUPPORT_URL")

            diagnosis = requests.post(f"{support_url}/diagnose", json={
                "error_type": "unknown",
                "error_message": str(e),
                "context": data,
                "endpoint": "process_workflow",
                "severity": "medium",
                "timestamp": datetime.now().isoformat()
            }, timeout=10).json()

            if diagnosis.get("can_auto_fix"):
                return {
                    "status": "diagnosing",
                    "message": "Unknown error - diagnosing and fixing",
                    "retry_in_seconds": 60
                }
            else:
                return {
                    "status": "escalated",
                    "message": "Complex error - human review required",
                    "ticket_id": diagnosis.get("ticket_id"),
                    "error": str(e)
                }

    # =========================================================================
    # TIER 3: CRITICAL ERRORS (Immediate Escalation)
    # =========================================================================
    except CriticalError as e:
        # Critical - escalate to human immediately via stuck agent
        support_url = os.environ.get("AGENTIC_SUPPORT_URL")

        response = requests.post(f"{support_url}/escalate", json={
            "error_type": "critical",
            "error_message": str(e),
            "context": data,
            "endpoint": "process_workflow",
            "severity": "high",
            "requires_human": True,
            "timestamp": datetime.now().isoformat()
        }, timeout=10)

        ticket_id = response.json().get("ticket_id", "UNKNOWN")

        return {
            "status": "escalated",
            "message": "Critical error - human intervention required",
            "ticket_id": ticket_id,
            "error": str(e)
        }

    # =========================================================================
    # CATCH-ALL: UNKNOWN EXCEPTIONS
    # =========================================================================
    except Exception as e:
        # Truly unknown error - be conservative, escalate
        support_url = os.environ.get("AGENTIC_SUPPORT_URL")

        try:
            diagnosis = requests.post(f"{support_url}/diagnose", json={
                "error_type": "unknown",
                "error_message": str(e),
                "context": data,
                "endpoint": "process_workflow",
                "severity": "medium",
                "timestamp": datetime.now().isoformat()
            }, timeout=10).json()

            if diagnosis.get("can_auto_fix"):
                return {
                    "status": "diagnosing",
                    "message": "Unexpected error - attempting diagnosis",
                    "retry_in_seconds": 60
                }
            else:
                return {
                    "status": "escalated",
                    "message": "Unexpected error - needs investigation",
                    "ticket_id": diagnosis.get("ticket_id"),
                    "error": str(e)
                }
        except:
            # Agentic Support is down or errored - fail gracefully
            return {
                "status": "failed",
                "message": "Service unavailable - please try again later",
                "error": "An unexpected error occurred",
                "support_contact": "support@example.com"
            }


# =============================================================================
# AGENTIC SUPPORT ENDPOINT (Error Diagnosis & Auto-Fixing)
# =============================================================================

support_image = modal.Image.debian_slim().pip_install(
    "anthropic",
    "fastapi",
    "httpx",
    "pygithub"  # For updating directives in GitHub
)

@app.function(
    image=support_image,
    secrets=[
        modal.Secret.from_name("anthropic-api-key"),
        modal.Secret.from_name("github-token"),
        modal.Secret.from_name("api-auth-token")
    ],
    timeout=300,
)
@modal.fastapi_endpoint(method="POST")
def diagnose(error_report: dict, authorization: str = Header(None)) -> dict:
    """
    Agentic Support: Diagnose errors and decide on fix strategy.

    Input: error_report dict with error_type, error_message, context, etc.
    Output: diagnosis with can_auto_fix decision and fix strategy
    """
    import anthropic
    import json

    # Authentication
    expected_token = os.environ.get("API_AUTH_TOKEN")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")

    token = authorization.replace("Bearer ", "")
    if token != expected_token:
        raise HTTPException(status_code=403, detail="Forbidden")

    # Use Claude Opus for complex diagnosis
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    diagnosis_prompt = f"""
You are an expert debugging agent analyzing a production error.

Error Type: {error_report['error_type']}
Error Message: {error_report['error_message']}
Context: {json.dumps(error_report.get('context', {}), indent=2)}
Endpoint: {error_report['endpoint']}
Severity: {error_report.get('severity', 'unknown')}

Analyze this error and provide:
1. Root cause analysis (what actually went wrong)
2. Can this be safely auto-fixed? (true/false)
3. If auto-fixable, provide exact code change needed
4. If not, explain why human intervention is required
5. Suggested directive update to prevent recurrence
6. Risk assessment (low/medium/high)

Respond in JSON format with these exact keys:
{{
  "root_cause": "explanation",
  "can_auto_fix": true/false,
  "confidence": "high|medium|low",
  "code_change": "exact fix if applicable",
  "human_reason": "why human needed if applicable",
  "directive_update": "learning to document",
  "risk_assessment": "low|medium|high"
}}

Be conservative: when in doubt, say can_auto_fix: false.
"""

    message = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=2000,
        messages=[{"role": "user", "content": diagnosis_prompt}],
        system="You are a precise, cautious debugging expert. Safety first. Never auto-fix if there's any doubt."
    )

    try:
        diagnosis = json.loads(message.content[0].text)
    except:
        # If Claude's response isn't valid JSON, be conservative
        diagnosis = {
            "root_cause": "Unable to parse diagnosis",
            "can_auto_fix": False,
            "confidence": "low",
            "human_reason": "Diagnosis parsing failed",
            "risk_assessment": "high"
        }

    # Decision tree: when to escalate
    should_escalate = (
        error_report.get('severity') == 'high' or
        not diagnosis.get('can_auto_fix') or
        diagnosis.get('confidence') == 'low' or
        diagnosis.get('risk_assessment') == 'high'
    )

    if should_escalate:
        # Create GitHub issue for human review
        ticket_id = create_github_issue(error_report, diagnosis)

        return {
            "can_auto_fix": False,
            "ticket_id": ticket_id,
            "diagnosis": diagnosis.get('root_cause'),
            "action": "escalated_to_human",
            "reason": diagnosis.get('human_reason', 'Safety check - needs human review')
        }
    else:
        # Auto-fix path
        # In production, this would trigger apply_fix() function
        # For now, just return the fix strategy
        return {
            "can_auto_fix": True,
            "diagnosis": diagnosis.get('root_cause'),
            "fix_strategy": diagnosis.get('code_change'),
            "action": "auto_fixing",
            "confidence": diagnosis.get('confidence')
        }


@app.function(
    image=support_image,
    secrets=[modal.Secret.from_name("github-token")],
    timeout=300,
)
def create_github_issue(error_report: dict, diagnosis: dict) -> str:
    """
    Create GitHub issue for human review (invokes stuck agent pattern).

    Returns: ticket_id (e.g., "ISSUE-123")
    """
    from github import Github
    import json

    g = Github(os.environ["GITHUB_TOKEN"])
    # TODO: Replace with your actual repository
    repo = g.get_repo("your-username/your-repo")

    issue = repo.create_issue(
        title=f"🚨 Production Error: {error_report['error_message'][:100]}",
        body=f"""
## Critical Production Error

**Endpoint**: `{error_report['endpoint']}`
**Severity**: {error_report.get('severity', 'unknown')}
**Error Type**: {error_report['error_type']}
**Timestamp**: {error_report.get('timestamp', 'unknown')}

### Error Message
```
{error_report['error_message']}
```

### Context
```json
{json.dumps(error_report.get('context', {}), indent=2)}
```

### Diagnosis
{diagnosis.get('root_cause', 'No diagnosis available')}

### Why Human Intervention Required
{diagnosis.get('human_reason', 'Requires manual review')}

### Suggested Action
{diagnosis.get('directive_update', 'Review and fix manually')}

### Risk Assessment
{diagnosis.get('risk_assessment', 'unknown')}

---
*Generated by Shadow Orchestrator - Agentic Support*
*This issue represents a production error that requires human review*
        """,
        labels=["production-error", "needs-human-review", "shadow-orchestrator"]
    )

    return f"ISSUE-{issue.number}"


# =============================================================================
# HEALTH CHECK & MONITORING
# =============================================================================

@app.function(
    image=modal.Image.debian_slim().pip_install("fastapi"),
    secrets=[modal.Secret.from_name("api-auth-token")],
)
@modal.fastapi_endpoint(method="GET")
def health_check(authorization: str = Header(None)) -> dict:
    """
    Health check and Shadow Orchestrator status.
    """
    # Authentication
    expected_token = os.environ.get("API_AUTH_TOKEN")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")

    token = authorization.replace("Bearer ", "")
    if token != expected_token:
        raise HTTPException(status_code=403, detail="Forbidden")

    return {
        "status": "healthy",
        "version": "1.0.0",
        "pattern": "shadow-orchestrator",
        "self_annealing": "active",
        "timestamp": datetime.now().isoformat()
    }


# =============================================================================
# DEPLOYMENT INSTRUCTIONS
# =============================================================================
"""
To deploy this Shadow Orchestrator endpoint:

1. Set up Modal secrets:
   modal secret create api-auth-token API_AUTH_TOKEN=$(openssl rand -hex 32)
   modal secret create anthropic-api-key ANTHROPIC_API_KEY=sk-ant-xxx
   modal secret create github-token GITHUB_TOKEN=ghp_xxx

2. Deploy to Modal:
   modal deploy shadow_orchestrator_template.py

3. Get the endpoint URLs and set agentic-support-url:
   modal secret create agentic-support-url AGENTIC_SUPPORT_URL=https://your-profile--diagnose.modal.run

4. Update the GitHub repo name in create_github_issue()

5. Test with cURL:
   curl -X POST "https://your-profile--process-workflow.modal.run" \\
     -H "Content-Type: application/json" \\
     -H "Authorization: Bearer YOUR_TOKEN" \\
     -d '{"prompt": "test"}'

6. Monitor GitHub issues for escalations

For full documentation, see: directives/shadow-orchestrator.md
"""
