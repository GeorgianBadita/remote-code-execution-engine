import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(10)

    PROJECT_NAME: str = "RemoteCodingCompilatonEngine"


settings = Settings()
