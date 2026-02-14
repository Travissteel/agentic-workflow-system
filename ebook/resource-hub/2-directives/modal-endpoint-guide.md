# Modal Endpoint Development Guide

**Purpose**: Reference guide for building production-ready Modal API endpoints for agentic workflows

---

## Overview

Modal is a serverless Python platform that lets you deploy functions as HTTP endpoints without managing infrastructure. This guide covers best practices for building secure, scalable endpoints that integrate seamlessly with n8n workflows in the Hybrid Wrapper Strategy.

---

## Basic Modal Endpoint Template

```python
import modal
from fastapi import Header, HTTPException
import os

app = modal.App("my-workflow")

# Define the container image with dependencies
image = modal.Image.debian_slim().pip_install(
    "anthropic==0.18.0",
    "fastapi==0.109.0",
    "pydantic==2.5.0",
)

@app.function(
    image=image,
    secrets=[modal.Secret.from_name("api-auth-token")],
    timeout=180,  # 3 minutes
)
@modal.fastapi_endpoint(method="POST")
def process_workflow(
    data: dict,
    authorization: str = Header(None)
) -> dict:
    """
    Main workflow endpoint with Bearer token authentication.

    Args:
        data: JSON payload with workflow inputs
        authorization: Bearer token from Authorization header

    Returns:
        dict: {"success": bool, "data": dict, "error": str}
    """

    # Step 1: Authenticate request
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

    # Step 2: Validate inputs
    required_fields = ["field1", "field2"]
    for field in required_fields:
        if field not in data:
            return {
                "success": False,
                "error": f"Missing required field: {field}"
            }

    # Step 3: Execute workflow logic
    try:
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

def do_the_work(data: dict) -> dict:
    """
    Your actual workflow logic goes here.
    Keep this separate from the endpoint for easier testing.
    """
    # Implementation here
    return {"result": "success"}
```

---

## Authentication Patterns

### Bearer Token Authentication (Recommended)

**Setup:**
```bash
# Generate secure token
openssl rand -hex 32

# Create Modal secret
modal secret create api-auth-token API_AUTH_TOKEN=your_generated_token
```

**Endpoint code:**
```python
@app.function(secrets=[modal.Secret.from_name("api-auth-token")])
@modal.fastapi_endpoint(method="POST")
def secure_endpoint(data: dict, authorization: str = Header(None)) -> dict:
    import os

    expected = os.environ.get("API_AUTH_TOKEN")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing authorization")

    token = authorization.replace("Bearer ", "")
    if token != expected:
        raise HTTPException(status_code=403, detail="Invalid token")

    # Proceed with authenticated request
    return {"success": True, "data": "..."}
```

**Client usage (cURL):**
```bash
curl -X POST https://endpoint.modal.run \
  -H "Authorization: Bearer your_generated_token" \
  -H "Content-Type: application/json" \
  -d '{"data": "value"}'
```

**Client usage (n8n):**
- HTTP Request Node
- Authentication: Generic Credential Type → Header Auth
- Name: `Authorization`
- Value: `Bearer your_generated_token`

---

## Input Validation

### Required Field Validation

```python
def validate_inputs(data: dict) -> dict:
    """
    Validate required fields and return error if missing.

    Returns dict with 'valid' bool and 'error' message if invalid.
    """
    required = ["name", "email", "company"]

    for field in required:
        if field not in data or not data[field]:
            return {
                "valid": False,
                "error": f"Missing required field: {field}"
            }

    return {"valid": True}

# In endpoint:
validation = validate_inputs(data)
if not validation["valid"]:
    return {
        "success": False,
        "error": validation["error"]
    }
```

### Type Validation

```python
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class WorkflowInput(BaseModel):
    """Define expected input structure with type validation."""
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    company: str
    phone: Optional[str] = None

@modal.fastapi_endpoint(method="POST")
def typed_endpoint(input_data: WorkflowInput) -> dict:
    """FastAPI automatically validates against the Pydantic model."""
    # If we reach here, data is valid
    return {
        "success": True,
        "data": {
            "name": input_data.name,
            "email": input_data.email
        }
    }
```

