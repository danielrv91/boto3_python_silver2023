# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Define the RouteTableId for the route table to be disassociated.
route_table_id = 'rtb-0bd805d8fcb8a67fe'

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to describe the specified route table.
response = ec2.describe_route_tables(
    RouteTableIds=[route_table_id],
)

# Iterate through the associations of the specified route table.
for association in response['RouteTables'][0]['Associations']:
    # Check if the association is not the main route table association.
    if not association['Main']:
        # Retrieve the AssociationId for the non-main association.
        association_id = association['RouteTableAssociationId']
        print(association_id)
        
        # Use the EC2 client to disassociate the specified route table association.
        ec2.disassociate_route_table(
            AssociationId=association_id,
        )
