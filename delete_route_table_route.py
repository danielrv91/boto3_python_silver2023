# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Define the RouteTableId for deleting the route.
route_table_id = 'rtb-0bd805d8fcb8a67fe'

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to delete a specific route from the specified route table.
ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',    # Destination CIDR block of the route to be deleted (0.0.0.0/0 represents all traffic).
    RouteTableId=route_table_id,          # RouteTableId of the route table from which the route should be deleted.
)
