# Shadow Orchestrator: Production Self-Annealing

**Version:** 1.0
**Last Updated:** February 2026
**Framework:** DOE Phase 5 - Advanced Cloudifying

This directive provides the advanced pattern for **production self-annealing**, where deployed Modal endpoints can diagnose and fix their own errors in real-time with graduated human escalation.

---

## Objective

Create a resilient, self-healing cloud deployment that:
- Detects errors in production automatically
- Diagnoses root causes using AI agents
- Auto-fixes non-critical errors without human intervention
- Escalates critical errors to humans via stuck agent
- Continuously updates directives with production learnings
- Maintains audit trail of all self-annealing actions

---

## Architecture Overview

### The Shadow Orchestrator Pattern

```
┌─────────────────────────────────────────────────────────┐
│                     Production Flow                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  n8n Trigger                                            │
│       ↓                                                  │
│  HTTP Request → Modal Endpoint                          │
│       ↓              ↓ (success)                        │
│  n8n Action          return result                       │
│                      ↓ (error)                          │
│                 Error Classification                     │
│                      ↓                                   │
│         ┌────────────┴────────────┐                     │
│         ↓                         ↓                      │
│   Non-Critical              Critical Error               │
│         ↓                         ↓                      │
│  Agentic Support         Human Escalation                │
│    (Auto-Fix)              (Stuck Agent)                 │
│         ↓                         ↓                      │
│  Diagnose & Fix           Wait for Decision              │
│         ↓                         ↓                      │
│  Update Directive          Implement Fix                 │
│         ↓                         ↓                      │
│  Redeploy                    Update Directive            │
│         ↓                         ↓                      │
│  Retry Request                Redeploy                   │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Three-Tier Error Handling

**Tier 1: Known Errors (Auto-Fix)**
- Expected edge cases
- Input validation errors
- Rate limiting, retries
- Agentic Support handles automatically

**Tier 2: Unknown Errors (Diagnose & Decide)**
- Unexpected but non-critical
- Agentic Support diagnoses
- Decides if safe to auto-fix or escalate

**Tier 3: Critical Errors (Human-in-the-Loop)**
- Data corruption risk
- Security implications
- Business logic failures
- Always escalate to stuck agent

---

## Prerequisites

Before implementing Shadow Orchestrator:

✅ **Standard Hybrid Wrapper deployed** - Working Modal endpoint with n8n
✅ **Modal account with permissions** - Ability to deploy multiple endpoints
✅ **GitHub integration** - For automatic directive updates
✅ **Monitoring setup** - Logging and error tracking
✅ **Human escalation path** - Stuck agent available for critical errors

---

## Components

### 1. Primary Modal Endpoint (Enhanced)

Your main workflow endpoint with error classification:

```python
import modal
from fastapi import Header, HTTPException
import requests
import os

app = modal.App("workflow-with-shadow")

# Define error types
class KnownError(Exception):
    """Non-critical, can auto-fix"""
    pass

class CriticalError(Exception):
    """Requires human intervention"""
    pass

