# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Send a request to describe EC2 subnets and store the response.
response = ec2.describe_subnets()

# Iterate through the list of subnets in the response and print their CidrBlock, SubnetId, and VpcId.
for subnet in response['Subnets']:
    print(subnet['CidrBlock'], subnet['SubnetId'], subnet['VpcId'])
