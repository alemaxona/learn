#  Почитать - class type() ???


# Создание списка из объектов!
class MyClass(object):
    def __init__(self, name):
        self.name = name

    def sum(self):
        print(1 + 2)


x = [MyClass('Max') for i in range(0, 3)]

print(x)
print(x[0].name)
x[1].sum()


# Если модуль импортирован с условим ниже, то в функция в условии не выполнится сразу, только по вызову!
# Если этого условия нет, - функция выполнится сразу при импорте!
if __name__ == '__main__':  # Она либо равна  __main__, либо имени того файла, из которого делали импорт!
    pass  # function()


# Перегрузить(оператор) - Переопределить, например переменную.


# Магические операторы:
# Нельзя создать свой магический метод, они все определены заранее.
# Самое частое - это сравнение.
class MathMethod(object):
    def __init__(self):
        self.value = 2

    def __add__(self, other):
        return self.value + other


t = MathMethod()
print(t + 4)
print(t.__add__(4))
# 6
# 6


# Магические - Математические и логические методы.
class MathObject(object):
    def __init__(self, value):
        self.value = value

    # Comparing:
    def __eq__(self, other):
        return self.value == other

    def __ge__(self, other):
        return self.value >= other

    def __gt__(self, other):
        return self.value > other

    def __lt__(self, other):
        return self.value < other

    # Operations:
    def __neg__(self):
        return -self.value

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        return self.value * other


if __name__ == '__main__':
    m = MathObject(10.) # Это float, то есть 10.0.
    # m = MathMethod(.0) - 0.0 тоже float
    print(m > 10)
    print(m >= 10)
    print(m == 10)

    print(-m)
    print(m + 2 == 2 + m)

    m += 3
    print(m)
    print(m * 2)


# Магические методы со словарями
class DictFunctionality(object):
    def __init__(self, values=None):
        if values is None:  # is - типа ==
                self.values = {}
        elif isinstance(values, dict):
                self.values = values
        else:
            raise ValueError()

    # Converting to string:
    def __str__(self):
        return str(self.values) if self.values else ''

    # Items management:
    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]


t = DictFunctionality()
print(t)  # Сразу пойдет в метод __str__, не в начало класса!


l = DictFunctionality({'1key': 'some_value'})
l[1] = 'item1'


# `in` operation:
def __contains__(self, item):
    return item in self.values


l = DictFunctionality()

print(2 in t)
# True or False


def __len__(self):
    return len(self.values)  # self.values.__len__()


print(len(l))

#
if __name__ == '__main__':
    l = DictFunctionality({'1key': 'some_value'})  # Вызов: __init__
    l[1] = 'item1'  # Вызов: __setitem__
    print(str(l), l[1])  # Вызов: __str__ and __getitem__

    for item in l:
        print(item, l[item])

    print('s' in l, 1 in l)  # Вызов: __contains__
    print(len(l))  # Вызов: __len__


# Статические атрибуты и методы
class MathObject(object):
    value = 2  # Статический атрибут, атрибюут класса, общий для объектов класса!

    def __init__(self, i):
        self.value = i

    @staticmethod  # Статический метод
    def count():  # self уже не нужен
        return 'some'

t = MathObject(10)
print(t.value, t.__class__.value)  # t.value - значение обекта, t.__class__.value( == MathObject.value) - значение класса.
# 10 2
print(MathObject.count())
# some
print(t.count())  # ==
# some


class MathObject2(object):
    value = 2  # Статический атрибут!

    def __init__(self, i):
        self.value = i

    @classmethod  # Метод класса, не объекта!
    def count(cls):  # cls (class, как self у методов объекта) - то есть принадлежит классу, а не объкуто созданного из данного класса!
        return cls.value


t = MathObject2(10)
print(t.value, t.count())
t.__class__.value = 3  # Изменение статического атрибута.


#
class MathObject3(object):
    count = 0  # Статический атрибут!

    def __init__(self):
        self.__class__.count += 1


