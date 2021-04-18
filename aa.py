import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image

# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])


def search_pharmacies(address):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

    search_params = {
        "apikey": api_key,
        "text": "аптека",
        "lang": "ru_RU",
        "ll": address,
        "type": "biz",
        "results": 10
    }

    response = requests.get(search_api_server, params=search_params)
    if not response:
        # ...
        pass
    # Преобразуем ответ в json-объект
    json_response = response.json()

    # Получаем первую найденную организацию.
    organizations = [json_response["features"][i] for i in range(10)]
    # Адрес организации.
    # Получаем координаты ответа.
    points = [i["geometry"]["coordinates"] for i in organizations]
    org_points = ["{0},{1}".format(points[i][0], points[i][1]) for i in range(10)]
    hours = [i["Hours"]["Availabilities"].get("TwentyFourHours", -1) for i in organizations]
    return org_points, hours


def geocode(t):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": t,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    return toponym


centre = geocode(toponym_to_find)
# Координаты центра топонима:
toponym_coodrinates = centre["Point"]["pos"]
# Долгота и широта:
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

pharms, hrs = search_pharmacies(f'{toponym_longitude},{toponym_lattitude}')
pts_sets = [0] * 10
for i in range(10):
    if hrs[i] == -1:
        pts_sets = f'{pharms[i]},pm2grm'
    elif not hrs:
        pts_sets = f'{pharms[i]},pm2blm'
    else:
        pts_sets = f'{pharms[i]},pm2dgm'
delta_x = max(map(lambda x: abs(float(x.split(',')[0]) - float(toponym_longitude)), pharms))
delta_x *= 1.05

delta_y = max(map(lambda x: abs(float(x.split(',')[1]) - float(toponym_lattitude)), pharms))
delta_y *= 1.05
# Собираем параметры для запроса к StaticMapsAPI:

map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": ",".join([str(delta_x), str(delta_y)]),
    "l": "sat",
    "pt": '~'.join(pts_sets)
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
# Создадим картинку
# и тут же ее покажем встроенным просмотрщиком операционной системы
