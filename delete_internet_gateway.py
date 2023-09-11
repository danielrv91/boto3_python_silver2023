# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Define the InternetGatewayId for deletion.
internet_gateway_id = 'igw-0aa7b42de4ddb5793'

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to delete the specified internet gateway.
ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)
