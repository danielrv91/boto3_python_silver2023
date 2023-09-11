# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Define the InternetGatewayId and VpcId for the attachment.
internet_gateway_id = 'igw-0aa7b42de4ddb5793'
vpc_id = 'vpc-02ee644eaeb747c86'

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to attach the specified internet gateway to the specified VPC.
ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)


