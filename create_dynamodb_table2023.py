# Import the 'boto3' library, which is a Python SDK for AWS services.
import boto3

# Create a DynamoDB client object.
dynamodb = boto3.client('dynamodb')

# Use the DynamoDB client to create a table named 'Movies2023'.
response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Title',  # Define the attribute name and type.
            'AttributeType': 'S',      # 'S' represents a string attribute.
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'Title',  # Define the primary key attribute.
            'KeyType': 'HASH',          # 'HASH' indicates it's the hash key.
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,       # Set read capacity units.
        'WriteCapacityUnits': 5,      # Set write capacity units.
    },
    TableName='Movies2023',          # Specify the table name.
)

# Print the response, which may contain information about the created table.
print(response)
