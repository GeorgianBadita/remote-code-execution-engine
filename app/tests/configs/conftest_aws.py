import pytest
import botocore


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
