import requests
import pytest
import register
from data import Urls as url
from data import Endpoints as ep
from faker import Faker
from register import register_new_courier_and_return_login_password



@pytest.fixture
def registered_courier():
    login, password, firstname = register.register_new_courier_and_return_login_password()
    payload = {
        "login": login,
        "password": password
    }

    yield payload
    response = requests.post(f'{url.BASE_URL}{ep.LOGIN_COURIER}', data=payload)
    courier_id = response.json()["id"]
    requests.delete(f'{url.BASE_URL}{ep.DELETE_COURIER}{courier_id}')


@pytest.fixture(scope="function")
def fake_courier_data():
    fake = Faker(locale="ru_RU")
    payload = {"login": fake.user_name(),
                 "password": fake.password(),
                 "firstName": fake.first_name()
                 }

    yield payload
    response = requests.post(f'{url.BASE_URL}{ep.LOGIN_COURIER}', data=payload)
    if response.status_code == 201:
        courier_id = response.json()["id"]
        requests.delete(f'{url.BASE_URL}{ep.DELETE_COURIER}{courier_id}')

