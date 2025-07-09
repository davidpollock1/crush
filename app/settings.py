import tomli
from functools import lru_cache
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    smtp_host: str
    smtp_port: int
    smtp_username: str
    smtp_password: str
    base_send_email_address: str
    slack_bot_default_name: str
    slack_bot_user_token: str | None = os.environ.get("SLACK_BOT_USER_TOKEN")


@lru_cache
def get_settings(path: str = "config.toml") -> Settings:
    with open(path, "rb") as f:
        data = tomli.load(f)
    return Settings(**data)
