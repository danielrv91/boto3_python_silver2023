# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Define the CIDR block and VPC ID for the new subnet.
cidr_block = '12.0.1.0/24'
vpc_id = 'vpc-02ee644eaeb747c86'

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to create a subnet with the specified CIDR block and associated with the given VPC.
subnet = ec2.create_subnet(CidrBlock=cidr_block, VpcId=vpc_id)

# Print the SubnetId of the newly created subnet.
print(subnet['Subnet']['SubnetId'])
