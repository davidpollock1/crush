from typing import Optional
from pydantic import BaseModel, EmailStr
from enum import Enum


class ChannelEnum(str, Enum):
    EMAIL = "email"
    SMS = "sms"

class BaseRequest(BaseModel):
    channel: ChannelEnum
    tags: Optional[list[str]] = None
    metadata: Optional[dict] = None


class EmailRequest(BaseRequest):
    to: list[EmailStr]
    cc: Optional[list[EmailStr]] = None
    subject: str
    body: str


class SmsRequest(BaseRequest):
    to: list[str]
    body: str
    image: Optional[str] = None