m1 = MathObject3()
print(m1.count)
# 1
m2 = MathObject3()
print(m2.count)
# 2
print(MathObject3.count)
# 2


# ! super() - Переиспользование методов родительского класса.
class Calc(object):
    def __init__(self, value):
        print('Calc constructor is called')
        self.value = value

    def count(self):
        return self.value * 8 + 9


class DoubleCalc(Calc):
    def count(self):
        return 2 * super().count()


class ExtendedCalc(DoubleCalc):
    def __init__(self, value, k=1):
        super().__init__(value)  # Сначала идет в DoubleCalc, если там нет -  в Calc!
        print('Extender', self.value)

        self.k = k

    def count(self):
        previous = super().count()  # Сначала идет в DoubleCalc, потом в Calc!

        return -1 * self.k * previous


e = ExtendedCalc(8, k=1.2)
print(e.count())
print(ExtendedCalc.__mro__)  # Структура наследования! Как метод super() определяет в какой класс идти- __mro__!
# (<class '__main__.ExtendedCalc'>, <class '__main__.DoubleCalc'>, <class '__main__.Calc'>, <class 'object'>


class Animal(object):
    def __init__(self, aggression, name):
        self.name = name
        self.aggression = aggression
        self.victim = []

    def is_dangerous(self, obj):  # Передача объекта как аргумент!
        if obj.name in self.victim:
            print('Yes.', obj.name, 'is dangerous for', self.name)
        else:
            print('No.', obj.name, 'don\'t dangerous for', self.name)

    # ...


class Human(Animal):

    def out(self):
        print('Human')

    # ...


snake = Animal(4, 'snake')
maxim = Human(1, 'Max')
snake.is_dangerous(maxim)


# !!!
class Test(object):
    a = 2

    def main(self, value):
        self.value = value
        print(self.a + self.value)


b = Test()
b.main(2)

Test.a = 12  # Поменяет значение в классе!
b.a = 12  # Поменяет значение в объекте, в инстансе!

# Можно решить ЛЮБУЮ задачу только с помощью функций!
# Никита Соболев: Если вы видите global, то нужно использовать класс!
# Class

# int(integer, тип данных) - Это класс, а 1 2 3 - его обекты(еще можно назвать экземпляры)
# В терминологии Python члены класса называются атрибутами,
# функции класса — методами, а поля класса — свойствами (или просто атрибутами).
# Определения методов аналогичны определениям функций,
# но (за некоторыми исключениями, о которых ниже) методы всегда имеют первый аргумент,
#  называемый по общепринятому соглашению self.


class Student(object):  # Класс, можно не писть - (object). Имя класса всегда с большой буквы!
    school = 286 # Атрибут (или поле класса). Все созданные объекты по этому кклассу будут иметь этот атрибут.
    learn = 'Python' # Второй атрибут. Все созданные объекты по этому кклассу будут иметь этот атрибут.

    def info(self, name, age):  # Метод. self - ОБЯЗАТЕЛЬНЫЙ аргумент метода.
        # И 2 не обязательных аргумента.Все созданные объекты по этому кклассу будут иметь этот метод.
        self.name = name  # 1-ый атрибут метода
        self.age = age
        print(self.name, self.age)


c = Student()  # Создание объекта класса Student
print(c.school, c.learn)
# 286 Python
c.name = 'Max'
c.age = 30
print('Student {} learn in {}'.format(c.name, c.school))
# Student Max learn in 286

print(c.info('Kate', 29))
# Kate 29
# None


# Класс конструтор. Отвечает за инициализацию переменных!
# Конструктором класса называют метод, который автоматически вызывается при создании объектов.
# Его также можно назвать конструктором объектов класса.
# Имя такого метода обычно регламентируется синтаксисом конкретного языка программирования.
# В Python роль конструктора играет метод __init__().
class Person:
    def __init__(self, n, s):  # Если аргементам не присовены знаечения(self, n = 3, s = 5), их необходимо будет указывать при создании объекта класса!
        self.name = n
        self.surname = s


