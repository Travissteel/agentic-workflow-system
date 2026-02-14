# Hybrid Wrapper Deployment Directive

**Created**: February 2026
**Owner**: Deployer Agent
**Frequency**: On-demand (per deployment request)

---

## Objective

**What needs to happen:**
Deploy a battle-tested local workflow to Modal as a secure API endpoint, wrap it in an n8n visual workflow, and deliver a complete handover package that enables clients to trigger and monitor the automation without touching code.

**Why this matters:**
The Hybrid Wrapper Strategy (n8n + Modal) is the recommended approach for 90% of client handoffs. It combines the power of agentic Python logic with the accessibility of no-code tools, giving clients full control without requiring developer expertise. This directive ensures consistent, secure, production-ready deployments every time.

---

## Inputs

**Required Data:**
- [ ] Completed workflow logic (Python code, tested locally)
- [ ] Input/output specification (what data flows in and out)
- [ ] Workflow requirements (APIs used, dependencies, secrets needed)
- [ ] Client information (who receives the handover package)

**Required Access:**
- [ ] Modal account with authentication configured
- [ ] Modal CLI installed and authenticated locally
- [ ] n8n account or self-hosted instance
- [ ] GitHub repository (if using version control)

**Trigger Conditions:**
- **When**: Orchestrator delegates a deployment task
- **If**: Phase 3 (build) and Phase 4 (test) are complete

---

## Process

**Step-by-step workflow (in plain English):**

### Phase 1: Modal Environment Setup

1. **Verify Modal Authentication**
   - Check if Modal CLI is authenticated
   - Success looks like: `modal token current` returns valid credentials
   - If error: Run `modal token set` to authenticate, or escalate to stuck agent

2. **Generate Bearer Token for Endpoint Security**
   - Run `openssl rand -hex 32` to generate 64-character token
   - Success looks like: Random token generated successfully
   - If error: Use Python `secrets.token_hex(32)` as fallback

3. **Create Modal Secret for Authentication**
   - Run `modal secret create api-auth-token API_AUTH_TOKEN=<generated-token>`
   - Success looks like: Secret created and appears in `modal secret list`
   - If error: Check if secret already exists; if yes, use existing; if no, escalate

4. **Verify Required Secrets Exist**
   - For each API used (Anthropic, OpenAI, etc.), check `modal secret list`
   - Success looks like: All required secrets are present
   - If error: Create missing secrets or escalate to stuck agent with list of missing items

### Phase 2: Build Modal Function

5. **Create Modal App File**
   - Name file descriptively (e.g., `lead_enrichment_modal.py`)
   - Success looks like: File created with proper naming convention
   - If error: Name collision or invalid characters in filename

6. **Import Required Libraries**
   - Add imports: `modal`, `fastapi`, `os`, plus workflow-specific libraries
   - Success looks like: All imports valid and available in Modal environment
   - If error: Missing library that's not available in Modal (need custom image)

7. **Define Modal App and Image**
   - Create app: `app = modal.App("app-name")`
   - Define image with dependencies: `modal.Image.debian_slim().pip_install(...)`
   - Success looks like: Image definition includes all required packages
   - If error: Missing dependency in pip_install list

8. **Implement Function with Authentication**
   - Add `@app.function()` decorator with secrets and timeout
   - Add `@modal.fastapi_endpoint(method="POST")` decorator
   - Implement Bearer token validation (check Authorization header)
   - Success looks like: Function validates token and returns 401/403 for invalid auth
   - If error: Authentication logic missing or incorrect

9. **Implement Workflow Logic**
   - Copy tested workflow logic into function body
   - Add input validation (check required fields)
   - Add error handling (try/except with clear error messages)
   - Return clean JSON: `{"success": bool, "data": {...}, "error": str}`
   - Success looks like: Logic matches local implementation exactly
   - If error: Logic differs from tested version (sync issue)

10. **Pin All Dependencies**
    - Create or update requirements.txt with exact versions
    - Success looks like: All packages pinned (e.g., `anthropic==0.3.0`)
    - If error: Version conflict or unpinned dependency

### Phase 3: Local Testing

11. **Test Function Locally with modal run**
    - Run `modal run app.py::function_name`
    - Provide sample input data
    - Success looks like: Function executes without errors and returns expected output
    - If error: Fix bugs and retest (do NOT proceed until local test passes)

12. **Test Authentication Locally**
    - Test without Bearer token (should get 401)
    - Test with wrong token (should get 403)
    - Test with correct token (should get 200)
    - Success looks like: All three scenarios behave correctly
    - If error: Authentication logic broken (fix before deploying)

