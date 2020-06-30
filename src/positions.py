import requests
import self

from src.login import APIService

BASE_URL = 'https://recruit-portnov.herokuapp.com/recruit/api/v1'
url_positions = BASE_URL + '/positions/'
url_new_position = BASE_URL + '/positions'

"""
return all existing positions
"""


class Positions():
    api = APIService('student@example.com', 'welcome')

    def get_all_positions(url_positions):
         return requests.get(url_positions)

    def get_positions_by_id(position_id):
        """
        :param position_id:
        :return: position description according requested ID
        """
        return requests.get(url_positions + str(position_id))

    def create_new_positions(position_data):
        """
        post new position
        required data: data_json = title&company
        user need to be authorized
        :return: new position created with assigned ID
        """
        return self.api.session.post(url_new_position, json=position_data)
