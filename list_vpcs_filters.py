# Import the 'boto3' library, which is a Python SDK for Amazon Elastic Compute Cloud (EC2).
import boto3

# Define a function 'get_vpc_information' that retrieves and prints VPC information.
def get_vpc_information(client, filters=[]):
    # Use the EC2 client to describe VPCs, applying any provided filters.
    response = ec2.describe_vpcs(Filters=filters)
    
    # Iterate through the list of VPCs in the response and print VpcId, CidrBlock, and IsDefault values.
    for vpc in response['Vpcs']:
        print(vpc['VpcId'], vpc['CidrBlock'], vpc['IsDefault'])

# Define a function 'get_vpc_name' that retrieves and prints VPC names.
def get_vpc_name(client, filters=[]):
    # Use the EC2 client to describe VPCs, applying any provided filters.
    response = ec2.describe_vpcs(Filters=filters)
    
    # Iterate through the list of VPCs in the response.
    for vpc in response['Vpcs']:
        # Check if the VPC has 'Tags' associated with it.
        if 'Tags' in vpc:
            # Iterate through the tags of the VPC.
            for tag in vpc['Tags']:
                # Check if a tag with the key 'Name' exists.
                if 'Name' == tag['Key']:
                    # If a 'Name' tag exists, print its value.
                    print(tag['Value'])

# Entry point of the script
if __name__ == '__main__':
    # Create an EC2 client object using boto3.
    ec2 = boto3.client('ec2')
    
    # Define a filter to retrieve only default VPCs.
    Filters = [{'Name': 'isDefault', 'Values': ['true', ]}, ]
    
    # Send a request to describe default VPCs and store the response.
    response = ec2.describe_vpcs(Filters=Filters)
    
    # Call the 'get_vpc_information' function to retrieve and print VPC information for all VPCs.
    get_vpc_information(ec2)
    
    # Call the 'get_vpc_information' function again, this time applying the defined filters.
    get_vpc_information(ec2, Filters)