@app.function(
    image=modal.Image.debian_slim().pip_install("anthropic", "fastapi", "httpx"),
    secrets=[
        modal.Secret.from_name("api-auth-token"),
        modal.Secret.from_name("anthropic-api-key"),
        modal.Secret.from_name("agentic-support-url")
    ],
    timeout=120,
)
@modal.fastapi_endpoint(method="POST")
def process_workflow(data: dict, authorization: str = Header(None)) -> dict:
    """
    Main workflow with Shadow Orchestrator error handling.
    """
    import anthropic

    # Authentication
    expected_token = os.environ.get("API_AUTH_TOKEN")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid authorization header")

    token = authorization.replace("Bearer ", "")
    if token != expected_token:
        raise HTTPException(status_code=403, detail="Invalid authentication token")

    try:
        # Main workflow logic
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

        # Validate inputs
        if not data.get("prompt"):
            raise KnownError("Missing required field: prompt")

        # Process
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": data["prompt"]}],
            system="You are a helpful assistant."
        )

        result = message.content[0].text
        return {"result": result, "status": "success"}

    except KnownError as e:
        # Non-critical - send to Agentic Support for auto-fix
        support_url = os.environ.get("AGENTIC_SUPPORT_URL")
        requests.post(f"{support_url}/diagnose", json={
            "error_type": "known",
            "error_message": str(e),
            "context": data,
            "endpoint": "process_workflow",
            "severity": "low"
        })

        return {
            "status": "fixing",
            "message": "Error detected, auto-fixing in progress",
            "retry_in_seconds": 30
        }

    except anthropic.APIError as e:
        # API errors - check if critical
        if "rate_limit" in str(e).lower():
            # Non-critical - can retry
            raise KnownError(f"Rate limit hit: {e}")
        else:
            # Potentially critical - escalate
            raise CriticalError(f"API error: {e}")

    except CriticalError as e:
        # Critical - escalate to human immediately
        support_url = os.environ.get("AGENTIC_SUPPORT_URL")
        ticket_id = requests.post(f"{support_url}/escalate", json={
            "error_type": "critical",
            "error_message": str(e),
            "context": data,
            "endpoint": "process_workflow",
            "severity": "high",
            "requires_human": True
        }).json().get("ticket_id")

        return {
            "status": "escalated",
            "message": "Critical error - human intervention required",
            "ticket_id": ticket_id
        }

    except Exception as e:
        # Unknown error - diagnose first
        support_url = os.environ.get("AGENTIC_SUPPORT_URL")
        diagnosis = requests.post(f"{support_url}/diagnose", json={
            "error_type": "unknown",
            "error_message": str(e),
            "context": data,
            "endpoint": "process_workflow",
            "severity": "medium"
        }).json()

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
                "ticket_id": diagnosis.get("ticket_id")
            }
