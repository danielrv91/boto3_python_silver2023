# Import the 'boto3' library, which is a Python SDK for Amazon Web Services (AWS).
import boto3

# Create an AWS S3 client object using boto3.
s3 = boto3.client('s3')

# Use the S3 client to upload a string ('Hey this is a string') to the specified S3 bucket and key (object name).
# Additionally, specify the content type as 'text/plain' for the object.
s3.put_object(Bucket='drosales-boto3-09062023', Key='test_text_string.txt', Body='Hey this is a string', ContentType='text/plain')
