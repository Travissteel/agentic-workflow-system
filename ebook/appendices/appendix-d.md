# Appendix D: Modal Deployment Checklist

**Status**: Complete
**Version**: 1.0
**Last Updated**: February 2026

---

## Introduction

This appendix provides a comprehensive pre-flight checklist for deploying workflows to Modal as part of Phase 5 (Cloudifying) in the DOE framework.

### What This Appendix Is

Think of this as your deployment safety checklist—the pilot's pre-flight protocol before taking your workflow from local development to production cloud deployment. This checklist covers every critical step from Modal account setup through successful client handoff using the Hybrid Wrapper Strategy.

Unlike troubleshooting documentation that you consult after something breaks, this is a preventative tool. Work through it systematically before every deployment, and you'll catch 90% of potential issues before they become production problems.

### Why It Matters

Modal deployment failures fall into predictable patterns:
- Authentication misconfiguration (401 errors that break n8n workflows)
- Missing dependencies (imports that work locally but fail in the cloud)
- Untested edge cases (workflows that break on unusual inputs)
- Documentation gaps (clients can't maintain what they don't understand)

Each checked box on this list represents a potential failure mode you've actively prevented. The 10 minutes you spend on this checklist saves hours of production firefighting and protects client relationships.

### When to Use This Checklist

Use this checklist at three critical moments:

1. **Before your first deployment** (work through it with the instructor/mentor)
2. **Before every subsequent deployment** (even if you think you remember everything)
3. **When deployment fails** (work backwards to find what you missed)

The most experienced developers still use checklists. They don't trust their memory—they trust their process.

### How This Fits the DOE Framework

This checklist operationalizes Chapter 10 (Phase 5: Cloudifying) and Chapter 18 (Hybrid Wrapper Strategy). You've built your workflow locally (Phase 3), tested it thoroughly (Phase 4), and now you're ready to make it autonomous and client-accessible.

The checklist follows the natural progression:
- **Phase 1-2**: Environment setup and Modal configuration
- **Phase 3**: Code preparation with proper structure
- **Phase 4**: Testing both locally and in Modal
- **Phase 5**: n8n integration (the "wrapper" in Hybrid Wrapper)
- **Phase 6**: Documentation and handover

By the time you reach the final "Go-Live" section, you'll have confidence that your deployment will succeed because you've systematically validated every dependency.

### Standard vs. Shadow Orchestrator Deployments

This checklist covers **Standard Hybrid Wrapper deployments** (Strategy 1)—the recommended approach for 90% of client handoffs. If you're deploying a Shadow Orchestrator system (Strategy 2) with production self-annealing, you'll need additional steps covered in Chapter 12.

Now, let's begin the checklist.

---

## Phase 1: Environment Setup

### Modal Account

Before writing any deployment code, verify your Modal infrastructure is ready:

