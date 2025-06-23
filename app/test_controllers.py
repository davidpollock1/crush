from fastapi.testclient import TestClient
from .controllers import router
from .main import app
import json

# Python

client = TestClient(app)

base_email_request = {
    "channel": "email",
    "tags": ["string"],
    "to": ["user@example.com"],
    "cc": ["user@example.com"],
    "subject": "string",
    "body": "string",
}


def test_send_message_valid_email():
    email_request = base_email_request.copy()
    email_request["channel"] = "email"

    response = client.post(
        json=email_request, headers={"X-Token": "hailhydra"}, url="/sendMessage/"
    )
    assert response.status_code == 200
    assert "status" in response.json()


def test_send_message_invalid_channel():
    email_request = {
        "channel": "INVALID",
        "tags": "",
        "to": "user@example.com",
        "cc": "user@example.com",
        "subject": "Test Subject",
        "body": "Test Body",
    }

    response = client.post(url="/sendMessage/", content=json.dumps(email_request))
    assert response.status_code == 422


def test_providers_endpoint():
    response = client.get(url="/providers/")
    assert response.status_code == 200
    assert "Providers" in response.json()


def test_health_endpoint():
    response = client.get(url="/health/")
    assert response.status_code == 200
    assert response.json() == {"Message": "get health called!"}
