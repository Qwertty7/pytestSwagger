import requests

from tests.conftest import url_positions

"""
return all existing positions
"""


class Positions():
    pass


def get_all_positions(url_positions):
    return requests.get(url_positions)

# need positions ID should it be in conftest?

def get_positions_by_id():
    pass

def get_candidate_positions ():
    pass
