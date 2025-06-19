from fastapi import FastAPI
from providers.provider_registry import get_provider
from models.request_dtos import EmailRequest, SmsRequest

app = FastAPI()


@app.post("/sendMessage/")
async def sendMessage(request: EmailRequest | SmsRequest):
    provider = get_provider(request.channel)
    msg = provider.send(request)
    return {"message": msg}


@app.get("/providers/")
async def providers():
    return {"message": "get providers called!"}


@app.get("/health/")
async def health():
    return {"message": "get health called!"}
