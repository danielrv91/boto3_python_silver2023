# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Create an EC2 client object using boto3.
ec2 = boto3.client('ec2')

# Send a request to describe Virtual Private Clouds (VPCs) and store the response.
response = ec2.describe_vpcs()

# Iterate through the list of VPCs in the response and print their VpcId, CidrBlock, and IsDefault values.
for vpc in response['Vpcs']:
    print(vpc['VpcId'], vpc['CidrBlock'], vpc['IsDefault'])

# Iterate through the list of VPCs in the response again.
for vpc in response['Vpcs']:
    # Check if the VPC has 'Tags' associated with it.
    if 'Tags' in vpc:
        # Iterate through the tags of the VPC.
        for tag in vpc['Tags']:
            # Check if a tag with the key 'Name' exists.
            if 'Name' == tag['Key']:
                # If a 'Name' tag exists, print its value.
                print(tag['Value'])
