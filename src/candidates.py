import requests

from src.login import APIService

BASE_URL = 'https://recruit-portnov.herokuapp.com/recruit/api/v1'
url = BASE_URL + '/candidates'


"""
check all end points for candidates
"""

api = APIService()

def create_candidate (candidate_data):
    return api.session.post(url, json=candidate_data)


def delete_candidate(candidate_id):
    # return api.session.delete(url + str(candidate_id))
    api.login('student@example.com', 'welcome')
    return api.session.delete(f'{url}/{candidate_id}')
