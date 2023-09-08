# Import the 'boto3' library, which is a Python SDK for Amazon Web Services (AWS).
import boto3

# Create an AWS S3 client object using boto3.
s3 = boto3.client('s3')

# Define the S3 bucket name and object key to be used in subsequent operations.
bucket = 'drosales-boto3-09062023'
key = 'test_text_string.txt'

# Configure Public Access Block settings for the specified S3 bucket.
response = s3.put_public_access_block(
    Bucket=bucket,
   
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,        # Block public access control lists (ACLs).
        'IgnorePublicAcls': False,       # Do not ignore public ACLs.
        'BlockPublicPolicy': False,      # Do not block public bucket policies.
        'RestrictPublicBuckets': False   # Do not restrict public buckets.
    },
)

# Configure Ownership Controls for the specified S3 bucket.
response = s3.put_bucket_ownership_controls(
    Bucket=bucket,
    OwnershipControls={
        'Rules': [
            {
                'ObjectOwnership': 'BucketOwnerPreferred'  # Set object ownership to 'BucketOwnerPreferred'.
            },
        ]
    }
)

# Set the ACL (Access Control List) of the specified S3 bucket to 'private'.
response = s3.put_bucket_acl(
    ACL='private',
    Bucket=bucket,
)

# Set the ACL of the specified S3 object (key) to 'public-read'.
response = s3.put_object_acl(
    ACL='public-read', 
    Bucket=bucket,
    Key=key
)

# Print the response from the last operation, which may contain confirmation or error information.
print(response)
