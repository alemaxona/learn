# 1
#  Basket, package, pack and objects.


class Basket(object):
    limit_basket = 5

    def __init__(self):
        print('Constructor called.')
        self.list_basket = []
        self.list_package = []
        self.list_pack = []

    def show(self):
        print('\nBasket:', self.list_basket)
        print('Package:', self.list_package)
        print('Pack:', self.list_pack, '\n')

    def add_basket(self, value):
        self.value = value
        if len(self.list_basket) < self.limit_basket:
            self.list_basket.append(self.value)
            print('You added one', self.value, 'in basket. Your basket have: ', self.list_basket)
        else:
            print('Basket is busy. Item -', self.value, 'not added! Basket have 5 items: ', self.list_basket)


class Package(Basket):
    limit_package = 4

    def add_package(self, value):
        self.value = value
        if len(self.list_package) < self.limit_package:
            self.list_package.append(self.value)
            print('You added one', self.value, 'in package. Package have: ', self.list_package)
        else:
            print('Package is busy. Item -', self.value, 'not added! Your package have 4 items: ', self.list_package)


class Pack(Package):
    limit_pack = 2

    def add_pack(self, value):
        self.value = value
        if len(self.list_pack) < self.limit_pack:
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
# Figure


class Figure(object):
    def __init__(self, value):
        self.value = value
        print(self.value)

    def square(self, value):
        self.value = value
        for i in self.value:
            self.square = int(i) ** 2
        print('Square =', self.square)
        return self.square

    def triangle(self, value):
        self.value = value


    def check_numbers(self, value):
        self.value = value
        if len(self.value) == 1:
            self.result = self.square(self.value)
        elif len(self.value) == 2:
            self.result = self.triangle(self.value)


print('\nBuild figure\n')
user_value = input('Enter numbers: ')
user_list = user_value.split(' ')

result = Figure(user_list)
result.check_numbers(user_value)