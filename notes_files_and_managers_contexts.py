__author__ = 'alemaxona'


print(__file__)  # Файл, который мы исполняем, то есть текущий!
# /Users/alemaxona/Documents/Projects/lern/notes_files.py


# Менеджер контекста
# Используется для того, чтобы выполнить код до и после.
# Нужен для того, чтобы, например сначала открыть файл, потом закрыть, или
# сделать предварительную авторизацию, а потом logout...
# Может быть классом или генератором

# В менеджере контекста всегда должны быть определены специальные методы __enter__ и __exit__!

class File:
    def __init__(self, file, mode):
        print('__init__')
        self.file = file
        self.mode = mode

    def __enter__(self):
        print('Open file')
        self.open_file = open(self.file, self.mode)
        return self.open_file

    def __exit__(self, *args):
        print('Close file')
        self.open_file.close


with File('file', 'w') as f:  # В f попадет return из __enter__!
    f.write('some text')
# На этой строке файл закроется! __Exit__ здесь всегда выполнится, даже если будет Exception.
# __init__
# Open file
# Close file

# Код выше можно заменить следующим кодом (более лаконичным):

from contextlib import contextmanager


@contextmanager
def do_work(file):
    user_file = open(file)
    yield user_file
    user_file.close()


with do_work('file') as f:
    print(f)

# some work before, __enter__
# 14
# some work after, __exit__


# Примеры из упражнений
# 1
class Lock:
    def __init__(self):
        self.lock = False

    def __enter__(self):
        self.lock = True
        return  self.lock

    def __exit__(self, *args):
        self.lock = False
        print('Exit, Again False.')


with Lock() as f:
    print(f)


# 2
class Exten:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __enter__(self):
        try:
            rez = self.value1 / self. value2
            return rez
        except Exception as f:
            return 'Exception message:', f
    
    def __exit__ (self, *args):
        print('Continues execution')

with Exten(4, 2) as f:
    print(f)
with Exten(1, 'str') as f:
    print(f)
with Exten(1, '0') as f:
    print(f)


# 3
from datetime import datetime

class Code_time:
    def __init__(self):
        pass

    def __enter__(self):
        a = datetime.now()
        print((2 ** 2048) ** 1024)
        b = datetime.now()
        rez = b.second - a.second
        return rez

    def __exit__(self, *args):
        pass


with Code_time() as f:
    print('Run time is {} seconds.'.format(f))


#
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