```

### 2. Agentic Support Endpoint

Separate Modal endpoint for error diagnosis and fixing:

```python
@app.function(
    image=modal.Image.debian_slim().pip_install(
        "anthropic",
        "fastapi",
        "httpx",
        "pygithub"  # For updating directives
    ),
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

    # Use Claude to diagnose
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    diagnosis_prompt = f"""
    You are an expert debugging agent. Analyze this production error:

    Error Type: {error_report['error_type']}
    Error Message: {error_report['error_message']}
    Context: {json.dumps(error_report['context'], indent=2)}
    Endpoint: {error_report['endpoint']}

    Provide:
    1. Root cause analysis
    2. Whether this can be safely auto-fixed (true/false)
    3. If auto-fixable, provide the exact code change needed
    4. If not, explain why human intervention is required
    5. Suggested directive update to prevent recurrence

    Respond in JSON format.
    """

    message = client.messages.create(
        model="claude-opus-4-5-20251101",  # Use Opus for complex diagnosis
        max_tokens=2000,
        messages=[{"role": "user", "content": diagnosis_prompt}],
        system="You are a precise, cautious debugging expert. Safety first."
    )

    diagnosis = json.loads(message.content[0].text)

    # Decision tree
    if error_report['severity'] == 'high' or not diagnosis['can_auto_fix']:
        # Escalate to human
        ticket_id = create_github_issue(error_report, diagnosis)
        return {
            "can_auto_fix": False,
            "ticket_id": ticket_id,
            "diagnosis": diagnosis['root_cause'],
            "action": "escalated_to_human"
        }
    else:
        # Attempt auto-fix
        fix_result = apply_fix.spawn(error_report, diagnosis)
        return {
            "can_auto_fix": True,
            "diagnosis": diagnosis['root_cause'],
            "fix_applied": diagnosis['code_change'],
            "action": "auto_fixing"
        }


@app.function(
    image=modal.Image.debian_slim().pip_install("anthropic", "pygithub"),
    secrets=[
        modal.Secret.from_name("github-token"),
        modal.Secret.from_name("anthropic-api-key")
    ],
    timeout=300,
)
def apply_fix(error_report: dict, diagnosis: dict):
    """
    Apply the fix and update directive (self-annealing).
    """
    from github import Github
    import os

    # 1. Update the directive with learnings
    g = Github(os.environ["GITHUB_TOKEN"])
    repo = g.get_repo("your-username/your-repo")

    # Read current directive
    directive_path = f"directives/{error_report['endpoint']}_directive.md"
    file = repo.get_contents(directive_path)
    current_content = file.decoded_content.decode()

    # Append learning to Self-Annealing section
    learning = f"""
### Learning: {error_report['error_message']}
**Date**: {datetime.now().isoformat()}
**Root Cause**: {diagnosis['root_cause']}
**Fix Applied**: {diagnosis['code_change']}
**Prevention**: {diagnosis['suggested_directive_update']}
"""

    updated_content = current_content + "\n" + learning

    # Commit update
    repo.update_file(
        file.path,
        f"Self-annealing: {error_report['error_message'][:50]}",
        updated_content,
        file.sha,
        branch="main"
    )

    # 2. Update and redeploy the endpoint
    # (This would trigger a CI/CD pipeline or direct Modal redeploy)
    # For now, just log that it needs redeployment

    return {
        "directive_updated": True,
        "fix_committed": True,
        "needs_redeploy": True
    }


def create_github_issue(error_report: dict, diagnosis: dict) -> str:
    """
    Create GitHub issue for human review (invokes stuck agent pattern).
    """
    from github import Github
    import os

    g = Github(os.environ["GITHUB_TOKEN"])
    repo = g.get_repo("your-username/your-repo")

    issue = repo.create_issue(
        title=f"🚨 Production Error: {error_report['error_message'][:100]}",
        body=f"""
## Critical Production Error

**Endpoint**: `{error_report['endpoint']}`
**Severity**: {error_report['severity']}
**Error Type**: {error_report['error_type']}

### Error Message
```
{error_report['error_message']}
```

### Context
```json
{json.dumps(error_report['context'], indent=2)}
```

### Diagnosis
{diagnosis['root_cause']}

### Why Human Intervention Required
{diagnosis.get('human_reason', 'Complex error requiring review')}

### Suggested Action
{diagnosis.get('suggested_directive_update', 'Review and fix manually')}

---
*Generated by Shadow Orchestrator - Agentic Support*
        """,
        labels=["production-error", "needs-human-review", "shadow-orchestrator"]
    )

    return f"ISSUE-{issue.number}"
```

### 3. Monitoring & Logging Endpoint

```python
@app.function(
    image=modal.Image.debian_slim().pip_install("fastapi"),
    secrets=[modal.Secret.from_name("api-auth-token")],
)
@modal.fastapi_endpoint(method="GET")
def health_check(authorization: str = Header(None)) -> dict:
    """
    Health check and self-annealing status.
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
        "shadow_orchestrator": "active",
        "self_annealing_count": get_annealing_count(),
        "escalations_count": get_escalation_count()
    }
```

---

## Deployment Process

### Step 1: Deploy Primary Endpoint

1. Deploy your main workflow endpoint with error classification
2. Set environment variables:
   ```bash
   modal secret create agentic-support-url AGENTIC_SUPPORT_URL=https://your-profile--workflow-diagnose.modal.run
   ```

### Step 2: Deploy Agentic Support

1. Deploy the `diagnose` and `apply_fix` functions
2. Set GitHub token for directive updates:
   ```bash
   modal secret create github-token GITHUB_TOKEN=ghp_xxxx
   ```

### Step 3: Configure Error Classification

In your main endpoint, define error types:

```python
# Non-critical (auto-fix)
KNOWN_ERRORS = [
    "Missing required field",
    "Rate limit exceeded",
    "Timeout error",
    "Invalid input format"
]

# Critical (escalate)
CRITICAL_ERRORS = [
    "Database corruption",
    "Security breach",
    "Data loss",
    "Authentication failure"
]
```

### Step 4: Test Self-Annealing

1. Trigger a known error
2. Verify Agentic Support diagnoses it
3. Check directive is updated
4. Confirm error doesn't recur

### Step 5: Monitor & Iterate

1. Watch GitHub issues for escalations
2. Review self-annealing logs
3. Adjust error classification as needed
4. Update directives with production learnings

---

## Error Classification Guidelines

### Auto-Fix Criteria

An error CAN be auto-fixed if:
- ✅ Root cause is clear and understood
- ✅ Fix doesn't affect other functionality
- ✅ No data corruption risk
- ✅ No security implications
- ✅ Similar errors have been fixed before
- ✅ Can be validated automatically

### Escalation Criteria

An error MUST be escalated if:
- ❌ Root cause is unclear
- ❌ Fix might break other features
- ❌ Risk of data corruption or loss
- ❌ Security implications
- ❌ Business logic decision required
- ❌ Affects multiple endpoints

---

## Graduated Response Strategy

**Level 1: Immediate Auto-Fix**
- Known errors with proven fixes
- No risk, high confidence
- Example: Input validation, rate limiting

**Level 2: Diagnose then Decide**
- Unknown but non-critical errors
- Agentic Support analyzes first
- Auto-fix if safe, else escalate

**Level 3: Immediate Escalation**
- Critical errors
- Always human-in-the-loop
- Create GitHub issue, notify team

---

## Self-Annealing Workflow

```
1. Error occurs in production
   ↓
2. Error is classified (Known/Unknown/Critical)
   ↓
3. Agentic Support diagnoses
   ↓
4. Decision tree:
   - Can auto-fix? → Apply fix → Update directive → Redeploy
   - Need human? → Create GitHub issue → Wait for human → Apply fix
   ↓
5. Directive updated with learning
   ↓
6. System is more resilient (battle-hardened)
```

---

## Audit Trail

Every self-annealing action creates:

1. **GitHub Commit** - Directive update with learning
2. **GitHub Issue** - For escalations (if needed)
3. **Log Entry** - Timestamp, error, fix, outcome
4. **Metrics** - Auto-fix success rate, escalation rate

---

## Safety Mechanisms

**1. Rate Limiting**
- Max 5 auto-fixes per hour per endpoint
- Prevents cascading failures

**2. Rollback Capability**
- Keep last 3 working versions
- Auto-rollback if new version fails

**3. Human Override**
- Emergency stop via environment variable
- `DISABLE_AUTO_FIX=true`

**4. Audit Review**
- Weekly review of all auto-fixes
- Monthly review of error patterns

---

## Definition of Done

✅ Primary endpoint deployed with error classification
✅ Agentic Support endpoint deployed
✅ GitHub integration configured
✅ Error types properly classified
✅ Test errors trigger appropriate responses
✅ Directive updates working automatically
✅ Escalation path tested
✅ Monitoring and logging active
✅ Audit trail functioning
✅ Safety mechanisms in place

---

## Monitoring & Metrics

**Key Metrics:**
- Auto-fix success rate (target: >95%)
- Escalation rate (target: <5%)
- Mean time to fix (target: <5 minutes)
- Recurrence rate (target: <1%)

**Alerts:**
- Auto-fix failure (immediate)
- Critical error escalation (immediate)
- Auto-fix rate > 10/hour (warning)

---

## When to Use Shadow Orchestrator

**Use for:**
- ✅ High-volume production workflows
- ✅ Mission-critical applications
- ✅ Long-running deployments
- ✅ Workflows with evolving requirements

**Don't use for:**
- ❌ Initial deployments (battle-test first)
- ❌ Low-volume workflows
- ❌ Prototypes or experiments
- ❌ Ultra-critical systems where any automation is risky

---

## Comparison: Standard vs. Shadow Orchestrator

| Aspect | Standard Hybrid Wrapper | Shadow Orchestrator |
|--------|------------------------|---------------------|
| **Self-Annealing** | Local only (Phase 3-4) | Production + Local |
| **Error Handling** | Return error to n8n | Auto-fix or escalate |
| **Complexity** | Low | High |
| **Risk** | Low (static code) | Medium (auto-fixes) |
| **Learning** | Manual updates | Automatic updates |
| **Best For** | Most client handoffs | Mission-critical systems |

---

## Next Steps

1. **Start with Standard Hybrid Wrapper** - Battle-test your workflow
2. **Monitor Production** - Collect error patterns for 2-4 weeks
3. **Classify Errors** - Determine which can be auto-fixed
4. **Deploy Shadow Orchestrator** - Add self-annealing capability
5. **Iterate** - Refine error classification based on results

---

## Related Files

- `directives/hybrid-wrapper-deployment.md` - Standard deployment workflow
- `.claude/agents/deployer.md` - Deployer subagent
- `.claude/agents/support.md` - Agentic Support agent
- `.claude/CLAUDE.md` - Phase 5 deployment strategies

---

**The Shadow Orchestrator transforms your deployed workflows from static code into living, learning systems that improve themselves over time! 🚀**
