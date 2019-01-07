__author__ = 'alemaxona'


def usr_path(path):
    file = '/Users/alemaxona/Documents/Projects/venv/lern12flask/' + path
    try:
        f = open(file)
        f.close()
        print('Yes')
        return 'Yes'
    except FileNotFoundError:
        print('No')
        return 'No'


usr_path('test/ttt')


# Символ "r" - отключает экранирование, иначе python увидел бы: \f
# Экранировать символ '\' можно так - \\
path = 'C\\users'
print(path)
# C\users

filename = r'C:\Project\learn\files\file.txt'
f = open(filename)
content = f.read()
print(content)
f.close()

# Создание, чтение, запись и добавление в\из файл\а
filename = 'file_create_with_python.txt'
open(filename, 'a')  # Создание фала в текущей дирректории
open('file.txt')  # ('r' - по умолчанию.) Открытие файла и чтение
open('file.txt', 'w')  # w - write  - Запись из файла
open('file.txt', 'a')  # a - append - Добавление в конец строки файла
# Обязательно нужно закрывать файл!
f = open('file.txt')
f.close()


# Эквивалентные операции.
# with - контекстный менеджер
with open('file.txt', 'w') as f:  # with - Закрывает файл и даже удаляет мусор, если будет ошибка.
    f.write('Hello world!')

f = open('file.txt', 'r')
# Если тут будет ошибка, файл не закроется!
print(f.read())
f.close()

# Если кодировка(по умолчанию - utf8) не понимает строки в файле, то ее
# можно ппрочитать по байтово (f = open('file.txt', 'rb')), а потом декодировать
# в другую кодировку (a = f.decode('cp1251'))!


# Создание каталога (в windows)
from os import *
source = r'C:\Project\dir_create_with_python'  # r - отключает механизм экранирования
makedirs(source)


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


