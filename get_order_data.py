# Мария Фёдорова, 8-я когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request

# Тест для проверки, что код ответа равен 200

def test_get_order_data_by_order_track():
    get_order_response = sender_stand_request.get_order_data()
    assert get_order_response.status_code == 200