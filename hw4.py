# 1
#  Basket, package, pack and objects.


class Basket(object):
    limit_basket = 5

    def __init__(self):
        self.list_basket = []
        self.list_package = []
        self.list_pack = []

    def show(self):
        print('\nBasket:', self.list_basket)
        print('Package:', self.list_package)
        print('Pack:', self.list_pack, '\n')

    def add_basket(self, value):
        self.value = value
        if len(self.list_basket) < Basket.limit_basket:
            self.list_basket.append(self.value)
            print('You added one', self.value, 'in basket. Your basket have: ', self.list_basket)
        else:
            print('Basket is busy. Item -', self.value, 'not added! Basket have 5 items: ', self.list_basket)


class Package(Basket):
    limit_package = 4

    def add_package(self, value):
        self.value = value
        if len(self.list_package) < Package.limit_package:
            self.list_package.append(self.value)
            print('You added one', self.value, 'in package. Package have: ', self.list_package)
        else:
            print('Package is busy. Item -', self.value, 'not added! Your package have 4 items: ', self.list_package)


class Pack(Package):
    limit_pack = 2

    def add_pack(self, value):
        self.value = value
        if len(self.list_pack) < Pack.limit_pack:
            self.list_pack.append(self.value)
            print('Pack have -', self.list_pack)
        elif len(self.list_pack) == 2:
            print('Pack is busy. Item -', self.value, 'not added! Pack have 2 items -', self.list_pack)


max_bag = Pack()
max_bag.add_pack('Mac')
max_bag.add_pack('iPhone 8')
max_bag.add_pack('Apple TV')
max_bag.add_basket('AirPods')
max_bag.add_basket('AirPods red')
max_bag.add_package('PostgreSQL')
max_bag.show()

kate_bag = Pack()
kate_bag.add_pack('Oracle Database 11G')
kate_bag.add_pack('MacBook Pro')
kate_bag.add_pack('iPhone XX')
kate_bag.add_package('Mac OS 10')
kate_bag.show()

nikita_bag = Package()
nikita_bag.add_package('MySQL')
nikita_bag.show()

print('\n', dir(max_bag))


# 2
# Figure. Bad work.


class Figure(object):
    def __init__(self, value):
        self.value = value

    def search_perimeter(self):
        index = 0
        self.p = 0
        while index < len(self.value):
            self.p += self.value[index]
            index += 1
        return self.p


class Triangle(Figure):
    def search_s(self):
        self.s_tri = self.value[0] + self.value[1] + self.value[2]
        print('S(Triangle) =', self.s_tri)
        print('P(Triangle)', self.search_perimeter())
        return self.s_tri


class Rectangle(Triangle):
    def search_s(self):
        self.s_rec = (self.value[0] + self.value[1]) * 2
        print('S(Rectangle) =', self.s_rec)
        print('P(Rectangle)', self.search_perimeter())


class Square(Rectangle):
    def search_s(self):
        self.s_squ = self.value[0] ** 2
        print('S(Square) =', self.s_squ)
        print('P(Square)', self.search_perimeter())


class Polygon(Rectangle):
    def search_s(self):
        self.s_pol = Triangle.search_s(self) * self.value[3]
        print('S(Polygon) =', self.s_pol)
        print('P(Polygon)', self.search_perimeter())


def check_user_value(value):
    value = value.split(' ')
    user_list = []
    index = 0
    while index < len(value):
        if value[index] == ' ':
            continue
        else:
            try:
                value[index] = int(value[index])
                user_list.append(value[index])
                index += 1
            except ValueError:
                print('Error: Please enter only numbers!')
                break
    return user_list


print('\nBuild figure\n')
user_value = input('Enter one or four numbers: ')
a = check_user_value(user_value)
if len(a) == 1:
    result = Square(a)
    result.search_s()
elif len(a) == 2:
    result = Rectangle(a)
    result.search_s()
elif len(a) == 3:
    result = Triangle(a)
    result.search_s()
elif len(a) == 4:
    result = Polygon(a)
    result.search_s()
else:
    print('You entered more numbers than 4.')


# ЗАДАЧА 1
#
# Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов: know(person),
#    который позволяет добавить другого человека в список знакомых.
# И метод is_known(person), который возвращает знакомы ли два человека


class Person(object):
    __friends = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age, 'years old.')

    def know(self, person):
        self.person = person
        Person.__friends.append(self.person.name)
        print(self.name, 'added', self.person.name, 'to friends.')

    def is_know(self, name_one):
        self.name_one = name_one
        if self.name in Person.__friends:
            print('Yes', self.name_one, 'your friend.')
        else:
            print('No', self.name_one, 'not', self.name, 'friend.')

    def is_know_they(self, name, name_two):
        self.name = name
        self.name_two = name_two
        if self.name in Person.__friends:
            if self.name_two in Person.__friends:
                print('Yes', self.name, 'and', self.name_two, 'is friends.')
            else:
                print('No', self.name, 'and', self.name_two, 'isn\'t friends.')
        else:
            print('No', self.name, 'and', self.name_two, 'isn\'t friends.')


max = Person('Max', 30)
max.show()

kate = Person('Kate', 29)
kate.show()

nikita = Person('Nikita', 25)
nikita.show()

elena = Person('Elena', 21)
elena.show()

elena.know(nikita)
kate.know(nikita)
nikita.know(kate)

max.know(kate)
max.is_know('Ivan')
max.is_know_they('Kate', 'Nikita')
max.is_know_they('Elena', 'Kate')

# ЗАДАЧА 2
#
# Есть класс, который выводит информацию в консоль: Printer,
# у него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *

# ЗАДАЧА 3
#
# Написать класс Animal и Human,
# сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)

# Слегка дополнил задачу:
# Человек наследуется от животного.
# И у животных и у людей добавлен параметр агрессии.
# У животного и у человека есть метод Атаковать человека.
# Если параметр агрессии у нападающего и жертвы совпадает считается,
# что жертва отбилась и не считает нападавшего опасным.
# В противном случае жертва добавляет нападающего в перечень опасных для себя существ