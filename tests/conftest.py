import pytest
from faker import Faker


@pytest.fixture
def candidate_data ():
    f = Faker()
    first_name = f.first_name()
    last_name = f.last_name()
    email = f.email()
    password = f.password()

    candidate_data = {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password

    }
    return candidate_data
