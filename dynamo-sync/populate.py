import boto3
import os
import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_name = os.getenv('TABLE_NAME', "dynamo-sync-example")
    table = dynamodb.Table(table_name)

    with table.batch_writer() as batch:
        for i in range(20000):
            batch.put_item(Item={
                'id': str(i),
                'name': generate_random_string(10),
                'age': random.randint(18, 80),
                'email': f"{generate_random_string(8)}@example.com"
            })

    return {
        'statusCode': 200,
        'body': 'DynamoDB table populated with 20000 entries'
    }
