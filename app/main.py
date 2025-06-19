from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .controllers import router
from models.custom_exceptions import EmailSendFailure, SmsSendFailure, ProviderNotFound

app = FastAPI()


@app.exception_handler(EmailSendFailure)
async def email_failure_handler(request: Request, exc: EmailSendFailure):
    return JSONResponse(
        status_code=502,
        content={"detail": exc.message},
    )


@app.exception_handler(ProviderNotFound)
async def provider_not_found(request: Request, exc: ProviderNotFound):
    return JSONResponse(status_code=502, content={"detail": exc.message})


@app.exception_handler(SmsSendFailure)
async def sms_failure_handler(request: Request, exc: SmsSendFailure):
    return JSONResponse(status_code=502, content={"detail": exc.message})


app.include_router(router)
