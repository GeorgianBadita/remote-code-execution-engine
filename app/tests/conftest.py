import pytest

from remote_coding_compilation_engine import schemas

from fastapi.testclient import TestClient
from fastapi import FastAPI


class MockWaitNoError():

    def wait(self, **kwargs):
        return {
            "has_error": False,
            "out_of_resources": False,
            "exit_code": 0,
            "out_of_time": False,
            "raw_output": "Hello World"
        }


class MockWaitRaises():

    def wait(self, **kwargs):
        raise Exception


@pytest.fixture
def mock_send_task_no_error() -> MockWaitNoError:
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
def app() -> FastAPI:
    """
    Fixture for new testing application
    """
    from remote_coding_compilation_engine.main import app
    return app


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    """
    FastAPI client fixture
    """

    return TestClient(app)


@pytest.fixture
def execution() -> schemas.Execution:
    return {
        "language": "python",
        "code": "print('Hello World')"
    }
