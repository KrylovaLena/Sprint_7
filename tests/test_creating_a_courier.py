import pytest
import requests
import allure
import random
import string
from data import Urls as url
from data import Endpoints as ep


class TestCreatingCourier:
    @allure.description('Проверяем успешное создание курьера')
    @allure.title('Создание курьера с новыми данными')
    def test_create_courier(self, fake_courier_data):
        request_url = f'{url.BASE_URL}{ep.CREATE_COURIER}'
        with allure.step("Шаг 1: Отправка POST-запроса на создание курьера"):
            response = requests.post(request_url, json=fake_courier_data)
        with allure.step("Шаг 2: Проверка кода ответа"):
            assert response.status_code == 201, "Ошибка: Неверный код ответа"
        with allure.step("Шаг 3: Проверка сообщения об успешном создании учетной записи"):
            assert response.json()['ok'] == True, "Ошибка: Создание учетной записи не удалось"


    @allure.description('Проверяем создание курьера без одного из обязательных полей')
    @allure.title('Создание курьера с новыми данными (без логина)')
    def test_create_courier_without_a_login(self, fake_courier_data):
        request_url = f'{url.BASE_URL}{ep.CREATE_COURIER}'
        with allure.step("Шаг 1: Отправка POST-запроса на создание курьера без логина"):
            courier_data = fake_courier_data.copy()
            courier_data.pop("login")
            response = requests.post(request_url, json=courier_data)
        with allure.step("Шаг 2: Проверка кода ответа"):
            assert response.status_code == 400, "Ошибка: Неверный код ответа"
        with allure.step("Шаг 3: Проверка сообщения об ошибке при создании учетной записи"):
            assert response.json()['message'] == "Недостаточно данных для создания учетной записи", "Ошибка: Неверное сообщение об ошибке"



    @allure.description('Проверяем создание курьера без одного из обязательных полей')
    @allure.title('Создание курьера с новыми данными (без пароля)')
    def test_create_courier_without_a_password(self, fake_courier_data):
        request_url = f'{url.BASE_URL}{ep.CREATE_COURIER}'
        with allure.step("Шаг 1: Отправка POST-запроса на создание курьера без пароля"):
            courier_data = fake_courier_data.copy()
            courier_data.pop("password")
            response = requests.post(request_url, json=courier_data)
        with allure.step("Шаг 2: Проверка кода ответа"):
            assert response.status_code == 400, "Ошибка: Неверный код ответа"
        with allure.step("Шаг 3: Проверка сообщения об ошибке при создании учетной записи"):
            assert response.json()['message'] == "Недостаточно данных для создания учетной записи", "Ошибка: Неверное сообщение об ошибке"


    @allure.description('Проверяем обработку неуникального логина при создании курьера')
    @allure.title('Создание курьера с неуникальным логином')
    def test_create_courier_duplicate_login(self, fake_courier_data):
        request_url = f'{url.BASE_URL}{ep.CREATE_COURIER}'
        with allure.step("Шаг 1: Отправка POST-запроса на создание курьера"):
            response = requests.post(request_url, json=fake_courier_data)
        with allure.step("Шаг 2: Отправка POST-запроса на повторное создание курьера с тем же логином"):
            duplicate_response = requests.post(request_url, json=fake_courier_data)
        with allure.step("Шаг 3: Проверка кода ответа"):
            assert duplicate_response.status_code == 409, "Ошибка: Неверный код ответа"
        with allure.step("Шаг 4: Проверка сообщения об ошибке"):
            assert duplicate_response.json()["message"] == "Этот логин уже используется. Попробуйте другой.", "Ошибка: Неверное сообщение об ошибке"