import boto3
import os
import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def handler(event, context):
    print(f"Lambda starting with event: {event.get('LastEvaluatedKey')}")
    dynamodb = boto3.resource('dynamodb')
    table_name = os.getenv('TABLE_NAME', "dynamo-sync-example")
    table = dynamodb.Table(table_name)
    lambda_client = boto3.client('lambda')
    lambda_function_name = os.getenv("LAMBDA_FUNCTION_NAME", "dynamo-scanner")

    try:
        if 'LastEvaluatedKey' in event:
            response = table.scan(
                Limit=1000,
                ExclusiveStartKey=event['LastEvaluatedKey']
            )
        else:
            response = table.scan(Limit=1000)

        current_count = 0
        for item in response['Items']:
            current_count += 1
            # print(f"Scanned item: {json.dumps(item, cls=DecimalEncoder)}")
        total_count = event.get('count', 0) + current_count
        if 'LastEvaluatedKey' in response:
            last_evaluated_key = last_evaluated_key = response.get('LastEvaluatedKey')
            print(f"More items to process. LastEvaluatedKey: {last_evaluated_key}, total count: {total_count}")
            payload = json.dumps({'LastEvaluatedKey': last_evaluated_key, 'count': total_count})
            lambda_client.invoke(
                FunctionName=lambda_function_name,
                InvocationType='Event',
                Payload=payload)
            return
        else:
            print(f"Scan complete, processed {total_count} items")

    except Exception as e:
        print(f"Error: {str(e)}")
        raise

    return {
        'statusCode': 200,
        'body': 'Scan batch complete',
        'LastEvaluatedKey': last_evaluated_key
    }
