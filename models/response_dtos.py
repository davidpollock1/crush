from typing import Optional
from pydantic import BaseModel
from enum import Enum


class StatusEnum(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"


class SendMessageResponse(BaseModel):
    status: StatusEnum


class SendResult(BaseModel):
    status: StatusEnum
    detail: Optional[str] = None
