import boto3

bucket = 'drosales-boto3-09062023'
key = 'test_text.txt'

s3 = boto3.client('s3')

response = s3.delete_object(
    Bucket=bucket,
    Key=key,
  
)