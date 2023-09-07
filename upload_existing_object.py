# Import the 'boto3' library, which is a Python SDK for Amazon Web Services (AWS).
import boto3

# Create an AWS S3 client object using boto3.
s3 = boto3.client('s3')

# Open the file 'test_text.txt' in binary read mode ('rb') using a context manager.
with open('test_text.txt', 'rb') as f:
    # Use the S3 client to upload the file contents ('Body') to the specified S3 bucket and key (object name).
    s3.put_object(Bucket='drosales-boto3-09062023', Key='test_text.txt', Body=f, ContentType='text/plain')
