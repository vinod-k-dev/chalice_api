from pytest_chalice.handlers import RequestHandler
import json

HEADERS = { 'Content-Type': 'application/json'}


def test_01_create_nozzle(client: RequestHandler) -> None:
    data = {
        "nozzle_id": 1,
        "status": "assigned",
        "nozzle_description": "this is for demo purpuse",
        "uom": "demo"
    }
    response = client.post('/create/nozzle', headers=HEADERS, body=json.dumps(data))
    assert response.status_code == 201 or 200


def test_02_create_nozzle(client: RequestHandler) -> None:
    data = {
        "status": "assigned",
        "nozzle_description": "this is for demo purpuse",
        "uom": "demo"
    }
    response = client.post('/create/nozzle', headers=HEADERS, body=json.dumps(data))
    assert response.status_code == 400


def test_03_create_nozzle(client: RequestHandler) -> None:
    response = client.post('/create/nozzle', headers=HEADERS, body={})
    assert response.status_code == 500


def test_04_update_nozzle(client: RequestHandler) -> None:
    data = {"nozzle_description" : "demo description", "uom" : "demo"}
    response = client.put('/update/nozzle/1', headers=HEADERS, body=json.dumps(data))
    assert response.status_code == 200


def test_05_get_nozzle_by_status(client: RequestHandler) -> None:
    response = client.get('/nozzle/by_status/unassigned')
    assert response.status_code == 200


def test_06_get_nozzle_by_id(client: RequestHandler) -> None:
    response = client.get('/nozzle/by_status/1')
    assert response.status_code == 200


def test_07_delete_nozzle(client: RequestHandler) -> None:
    response = client.delete('/delete/nozzle/1')
    assert response.status_code == 200

