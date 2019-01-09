# -*- coding: utf-8 -*-


# JSON - JavaScript Object Notation
# Как собособ представить объект ввиде текса
# Двойные кавычки
# Примеры того, как выглядит формат JSON

# { "name": "Max"}  # Пробелы необязательны!

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
obj = json.loads(data)  # Преобразует строку в словарь
# obj = json.dumps(data)  # Преобразует словарь в строку
print(obj, 'TYPE - ', type(obj), '\n')
print(obj['none'], obj['object']['key'])

# Можно использовать jsonify из модуля flask.json

from flask.json import jsonify


def my_dict():
    my_locale = {'ru': 'russian', 'en': 'english', 'it': 'italian'}
    return jsonify(my_locale)
