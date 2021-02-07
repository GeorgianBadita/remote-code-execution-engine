import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from remote_code_execution_engine import schemas


@pytest.fixture
def app() -> FastAPI:
    """
    Fixture for new testing application
    """
    from remote_code_execution_engine.main import app
    return app


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    """
    FastAPI client fixture
    """

    return TestClient(app)


class MockWaitNoError():

    def wait(self, **kwargs):
        return {
            "has_error": False,
            "out_of_resources": False,
            "exit_code": 0,
            "out_of_time": False,
            "raw_output": "Hello World"
        }


class MockWaitNoErrorSubmission():
    def wait(self, **kwargs):
        return {
            "has_error": False,
            "out_of_resources": False,
            "exit_code": 0,
            "out_of_time": False,
            "raw_output": "  ..\n"
        }


class MockWaitRaises():

    def wait(self, **kwargs):
        raise Exception


@pytest.fixture
def mock_send_task_no_error() -> callable:
    """
    Fixture for mocking the send task function from celery client
    """
    def mock_send(task_name: str, args: tuple = ()) -> MockWaitNoError:
        return MockWaitNoError()

    return mock_send


@pytest.fixture
def mock_send_task_raise() -> MockWaitRaises:
    """
    Fixture for mocking the send task function from celery client
    """
    def mock_send(task_name: str, args: tuple = ()) -> MockWaitRaises:
        return MockWaitRaises()

    return mock_send


@pytest.fixture
def execution() -> schemas.Execution:
    return {
        "language": "python",
        "code": "print('Hello World')"
    }


@pytest.fixture
def create_hello_world_py() -> str:
    """
    Fixture which returns a simple hello world code in python
    """

    return "print('Hello World')"


@pytest.fixture
def mock_send_task_no_error_submission() -> callable:
    """
    Fixture for mocking the send task function from celery client
    """
    def mock_send(task_name: str, args: tuple = ()) -> MockWaitNoErrorSubmission:
        return MockWaitNoErrorSubmission()

    return mock_send
