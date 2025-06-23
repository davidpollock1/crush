from typing import Optional
from pydantic import BaseModel
from enum import Enum


class StatusEnum(str, Enum):
    SUCCESS = "success"
    PARTIAL_SUCCESS = "partial_success"
    PENDING = "pending"
    FAILURE = "failure"


class SendMessageResponse(BaseModel):
    status: StatusEnum
    detail: Optional[dict]


class SendResult(BaseModel):
    status: StatusEnum
    detail: Optional[dict] = None
    message_id: Optional[str] = None
