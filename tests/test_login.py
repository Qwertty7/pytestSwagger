import pytest
import requests

from src.login import BASE_URL, APIError, APIService, AuthenticationError


@pytest.mark.parametrize('email,password,status_code', [
    ("student@example.com", "welcome", 200),
    ("s@example.com", "welcome", 400),
    ("student@example.com", "weme", 401)
])
def test_login_data (email, password, status_code):
    login_url = BASE_URL + '/login'
    response = requests.post(login_url, json={'email': email, 'password': password})
    assert response.status_code == status_code


@pytest.mark.parametrize('email, password, expected_exception', [
    ("s@example.com", "welcome", APIError),
    ("student@example.com", "wome", AuthenticationError)
])
def test_method_login_with_invalid_data(email, password, expected_exception):
    with pytest.raises(expected_exception):
        API = APIService()
        API.login(email, password)
