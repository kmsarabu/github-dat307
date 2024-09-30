import json
import boto3
from boto3.dynamodb.conditions import Attr
import os

def lambda_handler(event, context):
    # TODO implement
    print (event)
    print (context)
    
    # Initialize the DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    
    tableName = os.getenv('CWALERTTABLE')
    table  = dynamodb.Table(tableName)

    # Scan the table and filter based on sort key
    response = table.scan(
        FilterExpression=Attr('event_status').eq('pending')
    )
    print (response)
    return {
        'statusCode': '200',
        'body': json.dumps(response),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
    
    