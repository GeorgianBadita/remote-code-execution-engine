from fastapi import APIRouter
from celery import Celery

from remote_coding_compilation_engine import schemas

router = APIRouter()

celery_app = Celery('code-executions-tasks', broker='pyamqp://guest@rabbit//', backend='amqp://guest@rabbit//')


@router.post("/", response_model=schemas.ExecutionResult)
def create_executions(execution: schemas.Execution):
    result = celery_app.send_task('worker.add', args=(1, 2)).wait(timeout=None, interval=0.1)
    return {
        "has_error": False,
        "out_of_resources": False,
        "exit_code": result,
        "out_of_time": False,
        "raw_output": ""
    }
