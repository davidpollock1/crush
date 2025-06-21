from abc import ABC
import asyncio
from models.request_dtos import BaseRequest, EmailRequest, SmsRequest
from models.custom_exceptions import EmailSendFailure, SmsSendFailure
from services.email_service import send_email
from models.response_dtos import SendResult, StatusEnum
from app.logging_config import logging


class BaseProvider(ABC):
    async def send(self, request: BaseRequest):
        raise NotImplementedError


class EmailProvider(BaseProvider):
    async def send(self, request: EmailRequest) -> SendResult:
        try:
            await asyncio.to_thread(send_email, request)
            return SendResult(
                status=StatusEnum.SUCCESS,
                detail="Successfully sent message.",
                message_id="1234",
            )
        except Exception as e:
            logging.info(f"EmailProvider Send failed. {e}")
            raise EmailSendFailure(f"Email send failed.{e}")


class SmsProvider(BaseProvider):
    async def send(self, request: SmsRequest):
        try:
            # call to service to send email
            pass
        except Exception:
            raise SmsSendFailure
