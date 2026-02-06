# Hybrid Wrapper Deployment Workflow

**Version:** 1.0
**Last Updated:** February 2026
**Framework:** DOE Phase 5 - Cloudifying

This directive provides a complete, step-by-step workflow for deploying agentic workflows to the cloud using the **Hybrid Wrapper Strategy** (n8n + Modal).

---

## Objective

Transform a battle-tested local workflow into a production-ready cloud deployment that combines:
- **Visual Interface**: n8n workflow that clients can understand and maintain
- **Agentic Logic**: Python-powered Modal endpoint handling complex operations
- **Secure Connection**: Authenticated HTTP communication between layers

---

## Prerequisites

Before starting this workflow:

✅ **Phase 3-4 Complete**: Local implementation built and tested
✅ **Modal Account**: Active account at modal.com
✅ **Modal Credentials**: Token ID and Token Secret available
✅ **Workflow Specification**: Clear understanding of inputs, outputs, and logic
✅ **n8n Access**: n8n cloud account or self-hosted instance

---

## Input Specifications

This workflow requires:

1. **Workflow Logic Description**
   - What the workflow does (e.g., "Generate AI-powered email replies")
   - Business logic and processing steps
   - Any external APIs or services needed

2. **Input Data Structure**
   - What data comes from the n8n trigger
   - Data types and formats
   - Example payload

3. **Output Data Structure**
   - What data is returned to n8n
   - Required format for the final action
   - Example response

4. **External Dependencies**
   - API keys needed (Anthropic, OpenAI, etc.)
   - Python packages required
   - Any database connections

---

## Step-by-Step Process

### Step 1: Orchestrator Delegates to Deployer

**Orchestrator Action:**
```
Invoke deployer subagent with:
- Workflow description
- Input/output specifications
- Required dependencies
- Any special requirements
```

**What Happens:**
- Deployer receives task in fresh context window
- Begins deployment workflow with clean slate
- Follows Modal deployment protocol

---

### Step 2: Deployer Configures Modal Environment

**Deployer Actions:**

**2.1 Check Modal Authentication**
```bash
# Verify Modal is configured
modal token list
```

**If first-time user:**
```bash
# Configure Modal credentials
modal token set --token-id <TOKEN_ID> --token-secret <TOKEN_SECRET>

# Verify configuration
cat ~/.modal.toml
```

**2.2 Generate Bearer Token for Endpoint**
```bash
# Generate secure random token
openssl rand -hex 32

# Example output: 7f3e9d2a1b4c5e6f8g9h0i1j2k3l4m5n6o7p8q9r0s1t2u3v4w5x6y7z8a9b0c1
```

**2.3 Create Modal Secret**
```bash
# Store Bearer token as Modal secret
modal secret create api-auth-token API_AUTH_TOKEN=7f3e9d2a1b4c5e6f8g9h0i1j2k3l4m5n6o7p8q9r0s1t2u3v4w5x6y7z8a9b0c1

# Verify secret created
modal secret list
```

**2.4 Create Secrets for External APIs**
```bash
# If using Anthropic
modal secret create anthropic-api-key ANTHROPIC_API_KEY=sk-ant-xxx

# If using OpenAI
modal secret create openai-api-key OPENAI_API_KEY=sk-xxx

# Add others as needed
```

---

### Step 3: Deployer Builds Modal Function

**Deployer Creates:** `modal_app.py`

**File Structure:**
```python
"""
[Workflow Name] - Modal Endpoint for n8n Integration

This endpoint handles [description] via the Hybrid Wrapper Strategy.
"""

import modal
from fastapi import Header, HTTPException

app = modal.App("[app-name]")

# Define dependencies
image = modal.Image.debian_slim().pip_install(
    "anthropic",  # or other packages
    "fastapi",
    "httpx",
    # Add all required packages
)


@app.function(
    image=image,
    secrets=[
        modal.Secret.from_name("api-auth-token"),
        modal.Secret.from_name("anthropic-api-key"),  # if needed
        # Add other secrets
    ],
    timeout=120,  # Adjust based on workflow complexity
)
@modal.fastapi_endpoint(method="POST")
def process_workflow(data: dict, authorization: str = Header(None)) -> dict:
    """
    Main endpoint for [workflow name].

    Input: {
        "field1": "description",
        "field2": "description"
    }

    Output: {
        "result": "description"
    }
    """
    import os
    import anthropic  # or other imports

    # ===== AUTHENTICATION =====
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

    # ===== INPUT VALIDATION =====
    required_fields = ["field1", "field2"]
    for field in required_fields:
        if field not in data:
            raise HTTPException(
                status_code=400,
                detail=f"Missing required field: {field}"
            )

    # ===== WORKFLOW LOGIC =====
    try:
        # Extract inputs
        field1 = data.get("field1")
        field2 = data.get("field2")

        # Implement workflow logic here
        # Example: Call Claude API
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": f"Process this: {field1}, {field2}"
            }],
            system="Your system prompt here"
        )

        result = message.content[0].text

        # Return clean JSON for n8n
        return {
            "result": result,
            "status": "success"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Processing error: {str(e)}"
        )
```

