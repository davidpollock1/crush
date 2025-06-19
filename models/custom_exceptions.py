class ProviderNotFound(Exception):
    def __init__(self, message: str):
        self.message = message


class EmailSendFailure(Exception):
    def __init__(self, message: str):
        self.message = message


class SmsSendFailure(Exception):
    def __init__(self, message: str):
        self.message = message
