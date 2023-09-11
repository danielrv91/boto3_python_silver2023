# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Send a request to describe EC2 internet gateways and store the response.
response = ec2.describe_internet_gateways()

# Iterate through the list of internet gateways in the response.
for ig in response['InternetGateways']:
    # Print the InternetGatewayId of the current internet gateway.
    print(ig['InternetGatewayId'])
    
    # Iterate through the attachments of the current internet gateway.
    for attachment in ig['Attachments']:
        # Print the VpcId and State of the attachment.
        print(attachment['VpcId'], attachment['State'])
