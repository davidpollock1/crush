from typing import Dict
from models.request_dtos import ChannelEnum
from providers.providers import BaseProvider, EmailProvider, SmsProvider

_provider_registry: Dict[ChannelEnum, BaseProvider] = {
    ChannelEnum.EMAIL: EmailProvider(),
    ChannelEnum.SMS: SmsProvider(),
}


def get_provider(channel: ChannelEnum) -> BaseProvider:
    provider = _provider_registry.get(channel)
    if not provider:
        raise NotImplementedError

    return provider

def get_providers() -> list[BaseProvider]:
    providers = []
    for provider in _provider_registry:
        providers.append(provider)
        
    return providers