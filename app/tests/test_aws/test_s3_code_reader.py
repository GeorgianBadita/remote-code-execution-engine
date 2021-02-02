import pytest
import botocore

from remote_coding_compilation_engine.aws.s3_code_reader import S3CodeReader


def test_WHEN_correct_s3_code_path_THEN_return_code(mocker, mock_s3_boto_returns, create_hello_world_py):
    """
    Function which tests the happy flow of s3 test code gathering
    """

    mocker.patch(
        'remote_coding_compilation_engine.aws.s3_code_reader.client',
        mock_s3_boto_returns)

    assert S3CodeReader().get_test_code_from_s3("code_path") == create_hello_world_py


def test_WHEN_correct_s3_invalid_path_THEN_raise(mocker, mock_s3_boto_raise):
    """
    Function which tests that the s3 reader raises exception when given invalid code path
    """

    mocker.patch(
        'remote_coding_compilation_engine.aws.s3_code_reader.client',
        mock_s3_boto_raise)

    with pytest.raises(botocore.exceptions.ClientError):
        S3CodeReader().get_test_code_from_s3("invalid_code_path")
