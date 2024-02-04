import pytest
import requests
import json
import allure
from data import Urls as url
from data import Endpoints as ep
from data import OrderData as order


class TestCreatingOrder:
    @allure.title("Тест на успешное создание заказа при разном заполнении поля 'Цвет'")
    @allure.description('Отправляем запрос, который создаёт заказ с разным заполнением поля "цвет" и проверяем, '
            'что вернулся ожидаемый код и текст ответа об успешном создании содержит track')
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order(self, color):
        payload = json.dumps({
            "firstName": order.name,
            "lastName": order.surname,
            "address": order.address,
            "metroStation": 4,
            "phone": order.phone,
            "rentTime": 5,
            "deliveryDate": order.date,
            "comment": order.comment,
            "color": color
        })

        request_url = f'{url.BASE_URL}{ep.CREATE_ORDER}'
        with allure.step("Шаг 1: Отправка POST-запроса на создание заказа с цветом {color}"):
            response = requests.post(request_url, data=payload)
        with allure.step("Шаг 2: Проверка кода ответа"):
            assert response.status_code == 201
        with allure.step("Шаг 3: Проверка сообщения текст ответа соответствует ожидаемому значению. В ответе есть 'track'"):
            assert "track" in response.text

