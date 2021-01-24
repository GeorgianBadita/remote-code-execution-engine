from celery import Celery
from celery.utils.log import get_logger

# Create the celery app and get the logger
celery_app = Celery('code-executions-tasks', broker='pyamqp://guest@rabbit//', backend='amqp://guest@rabbit//')
logger = get_logger(__name__)


@celery_app.task
def add(x, y):
    res = x + y
    logger.info(f"{x}, {y}, res: {res}")

    return res


@celery_app.task
def execute_code(language: str, code: str) -> str:
    pass