### Phase 4: Deploy to Modal

13. **Deploy Function to Production**
    - Run `modal deploy app.py`
    - Capture endpoint URL from output
    - Success looks like: Deployment succeeds with URL: `https://[profile]--[app]-[func].modal.run`
    - If error: Deployment fails → Check logs → Fix → Retry (escalate if stuck)

14. **Test Deployed Endpoint with cURL**
    - Construct cURL command with Bearer token
    - Send test request
    - Success looks like: 200 response with expected JSON output
    - If error: Debug with Modal logs (`modal app logs app-name --follow`)

### Phase 5: n8n Integration

15. **Create n8n Workflow**
    - Create new blank workflow in n8n
    - Success looks like: Blank canvas ready for node configuration
    - If error: n8n access issue or account problem

16. **Add Trigger Node**
    - Based on client needs: Webhook, Schedule, Email, Form, etc.
    - Configure trigger settings
    - Success looks like: Trigger fires when expected event occurs
    - If error: Trigger misconfigured or not firing

17. **Add HTTP Request Node**
    - Method: POST
    - URL: Modal endpoint URL from deployment
    - Authentication: Generic Credential Type → Header Auth
      * Name: `Authorization`
      * Value: `Bearer <token-from-step-2>`
    - Body Content Type: JSON
    - JSON Body: Map trigger data to Modal function inputs
    - Success looks like: HTTP node configured with all required fields
    - If error: Missing or misconfigured field

18. **Add Conditional IF Node (Error Handling)**
    - Condition: `{{ $json.success }} === true`
    - True branch: Continue to final action
    - False branch: Send error notification with `{{ $json.error }}`
    - Success looks like: Error handling properly routes successes and failures
    - If error: IF node logic incorrect

19. **Add Final Action Node**
    - Based on workflow purpose: Email, CRM update, Slack message, etc.
    - Map HTTP response data to action inputs
    - Success looks like: Action executes with data from Modal response
    - If error: Data mapping incorrect or action node misconfigured

20. **Test n8n Workflow End-to-End**
    - Manually trigger the workflow
    - Verify data flows through all nodes
    - Check Modal logs to confirm endpoint received request
    - Verify final action executed correctly
    - Success looks like: Complete flow from trigger to action works perfectly
    - If error: Debug at failing node, fix, retest (escalate if stuck)

### Phase 6: Documentation and Handover

21. **Create Complete Handover Package**
    - Document endpoint URL
    - Document Bearer token (store securely)
    - Document input specification (required and optional fields)
    - Document output specification (success and error responses)
    - Create cURL test command (copy-paste ready)
    - Export n8n workflow as JSON
    - Success looks like: All documentation complete and client-ready
    - If error: Missing documentation component

22. **Create Client Training Materials**
    - How to trigger the workflow
    - How to view n8n execution logs
    - How to modify trigger or actions
    - What to do if errors occur
    - Success looks like: Clear, actionable instructions for non-technical users
    - If error: Documentation too technical or incomplete

23. **Deliver Handover Package to Orchestrator**
    - Return complete package with all URLs, tokens, docs, and n8n JSON
    - Success looks like: Orchestrator has everything needed for client handoff
    - If error: Incomplete package (missing critical component)

**Edge Cases & Exceptions:**

- **If Modal deployment fails repeatedly**: Check Modal dashboard for service status; may be platform issue
- **If Bearer token authentication doesn't work**: Verify secret name matches code reference exactly
- **If n8n can't reach Modal endpoint**: Check firewall rules or network issues
- **If workflow times out**: Increase timeout in `@app.function(timeout=300)` decorator
- **If client needs multiple environments**: Deploy separate endpoints for staging and production

---

## Definition of Done

**This deployment is complete when:**
- [ ] Modal endpoint is deployed and accessible via HTTPS
- [ ] Bearer token authentication works (401 without token, 200 with token)
- [ ] Local and production endpoints return identical outputs for same inputs
- [ ] n8n workflow is built and tested end-to-end
- [ ] Error handling routes failures correctly
- [ ] All documentation is complete and client-ready
- [ ] Handover package delivered to orchestrator
- [ ] Client can trigger workflow and view results without assistance

**Quality Standards:**
- Endpoint response time <30 seconds for typical requests
- Authentication properly blocks unauthorized access
- Error messages are clear and actionable (not raw stack traces)
- n8n workflow is visually organized and labeled
- Documentation uses non-technical language where possible
- All secrets stored securely (not hardcoded)