---

## Error Handling

### Comprehensive Error Handling

```python
@modal.fastapi_endpoint(method="POST")
def robust_endpoint(data: dict, authorization: str = Header(None)) -> dict:
    try:
        # Authentication
        validate_auth(authorization)

        # Input validation
        if "required_field" not in data:
            return {"success": False, "error": "Missing required_field"}

        # External API call
        try:
            api_result = call_external_api(data)
        except requests.Timeout:
            return {
                "success": False,
                "error": "External API timed out. Please try again."
            }
        except requests.HTTPError as e:
            return {
                "success": False,
                "error": f"External API error: {e.response.status_code}"
            }

        # Process result
        result = process_data(api_result)

        return {"success": True, "data": result}

    except HTTPException:
        # Re-raise HTTP exceptions (authentication failures)
        raise

    except Exception as e:
        # Catch-all for unexpected errors
        print(f"Unexpected error: {str(e)}")  # Logs to Modal
        return {
            "success": False,
            "error": "An unexpected error occurred. Please contact support."
        }
```

### Error Response Standards

Always return this structure:
```python
# Success
{
    "success": True,
    "data": {
        "result": "...",
        "metadata": {...}
    }
}

# Error
{
    "success": False,
    "error": "Clear, actionable error message"
}
```

---

## Working with External APIs

### Using Anthropic (Claude)

```python
image = modal.Image.debian_slim().pip_install("anthropic==0.18.0")

@app.function(
    image=image,
    secrets=[
        modal.Secret.from_name("anthropic-api-key"),
        modal.Secret.from_name("api-auth-token")
    ]
)
@modal.fastapi_endpoint(method="POST")
def ai_endpoint(data: dict, authorization: str = Header(None)) -> dict:
    import os
    from anthropic import Anthropic

    # Authenticate endpoint
    validate_auth(authorization)

    # Initialize Claude
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    # Call Claude
    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": data["prompt"]
        }]
    )

    return {
        "success": True,
        "data": {
            "response": response.content[0].text
        }
    }
```

### Using OpenAI

```python
image = modal.Image.debian_slim().pip_install("openai==1.10.0")

@app.function(
    image=image,
    secrets=[
        modal.Secret.from_name("openai-api-key"),
        modal.Secret.from_name("api-auth-token")
    ]
)
@modal.fastapi_endpoint(method="POST")
def openai_endpoint(data: dict, authorization: str = Header(None)) -> dict:
    import os
    from openai import OpenAI

    validate_auth(authorization)

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": data["prompt"]}
        ]
    )

    return {
        "success": True,
        "data": {
            "response": response.choices[0].message.content
        }
    }
```

---

## Timeout Configuration

### Setting Appropriate Timeouts

```python
@app.function(
    timeout=60     # 1 minute - quick API calls
)

@app.function(
    timeout=180    # 3 minutes - standard AI generation
)

@app.function(
    timeout=600    # 10 minutes - heavy data processing
)
```

**Guidelines:**
- Simple data transformation: 30-60 seconds
- AI generation (single prompt): 60-180 seconds
- Web scraping (single page): 60-120 seconds
- Batch processing: 300-600 seconds
- Maximum allowed: 900 seconds (15 minutes)

---

## Secrets Management

### Creating Secrets

```bash
# Authentication token
modal secret create api-auth-token \
  API_AUTH_TOKEN=your_token_here

# AI API keys
modal secret create anthropic-api-key \
  ANTHROPIC_API_KEY=sk-ant-...

modal secret create openai-api-key \
  OPENAI_API_KEY=sk-...

# Database credentials
modal secret create database-creds \
  DB_HOST=host \
  DB_USER=user \
  DB_PASS=pass
```

### Using Secrets in Code

