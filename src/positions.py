import requests

BASE_URL = 'https://recruit-portnov.herokuapp.com/recruit/api/v1'
url_positions = BASE_URL + '/positions/'

"""
return all existing positions
"""


class Positions():
    pass


def get_all_positions(url_positions):
    return requests.get(url_positions)


def get_positions_by_id(position_id):
    """
    :param position_id:
    :return: position description according requested ID
    """
    return requests.get(url_positions + str(position_id))

def get_candidate_positions():
    pass
