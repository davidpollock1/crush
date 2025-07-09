from slack_sdk.web.async_client import AsyncWebClient
from app.settings import get_settings
from models.request_dtos import SlackRequest


settings = get_settings()
client = AsyncWebClient(token=settings.slack_bot_user_token)


async def send_slack_message(request: SlackRequest):
    """
    Sends a message to the slack channel specified in the request using the slack_sdk.
    Args:
        request (SlackRequest): A SlackRequest object.

    Returns: A SlackResponse object from the slack_sdk.
    """
    if not request.bot_username:
        request.bot_username = settings.slack_bot_default_name

    response = await client.chat_postMessage(
        channel=request.slack_channel, text=request.body, username=request.bot_username
    )

    return response
