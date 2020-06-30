import json

import pytest
from faker import Faker

from src.positions import Positions

pos = Positions()

BASE_URL = 'https://recruit-portnov.herokuapp.com/recruit/api/v1'
url_positions = BASE_URL + '/positions'

"""
checking existing positions
"""


def test_get_all_positions ():
    positions = pos.get_all_positions(url_positions)
    json_positions = json.loads(positions.text)
    quantity_positions = len(json_positions)
    # assert len(json_positions) > 0
    assert quantity_positions == len(json_positions)

    # TODO: need to add negative test cases to this test, url move here or to class, url shouldn't be in fixture

    '''
    assert that function return a position by given position ID
    assert that function return "errorMessage" with following inputs:
    positions ID that not existing,
    position ID can't start from zero
    position ID must be an integer
    '''


@pytest.mark.parametrize('position_id,status_code', [
    ("5", 200),
    ("058", 400),
    ("-5", 400),
    ("789", 400),
    ("7&", 500)
    # ({'title':'', 'company':''}, 400)
])
def test_get_positions_by_id (position_id, status_code):
    position_by_id = pos.get_positions_by_id(position_id)
    assert position_by_id.status_code == status_code


def test_create_new_position():
    f = Faker()
    position_title = f.name()
    company_name = f.name()

    position_data = {
        "title": position_title,
        "company": company_name

    }
    new_position = pos.create_new_positions(position_data)
    assert "id" in new_position.json()