from .decorators import *
from . import utils
nozzle_table = dynamodb.Table('Nozzle')


@app.route('/create/nozzle', methods=['POST'], cors=True)
def create_nozzle():
    headers = {}
    data = app.current_request.json_body

    try:
        if not utils.check_object_exists('Nozzle', 'nozzle_id', int(data['nozzle_id'])):
            nozzle_data = {'Item': {
                    'uuid': str(uuid.uuid4()),
                    'nozzle_id': int(data['nozzle_id']),
                    'status': data['status'],
                    'nozzle_description': data['nozzle_description'],
                    'uom': data['uom'],
                    'created_date': datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                    'updated_date': datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),

                }
            }

            response = nozzle_table.put_item(**nozzle_data)
            return utils.return_response(response, True, 'Machine Successfully Created!', 201, headers)

        return utils.return_response({"ResponseMetadata": {"HTTPStatusCode": 200}}, False, 'Object already exists with nozzle id!', 200, headers)

    except KeyError as e:
        return utils.return_response({"ResponseMetadata": {"HTTPStatusCode": 400}}, False, 'Bad request', 400, headers)


@app.route('/update/nozzle/{nozzle_id}', methods=['PUT'], cors=True)
def update_nozzle(nozzle_id):
    data = app.current_request.json_body
    response = nozzle_table.update_item(Key={'nozzle_id': int(nozzle_id)},
                                        UpdateExpression='SET nozzle_description = :nozzle_description,uom = :uom,updated_date =:updated_date',
                                        ExpressionAttributeValues={':nozzle_description': data['nozzle_description'],
                                                                   ':uom': data['uom'], ':updated_date': datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")}, )
    headers = {}
    return utils.return_response(response, True, 'Nozzle Successfully Updated!', 200, headers)


@app.route('/nozzle/by_status/{status}', methods=['GET'], cors=True)
def get_nozzle_by_status(status):
    response = nozzle_table.scan(FilterExpression=Attr('status').eq(status))

    headers = {}
    return utils.return_response(response, True, 'Retrieved All Machine By Status ~', 200, headers)


@app.route('/nozzle/by_id/{nozzle_id}', methods=['GET'], cors=True)
def get_nozzle_by_id(nozzle_id):
    response = nozzle_table.scan(FilterExpression=Attr('nozzle_id').eq(int(nozzle_id)))

    headers = {}
    return utils.return_response(response, True, 'Retrieved All Machine By Id!', 200, headers)


@app.route('/delete/nozzle/{nozzle_id}', methods=['DELETE'], cors=True)
def delete_nozzle(nozzle_id):
    response = nozzle_table.delete_item(Key={'nozzle_id': int(nozzle_id)})

    headers = {}
    return utils.return_response(response, True, 'Machine Successfully Deleted!', 200, headers)