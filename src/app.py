import json

import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://172.17.0.2:8000")


def lambda_handler(event, context):
    votes_table = dynamodb.Table('users')

    if event['httpMethod'] == 'GET':
        resp = votes_table.scan()
        return {
            'body':
            json.dumps(
                {item['id']: int(item['votes'])
                 for item in resp['Items']})
        }
    elif event['httpMethod'] == 'POST':
        try:
            body = json.loads(event['body'])
        except boto3.exceptions.ClientError:
            return {'statusCode': 400, 'body': 'malformed json input'}

        if 'vote' not in body:
            return {'statusCode': 400, 'body': 'missing vote in request body'}
        if body['vote'] not in ['spaces', 'tabs']:
            return {
                'statusCode': 400,
                'body': 'vote value must be "spaces" or "tabs"'
            }

        resp = votes_table.update_item(Key={'id': body['vote']},
                                       UpdateExpression='ADD votes :incr',
                                       ExpressionAttributeValues={':incr': 1},
                                       ReturnValues='ALL_NEW')
        return {
            'body':
            "{} now has {} votes".format(body['vote'],
                                         resp['Attributes']['votes'])
        }
