from fastapi import APIRouter

from remote_coding_compilation_engine.api.api_v1.endpoints import submissions, executions


api_router = APIRouter()

api_router.include_router(submissions.router, prefix="/submissions", tags=["submissions"])
api_router.include_router(executions.router, prefix="/executions", tags=["executions"])
