# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Define the RouteTableId for deletion.
route_table_id = 'rtb-0bd805d8fcb8a67fe'

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to delete the specified route table.
ec2.delete_route_table(
    RouteTableId=route_table_id,
)
