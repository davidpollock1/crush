class ProviderNotFound(Exception):
    def __init__(self, message: str):
        self.message = message


class EmailSendFailure(Exception):
    def __init__(self, message: str):
        self.message = message


class SlackSendFailure(Exception):
    def __init__(self, message: str):
        self.message = message
