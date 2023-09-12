# Import the 'boto3' library, which is a Python SDK for AWS services.
import boto3

# Create a DynamoDB resource object.
dynamodb = boto3.resource('dynamodb')

# Get a reference to the 'Movies2023' table.
table = dynamodb.Table('Movies2023')

# Use the 'scan' method to retrieve items from the table.
response = table.scan()

# Extract the list of items from the response.
items = response['Items']

# Iterate through the retrieved items and print each one.
for movies in items:
    print(movies)
