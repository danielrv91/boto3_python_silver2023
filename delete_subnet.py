# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Define the SubnetId for deletion.
subnet_id = 'subnet-06b6d8ff25e1fdbeb'

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to delete the specified subnet.
ec2.delete_subnet(
    SubnetId=subnet_id,
)
