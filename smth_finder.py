import requests
from PIL import Image
from io import BytesIO


def get_org(toponym_to_find, mode):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
    d_mode = {'Scheme': 'map', 'Mixed': 'skl', 'Sputnik': 'sat'}

    find = toponym_to_find
    search_params = {
        "apikey": api_key,
        "text": find,
        "lang": "ru_RU",
        "results": 1
    }

    response = requests.get(search_api_server, params=search_params)
    if not response:
        print("smth with service searcher")

    json_response = response.json()

    # Получаем первую найденную организацию.
    organization = json_response["features"][0]
    # Название организации.
    org_name = organization["properties"]["CompanyMetaData"]["name"]
    # Адрес организации.
    org_address = organization["properties"]["CompanyMetaData"]["address"]

    # Получаем координаты ответа.
    point = organization["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": org_address,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]

    bound = (list(map(float, toponym["boundedBy"]["Envelope"]["lowerCorner"].split())),
             list(map(float, toponym["boundedBy"]["Envelope"]["upperCorner"].split())))

    delta = (str(bound[1][0] - bound[0][0]), str(bound[1][1] - bound[0][1]))
    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        # позиционируем карту центром на наш исходный адрес
        "ll": org_point,
        "spn": ",".join(delta),
        "l": d_mode[mode],
        # добавим точку, чтобы указать найденную организацию
        "pt": "{0},pm2dgl".format(org_point)
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)
    return response.content, org_point