```python
@app.function(
    secrets=[
        modal.Secret.from_name("api-auth-token"),
        modal.Secret.from_name("anthropic-api-key"),
        modal.Secret.from_name("database-creds")
    ]
)
@modal.fastapi_endpoint(method="POST")
def multi_secret_endpoint(data: dict) -> dict:
    import os

    # Access secrets via environment variables
    auth_token = os.environ["API_AUTH_TOKEN"]
    ai_key = os.environ["ANTHROPIC_API_KEY"]
    db_host = os.environ["DB_HOST"]

    # Use them in your logic
    return {"success": True}
```

---

## Testing Modal Functions

### Local Testing

```bash
# Test function locally before deploying
modal run app.py::function_name

# With sample data
modal run app.py::function_name --data '{"field": "value"}'
```

### Testing Deployed Endpoints

```bash
# Deploy first
modal deploy app.py

# Test with cURL
curl -X POST https://your-endpoint.modal.run \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token" \
  -d '{"test": "data"}'

# Verbose output for debugging
curl -X POST https://your-endpoint.modal.run \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token" \
  -d '{"test": "data"}' \
  -v
```

---

## Deployment Commands

```bash
# Deploy to production
modal deploy app.py

# Deploy specific function
modal deploy app.py::function_name

# View deployed apps
modal app list

# View logs (live tail)
modal app logs my-app --follow

# View recent logs
modal app logs my-app -n 100

# Stop an app
modal app stop my-app

# Delete an app
modal app delete my-app
```

---

## Common Patterns

### Pattern 1: Data Enrichment Endpoint

```python
@app.function(
    image=modal.Image.debian_slim().pip_install("requests==2.31.0"),
    secrets=[modal.Secret.from_name("api-auth-token")],
    timeout=120
)
@modal.fastapi_endpoint(method="POST")
def enrich_lead(data: dict, authorization: str = Header(None)) -> dict:
    """Enrich lead data from external API."""
    import requests

    validate_auth(authorization)

    if "email" not in data:
        return {"success": False, "error": "Missing email"}

    # Call enrichment API
    response = requests.get(
        f"https://api.enrichment.com/lookup?email={data['email']}",
        timeout=10
    )

    if response.status_code == 200:
        enriched = response.json()
        return {"success": True, "data": enriched}
    else:
        return {"success": False, "error": "Enrichment failed"}
```

### Pattern 2: Web Scraping Endpoint

```python
@app.function(
    image=modal.Image.debian_slim().pip_install(
        "playwright==1.40.0",
        "beautifulsoup4==4.12.0"
    ),
    secrets=[modal.Secret.from_name("api-auth-token")],
    timeout=300
)
@modal.fastapi_endpoint(method="POST")
def scrape_page(data: dict, authorization: str = Header(None)) -> dict:
    """Scrape data from a webpage."""
    from playwright.sync_api import sync_playwright
    from bs4 import BeautifulSoup

    validate_auth(authorization)

    if "url" not in data:
        return {"success": False, "error": "Missing url"}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(data["url"])

        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, 'html.parser')
    # Extract data...

    return {"success": True, "data": {"extracted": "data"}}
```

---

## Best Practices

**✅ DO:**
- Always implement authentication
- Validate all inputs
- Return consistent JSON structure
- Pin dependency versions
- Use try/except for external API calls
- Log errors for debugging
- Set appropriate timeouts
- Test locally before deploying

**❌ DON'T:**
- Hardcode secrets in code
- Skip input validation
- Return raw stack traces to clients
- Use unpinned dependencies
- Assume external APIs will always work
- Deploy without testing
- Ignore timeout limits

---

## Troubleshooting

**Problem: `ModuleNotFoundError`**
- **Solution**: Add package to image `.pip_install()` list

**Problem: `Secret not found`**
- **Solution**: Verify secret name matches exactly: `modal secret list`

**Problem: Timeout errors**
- **Solution**: Increase timeout in `@app.function(timeout=X)`

**Problem: 401/403 errors**
- **Solution**: Check Bearer token format: `Authorization: Bearer token`

---

**Related Resources:**
- `hybrid-wrapper-deployment.md`: Full deployment workflow
- `deployer-agent.md`: Deployer agent specification
- `modal-app-template.py`: Complete working template
- Appendix D: Modal Deployment Checklist
