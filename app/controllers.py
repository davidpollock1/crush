from fastapi import APIRouter
from providers.provider_registry import get_provider, get_providers
from models.request_dtos import EmailRequest, SmsRequest

router = APIRouter()


@router.post("/sendMessage/")
async def sendMessage(request: EmailRequest | SmsRequest):
    provider = get_provider(request.channel)
    msg = await provider.send(request)
    return {"message": msg}


@router.get("/providers/")
async def providers():
    providers = get_providers()
    return {"Providers": providers}


@router.get("/health/")
async def health():
    return {"message": "get health called!"}
