import boto3

vpc_id = 'vpc-02ee644eaeb747c86'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)