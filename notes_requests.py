# HTTP - Hyper Text Transfer Protocol
# Состоит из 2 часте запрос(request) и ответ(response)
# Request состоит из Headers и Body, Response из Headers, Cookies и Body.

# Заголовки — это набор пар имя-значение, разделенных двоеточием.
# В заголовках передается различная служебная информация:
# кодировка сообщения, название, версия браузера, адрес, с которого пришел клиент (Referrer) и так далее.

# Тело сообщения — это, собственно, передаваемые данные.
# В ответе передаваемыми данными, как правило, является html-страница, которую запросил браузер,
# а в запросе, например, в теле сообщения передается содержимое файлов, загружаемых на сервер.
# Но как правило, тело сообщения в запросе вообще отсутствует

# Основные запросы:
# GET — получение ресурса
# POST — создание ресурса

# Другие:
# PUT — обновление ресурса
# DELETE — удаление ресурса
# ...

# https://www.google.ru/search?q=translate&oq=translate&aqs=chrome..69i57j0l5.3912j0j8&sourceid=chrome&ie=UTF-8&safe=active&ssui=on
# query_args - так называют параметры, которые мы передаем с запросом по url
# Из ссылки выше - это все ключ=значение, которые идут после знака '?':  oq=translate, sourceid=chrome и т.д
# Разделяются они занком '&'.


import requests
# Использовать virtualenv!


# GET
def get_proglib():
    r = requests.get('https://proglib.io')
    print(r.status_code, '\n')
    print(r.headers, '\n')
    print(r.content, '\n')


# GET
def find_pet_by_tag(tag):
    params = {'tags': tag}  # query_args
    headers = {'Accept': 'application/xml'}  # 'Accept': 'application/json'
    url = 'http://petstore.swagger.io/v2/pet/findByTags'
    r = requests.get(url, params=params, headers=headers)
    print(r.status_code, r.headers, r.content, sep='\n\n')


if __name__ == '__main__':
    get_proglib()
    find_pet_by_tag('string')  # Do not work, because site is OLD!
