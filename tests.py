from moto import mock_s3
import requests

APP_URL = 'http://localhost:8000'

@mock_s3
def test_file_creation():

    r = requests.post(APP_URL + '/login', headers={'Content-Type': 'application/json'}, json={'username': 'altair', 'password': '1234'})

    access_token = r.json()['access_token']

    print("Login successful")

    r = requests.post(APP_URL + '/create', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}, json={'body': {'name': 'test'}})

    uuid = r.json()['uuid']

    print("File created")

    r = requests.post(APP_URL + '/read', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}, json={'uuid': uuid})

    print("File read")

    r = requests.post(APP_URL + '/update', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}, json={'uuid': uuid, 'body': {'name': 'test2'}})

    print("File updated")

    r = requests.post(APP_URL + '/delete', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}, json={'uuid': uuid})

    print("File deleted")

    assert r.status_code == 200

    print("Test successful")

if __name__ == '__main__':
    
    test_file_creation()