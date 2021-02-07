from fastapi import APIRouter

from remote_code_execution_engine.api.api_v1.endpoints import evaluations, executions


api_router = APIRouter()

api_router.include_router(evaluations.router, prefix="/evaluations", tags=["evaluations"])
api_router.include_router(executions.router, prefix="/executions", tags=["executions"])
