from abc import ABC
from models.request_dtos import BaseRequest, EmailRequest, SmsRequest
from models.custom_exceptions import EmailSendFailure, SmsSendFailure


class BaseProvider(ABC):
    async def send(self, request: BaseRequest):
        raise NotImplementedError


class EmailProvider(BaseProvider):
    async def send(self, request: EmailRequest):
        try:
            # call to service to send email.
            pass

        except Exception:
            raise EmailSendFailure("Email send failed. ")


class SmsProvider(BaseProvider):
    async def send(self, request: SmsRequest):
        try:
            # call to service to send email
            pass
        except Exception:
            raise SmsSendFailure