**Key Components:**
- ✅ Bearer token authentication
- ✅ Input validation
- ✅ Clear error handling
- ✅ Clean JSON output for n8n
- ✅ Proper HTTP status codes

---

### Step 4: Deployer Tests Locally

**Deployer Actions:**

**4.1 Run Local Test**
```bash
cd /path/to/project
modal run modal_app.py::process_workflow --data '{
  "field1": "test value 1",
  "field2": "test value 2"
}'
```

**4.2 Verify Output**
```json
{
  "result": "expected output",
  "status": "success"
}
```

**4.3 Test Authentication**
```bash
# Should fail without Bearer token
curl -X POST "http://localhost:..." \
  -H "Content-Type: application/json" \
  -d '{"field1": "test"}'

# Should succeed with Bearer token
curl -X POST "http://localhost:..." \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"field1": "test", "field2": "test"}'
```

**If ANY error occurs** → Invoke stuck agent immediately!

---

### Step 5: Deployer Deploys to Modal

**Deployer Actions:**

**5.1 Deploy Function**
```bash
modal deploy modal_app.py
```

**5.2 Capture Endpoint URL**
```
Deployment output will show:
✓ Created objects.
├── 🔨 Created function process_workflow.
└── 🔗 https://your-profile--app-name-process-workflow.modal.run
```

**5.3 Verify Deployment**
```bash
# Test deployed endpoint
curl -X POST "https://your-profile--app-name-process-workflow.modal.run" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "field1": "test value 1",
    "field2": "test value 2"
  }'
```

**If deployment fails** → Invoke stuck agent immediately!

---

### Step 6: Deployer Creates Handover Package

**Deployer Returns to Orchestrator:**

#### 6.1 Endpoint URL
```
https://your-profile--app-name-process-workflow.modal.run
```

#### 6.2 Bearer Token
```
7f3e9d2a1b4c5e6f8g9h0i1j2k3l4m5n6o7p8q9r0s1t2u3v4w5x6y7z8a9b0c1
```

#### 6.3 cURL Command (Ready to Paste)
```bash
curl -X POST "https://your-profile--app-name-process-workflow.modal.run" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 7f3e9d2a1b4c5e6f8g9h0i1j2k3l4m5n6o7p8q9r0s1t2u3v4w5x6y7z8a9b0c1" \
  -d '{
    "field1": "value1",
    "field2": "value2"
  }'
```

#### 6.4 n8n HTTP Request Node Configuration
```
Method: POST
URL: https://your-profile--app-name-process-workflow.modal.run

Authentication: Header Auth
  Name: Authorization
  Value: Bearer 7f3e9d2a1b4c5e6f8g9h0i1j2k3l4m5n6o7p8q9r0s1t2u3v4w5x6y7z8a9b0c1

Body Content Type: JSON
Body: {
  "field1": "{{ $json.field1 }}",
  "field2": "{{ $json.field2 }}"
}
```

#### 6.5 Input/Output Specification
```
INPUT:
{
  "field1": "string - description of field1",
  "field2": "string - description of field2"
}

OUTPUT:
{
  "result": "string - description of result",
  "status": "string - 'success' or 'error'"
}
```

#### 6.6 Example n8n Workflow Structure
```
[Trigger Node]
    ↓
[HTTP Request Node] ← Your Modal endpoint
    ↓
[Action Node]
```

---

### Step 7: Orchestrator Creates n8n Workflow (Optional)

If creating the complete n8n workflow:

**7.1 Create New Workflow in n8n**

**7.2 Add Trigger Node**
- Webhook trigger
- Schedule trigger
- Email trigger
- Form submission
- etc.

**7.3 Add HTTP Request Node**
- Use configuration from deployer's handover package
- Map trigger data to request body
- Test the connection

**7.4 Add Final Action Node**
- Send email (Gmail, SendGrid, etc.)
- Update CRM (HubSpot, Salesforce, etc.)
- Post to Slack
- Update database
- etc.

**7.5 Map Data**
```
Trigger Output → HTTP Request Input
HTTP Request Output → Final Action Input
```

**7.6 Test End-to-End**
- Execute workflow manually
- Verify trigger works
- Check endpoint is called correctly
- Confirm final action succeeds

