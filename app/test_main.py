from .main import app
from fastapi.testclient import TestClient
import json

client = TestClient(app)

base_email_request = {
    "channel": "email",
    "tags": ["string"],
    "to": ["user@example.com"],
    "cc": ["user@example.com"],
    "subject": "string",
    "body": "string",
}


def test_send_message_invalid_provider():
    email_request = base_email_request
    email_request["channel"] = "INVALID"

    response = client.post(json=email_request, url="/sendMessage/")
    assert response.status_code == 400
