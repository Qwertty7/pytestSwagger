import requests
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


def test_create_candidate(candidate_data):
    candidate_url = BASE_URL + '/candidates'
    response = requests.post(candidate_url, json=candidate_data)
    assert 'id' in response.text
