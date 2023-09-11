# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to create a Virtual Private Cloud (VPC) with the specified CIDR block.
vpc = ec2.create_vpc(CidrBlock='12.0.0.0/16')

# Print the VpcId of the newly created VPC.
print(vpc['Vpc']['VpcId'])
