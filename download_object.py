# Import the 'boto3' library, which is a Python SDK for Amazon Web Services (AWS).
import boto3

# Define variables for the S3 bucket, object key, and the local filename.
bucket = 'drosales-boto3-09062023'
key = 'test_text_string.txt'
filename = "test_text_string.txt"

# Create an AWS S3 client object using boto3.
s3 = boto3.client('s3')

# Define a function 'download_single_object' to download an S3 object to a local file.
def download_single_object(client, bucket, key, filename):
    # Use the S3 client's 'download_file' method to download the object specified by 'bucket' and 'key'
    # and save it to the local file with the provided 'filename'.
    client.download_file(bucket, key, filename)
