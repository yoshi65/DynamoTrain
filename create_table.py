import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.create_table(TableName='users',
                              KeySchema=[{
                                  'AttributeName': 'id',
                                  'KeyType': 'HASH'
                              }],
                              AttributeDefinitions=[{
                                  'AttributeName': 'id',
                                  'AttributeType': 'S'
                              }],
                              ProvisionedThroughput={
                                  'ReadCapacityUnits': 1,
                                  'WriteCapacityUnits': 1
                              })

print('Table status:', table.table_status)
