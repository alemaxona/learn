#
a = ['s', 'b', 'g']

print(range(len(a)))
#range(0, 3)

for i in range(len(a)):
    print(a[i])
#s
#b
#g


# Встроенные объекты. (list, int, dict, len...)
import builtins # Можно не импортировать!
print(dir(__builtins__))

# Короткая запись - Списковые выражения:
s = [w for w in range(1, 14)]
print(s)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

s = [w for w in range(1, 14) if w % 2 == 0]
print(s)
# [2, 4, 6, 8, 10, 12]

#
import os
print(os)
#<module 'os' from '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py'>

# Сравнение
1 == 1 # По сути сравнение ячеек памяти.

a = 257
b = 257 # Так как > 256 (С кешем связано...)
a is b
#False
id(a), id(b)
#(31833360, 31833120)

a = 256
b = 256
a is b
#True
id(a), id(b) #Посмотреть ячейку памяти
#(266881264, 266881264)

1 == True
# True
1 is True
# False


# Help
help(object)


# Функция isinstance() специально создана для проверки принадлежности данных определенному классу (типу данных).
isinstance(a, int)
# True
isinstance(b, list)
# True
isinstance(b, tuple)
# False
c = (4,5,6)
isinstance(c,tuple)
# True

#  Если словарь пустой то возвращается False!
bool({}) # По сути идет сравнение длины, если длина = 0, то возвращается False!
# False
bool ({'Max': 5})
# True

# Сравнение едит по ключам!
2 in {'1': 2}
# False
'1' in {'1': 2}
# True


# Короткая запись условия
value  = 2

if value > 0:
    print(str(value))
else:
    print('')

#==

print(str(value)) if value > 0 else print('')


# index letter
chose = 'max'
c = 'm'
index = 0
c == chose[index]
#True
a = chose[index]
print(a)
#m


#
s, k = (1, 2) #Но не s,k,m = (1,2)
print(s, k)
#1 2

first, *second = (1, 2, 3, 4, 5)
print(first, second)
#1 [2, 3, 4, 5]

*f,s = 'Moscow'
print(f)
#['M', 'o', 's', 'c', 'o']


#
print('Word', end = '!')
#Word!>>>

print('Word', end = '\n')
#Word
#>>>
print('Max', end='!') #Не переходит на новую строку
print('Max', end='\n')


#RANDOM
from random import randint
value = randint(0, 20)
print(value)
#12

import random
items = ['one', 'two', 'three', 'four', 'five']
random.choice(items)
#'four'

#
tuple1 = (1, 2, 'string', 'one more', )
new_tuple = tuple()
for item in tuple1:
    # if not isinstance(item, (str, unicode)):  # or `basestring`
    if not isinstance(item, str): # Если этот елемент не строка
        new_tuple += (item, ) # new_tuple = new_tuple + (item, )
print(new_tuple)
#(1, 2)

#
list1 = [1, 2 ]
list2 = [7, 8 ]
list1.append(list2) # Мутация, append - добавление в список 1 елемент
print(list1)
#[1, 2, [7, 8]]

list1.extend(list2) # Мутация, extend - добавление нескольких елементов
print(list1)
#[1, 2, 7, 8]

list1.insert(1, 'str') # Не стоит использовать! 1 здесь позиция в list
#list1.pop(1) # Delete element for index
#list1.remove('2') # Delete element for value
#del list1[0] # Delete element for index !Некрасивая версия pop!


for row in multi:
    for element in row:

list(range(1, 10, 1)) # Генератор. 3 параметр - шаг
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

# Все ключи в словаре уникальные!
# Неизменяемый тип данных не может быть ключем!
s = {'a' : 'a', 1 : 'str', None : 3}
s.update({2: 'q'}) # Мутация в словаре. Добавить пару ключ - значение
s[2] = None
#s[ma] # Выдаст ошибку, так как ключа такого нет
#s.get(ma) # Ошибку не выдаст, но и результат тоже.
#s.keys() # Получить ключи словаря
#s.values() # Получить елементы словаря
for k in s:
    print(k, s[k])
#s s
#1 str
#None 3

for k, v in s.items():
    print(k, v)
#s s
#1 str
#None 3

#s.pop('s') # Удаляет и ключ и значение

#
try:
    print(1 / 0)
except Exception:  # it is almost the same as just `except:`
    print('0!!')
#
#try:
#    1 / 0
#except ValueError: # Не сработает так как ошибка ZeroDivisionError а не ValueError!
#    print('0!!')

try:
    1 / 0
except ZeroDivisionError: # Сработает так как ошибка ZeroDivisionError!
    print('0!!')
#
try:
    1 / int(input('x: '))
except ZeroDivisionError:
    print('/0')
except TypeError:
    print('WrongValue')

#
try:
    print(1 / 0)
except ZeroDivisionError as e: # В переменную!
    print('Exception! Stop it!')
    print(e)
#
raise IndexError('Hi!') # Выкинуть ошибку
#
try:
    raise TypeError('Some message')
except TypeError as e:
    print(e)
#Some message

try:
    print('Fine')
except KeyError:
    print('Nope')
else:
    print('Else clause')
#Fine
#Else clause

try:
    print(1 / 0)
except ZeroDivisionError:
    print('0!')
finally: # finally всегда работает!
    print('I will be called in the end!')
#0!
#I will be called in the end!

try:
    print('try')
except ValueError:
    pass #Игнорирует ошибку!
    print('else')
finally:
    print('finally')


