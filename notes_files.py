__author__ = 'alemaxona'

# Символ "r" - отключает экранирование, иначе python увидел бы: \f
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