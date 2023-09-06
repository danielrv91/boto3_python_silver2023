# Import the 'boto3' library, which is a Python SDK for Amazon Web Services (AWS).
import boto3

# Create an AWS S3 client object using boto3.
s3 = boto3.client('s3')

# Use the S3 client to send a request to list all buckets in the AWS account.
response = s3.list_buckets()

# Print the response, which contains information about the buckets.
print(response)

# Extract the 'Buckets' field from the response, which is a list of bucket objects.
buckets = response['Buckets']

# Iterate through the list of buckets and print the name of each bucket.
for bucket in buckets:
    print(bucket['Name'])

    
    
