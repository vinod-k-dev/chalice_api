import boto3
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")


def create_machine_table():
    table = dynamodb.create_table(TableName='machine',
                                  KeySchema=[{'AttributeName': 'machine_id', 'KeyType': 'integer'}],
                                  AttributeDefinitions=[{'AttributeName': 'machine_id', 'AttributeType': 'N'}],
                                  ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10})

    return table


def create_table_nozzle():
    table = dynamodb.create_table(TableName='nozzle',
                                  KeySchema=[{'AttributeName': 'nozzle_id', 'KeyType': 'nozzle_id'}, ],
                                  AttributeDefinitions=[{'AttributeName': 'nozzle_id', 'AttributeType': 'N'}, ],
                                  ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10})

    return table


if __name__ == '__main__':
    machine_table = create_machine_table(),
    print("Status:", machine_table.table_status),
    nozzle_table = create_table_nozzle(),
    print("Status:", nozzle_table.table_status)