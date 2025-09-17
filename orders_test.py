# Юлия Иванько, 34-я когорта — Финальный проект. Инженер по тестированию плюс

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API. 
import sender_stand_request 
# Импорт данных запроса из модуля data
import data

def test_create_and_get_order_by_track():
    response = sender_stand_request.post_new_order(data.user_order)
    assert response.status_code == 201

    resp_json = response.json()
    track = resp_json.get("track")

    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200
    