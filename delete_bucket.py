# Import the 'boto3' library, which is a Python SDK for Amazon Web Services (AWS).
import boto3

# Define a function 'empty_bucket' that takes an AWS S3 client and a bucket name as arguments.
def empty_bucket(client, bucket):
    # Use the S3 client to list objects in the specified bucket.
    response = client.list_objects_v2(Bucket=bucket)
    
    # Check if there are objects in the bucket ('Contents' field in the response).
    if 'Contents' in response:
        # Create a list of objects to be deleted, using their keys.
        objects = [{'Key': content['Key']} for content in response['Contents']]
        
        # Send a request to delete the objects in the list.
        response = client.delete_objects(
            Bucket=bucket,
            Delete={
                'Objects': objects
            }
        )
        
        # Continue deleting objects in the bucket using continuation tokens.
        while response.get('NextContinuationToken'):
            response = client.list_objects_v2(Bucket=bucket,
                            ContinuationToken=response['NextContinuationToken'])
            
            # Create a list of objects to be deleted in the current batch.
            objects = [{'Key': content['Key']} for content in response['Contents']]
            
            # Send a request to delete the objects in the current batch.
            response = client.delete_objects(
                Bucket=bucket,
                Delete={
                    'Objects': objects
                }
            )   

# Create an AWS S3 client object using boto3.
s3 = boto3.client('s3')

# Specify the S3 bucket to be emptied and deleted.
bucket = 'drosales-boto3-09062023'

# Call the 'empty_bucket' function to delete all objects within the specified bucket.
empty_bucket(s3, bucket)

# Finally, send a request to delete the now-empty bucket.
response = s3.delete_bucket(
    Bucket=bucket
)
