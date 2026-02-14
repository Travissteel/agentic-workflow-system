# Modal Deployment Checklist

Print this page and check boxes as you go through your deployment.

---

## Phase 1: Environment

- [ ] Modal account created at modal.com
- [ ] Modal CLI installed via `pip install modal`
- [ ] Authenticated successfully with `modal token set`
- [ ] Modal dashboard accessible
- [ ] Python 3.9+ installed locally
- [ ] Virtual environment created and activated
- [ ] All dependencies listed in requirements.txt
- [ ] Local testing complete (workflow runs without errors)

---

## Phase 2: Code

- [ ] `@app.function()` decorator added to main function
- [ ] Function signature is HTTP-compatible (accepts dict, returns dict)
- [ ] Input validation implemented (check required fields)
- [ ] Error handling added for all failure modes
- [ ] Response format is JSON with consistent structure
- [ ] Timeout configured appropriately
- [ ] Function name follows naming conventions
- [ ] Bearer token authentication implemented
- [ ] Token stored as Modal secret
- [ ] No hardcoded credentials in code
- [ ] All imports work in Modal environment
- [ ] requirements.txt includes all packages
- [ ] Package versions pinned (e.g., `anthropic==0.3.0`)

---

## Phase 3: Testing

- [ ] Workflow runs successfully locally
- [ ] All edge cases handled gracefully
- [ ] Error messages are clear and actionable
- [ ] Output matches "Definition of Done" from directive
- [ ] Performance acceptable (completes within timeout)
- [ ] Modal test deployment succeeds via `modal deploy`
- [ ] Function URL returned without errors
- [ ] cURL test command works
- [ ] Bearer token authentication works (401 without token, 200 with token)
- [ ] Response time acceptable (< 30 seconds typical)
- [ ] Modal logs show successful execution
- [ ] Error scenarios handled correctly

---

## Phase 4: Integration

- [ ] n8n workflow created
- [ ] Trigger node configured
- [ ] HTTP Request node added with all settings:
  - [ ] Method: POST
  - [ ] URL: Modal endpoint URL
  - [ ] Authentication: Header Auth
  - [ ] Name: `Authorization`
  - [ ] Value: `Bearer token`
  - [ ] Body Content Type: JSON
  - [ ] Timeout set appropriately
- [ ] Output mapping configured
- [ ] Final action node added
- [ ] Error handling node added (IF node for success check)
- [ ] End-to-end test passes (trigger → Modal → action)
- [ ] Invalid input tested
- [ ] Missing Bearer token tested (401 error)
- [ ] Modal function timeout tested

---

## Phase 5: Documentation

- [ ] Endpoint URL documented
- [ ] Bearer token documented (stored securely)
- [ ] Input specification documented (required and optional fields)
- [ ] Output specification documented (success and error responses)
- [ ] Error codes documented (200, 400, 401, 500, 504)
- [ ] cURL example command created
- [ ] n8n workflow JSON exported

---

## Phase 6: Go-Live

- [ ] Client/team trained on n8n workflow
- [ ] Emergency contact info provided
- [ ] Rollback plan documented
- [ ] First production run monitored manually
- [ ] Success metrics defined
- [ ] Monitor for 48 hours (check logs daily)
- [ ] Collect feedback from client/team
- [ ] Document any issues for self-annealing

---

## Security Checklist

**BEFORE deploying, verify:**
- [ ] Bearer token is 32+ characters
- [ ] Bearer token stored as Modal secret (not in code)
- [ ] Authentication check happens BEFORE any logic executes
- [ ] No API keys or secrets hardcoded
- [ ] All secrets referenced via `os.environ.get()`
- [ ] Error messages don't expose sensitive information
- [ ] Input validation prevents injection attacks

---

## Common Gotchas

**Check these if deployment fails:**
- [ ] Package versions are pinned in requirements.txt
- [ ] Bearer token format is correct: `Authorization: Bearer token`
- [ ] No local file paths in code
- [ ] All exceptions are caught and handled
- [ ] Edge cases are tested
- [ ] n8n timeout matches Modal function timeout
- [ ] No hardcoded credentials visible in logs
- [ ] n8n workflow is exported as backup
- [ ] Monitoring is set up for first week

---

**If all boxes checked**: Your deployment is production-ready!

**If any boxes unchecked**: Work backwards through this checklist. Every unchecked box is a potential production failure.

---

**Related Resources:**
- `hybrid-wrapper-deployment.md` - Full deployment workflow
- `modal-endpoint-guide.md` - Guide for building endpoints
- `modal-app-template.py` - Python template
- Appendix D: Full Modal Deployment Checklist
