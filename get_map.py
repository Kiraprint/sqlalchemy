import requests


def get_map(x, y, delta, mode, point):
    d_mode = {'Scheme': 'map', 'Mixed': 'skl', 'Sputnik': 'sat'}
    map_params = {
        "ll": ",".join([str(x), str(y)]),
        "spn": f'{delta},{delta}',
        "l": d_mode[mode],

    }
    if point:
        map_params.update({"pt": f"{point},pm2dgl"})
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)
    return response.content
