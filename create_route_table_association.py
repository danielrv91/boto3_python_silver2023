# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Define the RouteTableId and SubnetId for the association.
route_table_id = 'rtb-0bd805d8fcb8a67fe'
subnet_id = 'subnet-06b6d8ff25e1fdbeb'

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to associate the specified route table with the specified subnet.
association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

# Print the AssociationId of the newly created association.
print(association['AssociationId'])
