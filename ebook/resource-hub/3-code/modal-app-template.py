"""
Modal Endpoint Template for DOE Framework Workflows
====================================================

This template provides a production-ready Modal endpoint with:
- Bearer token authentication
- Input validation
- Error handling
- JSON response format
- Secrets management

Usage:
1. Copy this file and rename it for your workflow
2. Update the app name and function name
3. Implement your workflow logic in the process_workflow function
4. Create Modal secrets: modal secret create my-app-secrets BEARER_TOKEN=...
5. Deploy: modal deploy your_app.py
"""

import modal
import os
import json
from datetime import datetime
from typing import Dict, Any

# Create Modal app with a descriptive name
app = modal.App("workflow-name")  # Change this to your workflow name

# Define the Modal function with secrets and timeout
@app.function(
    secrets=[modal.Secret.from_name("my-app-secrets")],  # Update secret name
    timeout=300  # 5 minutes - adjust based on your workflow duration
)
@modal.web_endpoint(method="POST")
def process_workflow(request_data: Dict[str, Any]) -> tuple[Dict[str, Any], int]:
    """
    Main workflow endpoint that processes incoming requests.

    Args:
        request_data: Dictionary containing the request payload

    Returns:
        Tuple of (response dict, HTTP status code)
    """

    # ===========================================
    # 1. AUTHENTICATION
    # ===========================================

    auth_header = request_data.get("auth_token", "")
    expected_token = os.environ.get("BEARER_TOKEN")

    if not expected_token:
        return {
            "success": False,
            "error": "Server configuration error: BEARER_TOKEN not set"
        }, 500

    if auth_header != expected_token:
        return {
            "success": False,
            "error": "Unauthorized - invalid or missing auth token"
        }, 401

    # ===========================================
    # 2. INPUT VALIDATION
    # ===========================================

    # Define required fields for your workflow
    required_fields = ["input_field_1", "input_field_2"]  # Update these

    missing_fields = [field for field in required_fields if field not in request_data]

    if missing_fields:
        return {
            "success": False,
            "error": f"Missing required fields: {', '.join(missing_fields)}"
        }, 400

    # Extract and validate input data
    try:
        # Update these based on your workflow's inputs
        input_1 = request_data.get("input_field_1")
        input_2 = request_data.get("input_field_2")

        # Add your validation logic here
        if not input_1 or not isinstance(input_1, str):
            return {
                "success": False,
                "error": "input_field_1 must be a non-empty string"
            }, 400

    except Exception as e:
        return {
            "success": False,
            "error": f"Input validation error: {str(e)}"
        }, 400

    # ===========================================
    # 3. WORKFLOW LOGIC
    # ===========================================

    try:
        # REPLACE THIS SECTION with your actual workflow logic
        # Examples:
        # - Call Claude API for AI processing
        # - Scrape web data with Playwright
        # - Transform data
        # - Query databases
        # - Call third-party APIs

        result = {
            "processed_data": f"Processed: {input_1}",
            "timestamp": datetime.now().isoformat(),
            "status": "completed"
        }

        # Your workflow logic here
        # result = your_processing_function(input_1, input_2)

        # ===========================================
        # 4. SUCCESS RESPONSE
        # ===========================================

        return {
            "success": True,
            "data": result,
            "processed_at": datetime.now().isoformat()
        }, 200

    except Exception as e:
        # ===========================================
        # 5. ERROR HANDLING
        # ===========================================

        # Log the error (Modal will capture this in logs)
        print(f"ERROR: {type(e).__name__}: {str(e)}")

        # Return user-friendly error
        return {
            "success": False,
            "error": f"Processing failed: {str(e)}",
            "error_type": type(e).__name__
        }, 500


# ===========================================
# HELPER FUNCTIONS (add your own)
# ===========================================

def your_processing_function(input_1: str, input_2: str) -> Dict[str, Any]:
    """
    Replace this with your actual workflow logic.

    Args:
        input_1: First input parameter
        input_2: Second input parameter

    Returns:
        Dictionary with processing results
    """
    # Your implementation here
    return {"result": "placeholder"}


# ===========================================
# LOCAL TESTING (optional)
# ===========================================

def test_locally():
    """
    Test the endpoint locally before deploying to Modal.
    Run with: python your_app.py
    """
    test_payload = {
        "auth_token": "test_token_123",  # Use your actual token for testing
        "input_field_1": "test value 1",
        "input_field_2": "test value 2"
    }

    # Set environment variable for testing
    os.environ["BEARER_TOKEN"] = "test_token_123"

    response, status_code = process_workflow(test_payload)
    print(f"Status: {status_code}")
    print(f"Response: {json.dumps(response, indent=2)}")


if __name__ == "__main__":
    # Run local test
    test_locally()


# ===========================================
# DEPLOYMENT INSTRUCTIONS
# ===========================================

"""
STEP 1: Create Modal Secrets
-----------------------------
modal secret create my-app-secrets \
    BEARER_TOKEN="your_generated_token_here" \
    ANTHROPIC_API_KEY="your_api_key_if_needed"

Generate a secure bearer token with:
python -c "import secrets; print(secrets.token_urlsafe(32))"


STEP 2: Deploy to Modal
------------------------
modal deploy your_app.py

Modal will return your endpoint URL:
https://username--app-name-function.modal.run


STEP 3: Test with cURL
-----------------------
curl -X POST https://username--app-name-function.modal.run \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_token_here" \
  -d '{
    "auth_token": "your_token_here",
    "input_field_1": "test value",
    "input_field_2": "test value"
  }'


STEP 4: Connect to n8n (Hybrid Wrapper)
----------------------------------------
In n8n:
1. Add HTTP Request node
2. Method: POST
3. URL: [your Modal endpoint URL]
4. Authentication: Header Auth
   - Name: Authorization
   - Value: Bearer your_token_here
5. Body: JSON with your input fields


STEP 5: Monitor Logs
---------------------
modal app logs your-app-name --follow
"""
