import pytest
import requests
from faker import Faker

from src.login import APIService


@pytest.fixture
def candidate_data ():
    f = Faker()
    first_name = f.first_name()
    last_name = f.last_name()
    email = f.email()
    password = f.password()

    candidate_data = {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password

    }
    return candidate_data

@pytest.fixture
def session():
    return requests.Session()
# this is not auth session


@pytest.fixture
def auth_session(session):
    service = APIService()
    token = service.login('student@example.com', 'welcome')
    session.headers.update({'Authorization': f'Bearer {token}'})
    return session


@pytest.yield_fixture
def candidate(auth_session, candidate_data):
    BASE_URL = 'https://recruit-portnov.herokuapp.com/recruit/api/v1'
    url = BASE_URL + '/candidates'
    response = auth_session.post(url, json=candidate_data)
    json_data = response.json()
    candidate_id = json_data['id']
    yield json_data
    auth_session.delete(f'{url}/{candidate_id}')

