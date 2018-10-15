# Генераторы
# Генератор работает с каждым значением только 1 раз!
# В генераторе не может быть return


def fib():
    a, b = 0, 1  # a = 1, b = 1
    while True:
        yield a  # Как return, но не останавливает работу функции.
        a, b = b, a + b


x = fib()
print(x)
# <generator object fib at 0x030B8F30>
next(x)
# 0
next(x)
# 1


# Бесконечный генератор
def fib():
    while True:
        yield 'value'


# Получение генераторы из массива - функия iter
x = iter([1, 2, 3])
print(x)
# <list_iterator object at 0x005B0950>
next(x)
# 1
next(x)
# 2
next(x)
# 3
next(x)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

fib_gen = fib()
for index, _ in enumerate(range(10)):  # _ - Разаработчики показывают, что аргумент не нужен.
    print(index, next(fib_gen))



