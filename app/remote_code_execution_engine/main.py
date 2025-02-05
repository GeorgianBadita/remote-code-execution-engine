from fastapi import FastAPI

from remote_code_execution_engine.core.config import settings
from remote_code_execution_engine.api.api_v1.api import api_router

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)
