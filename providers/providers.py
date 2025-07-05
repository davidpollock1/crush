from abc import ABC
import asyncio
from models.request_dtos import BaseRequest, EmailRequest, SlackRequest
from models.custom_exceptions import EmailSendFailure, SlackSendFailure
from services.email_service import send_email
from services.slack_service import send_slack_message
from models.response_dtos import SendResult, StatusEnum
from app.logging_config import logging
from typing import TypeVar, Generic

T = TypeVar("T", bound=BaseRequest)


class BaseProvider(ABC, Generic[T]):
    async def send(self, request: T):
        raise NotImplementedError


class EmailProvider(BaseProvider[EmailRequest]):
    async def send(self, request: EmailRequest) -> SendResult:
        try:
            response = await asyncio.to_thread(send_email, request)
            send_result = SendResult(status=StatusEnum.PENDING)

            if not response:
                send_result.status = StatusEnum.SUCCESS
            else:
                send_result.status = StatusEnum.PARTIAL_SUCCESS
                send_result.detail = response

            return send_result
        except Exception as e:
            logging.info(f"EmailProvider Send failed. {e}")
            raise EmailSendFailure(f"Email send failed.{e}")


class SlackProvider(BaseProvider[SlackRequest]):
    async def send(self, request: SlackRequest):
        try:
            response = await send_slack_message(request)

            send_result = SendResult(status=StatusEnum.PENDING)

            if response.validate():
                send_result.status = StatusEnum.SUCCESS
                send_result.detail = response.get("message")
            else:
                send_result.status = StatusEnum.FAILURE
                send_result.detail = response.get("message")

            return send_result
        except Exception as e:
            logging.info(f"SlackProvider Send failed. {e}")
            raise SlackSendFailure(f"Slack send failed. {e}")
