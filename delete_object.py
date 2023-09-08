# Import the 'boto3' library, which is a Python SDK for Amazon Web Services (AWS).
import boto3

# Define variables for the S3 bucket and object key to be deleted.
bucket = 'drosales-boto3-09062023'
key = 'test_text.txt'

# Create an AWS S3 client object using boto3.
s3 = boto3.client('s3')

# Use the S3 client to send a request to delete the specified object from the specified bucket.
response = s3.delete_object(
    Bucket=bucket,
    Key=key,
)

# The 'response' variable may contain confirmation or error information.
