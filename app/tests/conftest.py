import pytest
import botocore

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


class Readable:
    """
    Class for mocking a readable object
    """

    def read(self):
        """
        Class for mocking read call
        """
        return "print('Hello World')".encode()


class BotoMockReturns:

    def get_object(self, Bucket='', Key=''):
        return {
            "Body": Readable()
        }


class BotoMockRaise:
    def get_object(self, Bucket='', Key=''):
        raise botocore.exceptions.ClientError({}, {})


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


@pytest.fixture
def create_hello_world_py() -> str:
    """
    Fixture which returns a simple hello world code in python
    """

    return "print('Hello World')"


@pytest.fixture
def mock_s3_boto_returns() -> callable:
    """
    Fixture which returns a mock for s3 client
    when the file gathering works properly

    @return object mocking the s3 boto client method
    """

    def client(aws_res, aws_access_key_id=None, aws_secret_access_key=None):
        return BotoMockReturns()

    return client


@pytest.fixture
def mock_s3_boto_raise() -> callable:
    """
    Fixture which returns a mock for s3 client when invalid path is given

    @return object mocking s3 boto client method
    """

    def client(aws_res, aws_access_key_id=None, aws_secret_access_key=None):
        return BotoMockRaise()

    return client