**Notification:**
- **Who to notify**: Orchestrator (who delegated the deployment task)
- **How**: Return detailed completion report
- **What to include**: Endpoint URL, Bearer token, cURL command, n8n JSON, input/output spec, any issues encountered

---

## Notes & Learnings

**Known Issues:**
- First-time Modal users often forget to run `modal token set` before deploying
- Common mistake: Forgetting to include `Authorization` in Header Auth name (not just the token)
- n8n free tier has execution limits (60 executions/day) - clients may need paid plan

**Optimization Ideas:**
- Create reusable Modal app templates for common patterns (AI endpoints, scraping, data processing)
- Build n8n workflow library for common trigger/action combinations
- Automate Bearer token generation and secret creation

**Self-Annealing Updates:**
- [Date]: [What was changed and why based on deployment experiences]

---

## Security Checklist

**BEFORE deploying, verify:**
- ✅ Bearer token is 32+ characters (strong security)
- ✅ Bearer token stored as Modal secret (not in code)
- ✅ Authentication check happens BEFORE any logic executes
- ✅ No API keys or secrets hardcoded in Python file
- ✅ All secrets referenced via `os.environ.get()`
- ✅ Error messages don't expose sensitive information
- ✅ Input validation prevents injection attacks

**NEVER:**
- ❌ Deploy without authentication
- ❌ Use weak tokens (less than 32 characters)
- ❌ Store secrets in GitHub repository
- ❌ Expose internal error details to public endpoints

---

## n8n Node Configuration Reference

**HTTP Request Node Settings:**
```
Method: POST
URL: https://your-username--app-name-function.modal.run
Authentication: Generic Credential Type
  ├─ Credential Type: Header Auth
  ├─ Name: Authorization
  └─ Value: Bearer abc123xyz789...
Body Content Type: JSON
JSON/RAW Parameters: {
  "field1": "{{ $json.field_from_trigger }}",
  "field2": "value"
}
Timeout: 300000 (5 minutes)
```

**IF Node Error Handling:**
```
Condition: {{ $json.success }} === true
True Branch: Final Action Node
False Branch: Error Notification Node
```

---

## Common Deployment Errors and Fixes

**Error: `ModuleNotFoundError` during deployment**
- **Cause**: Missing package in requirements.txt or image definition
- **Fix**: Add to `.pip_install()` list in image definition

**Error: `401 Unauthorized` when testing endpoint**
- **Cause**: Bearer token not in request OR incorrect Authorization header format
- **Fix**: Ensure header is `Authorization: Bearer <token>` with "Bearer " prefix

**Error: `Workflow execution timed out` in n8n**
- **Cause**: n8n timeout (default 5 min) shorter than Modal function runtime
- **Fix**: Increase timeout in HTTP Request node settings

**Error: `Secret not found` in Modal logs**
- **Cause**: Secret name in code doesn't match created secret
- **Fix**: Verify exact match: `modal.Secret.from_name("api-auth-token")` and `modal secret create api-auth-token`

---

## Handover Package Template

**File: HANDOVER.md**

```markdown
# [Workflow Name] - Deployment Complete

## Endpoint Details
**URL**: https://username--app-name-function.modal.run
**Method**: POST
**Authentication**: Bearer Token

## Authentication
Add this header to all requests:
```
Authorization: Bearer [TOKEN_HERE]
```

## Input Specification
Required fields:
- `field1` (string): Description
- `field2` (number): Description

Optional fields:
- `field3` (boolean): Description (default: false)

## Output Specification
**Success Response** (200):
```json
{
  "success": true,
  "data": {
    "result": "..."
  }
}
```

**Error Response** (400/401/500):
```json
{
  "success": false,
  "error": "Error description"
}
```

## n8n Workflow
Import the attached `workflow.json` file into your n8n instance.

**Setup steps:**
1. Import JSON file
2. Update Bearer token in HTTP Request node credentials
3. Test manually before activating
4. Activate workflow

## Testing
Use this cURL command to test:
```bash
curl -X POST https://username--app-name-function.modal.run \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [TOKEN]" \
  -d '{"field1": "test", "field2": 123}'
```

## Support
- **Modal Logs**: https://modal.com/dashboard
- **n8n Docs**: https://docs.n8n.io
- **Contact**: your-email@example.com
```

---

**Related Resources:**
- Chapter 18: The Hybrid Wrapper Strategy (why n8n + Modal)
- Appendix D: Modal Deployment Checklist (pre-flight checks)
- `deployer-agent.md`: Full deployer agent specification
- `modal-app-template.py`: Python template to start from
