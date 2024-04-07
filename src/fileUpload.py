import logging
import boto3
from botocore.exceptions import ClientError
import os


# This method uploads a file to Amazon S3 bucket
def upload_file(fileName, bucket, objectName=None):
    """

    :param fileName: is name of the file to upload
    :param bucket: the bucket to upload to
    :param objectName: S3 object name.
    :return: a boolean value on the file upload
    """
    if objectName is None:
        objectName = os.path.basename(fileName)

    # upload file to S3 bucket
    s3Client = boto3.client('aws-testbucket-zain')

    try:
        response = s3Client.upload_file(fileName, bucket, objectName)
    except ClientError as e:
        logging.error(e)
        return False
    return True
