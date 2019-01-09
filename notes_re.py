# -*- coding: utf-8 -*-


# Регулярные выражения!

# . - любой символ.  # Te.t - соответсвует и Text и Test!
# ^ - начало строки
# $ - конец строки
# [xs] - Любые символы из массива (x или s)
# [^xs] - Любые кроме x или s
# * - Параметр колличества (0 или больше)
# + - Параметр колличества (от 1(хотя бы одна буква) и больше)
# ? - Есть буква или нет
# Те.{2} - конкретное число вхождений
# Te\d - любая цифра (Тоже самое - Te[0123456789], Te[0-9])
# Te[a-zA-Z] - любая буква
# Te\w - Все буквы и нижнее подчеркивание(Тоже самое - Te[0-9a-zA-Z_])
# Другие символы  и примеры можно глянуть например тут - https://pythex.org/

import re

name_pattern = r'My name is .*\.'  # \. - Точка, а не любой символ!
is_name = re.match(name_pattern, 'My name is Maxim.')
print('is name:', bool(is_name))

is_name = re.match(name_pattern, 'I am just a string.')
print('is name:', bool(is_name))

name_pattern_group = r'My name is (.*)\.'  # (.*) - Скобки для вывода метода findall
name = re.findall(name_pattern_group, 'My name is Maxim.')
print(name)
# is name: True
# is name: False
# ['Maxim']


#
import re
import requests


def get_from_site(site: str):
    r = requests.get(site)
    return r.content


def parsing_site(site: str):
    pattern = r'(https://habr.com/[^\\].+?")'
    pars = re.findall(pattern, site)
    return pars


get_content = str(get_from_site('https://habrahabr.ru/'))

go_pars = parsing_site(get_content)
for i in go_pars:
    print(i)
