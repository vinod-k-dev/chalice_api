from http import HTTPStatus
from pytest_chalice.handlers import RequestHandler
import json

HEADERS = { 'Content-Type': 'application/json'}


def test_index(client: RequestHandler) -> None:
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json == {'status': 'It  works'}



def test_01_create_machine(client: RequestHandler) -> None:
    data = {
        "machine_id": 1,
        "status": "assigned",
        "machine_description": "this is for demo purpuse",
        "uom": "demo"
    }
    response = client.post('/create/machine', headers=HEADERS, body=json.dumps(data))
    assert response.status_code == 201 or 200


def test_02_create_machine(client: RequestHandler) -> None:
    data = {
        "status": "assigned",
        "machine_description": "this is for demo purpuse",
        "uom": "demo"
    }
    response = client.post('/create/machine', headers=HEADERS, body=json.dumps(data))
    assert response.status_code == 400


def test_03_create_machine(client: RequestHandler) -> None:
    response = client.post('/create/machine', headers=HEADERS, body={})
    assert response.status_code == 500


def test_04_update_machine(client: RequestHandler) -> None:
    data = {"machine_description" : "demo description", "uom" : "demo"}
    response = client.put('/update/machine/1', headers=HEADERS, body=json.dumps(data))
    assert response.status_code == 200


def test_05_get_machine_by_status(client: RequestHandler) -> None:
    response = client.get('/machine/by_status/unassigned')
    assert response.status_code == 200


def test_06_get_machine_by_id(client: RequestHandler) -> None:
    response = client.get('/machine/by_status/1')
    assert response.status_code == 200


def test_07_delete_machine(client: RequestHandler) -> None:
    response = client.delete('/delete/machine/1')
    assert response.status_code == 200

