import random
from datetime import datetime, timedelta

class Urls:
    BASE_URL = 'http://qa-scooter.praktikum-services.ru'

class Endpoints:
    CREATE_COURIER  = '/api/v1/courier'                 # POST Создание курьера
    LOGIN_COURIER   = '/api/v1/courier/login'           # POST Логин курьера в системе
    DELETE_COURIER  = '/api/v1/courier/'                # DELETE Удаление курьера (/api/v1/courier/:id)
    CREATE_ORDER    = '/api/v1/orders'                  # POST Создание заказа
    GET_ORDER_LIST  = '/api/v1/orders'                  # GET Получение списка заказов



class OrderData:
    name_list = ["Таня", "Аня", "Ивана", "Всеволод", "Пётр", "Илья", "Евсений"]
    name = random.choice(name_list)

    surname_list = ["Иванов", "Сергеев", "Алексеев", "Сергеенко", "Петрова"]
    surname = random.choice(surname_list)

    address_list = ["Москва, ул. Самокатная, д. 132", "город Иваново, улица Петрова, 77", "г. Москва, ул. Бауманская, д.131", "Москва, Андреевка, 15", "г. Москва, г. Зеленоград, корпус 1832"]
    address = random.choice(address_list)

    phone = f'+7{random.randint(9000000000, 9999999999)}'

    comment_list = ["Пожалуйста, доставьте самокат в указанное время и место.",
                    "Не забудьте осторожно обращаться с самокатом при доставке.",
                    "Жду с нетерпением приятную и быструю доставку самоката.",
                    "Буду благодарен за оперативность и профессионализм в доставке самоката.",
                    "Уверен, что ваш курьер надежно упакует и доставит самокат."
                    "Надеюсь, курьер будет вежливым и поможет мне с самокатом при доставке."
                    "Спасибо, что заботитесь о сохранности самоката при его доставке."]
    comment = random.choice(comment_list)


    # Текущая дата и время
    current_datetime = datetime.now()
    # Количество дней, на которое нужно сдвинуть дату в будущее
    days_to_add = 7
    # Генерация будущей даты
    future_datetime = current_datetime + timedelta(days=days_to_add)
    # Форматирование даты в нужном формате
    future_datetime_str = future_datetime.strftime('%Y-%m-%d')
    date = future_datetime_str

