# Import the 'boto3' library, which is a Python SDK for Amazon Web Services (AWS).
import boto3

# Create an AWS S3 client object using boto3.
s3 = boto3.client('s3')

# Use the S3 client to send a request to list objects in the specified S3 bucket ('drosales-boto3-09062023') with a prefix ('test_text').
response = s3.list_objects_v2(Bucket='drosales-boto3-09062023', Prefix='test_text')

# Print the response, which contains information about the listed objects.
print(response)

# Iterate through the list of objects in the 'Contents' field of the response.
for content in response['Contents']:
    # Print the 'Key' of each object, which represents its name or path in the S3 bucket.
    print(content['Key'])
