try:
    print(1 / 0)
except Exception:  # it is almost the same as just `except:`
    print('0!!')

#
# try:
#    1 / 0
# except ValueError: # Не сработает так как ошибка ZeroDivisionError а не ValueError!
#    print('0!!')

try:
    1 / 0
except ZeroDivisionError:  # Сработает так как ошибка ZeroDivisionError!
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
except ZeroDivisionError as e:  # В переменную!
    print('Exception! Stop it!')
    print(e)
#
raise IndexError('Hi!')  # Выкинуть ошибку
#
try:
    raise TypeError('Some message')
except TypeError as e:
    print(e)
# Some message

try:
    print('Fine')
except KeyError:
    print('Nope')
else:
    print('Else clause')
# Fine
# Else clause

try:
    print(1 / 0)
except ZeroDivisionError:
    print('0!')
finally:  # finally всегда работает!
    print('I will be called in the end!')
# 0!
# I will be called in the end!

try:
    print('try')
except ValueError:
    pass  # Игнорирует ошибку!
    print('else')
finally:
    print('finally')


