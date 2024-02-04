import requests
import random
import string
import pytest
import register
from data import Urls as url
from data import Endpoints as ep




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
    def generate_random_string(length):
        # Генерация случайной строки заданной длины
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # Генерация случайных данных для регистрации нового курьера
    login = generate_random_string(13)
    password = generate_random_string(13)
    first_name = generate_random_string(13)

    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }

