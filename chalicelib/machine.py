from .decorators import *
from . import utils

machine_table = dynamodb.Table('Machine')


@app.route('/', methods=['GET','POST'],cors=True, content_types=['text/plain', 'application/json'])
def index():

    return {'status': 'It  works'}

# • PUT /machine - Update an existing machine configuration.
# • GET /machine/findByStatus - List machine by status, status: [assigned, unassigned, all]
# • GET /machine/{machineId} - Find machine by ID - machineId
# • DELETE /machine/{machineId} - Delete a machine configuration by ID - machineId


# • POST /machine - Add a new machine configuration
@app.route('/create/machine', methods=['POST'], cors=True)
def create_machine():
    headers = {}
    data = app.current_request.json_body

    try:
        if not utils.check_object_exists('Machine', 'machine_id', int(data['machine_id'])):
            machine_data = {'Item': {
                    'uuid': str(uuid.uuid4()),
                    'machine_id': int(data['machine_id']),
                    'status': data['status'],
                    'machine_description': data['machine_description'],
                    'uom': data['uom'],
                    'created_date': datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                    'updated_date': datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),

                }
            }

            response = machine_table.put_item(**machine_data)
            return utils.return_response(response, True, 'Machine Successfully Created!', 201, headers)

        return utils.return_response({"ResponseMetadata": {"HTTPStatusCode": 200}}, False, 'Object already exists with machine id!', 200, headers)

    except KeyError as e:
        return utils.return_response({"ResponseMetadata": {"HTTPStatusCode": 400}}, False, 'Bad request', 400, headers)


@app.route('/update/machine/{machine_id}', methods=['PUT'], cors=True)
def update_machine(machine_id):

    data = app.current_request.json_body
    response = machine_table.update_item(Key={'machine_id': int(machine_id)},
                                         UpdateExpression='SET machine_description = :machine_description,uom = :uom,updated_date = :updated_date',
                                         ExpressionAttributeValues={':machine_description': data['machine_description'], ':uom': data['uom'],
                                                                    ':updated_date': datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")})
    headers = {}
    return utils.return_response(response, True, 'Machine Successfully Updated!', 200, headers)


@app.route('/machine/by_status/{status}', methods=['GET'], cors=True)
def get_machine_by_status(status):

    response = machine_table.scan(FilterExpression=Attr('status').eq(status))

    headers = {}
    return utils.return_response(response, True, 'Retrieved All Machine By Status ~', 200, headers)


@app.route('/machine/by_id/{machine_id}', methods=['GET'], cors=True)
def get_machine_by_id(machine_id):

    response = machine_table.scan(FilterExpression=Attr('machine_id').eq(int(machine_id)))

    headers = {}
    return utils.return_response(response, True, 'Retrieved All Machine By Id!', 200, headers)


@app.route('/delete/machine/{machine_id}', methods=['DELETE'], cors=True)
def delete_machine(machine_id):
    response = machine_table.delete_item(Key={'machine_id': int(machine_id)})

    headers = {}
    return utils.return_response(response, True, 'Machine Successfully Deleted!', 200, headers)