import json
import os

import boto3

tableName = os.environ['SAMPLE_TABLE']
ENDPOINT_OVERRIDE = os.environ['ENDPOINT_OVERRIDE']

options = {}

if ENDPOINT_OVERRIDE != '':
    options['endpoint_url'] = ENDPOINT_OVERRIDE

dynamodb = boto3.resource('dynamodb', **options)


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    print('TABLE', tableName)
    print('END', ENDPOINT_OVERRIDE)
    table = dynamodb.Table(tableName)
    table.put_item(Item={'id': 'hello!', 'name': 'world!'})

    return {
        "statusCode":
        200,
        "body":
        json.dumps({
            "message": "yo world",
            # "location": ip.text.replace("\n", "")
        }),
    }
