from abc import ABC
from models.request_dtos import BaseRequest, EmailRequest, SmsRequest


class BaseProvider(ABC):
    def send(self, request: BaseRequest):
        raise NotImplementedError


class EmailProvider(BaseProvider):
    def send(self, request: EmailRequest):
        return "called send on EmailProvider"


class SmsProvider(BaseProvider):
    def send(self, request: SmsRequest):
        return "called send on SmsProvider"
