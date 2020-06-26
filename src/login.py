import requests
from requests import Session

BASE_URL = 'https://recruit-portnov.herokuapp.com/recruit/api/v1'


class AuthenticationError(Exception):
    pass


class APIError(Exception):
    pass


class APIService:
    """
    API service.
    """

    session = Session()

    def login(self, email, password):
        url = BASE_URL + '/login'
        response = requests.post(url, json={'email': email, 'password': password})
        json_data = response.json()
        if 'authenticated' in json_data and json_data['authenticated']:
            token = json_data['token']
            self.session.headers.update({'Authorization': f'Bearer {token}'})
            return token
        elif 'errorMessage' in json_data:
            raise APIError(json_data['errorMessage'])
        else:
            raise AuthenticationError("Authentication failed")

