# Add __doc__ to function!
def print_doc():
    '''Notes for learning.

    This learning Python 3 notes.
    Here more errors.'''
    print(print_doc.__doc__)


# FUNCTIONS Всегда с маленькой буквы!
def return_none(x):
    print('Param was', x) # Если у функции нет return то она возвращает None!


test = return_none(6)
# Param was 6
print(test)
# None


def sum_numbers(n1, n2, n3):
    print(n1, n2, n3, 'summing...')
    return n1 + n2 + n3


total = sum_numbers(7, 0.3, 0.3)
# 7 0.3 0.3 summing...
print(total)
# 7.6


def sum_my(a, b=3): # Значение по умолчанию, если аргумент не ввели!
    print(a + b)


# >>> sum_my(1)
# 4

# def my_numbers(*args): # Сколь угодно аргументов!
# Class - DICT!
def any_keywords(**kwargs): # Сколь угодно елементов со значением по умолчанию!
    print(kwargs, type(kwargs))


any_keywords(k=1, some=2, wo=3)
# {'k': 1, 'some': 2, 'wo': 3} <class 'dict'>


# CLass - TUPLE. LIST??
def any_keywords(*kwargs): # Сколь угодно елементов со значением по умолчанию!
    print(kwargs, type(kwargs))


any_keywords([1, 2, 3, 4, 5])


# Является ли аргумент функцией? callable()
callable(print)


# Не обязательно ставить "()" у функции, нужно стаить "()" при объявлении и вызове!
def return_min_function():
    return min


test = return_min_function()
min_value = test(4, 5, -9, 12)
print('Min values is', min_value)


# Глобальные переменные принято называть БОЛЬШИМИ БУКВАМИ: GLOBAL_VAR = []!
# Замыкание - возможность функций использовать чужие переменные!
# Рекурсия - способ функции вызвать саму себя! (Медленная! Лучше циклы!)


def accept_args(*args):
    print(args)
    return sum(args)


print(accept_args(1,2,3,4,5)) # Tuple
values = [1,2,3,4,5] # List
accept_args(values) # Будет ошибка!
accept_args(*values) # Будет работать! Распаковка! Tuple => List


def accept_kwargs(**kawargs):
    print(kawargs)


accept_kwargs(name='Max', job='DBA')
values = {'day':'wed', 'month':'may'}
accept_kwargs(values)# Будет ошибка!
accept_kwargs(**values)# Будет работать! Распаковка! Сколько пар - столько и ключей!