# Импорт настроек
import configuration
# Импорт библиотеки requests для выполнения HTTP-запросов 
import requests 
# Импорт данных запроса из модуля data
import data

# Функция отправки POST-запроса на создание нового заказа пользователя
def post_new_order(user_order):
    # URL_SERVICE и CREATE_USER_ORDERS объединяются для формирования полного URL для запроса
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_ORDERS, 
                         json=user_order)
# Вызов функции post_new_order с телом запроса для создания нового заказа пользователя из модуля data
response = post_new_order(data.user_order)

# Выполнить запрос на получение заказа по треку заказа
def get_order_by_track(track):
    params = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,
                         params=params)

track = response.json().get("track")
response = get_order_by_track (track)