**7.7 Activate Workflow**
- Turn on workflow in n8n
- Monitor for errors in n8n execution log

---

## Error Handling Protocol

**At ANY step, if errors occur:**

1. **STOP immediately**
2. **Document the error**:
   - Error message
   - Step where it occurred
   - What was attempted
   - Expected vs actual behavior
3. **Invoke stuck agent** using Task tool
4. **Wait for human guidance**
5. **Implement fix** based on human decision
6. **Document learning** for self-annealing

**Common Errors:**

| Error | Solution |
|-------|----------|
| Modal authentication fails | Check Token ID/Secret, reconfigure |
| Secret creation fails | Verify Modal account permissions |
| Local test fails | Debug Python code, check secrets |
| Deployment fails | Check Modal app name conflicts |
| Endpoint 401/403 | Verify Bearer token in request header |
| Endpoint 500 | Check logs, debug Python logic |
| n8n connection fails | Verify URL, authentication, test cURL |

---

## Definition of Done

**ALL of these must be true before marking complete:**

- ✅ Modal environment configured and authenticated
- ✅ Bearer token generated and stored as secret
- ✅ Python function written with proper authentication
- ✅ All dependencies included in image definition
- ✅ Local test passes successfully
- ✅ Deployed to Modal without errors
- ✅ Endpoint URL captured and verified
- ✅ cURL command tested and works
- ✅ Complete handover package delivered to orchestrator
- ✅ n8n HTTP Request configuration documented
- ✅ Input/output specification clear and accurate
- ✅ Optional: n8n workflow created and tested end-to-end

**If ANY item is incomplete, the deployment is NOT done!**

---

## Success Criteria

**For Deployer:**
- Returns complete handover package with all 6 components
- Endpoint is live and responds correctly
- Authentication works properly
- No errors in deployment process

**For Orchestrator:**
- Receives handover package from deployer
- Can test endpoint with cURL command
- Has everything needed for n8n integration
- Can provide client with working solution

**For Client:**
- Receives visual n8n workflow
- Can trigger workflow and see results
- Understands how to maintain workflow
- Has documentation for troubleshooting

---

## Client Handover Documentation

When handing off to client, provide:

### 1. n8n Workflow File
- Export workflow as JSON
- Include setup instructions
- Document required credentials

### 2. Endpoint Documentation
```markdown
# [Workflow Name] API Endpoint

## Endpoint URL
https://your-profile--app-name-process-workflow.modal.run

## Authentication
Bearer Token: [provide securely, not in documentation]

## Request Format
POST request with JSON body:
{
  "field1": "description",
  "field2": "description"
}

## Response Format
{
  "result": "description",
  "status": "success"
}

## Error Codes
- 400: Missing required field
- 401: Missing/invalid authorization header
- 403: Invalid authentication token
- 500: Processing error

## Testing
Use the provided cURL command to test:
[paste cURL command]

## Support
Contact: [your contact info]
```

### 3. Maintenance Guide
```markdown
# Maintenance Guide

## Monitoring
- Check n8n execution log for errors
- Monitor Modal app logs: `modal app logs app-name`

## Troubleshooting
- If endpoint returns 401/403: Check Bearer token
- If endpoint returns 500: Check Modal app logs
- If n8n workflow fails: Check execution details

## Updating
To update the workflow logic:
1. Modify modal_app.py
2. Run: modal deploy modal_app.py
3. Test with cURL command
4. No changes needed in n8n

## Credentials
Bearer Token stored in: [secure location]
To rotate token:
1. Generate new: openssl rand -hex 32
2. Update Modal secret: modal secret create api-auth-token API_AUTH_TOKEN=NEW_TOKEN
3. Update n8n HTTP Request node with new token
```

---

## Self-Annealing Notes

**Learnings to Document:**

When errors occur, capture:
- What caused the error
- How it was resolved
- Edge cases discovered
- Updates to make to this directive

**Common Issues Found:**
- [Document issues as they're discovered]
- [Update this section with solutions]
- [Build institutional knowledge]

---

## Related Files

- `.claude/agents/deployer.md` - Deployer subagent definition
- `.claude/CLAUDE.md` - Main orchestrator instructions (Phase 5)
- `templates/modal_app_template.py` - Modal function template
- `directives/modal-endpoint-guide.md` - Modal endpoint building guide

---

## Attribution

This workflow implements the **Hybrid Wrapper Strategy** from Nick Saraev's DOE Framework, combining:
- Visual no-code interfaces (n8n)
- Agentic Python logic (Modal)
- Secure HTTP communication
- Clean separation of concerns

**Result:** Clients get accessible workflows powered by sophisticated agentic logic!
