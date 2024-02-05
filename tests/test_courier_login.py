import pytest
import requests
import allure
from data import Urls as url
from data import Endpoints as ep
from data import CourierErrors


class TestCourierLogin:
    @allure.title("Тест на успешный логин курьера")
    @allure.description("Проверка кода ответа и возврата 'id' в тексте ответа при успешном логине")
    def test_successful_login(self, registered_courier):
        payload = registered_courier
        request_url = f'{url.BASE_URL}{ep.LOGIN_COURIER}'
        with allure.step("Шаг 1: Отправка POST-запроса на логин курьера в системе"):
            response = requests.post(request_url, data=payload)
        with allure.step("Шаг 2: Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Шаг 3: Проверка сообщения при успешном ответе - 'id' курьера в тексте"):
            assert "id" in response.text, "Ошибка: Отсутствует 'id' курьера в тексте"


    @allure.title('Тест на ошибки при авторизации без передачи поля логина')
    @allure.description(
    'Отправляем запрос, который авторизует курьера без поля логина и проверяем, '
    'что вернулся ожидаемый код и текст ответа об ошибке'
    )
    def test_login_courier_no_login(self, registered_courier):
        payload = registered_courier.copy()
        # Удаляем поле login из payload
        del payload['login']
        request_url = f'{url.BASE_URL}{ep.LOGIN_COURIER}'
        with allure.step("Шаг 1: Отправка POST-запроса на логин курьера в системе"):
            response = requests.post(request_url, data=payload)
        with allure.step("Шаг 2: Проверка кода ответа"):
            assert response.status_code == 400
        with allure.step("Шаг 3: Проверка сообщения текст ответа соответствует ожидаемому значению"):
            assert response.json()['message'] == CourierErrors.error_login_no_data, "Ошибка: Неверное сообщение об ошибке"

    @allure.title('Тест на ошибки при авторизации без передачи поля пароль')
    @allure.description(
        'Отправляем запрос, который авторизует курьера без поля пароль и проверяем, '
        'что вернулся ожидаемый код и текст ответа об ошибке'
    )
    def test_login_courier_no_password(self, registered_courier):
        payload = registered_courier.copy()
        # Удаляем поле password из payload
        del payload['password']
        request_url = f'{url.BASE_URL}{ep.LOGIN_COURIER}'
        with allure.step("Шаг 1: Отправка POST-запроса на логин курьера в системе"):
            response = requests.post(request_url, data=payload)
        with allure.step("Шаг 2: Проверка кода ответа"):
            assert response.status_code == 400
        with allure.step("Шаг 3: Проверка сообщения текст ответа соответствует ожидаемому значению"):
            assert response.json()['message'] == CourierErrors.error_login_no_data, "Ошибка: Неверное сообщение об ошибке"



    @allure.title('Тест на ошибки при авторизации с пустым значением в поле логина или пароля')
    @allure.description(
        'Отправляем запрос, который авторизует курьера с пустым значением в поле логина или пароля и проверяем, '
        'что вернулся ожидаемый код и текст ответа об ошибке'
    )
    @pytest.mark.parametrize("login, password", [
        ('', 'somepassword'),
        ('somelogin', ''),
        ('', '')
    ])
    def test_login_courier_empty_credentials(self, registered_courier, login, password):
        payload = registered_courier.copy()
        payload['login'] = login
        payload['password'] = password
        request_url = f'{url.BASE_URL}{ep.LOGIN_COURIER}'
        with allure.step("Шаг 1: Отправка POST-запроса на логин курьера в системе"):
            response = requests.post(request_url, data=payload)
        with allure.step("Шаг 2: Проверка кода ответа"):
            assert response.status_code == 400
        with allure.step("Шаг 3: Проверка текста ответа соответствует ожидаемому значению"):
            assert response.json()['message'] == CourierErrors.error_login_no_data, "Ошибка: Неверное сообщение об ошибке"

    @allure.title('Тест на ошибки при авторизации с несуществующей парой логин и пароль')
    @allure.description(
        'Отправляем запрос, который авторизует курьера с несоответствующим значением в поле логина или пароля и проверяем, '
        'что вернулся ожидаемый код и текст ответа об ошибке'
    )
    @pytest.mark.parametrize('invalid_field', ['login', 'password'])
    def test_invalid_field_courier(self, registered_courier, invalid_field):
        payload = registered_courier.copy()
        payload[invalid_field] += 'invalid'
        request_url = f'{url.BASE_URL}{ep.LOGIN_COURIER}'
        with allure.step("Шаг 1: Отправка POST-запроса на логин курьера в системе"):
            response = requests.post(request_url, data=payload)
        with allure.step("Шаг 2: Проверка кода ответа"):
            assert response.status_code == 404
        with allure.step("Шаг 3: Проверка текста ответа соответствует ожидаемому значению"):
            assert response.json()['message'] == CourierErrors.error_login_no_such_user, "Ошибка: Неверное сообщение об ошибке"

