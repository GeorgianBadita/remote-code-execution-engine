import uuid

from fastapi import APIRouter, HTTPException
from fastapi.logger import logger

from remote_coding_compilation_engine import schemas
from remote_coding_compilation_engine.celery.celery_client import celery_client
from remote_coding_compilation_engine.submission_helper.result_extractors import python_result_extractor

router = APIRouter()


@router.post("/", response_model=schemas.SubmissionResult)
def create_submission(execution: schemas.Execution):
    try:
        logger.debug(f"Start code submission request with payload: {execution}")

        result = celery_client.send_task('worker.execute_code', args=(
            execution.language, execution.code, execution.timeout)).wait(timeout=None, interval=0.1)

        result['submission_id'] = str(uuid.uuid4())
        if not result['has_error']:
            result['results'] = python_result_extractor(result['raw_output'])
        else:
            result['results'] = []

        logger.debug(f"Code submission succeeded with result: {result}")

        return result
    except ValueError as vle:
        logger.error(f"Invalid raw output test format, error: {str(vle)}")
        raise HTTPException(status_code=400, detail="Invalid test code format")
    except Exception as exc:
        logger.error(f"Worker could not process submission, error {exc}, payload: {execution}")
        raise HTTPException(status_code=500, detail="The server could not process the code execution")
