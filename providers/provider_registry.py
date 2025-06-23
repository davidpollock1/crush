from typing import Dict
from models.request_dtos import ChannelEnum
from providers.providers import BaseProvider, EmailProvider, SlackProvider
from models.custom_exceptions import ProviderNotFound

_provider_registry: Dict[ChannelEnum, BaseProvider] = {
    ChannelEnum.EMAIL: EmailProvider(),
    ChannelEnum.SLACK: SlackProvider(),
}


def get_provider(channel: ChannelEnum) -> BaseProvider:
    provider = _provider_registry.get(channel)
    if not provider:
        raise ProviderNotFound("Provider not found. ")

    return provider


def get_providers() -> list[BaseProvider]:
    providers = []
    for provider in _provider_registry:
        providers.append(provider)

    return providers
