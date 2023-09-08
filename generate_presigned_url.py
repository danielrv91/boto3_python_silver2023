# Import the 'boto3' library, which is a Python SDK for Amazon Web Services (AWS).
import boto3

# Create an AWS S3 client object using boto3.
s3 = boto3.client('s3')

# Generate a pre-signed URL for an S3 object that allows a temporary and secure access to it.
# In this case, it's generating a URL for the 'get_object' operation on the specified S3 object.
# Params dictionary specifies the 'Bucket' and 'Key' of the object to be accessed.
# ExpiresIn=300 sets the URL's expiration time to 300 seconds (5 minutes).
response = s3.generate_presigned_url('get_object', Params={'Bucket': 'drosales-boto3-09062023', 'Key': 'test_text.txt'}, ExpiresIn=300)

# Print the generated pre-signed URL, which can be used to access the S3 object securely for a limited time.
print(response)
