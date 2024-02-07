import pytest
import requests
import json
import allure
from data import Urls as url
from data import Endpoints as ep


class TestListOrder:
    @allure.title("Тест на возврат списка заказов в тело ответа и код ответа")
    @allure.description('Отправляем запрос, который получает список заказов и проверяем, '
                        'что в тело ответа вернулся список заказов')
    def test_list_order(self):
        request_url = f'{url.BASE_URL}{ep.GET_ORDER_LIST}'
        with allure.step("Шаг 1: Отправка GET-запроса на получение списка заказов"):
            response = requests.get(request_url)
        with allure.step("Шаг 2: Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Шаг 3: Проверка что в ответе содержится список заказов"):
            assert "orders" in response.json() and type(response.json()["orders"]) is list