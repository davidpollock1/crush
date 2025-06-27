from fastapi import APIRouter
from providers.provider_registry import get_provider, get_providers
from models.request_dtos import EmailRequest, SlackRequest
from models.response_dtos import SendMessageResponse

router = APIRouter()


@router.post("/sendMessage/", response_model=SendMessageResponse)
async def sendMessage(request: EmailRequest | SlackRequest):
    provider = get_provider(request.channel)
    result = await provider.send(request)
    return SendMessageResponse(status=result.status, detail=result.detail)


@router.get("/providers/")
async def providers():
    providers = get_providers()
    return {"Providers": providers}