p1 = Person("Max", "M")  # Если не указать аргументы, - будет ошибка!
print(p1.name, p1.surname)
# Max M


class Car:
    engine = 'v8'
# Здесь пустая строка, так принято!

    def __init__(self, color):
        self.color = color


t = Car('green')
print(t.color, t.engine)
t1 = Car('red')
print(t1.color)


# class Door(object):
class Door:
    def open(self):  # note that `self` is the object itself!
        print('self is', self)
        print('Door is opened!')
        self.opened = True


d = Door()
d.open()

d1 = Door()
d1.open()  # == Door.open(d1)


# Если у класса потомка есть свой конструктор,
# то объект потомка возьмет конструктор потомка,
# но методы и атрибуты класса родителя также возьмет!
class Parent(object):
    def __init__(self):
        print('Parent inited')
        self.value = 'Parent'

    def do(self):
        print('Parent do(): {}'.format(self.value))


class Child(Parent):
    def __init__(self):
        print('Child inited')
        self.value = 'Child'


parent = Parent()
parent.do()
child = Child()
child.do()


# ООП
# Наследование. (Переиспользование кода):
class Calc(object):
    def __init__(self, number):
        self.number = number

    def calc_and_print(self):
        value = self.calc_value()
        self.print_number(value)

    def calc_value(self):
        return self.number * 10 + 2

    def print_number(self, value_to_print):
        print('-----')
        print('Number is', value_to_print)
        print('-----')


c = Calc(8)
c.calc_and_print()
# -----
# Number is 82
# -----


class CalcExtraValue(Calc):
    def calc_value(self):
        return self.number - 100


t = CalcExtraValue(3)
t.calc_and_print()
# -----
# Number is -97
# -----


# Инкапсуляция. Способность скрывать реализацию методов. Практически не работает в Python!
class Example(object):
    def __init__(self):
        self.a = 1  # Если перед атрибутом нет знаков "_" и "__", то можно свободно использовать данный атрибут.
        self._b = 2  # Если перед атрибутом один знак "_", то это сообщениеразработчикам,
        # что "лучше не использовать данный метод"!
        self.__c = 3  # Если перед атрибутом два знака "__", то атрибут становится недоступным для использования.
        print('{},{},{}'.format(self.a, self._b, self.__c))

    def _max(self):
        pass

    def __max2(self):
        pass

    def call(self):
        print('called')


ex = Example()
print(ex.a)
print(ex._b)
print(ex.__c)  # Выдаст ошибку!


# Полиморфизм - возможность использовать функции по разному в зависимости от входных аргументов!
def sum_two_objects(one, two):
    return one + two


a = sum_two_objects(1,2)
print(a)
b = sum_two_objects('Max', 'Wow')
print(b)


#
class Parent(object):
    def call(self):
        print('Parent')


class Child(Parent):
    def call(self):
        print('Child')


class Example(object):
    def call(self):
        print('Ex')


def call_obj(obj):
    obj.call()


call_obj(Child())
call_obj(Parent())
c = Parent()
c.call()


# Абстрация. Посзоляет упрощать сложные задачи, создавая небольшие классы для решения простых!
# То есть, если необходимо отправить файл по почте и написать уведомление, то предполагается, что можно это сделать,
# например, в три этапа: 1) выбрать файл 2) отправить файл по почте 3) написать уведомление.

GLOBAL_VALUE = 2  # Глобальная переменная может быть только одна. С таким именем естесственно!


def do_work(value):
    return GLOBAL_VALUE * value + 2


def change_var(x):
    global GLOBAL_VALUE
    GLOBAL_VALUE = x


# ==
class Calc:  # А вот объектов класса может быть сколько угодно!
    def __init__(self, param):
        self.param = param

    def do_work(self, value):
        return self.param * value + 2

    def change_var(self, x):
        self.param = x