from typing import Optional
from pydantic import BaseModel, EmailStr
from enum import Enum


class ChannelEnum(str, Enum):
    EMAIL = "email"
    SLACK = "slack"


class BaseRequest(BaseModel):
    channel: ChannelEnum
    tags: Optional[list[str]] = None


class EmailRequest(BaseRequest):
    to: list[EmailStr]
    cc: Optional[list[EmailStr]] = None
    subject: str
    body: str


class SlackRequest(BaseRequest):
    slack_channel: str
    body: str
    bot_username: Optional[str]
