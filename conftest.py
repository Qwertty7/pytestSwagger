
import pytest
import requests


# parametrized fixture function:
# scope is default now - for each test
# объявляем фикстуру
#
#    @pytest.fixture(params=[('student@example.com,', 'welcome'), ('jane@exmaple.com', 'bla')])
   # def login (email, password):
   #     login_url = '/recruit-portnov.herokuapp.com/recruit/api/v1/login'
   #     response = requests.post(login_url, json={'email': email, 'password': password})
   #     response_json = response.json()
   #     if 'aithenticated' in response_json['authenticate']:
   #         token = response_json['token']
   #     else:
   #         with pytest.raises(RuntimeError):
   #             print('error')



import requests


class BaseClient(object):
    def __init__(self, client=None):
        self.client = client

        if client and isinstance(client, BaseClient):
            self.base_url = client.base_url
            self.session = client.session
        else:
            self.base_url = 'https://recruit-portnov.herokuapp.com/recruit/api/v1'
            self.session = requests.Session()
            self.session.headers.update({'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        )


@pytest.fixture
def client():
    return BaseClient






