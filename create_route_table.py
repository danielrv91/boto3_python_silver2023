# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Define the VPC ID for which to create the route table.
vpc_id = 'vpc-02ee644eaeb747c86'

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to create a route table associated with the specified VPC.
routeTable = ec2.create_route_table(VpcId=vpc_id)

# Print the RouteTableId of the newly created route table.
print(routeTable['RouteTable']['RouteTableId'])