- [ ] **Modal account created** at modal.com (use GitHub sign-in for easy auth)
- [ ] **Modal CLI installed** via `pip install modal`
- [ ] **Authenticated successfully** by running `modal token set` in terminal
- [ ] **Token ID and Token Secret saved securely** (you'll need these for secrets)
- [ ] **Modal dashboard accessible** at modal.com/dashboard (verify you can see your apps)

**Why this matters**: Missing any of these steps means deployment will fail with cryptic authentication errors. Set up once, deploy many times.

### Local Development Environment

Your local environment must mirror the Modal execution environment:

- [ ] **Python 3.9+ installed** (check with `python --version`)
- [ ] **Virtual environment created** for this project (keeps dependencies isolated)
- [ ] **Virtual environment activated** before installing packages
- [ ] **All dependencies listed in requirements.txt** (if it's imported, it must be listed)
- [ ] **Local testing complete** (workflow runs without errors on your machine)
- [ ] **Edge cases tested and handled** (empty inputs, invalid data, API failures)

**Critical**: If it doesn't work locally with clean dependencies, it won't work in Modal. Test thoroughly before deploying.

---

## Phase 2: Code Preparation

### Modal App Structure

Your Python code must follow Modal's conventions:

- [ ] **`@app.function()` decorator added** to your main function
- [ ] **Function signature is HTTP-compatible** (accepts `dict`, returns `dict`)
- [ ] **Input validation implemented** (check required fields, data types)
- [ ] **Error handling added for all failure modes** (API timeouts, invalid inputs, etc.)
- [ ] **Response format is JSON** with consistent structure: `{"success": bool, "data": {...}, "error": str}`
- [ ] **Timeout configured appropriately** (default 5 min, adjust based on workflow duration)
- [ ] **Function name follows naming conventions** (lowercase, underscores, descriptive)

**Example of proper structure**:

```python
import modal

app = modal.App("my-workflow")

@app.function(
    secrets=[modal.Secret.from_name("my-app-token")],
    timeout=180  # 3 minutes
)
@modal.web_endpoint(method="POST")
def process_workflow(data: dict) -> dict:
    """
    Process the workflow with proper validation and error handling.
    """
    # Validate inputs
    if "required_field" not in data:
        return {
            "success": False,
            "error": "Missing required field: required_field"
        }

    try:
        # Your workflow logic here
        result = do_the_work(data)

        return {
            "success": True,
            "data": result
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Processing failed: {str(e)}"
        }
```

### Authentication & Security

Security isn't optional—it's required:

- [ ] **Bearer token authentication implemented** (check Authorization header)
- [ ] **Token stored as Modal secret** via `modal secret create my-app-token TOKEN="your_secret_here"`
- [ ] **No hardcoded credentials in code** (check for API keys, passwords, tokens)
- [ ] **Environment variables properly configured** (use Modal secrets for all sensitive data)
- [ ] **Rate limiting implemented** (if needed to prevent abuse)
- [ ] **HTTPS enforced** (Modal does this automatically, but verify endpoint uses https://)
- [ ] **Input sanitization implemented** (prevent injection attacks)

**Example authentication check**:

```python
@app.function(secrets=[modal.Secret.from_name("my-app-token")])
@modal.web_endpoint(method="POST")
def process_workflow(data: dict, request: modal.web_endpoint.Request) -> dict:
    import os

    # Validate Bearer token
    auth_header = request.headers.get("Authorization", "")
    expected_token = os.environ.get("TOKEN")

    if not auth_header.startswith("Bearer ") or auth_header[7:] != expected_token:
        return {
            "success": False,
            "error": "Unauthorized"
        }, 401

    # Continue with workflow...
```

### Dependencies

Dependency mismatches are the #1 cause of "works locally, fails in Modal" issues:

- [ ] **All imports work in Modal environment** (no local-only packages)
- [ ] **requirements.txt includes all packages** (every import statement has a corresponding requirement)
- [ ] **Package versions pinned** (e.g., `google-generativeai==0.3.0` not just `google-generativeai`)
- [ ] **No local file dependencies** (everything must be in code, Modal volumes, or fetched from URLs)
- [ ] **No system-level dependencies** (Modal provides standard Debian environment)
- [ ] **Tested with fresh virtual environment** (proves requirements.txt is complete)

**How to generate requirements.txt**:

```bash
# In your project directory with venv activated
pip freeze > requirements.txt

# Then manually review and clean up (remove unnecessary packages)
```

**Common packages to pin**:
- `google-generativeai==0.3.0` (Gemini API)
- `requests==2.31.0` (HTTP requests)
- `beautifulsoup4==4.12.0` (web scraping)
- `pydantic==2.5.0` (data validation)

---

## Phase 3: Testing

### Local Validation

Before touching Modal, prove it works locally:

- [ ] **Workflow runs successfully locally** (no errors, correct output)
- [ ] **All edge cases handled gracefully** (empty inputs, missing fields, API failures)
- [ ] **Error messages are clear and actionable** (tell user what went wrong and how to fix)
- [ ] **Output matches "Definition of Done" from directive** (verify against success criteria)
- [ ] **Self-annealing tested** (if applicable—errors logged and directives updated)
- [ ] **Performance acceptable** (completes within timeout limits)
- [ ] **Memory usage reasonable** (won't exceed Modal container limits)

**Test script example**:

```python
# test_local.py
from my_workflow import process_workflow

# Test happy path
result = process_workflow({"input": "valid data"})
assert result["success"] == True

# Test missing required field
result = process_workflow({})
assert result["success"] == False
assert "required" in result["error"].lower()

# Test invalid input type
result = process_workflow({"input": 12345})  # Should be string
assert result["success"] == False

print("All local tests passed!")
```

### Modal Test Deployment

Now deploy to Modal's staging environment:

- [ ] **Test deployment succeeds** via `modal deploy app.py`
- [ ] **Function URL returned without errors** (copy this URL for testing)
- [ ] **cURL test command works** (see example below)
- [ ] **Bearer token authentication works** (401 without token, 200 with token)
- [ ] **Response time acceptable** (< 30 seconds for most workflows, < 5 min max)
- [ ] **Modal logs show successful execution** (check `modal app logs your-app-name`)
- [ ] **Error scenarios handled correctly** (test with invalid inputs)

**cURL test command**:

```bash
curl -X POST https://your-username--your-app-function.modal.run \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_secret_token" \
  -d '{
    "required_field": "test value"
  }'
```

**Expected response**:

```json
{
  "success": true,
  "data": {
    "result": "processed successfully"
  }
}
```

---

## Phase 4: Integration

### n8n Setup (Hybrid Wrapper)

This is where your Modal endpoint becomes client-accessible:

- [ ] **n8n workflow created** (start with blank workflow)
- [ ] **Trigger node configured** (webhook, schedule, email, form submission, etc.)
- [ ] **HTTP Request node added** with all settings below:

**HTTP Request Node Configuration**:
- [ ] **Method**: POST
- [ ] **URL**: Your Modal endpoint URL (from `modal deploy` output)
- [ ] **Authentication**: Generic Credential Type → Header Auth
  - [ ] **Name**: `Authorization`
  - [ ] **Value**: `Bearer your_secret_token`
- [ ] **Body Content Type**: JSON
- [ ] **JSON Body**: Properly mapped from trigger node
  - Example: `{ "required_field": "{{ $json.field_from_trigger }}" }`
- [ ] **Timeout**: Set appropriately (default 5 min, adjust based on workflow)
- [ ] **Response Format**: JSON

**Additional n8n Nodes**:
- [ ] **Output mapping configured** (extract data from HTTP response)
- [ ] **Final action node added** (email, CRM update, Slack message, etc.)
- [ ] **Error handling node added** (what happens if Modal returns error)

**n8n Error Handling Example**:

Add an IF node after HTTP Request:
- **Condition**: `{{ $json.success }} === true`
- **True Branch**: Continue to final action
- **False Branch**: Send error notification with `{{ $json.error }}`

### End-to-End Test

The moment of truth—test the complete flow:

- [ ] **Trigger the n8n workflow** (manually first, then via real trigger)
- [ ] **Verify Modal endpoint receives request** (check Modal logs)
- [ ] **Verify Modal returns correct response** (check n8n execution log)
- [ ] **Verify n8n processes response correctly** (data flows to next node)
- [ ] **Verify final action executes** (email sent, CRM updated, Slack message posted)
- [ ] **Test error scenarios**:
  - [ ] Invalid input from trigger
  - [ ] Missing Bearer token (should see 401 error)
  - [ ] Modal function timeout (should see timeout error in n8n)
  - [ ] API failure in Modal function (should return `success: false`)

**Success criteria**: You can trigger the workflow from start to finish without manual intervention, and errors are handled gracefully with clear notifications.

---

## Phase 5: Documentation

### Handover Package

Create a complete handover package for client/team:

- [ ] **Endpoint URL documented** (include full URL with https://)
- [ ] **Bearer token documented** (store securely—use password manager, not plain text)
- [ ] **Input specification documented**:
  - [ ] List all required fields with data types
  - [ ] List all optional fields with defaults
  - [ ] Provide example JSON payload
- [ ] **Output specification documented**:
  - [ ] Describe success response structure
  - [ ] Describe error response structure
  - [ ] Provide example success and error responses
- [ ] **Error codes documented**:
  - [ ] 200: Success
  - [ ] 400: Invalid input (missing required fields)
  - [ ] 401: Unauthorized (missing/invalid Bearer token)
  - [ ] 500: Server error (workflow failed)
  - [ ] 504: Timeout (workflow took too long)
- [ ] **cURL example command created** (copy-paste ready for testing)
- [ ] **n8n workflow JSON exported** (File → Export → Download)

**Example documentation template**:

```markdown
# Workflow Name: Lead Enrichment API

## Endpoint
**URL**: https://username--lead-enricher-enrich.modal.run
**Method**: POST
**Authentication**: Bearer Token

## Authentication
Add to headers:
```
Authorization: Bearer abc123xyz789
```

## Input Specification
**Required Fields**:
- `company_name` (string): Company name to enrich
- `email` (string): Contact email address

**Optional Fields**:
- `industry` (string): Industry filter (default: any)

**Example Request**:
```json
{
  "company_name": "Acme Corp",
  "email": "contact@acme.com",
  "industry": "SaaS"
}
```

## Output Specification
**Success Response** (200):
```json
{
  "success": true,
  "data": {
    "company": "Acme Corp",
    "enriched_data": {
      "employee_count": 50,
      "revenue": "$5M",
      "technologies": ["Salesforce", "HubSpot"]
    }
  }
}
```

**Error Response** (400/401/500):
```json
{
  "success": false,
  "error": "Missing required field: company_name"
}
```

## Error Codes
- **200**: Success
- **400**: Invalid input (check error message)
- **401**: Unauthorized (check Bearer token)
- **500**: Processing error (check Modal logs)
- **504**: Timeout (workflow took > 5 minutes)

## cURL Test Command
```bash
curl -X POST https://username--lead-enricher-enrich.modal.run \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer abc123xyz789" \
  -d '{
    "company_name": "Acme Corp",
    "email": "contact@acme.com"
  }'
```

## n8n Integration
1. Import the n8n workflow: `lead-enrichment.json`
2. Update the Bearer token in HTTP Request node credentials
3. Test manually before activating

## Support
- **Modal Logs**: modal.com/dashboard → Apps → lead-enricher → Logs
- **Contact**: your-email@example.com
```

### Monitoring

Set up observability before going live:

- [ ] **Modal logs accessible** (share dashboard access with team if needed)
- [ ] **Error alerts configured** (use Modal's built-in monitoring or external service)
- [ ] **Usage limits understood**:
  - [ ] Modal free tier: 30 CPU-hours/month
  - [ ] What happens when limit is exceeded (workflow stops)
  - [ ] Plan for scaling (upgrade to paid tier if needed)
- [ ] **Backup plan if Modal is down**:
  - [ ] Document manual fallback process
  - [ ] Set up status page monitoring (uptime.com, etc.)

---

## Phase 6: Go-Live

### Final Checks

Before enabling the workflow for production use:

- [ ] **Client/team trained on n8n workflow**:
  - [ ] Can manually trigger workflow
  - [ ] Understands how to read execution logs
  - [ ] Knows how to handle errors (check error message, retry, escalate)
- [ ] **Emergency contact info provided**:
  - [ ] Your contact info for urgent issues
  - [ ] Modal support email (support@modal.com)
  - [ ] n8n support docs (docs.n8n.io)
- [ ] **Rollback plan documented**:
  - [ ] How to disable n8n workflow (deactivate button)
  - [ ] How to revert to previous Modal version (redeploy old code)
  - [ ] Manual process if automation fails completely
- [ ] **First production run monitored manually**:
  - [ ] Watch Modal logs in real-time
  - [ ] Watch n8n execution
  - [ ] Verify final action (email received, CRM updated, etc.)
- [ ] **Success metrics defined**:
  - [ ] What "working correctly" looks like (e.g., 95% success rate)
  - [ ] How often to check logs (daily for first week)
  - [ ] When to escalate issues (critical errors, repeated failures)

### Post-Deployment

Your job isn't done when deployment succeeds—monitor for 48 hours:

- [ ] **Monitor for 48 hours** (check logs daily at minimum)
- [ ] **Check Modal logs for errors** (even if n8n shows success—silent failures happen)
- [ ] **Verify n8n workflow runs on schedule** (if using scheduled trigger)
- [ ] **Collect feedback from client/team**:
  - [ ] Is output meeting expectations?
  - [ ] Are error messages clear enough?
  - [ ] Any feature requests or improvements?
- [ ] **Document any issues for self-annealing**:
  - [ ] What errors occurred?
  - [ ] What edge cases weren't handled?
  - [ ] Update the directive with learnings

**48-Hour Monitoring Schedule**:
- **Hour 0**: Deployment complete, first manual test
- **Hour 1**: Check logs for first automated run
- **Hour 24**: Daily check-in (review all executions)
- **Hour 48**: Final check-in (decide if stable enough for weekly monitoring)

---

## Common Gotchas

Learn from others' mistakes—these are the most common deployment failures:

### ❌ Forgot to pin package versions
**Symptom**: Deployment works today, breaks tomorrow with "ModuleNotFoundError" or "AttributeError"
**Why**: Dependencies auto-update to incompatible versions
**Fix**: Pin all versions in requirements.txt: `google-generativeai==0.3.0` not `google-generativeai`

### ❌ Didn't test authentication
**Symptom**: 401 Unauthorized errors in n8n, even though code looks correct
**Why**: Bearer token not passed correctly, or Modal secret misconfigured
**Fix**: Test with cURL first to isolate n8n from Modal issues

### ❌ Local file paths in code
**Symptom**: Works perfectly locally, crashes in Modal with "FileNotFoundError"
**Why**: Modal containers don't have access to your local filesystem
**Fix**: Use Modal volumes for large files, or fetch from URLs, or embed small data in code

### ❌ No error handling
**Symptom**: Silent failures that look like success (200 status but wrong data)
**Why**: Exceptions caught but not logged, or success always returned
**Fix**: Always wrap workflow logic in try/except and return `{"success": false, "error": str(e)}`

### ❌ Didn't test edge cases
**Symptom**: Workflow breaks on unusual inputs (empty strings, None values, special characters)
**Why**: Only tested happy path locally
**Fix**: Create test suite with edge cases before deploying

### ❌ n8n timeout too short
**Symptom**: n8n shows "Workflow Error: Request Timeout" even though Modal function succeeds
**Why**: n8n default timeout (5 min) shorter than Modal function duration
**Fix**: Increase timeout in n8n HTTP Request node settings

### ❌ Hardcoded credentials
**Symptom**: API keys visible in Modal logs or code repository
**Why**: Forgot to move credentials to Modal secrets
**Fix**: Use `modal secret create` and `os.environ.get()` for all sensitive data

### ❌ Didn't export n8n workflow
**Symptom**: Can't recreate n8n workflow if accidentally deleted
**Why**: No backup of workflow JSON
**Fix**: Export workflow immediately after configuring (File → Export → Download)

### ❌ No monitoring after deployment
**Symptom**: Workflow fails silently for days before anyone notices
**Why**: Assumed deployment success means ongoing success
**Fix**: Set calendar reminders to check logs for first week minimum

### ❌ Unclear error messages
**Symptom**: Client reports "it's broken" but can't explain what's wrong
**Why**: Error responses don't explain what failed or how to fix
**Fix**: Return specific error messages: "Missing required field: company_name" not "Invalid input"

---

## Troubleshooting Guide

When deployment fails, work through this systematically:

### Problem: `modal deploy` fails with import error

**Symptoms**:
```
ModuleNotFoundError: No module named 'google.generativeai'
```

**Diagnosis**:
- Package not listed in requirements.txt
- Package name misspelled
- Virtual environment not activated during testing

**Solution**:
1. Check what's imported in your code: `grep -r "^import\|^from" app.py`
2. Add missing packages to requirements.txt with versions: `google-generativeai==0.3.0`
3. Test in fresh virtual environment:
   ```bash
   python -m venv test_env
   source test_env/bin/activate  # Windows: test_env\Scripts\activate
   pip install -r requirements.txt
   python app.py  # Should work without errors
   ```

### Problem: 401 Authentication Failed

**Symptoms**:
```json
{
  "success": false,
  "error": "Unauthorized"
}
```

**Diagnosis**:
- Bearer token not in request
- Bearer token incorrect
- Modal secret not configured
- Authentication check logic wrong

**Solution**:
1. Verify Modal secret exists: `modal secret list` (should show your secret name)
2. Test with cURL (replace with your actual token):
   ```bash
   curl -X POST https://your-endpoint.modal.run \
     -H "Authorization: Bearer correct_token_here" \
     -d '{"test": "data"}'
   ```
3. Check n8n HTTP Request node:
   - Authentication → Generic Credential Type → Header Auth
   - Name: `Authorization`
   - Value: `Bearer your_token` (include "Bearer " prefix)
4. Verify code checks token correctly:
   ```python
   expected = os.environ.get("TOKEN")  # From Modal secret
   provided = request.headers.get("Authorization", "")[7:]  # Skip "Bearer "
   if provided != expected:
       return {"success": False, "error": "Unauthorized"}, 401
   ```

### Problem: Modal function times out

**Symptoms**:
- n8n shows "Request Timeout"
- Modal logs show function killed after 5 minutes (or custom timeout)

**Diagnosis**:
- Workflow takes longer than timeout setting
- Infinite loop in code
- External API not responding
- Too much data processing

**Solution**:
1. Check Modal logs for where execution stops
2. Increase timeout in decorator:
   ```python
   @app.function(timeout=600)  # 10 minutes
   ```
3. Optimize slow operations:
   - Use async/await for API calls
   - Batch process instead of individual items
   - Cache results when possible
4. If workflow genuinely needs > 10 minutes, consider:
   - Breaking into multiple smaller endpoints
   - Using Modal's async endpoints with polling
   - Switching to Modal's scheduled jobs instead of HTTP

### Problem: Works locally, fails in Modal

**Symptoms**:
- Local testing passes
- Modal deployment succeeds
- Modal execution fails with mysterious errors

**Diagnosis**:
- Local file paths (most common)
- Environment variables not set
- System dependencies missing
- Different Python versions

**Solution**:

**For file paths**:
```python
# ❌ Won't work in Modal
with open("/Users/you/project/data.json") as f:
    data = json.load(f)

# ✅ Works in Modal
import json
data = {
    "key": "value"
}  # Embed small data directly

# Or use Modal volumes for large files
from modal import Volume
volume = Volume.from_name("my-data")

@app.function(volumes={"/data": volume})
def process():
    with open("/data/data.json") as f:
        data = json.load(f)
```

**For environment variables**:
```python
# ❌ Won't work in Modal
API_KEY = "hardcoded_key"

# ✅ Works in Modal
import os
API_KEY = os.environ.get("API_KEY")  # From Modal secret
```

**For system dependencies**:
```python
# ❌ Might not work in Modal
import cv2  # Requires system libs

# ✅ Tell Modal to install system dependencies
from modal import Image

image = Image.debian_slim().apt_install("libopencv-dev")

@app.function(image=image)
def process():
    import cv2  # Now works
```

### Problem: n8n shows "Workflow Error"

**Symptoms**:
- n8n execution shows red error state
- Error message vague or unhelpful

**Diagnosis**:
- Check Modal logs for actual error (n8n might not show full details)
- Input mapping incorrect (sending wrong data structure)
- Response parsing failed (n8n can't parse JSON)

**Solution**:
1. Check Modal logs: `modal app logs your-app-name --follow`
2. Test endpoint directly with cURL (bypasses n8n):
   ```bash
   curl -X POST https://your-endpoint.modal.run \
     -H "Authorization: Bearer token" \
     -H "Content-Type: application/json" \
     -d '{"field": "value"}' -v  # -v shows full response
   ```
3. If cURL works but n8n fails:
   - Check n8n input mapping (might be sending `"{{ $json.field }}"` instead of actual value)
   - Verify JSON structure matches exactly what Modal expects
   - Check n8n "Previous Node" output to see what data is actually being sent
4. If both fail:
   - Check Modal logs for Python traceback
   - Fix error in code
   - Redeploy: `modal deploy app.py`

### Problem: Workflow returns wrong data

**Symptoms**:
- No error messages
- HTTP 200 status
- But output data is incorrect or empty

**Diagnosis**:
- Logic error in workflow code
- Input data not what you expected
- Success returned even when processing failed

**Solution**:
1. Add extensive logging to Modal function:
   ```python
   @app.function()
   def process(data: dict):
       print(f"Received input: {data}")  # Shows in Modal logs

       result = do_processing(data)
       print(f"Processing result: {result}")

       return {"success": True, "data": result}
   ```
2. Check Modal logs for what's actually happening
3. Test with controlled inputs to isolate where logic fails
4. Add validation to ensure processing succeeded:
   ```python
   result = do_processing(data)

   if not result or "expected_field" not in result:
       return {
           "success": False,
           "error": "Processing failed: missing expected data"
       }
   ```

---

## Quick Reference: Modal Commands

Keep these commands handy during deployment:

### Setup & Authentication
```bash
# Install Modal CLI
pip install modal

# Authenticate (opens browser)
modal token set

# Verify authentication
modal token current
```

### Secrets Management
```bash
# Create a secret (interactive prompts for values)
modal secret create my-app-token

# Create secret from command line
modal secret create my-app-token TOKEN="your_secret_here" API_KEY="another_secret"

# List all secrets
modal secret list

# Delete a secret
modal secret delete my-app-token
```

### Deployment
```bash
# Deploy app (creates/updates endpoint)
modal deploy app.py

# Deploy specific function
modal deploy app.py::process_workflow

# Serve app locally (for testing)
modal serve app.py
```

### Monitoring & Logs
```bash
# View app logs (live tail)
modal app logs my-app --follow

# View recent logs (last 100 lines)
modal app logs my-app -n 100

# List all deployed apps
modal app list

# Stop a running app
modal app stop my-app

# View app details (endpoint URL, etc.)
modal app show my-app
```

### Testing
```bash
# Test endpoint with cURL
curl -X POST https://username--app-function.modal.run \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token" \
  -d '{"test": "data"}'

# Test with verbose output (shows headers)
curl -X POST https://username--app-function.modal.run \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token" \
  -d '{"test": "data"}' -v
```

### Cleanup
```bash
# Delete deployed app
modal app delete my-app

# Clear local cache
modal cache clear
```

---

## Deployment Strategies

### Standard Hybrid Wrapper (Recommended)

**What it is**: Static Modal endpoint + n8n wrapper for triggers and actions

**Architecture**:
```
User Action → n8n Trigger → Modal Endpoint → n8n Final Action → Result
   (form)     (webhook)    (Python logic)     (email/CRM)     (sent)
```

**When to use**:
- ✅ Client handoffs (clients understand n8n visual workflows)
- ✅ Stable workflows (requirements don't change frequently)
- ✅ Lower-risk projects (client success doesn't depend on 99.9% uptime)
- ✅ First-time Modal deployments (simplest approach)

**Pros**:
- Simple to set up and maintain
- Clients can modify triggers and actions without touching code
- Proven, stable (no auto-modification in production)
- Easy to debug (n8n shows execution logs visually)

**Cons**:
- Can't learn from production errors automatically
- Manual update cycle when issues are discovered
- Client must report errors for fixes

**Self-annealing**: Local only (Phase 3-4). Production endpoint is static.

**Checklist sections to focus on**:
- Phase 2: Code Preparation
- Phase 3: Testing (especially local validation)
- Phase 4: Integration (n8n setup is critical)
- Phase 5: Documentation (client needs clear handover docs)

### Shadow Orchestrator (Advanced)

**What it is**: Production self-healing system with automatic error diagnosis and fixes

**Architecture**:
```
n8n Trigger → Primary Modal Endpoint → Error? → Agentic Support → Auto-fix or Escalate
                                                    (Diagnose)      ↓               ↓
                                                                Update Directive  Stuck Agent
                                                                    ↓               ↓
                                                                Redeploy        Human Decides
```

**When to use**:
- ✅ High-volume production workflows (hundreds/thousands of executions daily)
- ✅ Mission-critical applications (client business depends on uptime)
- ✅ Long-running deployments (will be in production for months/years)
- ✅ Workflows with evolving requirements (needs to adapt over time)

**Pros**:
- Learns from production errors continuously
- Self-healing for non-critical issues (auto-fixes without human intervention)
- Reduces manual support work over time
- Continuous improvement without redeployment

**Cons**:
- Higher complexity (two Modal endpoints + GitHub integration)
- Risk of auto-fixing incorrectly (mitigated by graduated response tiers)
- Requires sophisticated monitoring and alerting
- More expensive (runs Opus model for error diagnosis)

**Self-annealing**: Local (Phase 3-4) + Production (continuous)

**Additional requirements beyond this checklist**:
- Secondary Modal endpoint for agentic support
- GitHub integration for directive updates
- Error classification logic (Tier 1/2/3)
- Stuck agent integration for critical errors
- See Chapter 12 for complete Shadow Orchestrator deployment guide

**When NOT to use Shadow Orchestrator**:
- First Modal deployment (learn with Standard first)
- Low-volume workflows (< 50 executions/day)
- Static requirements (workflow logic won't change)
- Budget-conscious projects (Opus calls add up)

---

## Resource Downloads

┌─────────────────────────────────────────────────────┐
│  DOWNLOAD FULL DEPLOYMENT GUIDE                     │
│                                                      │
│  Get the complete checklist, code templates, and    │
│  troubleshooting guide:                             │
│                                                      │
│  travissteel.net/the-last-employee/resources#deployment         │
│                                                      │
│  Included resources:                                │
│  • Printable checklist PDF (this appendix)          │
│  • Modal Python template (app.py starter)           │
│  • n8n workflow templates (pre-built wrappers)      │
│  • Handover document template (client-ready)        │
│  • cURL test script (automated endpoint testing)    │
│  • Video walkthrough (first deployment tutorial)    │
└─────────────────────────────────────────────────────┘

---

## Final Checklist Summary

Print this page and check boxes as you go:

**Phase 1: Environment**
- [ ] Modal account + CLI + auth complete
- [ ] Local Python environment ready

**Phase 2: Code**
- [ ] Modal structure correct (@app.function, @modal.web_endpoint)
- [ ] Authentication implemented
- [ ] Dependencies pinned in requirements.txt

**Phase 3: Testing**
- [ ] Local tests pass (happy path + edge cases)
- [ ] Modal deployment succeeds
- [ ] cURL test works with Bearer token

**Phase 4: Integration**
- [ ] n8n workflow built
- [ ] HTTP Request node configured correctly
- [ ] End-to-end test passes

**Phase 5: Documentation**
- [ ] Handover package created
- [ ] Input/output specs documented
- [ ] n8n workflow exported

**Phase 6: Go-Live**
- [ ] Client trained
- [ ] Emergency contacts shared
- [ ] First production run monitored
- [ ] 48-hour monitoring complete

**If all boxes checked**: Your deployment is production-ready. Ship it!

**If any boxes unchecked**: Work backwards through this appendix. Every unchecked box is a potential production failure waiting to happen.

---

## Next Steps

After completing this checklist:

1. **If deployment succeeded**: Document lessons learned for next deployment
2. **If deployment failed**: Note which checklist item you missed, update your process
3. **For team deployments**: Share this checklist with anyone deploying to Modal
4. **For client handoffs**: Schedule 48-hour check-in to review logs together

Remember: The best deployments are boring. If everything goes smoothly and nothing breaks, you used the checklist correctly.

---

**Related Resources**:
- **Chapter 10**: Phase 5 (Cloudifying) - The big picture
- **Chapter 18**: Hybrid Wrapper Strategy - Why we use n8n + Modal
- **Chapter 12**: Shadow Orchestrator - Advanced self-healing deployments
- **Appendix B**: Agent System Prompt Library - Full subagent definitions
- **directives/hybrid-wrapper-deployment.md**: Step-by-step deployment workflow
- **templates/modal_app_template.py**: Python template to start from

**Attribution**: This checklist operationalizes the Hybrid Wrapper Strategy from Nick Saraev's DOE Framework for bulletproof cloud deployments.
