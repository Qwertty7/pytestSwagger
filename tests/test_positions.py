import json

import pytest

from src.positions import get_all_positions, get_positions_by_id

BASE_URL = 'https://recruit-portnov.herokuapp.com/recruit/api/v1'
url_positions = BASE_URL + '/positions'

"""
checking existing positions
"""


def test_get_all_positions ():
    positions = get_all_positions(url_positions)
    json_positions = json.loads(positions.text)
    quantity_positions = len(json_positions)
    # assert len(json_positions) > 0
    assert quantity_positions == len(json_positions)


# TODO: need to add negative test cases to this test, url move here or to class, url shouldn't be in fixture


@pytest.mark.parametrize('position_id,status_code', [
    ("5",  200),
    ("058", 400),
    ("-5", 400),
    ("789", 400),
    ("7&", 500)
])
def test_get_positions_by_id(position_id,status_code):
    '''
    assert that function return a position by given position ID
    assert that function return "errorMessage" with following inputs:
    positions ID that not existing,
    position ID can't start from zero
    position ID must be an integer
    '''
    position_by_id = get_positions_by_id(position_id)
    # assert 'id' in position_by_id.text
    assert position_by_id.status_code == status_code


# def test_incorrect_positions_id():
#
#     incorrect_position_id = get_positions_by_id('-45')
#     # json_position_by_id = json.loads(incorrect_position_id.text)
#     # print(json_position_by_id)
#     assert 'Incorrect positionId' in incorrect_position_id.text
