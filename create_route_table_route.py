# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Define the RouteTableId and InternetGatewayId for creating the route.
route_table_id = 'rtb-0bd805d8fcb8a67fe'
internet_gateway_id = 'igw-0aa7b42de4ddb5793'

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to create a route in the specified route table.
ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',    # Destination CIDR block for the route (0.0.0.0/0 represents all traffic).
    GatewayId=internet_gateway_id,        # Internet GatewayId for the route.
    RouteTableId=route_table_id,          # RouteTableId of the route table where the route should be added.
)
