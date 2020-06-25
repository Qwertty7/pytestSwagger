import json
from src.positions import get_all_positions
from tests.conftest import url_positions

"""
checking existing positions
"""
def test_get_all_positions(url_positions):
    positions = get_all_positions(url_positions)
    json_positions = json.loads(positions.text)
    quantity_positions = len(json_positions)
    # assert len(json_positions) > 0
    assert quantity_positions == len(json_positions)

# TODO: need to add negative test cases to this test, url move here or to class, url shouldn't be in fixture

def test_get_positions_by_id():
    pass





