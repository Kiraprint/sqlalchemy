import requests


def get_map(x, y, delta):
    map_params = {
        "ll": ",".join([str(x), str(y)]),
        "spn": f'{delta},{delta}',
        "l": "sat",
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)
    return response.content
