# HTTP - Hyper Text Transfer Protocol
# Состоит из 2 часте запрос(request) и ответ(response)
# Request состоит из Headers и Body, Response из Headers, Cookies и Body.

# https://www.google.ru/search?q=translate&oq=translate&aqs=chrome..69i57j0l5.3912j0j8&sourceid=chrome&ie=UTF-8&safe=active&ssui=on
# query_args - так называют параметры, которые мы передаем с запросом по url
# Из ссылки выше - это все ключ=значение, которые идут после знака '?':  oq=translate, sourceid=chrome и т.д
# Разделяются они занком '&'.


import requests
# Использовать virtualenv!


def get_proglib():
    r = requests.get('https://proglib.io')
    print(r.status_code, '\n')
    print(r.headers, '\n')
    print(r.content, '\n')


def find_pet_by_tag(tag):
    params = {'tags': tag}  # query_args
    headers = {'Accept': 'application/xml'}  # 'Accept': 'application/json'
    url = 'http://petstore.swagger.io/v2/pet/findByTags'
    r = requests.get(url, params=params, headers=headers)
    print(r.status_code, r.headers, '\n')
    print(r.content)


if __name__ == '__main__':
    get_proglib()
    find_pet_by_tag('string')  # Do not work!

