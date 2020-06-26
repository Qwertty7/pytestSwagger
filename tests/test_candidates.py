import json

import requests

from src.candidates import create_candidate, delete_candidate
from src.login import BASE_URL


# def test_create_candidate():
#     f = Faker()
#     first_name = f.first_name()
#     last_name = f.last_name()
#     email = f.email()
#     password = f.password()
#
#     candidate_data = {
#         "firstName": first_name,
#         "lastName": last_name,
#         "email": email,
#         "password": password
#
#     }
#
#     candidate_url = BASE_URL + '/candidates'
#     response = requests.post(candidate_url, json=candidate_data)
#     assert 'id' in response.text


# def test_create_candidate(candidate_data):
#     candidate_url = BASE_URL + '/candidates'
#     response = requests.post(candidate_url, json=candidate_data)
#     assert 'id' in response.text
"""
tests
"""
# def test_create_candidate_method(candidate_data):
#     response = create_candidate(candidate_data)
#     print(response.text)
#     assert 'id' in response.text
#
#
# def test_delete_candidate(candidate_data):
#     response_candidate = create_candidate(candidate_data)
#     assert response_candidate.status_code == 201
#     json_response_candidate = json.loads(response_candidate.content)
#     candidate_id = json_response_candidate['id']
#     response_delete_candidate = delete_candidate(candidate_id)
#     assert response_delete_candidate.status_code == 204


def test_change_candidate_data(candidate, session):
    BASE_URL = 'https://recruit-portnov.herokuapp.com/recruit/api/v1'
    url = BASE_URL + '/candidates'
    # get id value , assign to cand_id, remove it from candidate dictionary
    candidate_id = candidate.pop('id')
    new_last_name = 'Newlastname'
    response = session.patch(f'{url}/{candidate_id}', json={'lastName': new_last_name})
    assert response.status_code == 200
    assert response.json()['lastName'] != candidate['lastName']

# need to check response = 200 take response, find last_name == new last name OR last_name != candidate_last_name













