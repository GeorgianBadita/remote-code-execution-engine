from fastapi import APIRouter, HTTPException
from fastapi.logger import logger

from remote_coding_compilation_engine import schemas
from remote_coding_compilation_engine.celery.celery_client import celery_client

router = APIRouter()


@router.post("/", response_model=schemas.ExecutionResult)
def create_executions(execution: schemas.Execution):

    try:
        logger.debug(f"Start code execution request with payload: {execution}")

        result = celery_client.send_task('worker.execute_code', args=(
            execution.language, execution.code, execution.timeout)).wait(timeout=None, interval=0.1)

        logger.debug(f"Code execution succeeded with result: {result}")
        return result
    except Exception as exc:
        logger.error(f"Worker could not execute code, error {exc}, payload: {execution}")
        raise HTTPException(status_code=500, detail="The server could not process the code execution")
