from .main import app
from fastapi.testclient import TestClient

client = TestClient(app)

base_email_request = {
    "channel": "email",
    "tags": ["string"],
    "to": ["user@example.com"],
    "cc": ["user@example.com"],
    "subject": "string",
    "body": "string",
}

base_slack_request = {
    "channel": "slack",
    "tags": ["tag"],
    "slack_channel": "bot-updates",
    "body": "Notification Body",
    "bot_username": "Not Username",
}


class TestSendMessageEndpoint:
    def test_send_message_invalid_provider(self):
        email_request = (
            base_email_request.copy()
        )  # Use copy to avoid modifying the original
        email_request["channel"] = "INVALID"

        response = client.post(json=email_request, url="/sendMessage/")
        assert response.status_code == 422  # Pydantic validation error for invalid enum

    def test_send_slack_message(self):
        slack_request = base_slack_request.copy()

        response = client.post(json=slack_request, url="/sendMessage/")
        assert response.status_code == 200

    def test_send_email(self):
        email_request = base_email_request.copy()

        response = client.post(json=email_request, url="/sendMessage/")
        assert response.status_code == 200

    def test_providers_endpoint(self):
        response = client.get(url="/providers/")
        assert response.status_code == 200
        assert "Providers" in response.json()
