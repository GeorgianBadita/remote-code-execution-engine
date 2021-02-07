import os
import botocore
import logging

from boto3 import client

logging.basicConfig(level=logging.INFO)


class S3CodeReader:

    # AWS Credentials
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
    AWS_REGION = os.environ.get('AWS_REGION', '')
    AWS_S3_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME', '')

    @classmethod
    def get_test_code_from_s3(cls, s3_test_file_key: str) -> str:
        """
        Function to download a code test from AWS s3

        @param s3_test_file_key - url to resource code in s3

        @return the test file content
        """

        s3 = client(
            's3',
            aws_access_key_id=cls.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=cls.AWS_SECRET_ACCESS_KEY
        )

        logging.info(f"Starting gathering code test at {s3_test_file_key}")
        try:

            file_obj = s3.get_object(
                Bucket=cls.AWS_S3_BUCKET_NAME, Key=s3_test_file_key)

            return file_obj['Body'].read().decode('utf-8')
        except botocore.exceptions.ClientError as err:
            logging.error(f"Error gathering the file, err: {err}")
            raise err
