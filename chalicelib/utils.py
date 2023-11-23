from .settings import *
client = boto3.client('dynamodb')


def return_response(data, success, message, status, headers):
    try:
        if not success and message == 'Bad request!':
            data_keys = list(data.keys())
            message = "".join(data[data_keys[0]])
    except Exception as e:
        pass

    response_data = {"data":data, "success": success, "message": message, 'status': status}
    return Response(response_data, status_code=status, headers=headers)


def check_object_exists(table, hash_key, object_id):
    try:
        dynamodb_table = dynamodb.Table(table)

        res = dynamodb_table.get_item( Key={hash_key: int(object_id)})['Item']
        item = True
    except KeyError:
        item = False
    return item