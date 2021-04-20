import requests


def get_map(x, y, delta, mode):
    d_mode = {'Scheme': 'map', 'Mixed': 'skl', 'Sputnik': 'sat'}
    map_params = {
        "ll": ",".join([str(x), str(y)]),
        "spn": f'{delta},{delta}',
        "l": d_mode[mode],
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)
    return response.content
