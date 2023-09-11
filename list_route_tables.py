# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Send a request to describe EC2 route tables and store the response.
response = ec2.describe_route_tables()

# Iterate through the list of route tables in the response.
for routeTable in response['RouteTables']:
    # Print the VpcId and RouteTableId of the current route table.
    print(routeTable['VpcId'], routeTable['RouteTableId'])
    
    # Iterate through the associations of the current route table.
    for association in routeTable['Associations']:
        # Print the RouteTableAssociationId.
        print(association['RouteTableAssociationId'])
        # Check if 'SubnetId' exists in the association, and if so, print it.
        if 'SubnetId' in association:
            print(association['SubnetId'])
    
    # Iterate through the routes of the current route table.
    for route in routeTable['Routes']:
        # Print the DestinationCidrBlock and GatewayId of each route.
        print(route['DestinationCidrBlock'], route['GatewayId'])
