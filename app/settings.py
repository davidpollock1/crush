from functools import lru_cache
from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env"))
    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_USERNAME: EmailStr
    SMTP_PASSWORD: str
    BASE_SENDER_EMAIL_ADDRESS: str
    SLACK_BOT_USER_TOKEN: str
    SLACK_BOT_DEFAULT_NAME: str


@lru_cache
def get_settings() -> Settings:
    return Settings()
