<<<<<<< HEAD
# Sprint_7
=======
Тестирование API для веб-сайта: https://qa-scooter.praktikum-services.ru/

Документация: https://qa-scooter.praktikum-services.ru/docs/


Основа для написания автотестов — фреймворк pytest

Установить зависимости из requirements.txt

Команда для запуска — pytest .\tests --alluredir=allure_results


Файлы с тестами лежат в папке tests и имеют следующие название:

1. test_creating_a_courier.py - тесты по созданию курьера

test_create_courier - проверка создания курьера с уникальными данными (код ответа сервера и текст ответа);
test_create_courier_without_a_login- проверка создания курьера без обязательного поля (логин);
test_create_courier_without_a_password- проверка создания курьера без обязательного поля (пароль);
test_create_courier_duplicate_login- проверка, что невозможно создать двух пользователей с одним логином;

2. test_courier_login.py - тесты по авторизации курьера

test_successful_login- курьер может авторизоваться (статус кода и возврат id);
test_login_courier_no_login - ошибка авторизации без передачи логина;
test_login_courier_no_password - ошибка без передачи пароля;
test_login_courier_empty_credentials - параметризованный тест при передачи запроса с пустым значением логина или пароля - ошибка авторизации;
test_invalid_field_courier- параметризованный тест при передачи запроса с несуществующей парой логин и пароль - ошибка авторизации;


3. test_creating_an_order.py - тесты по созданию заказа

test_create_order - параметризованный тест, который возвращает track при: 
- указать один из цветов — BLACK или GREY
- указать оба цвета
- совсем не указывать цвет;

4. test_list_of_orders.py - тесты по проверке списка заказов

test_list_order -на возврат списка заказов в тело ответа и код ответа.
>>>>>>> 3d10d10 (The first delivery of the project)
