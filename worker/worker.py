import logging
import subprocess
from typing import Optional

from celery import Celery
from celery.utils.log import get_logger

from code_execution.code_execution import CodeExcution
from utils import generate_random_file


tmp_dir_path = '/worker/tmp'
compiled_dir_path = '/worker/tmp/compiled_files'

# Create the celery app and get the logger
celery_app = Celery('code-executions-tasks',
                    broker='pyamqp://guest@rabbit//', backend='amqp://guest@rabbit//')

# Add CELERY_ACKS_LATE in order to wait for infinite loop code executions
# celery_app.conf.update(
#     CELERY_ACKS_LATE=True
# )

logger = get_logger(__name__)


@celery_app.task
def execute_code(language: str, code: str, timeout: Optional[float] = 10) -> str:
    """
    Task for code execution

    @param language: code programming language
    @param code: code to be executed
    @param timeout: maximum time the code is allowed to run

    @return: dict containgin execution results
    """

    logger.info("Starting code execution")

    in_file_path = (f"{tmp_dir_path}/in_files/{generate_random_file()}."
                    f"{CodeExcution.get_lang_extension(language)}")

    compiled_file = f'{compiled_dir_path}/{generate_random_file()}.out'

    command_to_execute_code = CodeExcution.provide_code_execution_command(
        in_file_path, language, compiled_file)

    default_dict = {
        "has_error": False,
        "out_of_resources": False,
        "exit_code": 0,
        "out_of_time": False,
        "raw_output": ""
    }

    try:
        code_output = CodeExcution.execute_code(
            command_to_execute_code, in_file_path, compiled_file, code, timeout)
        logging.info(f"Code Returned, result: {code_output}")

        default_dict["raw_output"] = code_output
    except subprocess.CalledProcessError as cpe:
        logging.debug(f"Code execution was errored: {cpe}")

        default_dict["has_error"] = True
        default_dict["exit_code"] = cpe.returncode
        default_dict["raw_output"] = cpe.output
    except subprocess.TimeoutExpired as te:
        logger.debug(f"Code timeout after: {te.timeout}")

        default_dict["has_error"] = True
        default_dict["exit_code"] = 124
        default_dict["out_of_time"] = True
        default_dict["raw_output"] = "Time Limit Exceeded"

    return default_dict
