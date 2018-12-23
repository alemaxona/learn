# -*- coding: utf-8 -*-


# Протокол WSGI - Web Server Gateway Interface
# Используется для общения Python-программы и сервера (Nginx, Apache) (PEP-3333)
# Используетс всеми web-фреймворками


# JSON - JavaScript Object Notation
# Как собособ представить объект ввиде текса
# Двойные кавычки
# Примеры того, как выглядит формат JSON

# { "name":"Max"}  # Пробелы необязательны!

# {
#     "people":{ "name": "Max", "age": 30 }
# }

# { "people":["Max", 30] }


import json
filename = r'C:\Project\learn\files\json_test.json'


def open_file(file):
    with open(file) as f:
        return f.read()


data = open_file(filename)  # Сейчас data - это строка!
print(data, 'TYPE - ', type(data), '\n')

# При преобразовании заменяет двойные кавычки на одинарные, null на None и т.д.
obj = json.loads(data)  # Преобразует строку в дикт
print(obj, 'TYPE - ', type(obj), '\n')
print(obj['none'], obj['object']['key'])