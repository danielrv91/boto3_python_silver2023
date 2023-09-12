# Import the 'boto3' library, which is a Python SDK for AWS services.
import boto3

# Create a DynamoDB resource object.
dynamodb = boto3.resource('dynamodb')

# Get a reference to the 'Movies2023' table.
table = dynamodb.Table('Movies2023')

# Start a batch write operation using a 'with' statement.
with table.batch_writer() as batch:
    # Add an item to the batch for insertion.
    batch.put_item(
        Item={
            'Title': 'Mission Impossible',
            'genre': 'Action',
            'rating': 'PG',
            'release': 'Jul-12-2023'
        }
    )
    batch.put_item(
        Item={
            'Title': 'Asteroid City',
            'genre': 'Comedy',
            'rating': 'PG',
            'release': 'Jun-23-2023'
            }
    )
    batch.put_item(
        Item={
            'Title': 'Barbie',
            'genre': 'Comedy',
            'rating': 'PG',
            'release': 'Jul-21-2023'
            }
    )
    batch.put_item(
        Item={
            'Title': 'Indiana Jones',
            'genre': 'Adventure',
            'rating': 'PG',
            'release': 'Jun-30-2023'
            }
    )
    batch.put_item(
        Item={
            'Title': 'Leave No Trace',
            'genre': 'Drama',
            'rating': 'PG',
            'release': 'Jun-29-2023'
            }
    )
    batch.put_item(
        Item={
            'Title': 'Oppenheimer',
            'genre': 'Drama',
            'rating': 'R',
            'release': 'Jul-21-2023'
            }
    )
    batch.put_item(
        Item={
            'Title': 'Sound of Freedom',
            'genre': 'Crime',
            'rating': 'PG',
            'release': 'Jul-4-2023'
            }
    )
    batch.put_item(
        Item={
            'Title': 'Stephen Curry',
            'genre': 'Documentary',
            'rating': 'PG',
            'release': 'Jul-21-2023'
            }
    )
    batch.put_item(
        Item={
            'Title': 'The Flash',
            'genre': 'Action',
            'rating': 'PG',
            'release': 'Jul-16-2023'
            }
    )
    batch.put_item(
        Item={
            'Title': 'They Cloned Tyrone',
            'genre': 'Comedy',
            'rating': 'R',
            'release': 'Jul-14-2023'
            }
    )