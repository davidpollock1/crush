# Pluggable Notification Service

## Overview

This project is a **lightweight otification gateway** built with **FastAPI**. It is designed to run as a lightweight service within a local network or on a cloud instance, enabling internal applications and services to send alerts via common channels like **email** and **Slack**.

The service exposes a single REST endpoint (`POST /sendMessage`) for dispatching notifications. Requests are validated using **Pydantic DTOs** and routed through a registry of channel providers.

---

## Features

- **Multi-Channel Support**: Send notifications via email or Slack.
- **Pluggable Architecture**: Easily extend the service by adding new providers.
- **Structured Validation**: Requests are validated using Pydantic models (`EmailRequest`, `SlackRequest`).
- **Error Handling**: Global exception handlers for known failures like `EmailSendFailure` and `SlackSendFailure`.
- **Configuration via Environment Variables**: Secrets and credentials are managed using `.env` files and Pydantic settings.
- **Extensibility**: Add new providers by extending `BaseProvider` and registering them in the service.

---

## Installation

### Prerequisites

- Python 3.10+
- SMTP server credentials for email notifications
- Slack bot token for Slack notifications

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/davidpollock1/crush.git
   cd crush
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Create a `.env` file in the project root.
   - Add your SMTP and Slack credentials (refer to the example `.env` file in the repository).

---

## Usage

### Endpoints

#### 1. **Send Msesage**

- **URL**: `POST /sendMessage/`
- **Description**: Dispatches a notification via the specified channel.
- **Request Body**:
  - For Email:
    ```json
    {
      "channel": "email",
      "tags": ["tag"],
      "to": ["user@example.com"],
      "cc": ["user@example.com"],
      "subject": "Notification Subject",
      "body": "Notification Body"
    }
    ```
  - For Slack:
    ```json
    {
      "channel": "slack",
      "tags": ["tag"],
      "slack_channel": "bot-updates",
      "body": "Notification Body",
      "bot_username": "Not Username"
    }
    ```
- **Response**:
  ```json
  {
    "status": "success",
    "detail": {
      "message_id": "1234"
    }
  }
  ```

#### 2. **Providers**

- **URL**: `GET /providers/`
- **Description**: Lists all registered notification providers.
- **Response**:
  ```json
  {
    "Providers": ["EmailProvider", "SlackProvider"]
  }
  ```

---

## Configuration

The service uses **Pydantic settings** to load configuration from `.env` files. Below is an example `.env` file:

```env
SMTP_HOST=yourHost
SMTP_PORT=8025
SMTP_USERNAME=example@gmail.com
SMTP_PASSWORD=app-specific-password
BASE_SENDER_EMAIL_ADDRESS=exampleEmail@ex81.com

SLACK_BOT_USER_TOKEN=your-bot-token
SLACK_BOT_DEFAULT_NAME=CRUSH-BOT
```

---

## Extending the Service

To add a new notification provider:

1. **Create a new provider class**:

   - Extend `BaseProvider` and implement the `send` method.

2. **Register the provider**:
   - Add the provider to `_provider_registry` in `providers/provider_registry.py`.

Example:

```python
class SMSProvider(BaseProvider):
    async def send(self, request: SMSRequest):
        # Implement SMS sending logic
        pass

_provider_registry[ChannelEnum.SMS] = SMSProvider()
```

---

## Testing

The project uses **pytest** for testing. To run the tests:

```bash
pytest
```

Test cases are located in `app/test_main.py`

---

## Dependencies

Key dependencies include:

- **FastAPI**: Web framework for building APIs.
- **Pydantic**: Data validation and settings management.
- **Slack SDK**: For Slack integration.
- **smtplib**: For email integration.

Refer to the `requirements.txt` file for the full list.

---
