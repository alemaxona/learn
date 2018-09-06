# Class

# int(integer, тип данных) - Это класс, а 1 2 3 - его обекты(еще можно назвать экземпляры)
# В терминологии Python члены класса называются атрибутами,
# функции класса — методами, а поля класса — свойствами (или просто атрибутами).
# Определения методов аналогичны определениям функций,
# но (за некоторыми исключениями, о которых ниже) методы всегда имеют первый аргумент,
#  называемый по общепринятому соглашению self.

class Student(object): # Класс, можно не писть - (object). Имя класса всегда с большой буквы!
    school = 286 # Атрибут (или поле класса). Все созданные объекты по этому кклассу будут иметь этот атрибут.
    learn = 'Python' # Второй атрибут. Все созданные объекты по этому кклассу будут иметь этот атрибут.
    def info(self, name, age):  # Метод. self - ОБЯЗАТЕЛЬНЫЙ аргумент метода.
        # И 2 не обязательных аргумента.Все созданные объекты по этому кклассу будут иметь этот метод.
        self.name = name # 1-ый атрибут метода
        self.age = age
        print(self.name, self.age)

c = Student() # Создание объекта класса Student
print(c.school, c.learn)
#286 Python
c.name = 'Max'
c.age = 30
print('Student {} learn in {}'.format(c.name, c.school))
# Student Max learn in 286

print(c.info('Kate', 29))
#Kate 29
#None

# Класс конструтор
# Конструктором класса называют метод, который автоматически вызывается при создании объектов.
# Его также можно назвать конструктором объектов класса.
# Имя такого метода обычно регламентируется синтаксисом конкретного языка программирования.
# В Python роль конструктора играет метод __init__().
class Person:
    def __init__(self, n, s): # Если аргементам не присовены знаечения(self, n = 3, s = 5), их необходимо будет указывать при создании объекта класса!
        self.name = n
        self.surname = s


p1 = Person("Max", "M") # Если не указать аргументы, - будет ошибка!
print(p1.name, p1.surname)
#Max M
#
class Table:
    def __init__(self, number_of_legs):
        print('New table has {} legs'.format(number_of_legs))

t = Table(4)
#
class Chair:
    def __init__(self, color):
        self.color = color

c = Chair('green')
print(c, c.color)

#class Door(object):
class Door:
    def open(self):  # note that `self` is the object itself!
        print('self is', self)
        print('Door is opened!')
        self.opened = True

d = Door()
d.open()

d1 = Door()
d1.open() # == Door.open(d1)

# Add __doc__ to function!
def print_doc():
    '''Notes for learning.

    This learning Python 3 notes.
    Here more errors.'''
print(print_doc.__doc__)

# index letter
chose = 'max'
c = 'm'
index = 0
c == chose[index]
#True
a = chose[index]
print(a)
#m

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
s.update({2: 'q'}) #Мутация в словаре. Добавить пару ключ - значение
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


# FUNCTIONS Всегда с маленькой буквы!

def return_none(x):
    print('Param was', x) #Если у функции нет return то она возвращает None!
test = return_none(6)
#Param was 6

print(test)
#None

def sum_numbers(n1, n2, n3):
    print(n1, n2, n3, 'summing...')
    return n1 + n2 + n3

total = sum_numbers(7, 0.3, 0.3)
#7 0.3 0.3 summing...

print(total)
#7.6


def sum_my(a, b=3): # Значение по умолчанию, если аргумент не ввели!
    print(a + b)
# >>> sum_my(1)
#4

#def my_numbers(*args): # Сколь угодно аргументов!

# Class - DICT!
def any_keywords(**kwargs): # Сколь угодно елементов со значением по умолчанию!
    print(kwargs, type(kwargs))

any_keywords(k=1, some=2, wo=3)
#{'k': 1, 'some': 2, 'wo': 3} <class 'dict'>

#CLass - TUPLE. LIST??
def any_keywords(*kwargs): # Сколь угодно елементов со значением по умолчанию!
    print(kwargs, type(kwargs))

any_keywords([1, 2, 3, 4, 5])

#
print('Word', end = '!')
#Word!>>>

print('Word', end = '\n')
#Word
#>>>

#Является ли аргумент функцией? callable()
callable(print)

#Не обязательно ставить "()" у функции, нужно стаить "()" при объявлении и вызове!
def return_min_function():
    return min

test = return_min_function()
min_value = test(4, 5, -9, 12)
print('Min values is', min_value)

#Глобальные переменные принято называть БОЛЬШИМИ БУКВАМИ: GLOBAL_VAR = []!
#Замыкание - возможность функций использовать чужие переменные!
#Рекурсия - способ функции вызвать саму себя! (Медленная! Лучше циклы!)


print('Max', end='!') #Не переходит на новую строку
print('Max', end='\n')

s, k = (1,2) #Но не s,k,m = (1,2)
print(s,k)
#1 2

first, *second = (1,2,3,4,5)
print(first,second)
#1 [2, 3, 4, 5]

*f,s = 'Moscow'
print(f)
#['M', 'o', 's', 'c', 'o']

def accept_args(*args):
    print(args)
    return sum(args)
print(accept_args(1,2,3,4,5)) #Tuple
values = [1,2,3,4,5] #List
accept_args(values) #Будет ошибка!
accept_args(*values) #Будет работать! Распаковка! Tuple => List

def accept_kwargs(**kawargs):
    print(kawargs)
accept_kwargs(name='Max', job='DBA')
values = {'day':'wed', 'month':'may'}

accept_kwargs(values)#Будет ошибка!
accept_kwargs(**values)#Будет работать! Распаковка! Сколько пар - столько и ключей!
