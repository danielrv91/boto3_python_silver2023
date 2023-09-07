# Import the 'boto3' library, which is a Python SDK for Amazon Web Services (AWS).
import boto3

# Create an AWS S3 client object using boto3.
s3 = boto3.client('s3')

# Use the S3 client to send a request to create a new S3 bucket with the specified name.
response = s3.create_bucket(
    Bucket='drosales-boto3-09062023'
)

# Print the response, which contains information about the result of the bucket creation.
print(response)
