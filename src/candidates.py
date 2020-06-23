import requests

BASE_URL = 'https://recruit-portnov.herokuapp.com/recruit/api/v1'

"""
check all end points for candidates
"""


def create_candidate(candidate_data):
    url = BASE_URL + '/candidates'
    return requests.post(url, json=candidate_data)

