#1 ?
def func_try(a, b):
    try:
        c = a / b
        c = c / 0
    except RuntimeError as q:
        print('Error Runtime: ',q)
    except TypeError as w:
        print('Error Type: ',w)
    except ValueError as e:
        print('Error Value',e)
    except ZeroDivisionError as r:
        print('Error Zero:', r)
    else:
        print('Error :)')

a = func_try(1, 2)
print('\n')

#2
def func_list(values=[]):
    try:
        values.sort()
        print(values)
    except TypeError as a:
        print('Value error: ', a)

func_list([5, 2.3, 4, 1, 2])
func_list([5, 2.3, 4, 1, 2, 't'])
print('\n')

#3
def func_dict(**userdict):
    new_dict = {}
    for key, value in userdict.items():
        key = str(key)
        new_dict[key] = value
    print(new_dict)

func_dict(a='max',b=3, c='2',d=12)
print('\n')

#4
def sum_all(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

a = sum_all(1, 2 ,5, 10)
print(a)
print('\n')

#HW1
#Можно также решить путем сортировки, выбрав потом по индексу макс. и мин.!
def max_min(*user_values):
    a = max(user_values)
    b = min(user_values)
    print('Max: {}, Min: {}'.format(a,b),'\n')

max_min(1, 5, 2.3, 7, 9, 100, 0.5, -3, 33, 0.01)

#HW2
def str_flag(str, flag=True):
    if flag == True:
        print('\n', str.upper())
    else:
        print('\n', str.lower())

str_flag('Maxim and Katya')
str_flag('Maxim and Katya', False)
print('\n')

#HW3
def str_concat(*string, glue=':'):
    out = ''
    for str in string:
        if len(str) > 3:
            out += (str + glue)
    print(out[:-1])

str_concat('Max', 'Maxim', 'Katya', 'Ivan', 'Sanya', 'Bob')