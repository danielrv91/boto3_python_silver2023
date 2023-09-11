# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to create an internet gateway.
ig = ec2.create_internet_gateway()

# Print the InternetGatewayId of the newly created internet gateway.
print(ig['InternetGateway']['InternetGatewayId'])
