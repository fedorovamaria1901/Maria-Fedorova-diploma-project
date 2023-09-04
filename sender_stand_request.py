import configuration
import requests
import data

# Запрос на создание нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)

order_response = post_new_order(data.order_body.copy())
print(order_response.json())


# Запрос на получение заказа по треку заказа
def get_order_data():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params={'t': order_response.json()['track']})

get_order_response = get_order_data()
print(get_order_response.json())
