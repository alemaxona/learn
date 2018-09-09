# Basket, package and objects.


class Basket(object):
    limit_basket = 5
    limit_package = 4
    limit_arms = 2

    def __init__(self):
        self.list_basket = []
        self.list_package = []
        self.list_arms = []

    def add_basket(self, value):
        self.value = value
        if len(self.list_basket) < self.limit_basket:
            self.list_basket.append(self.value)
            print('You added one', self.value, 'in basket. Your basket have: ', self.list_basket)
        else:
            print('Basket is busy. Item -', self.value, 'not added! Basket have 5 items: ', self.list_basket)

    def show(self):
        print('Basket:', self.list_basket)
        print('Package:', self.list_package)
        print('Arms:', self.list_arms)



class Package(Basket):
    def add_package(self, value):
        self.value = value
        if len(self.list_package) < self.limit_package:
            self.list_package.append(self.value)
            print('You added one', self.value, 'in package. Package have: ', self.list_package)
        else:
            print('Package is busy. Item -', self.value, 'not added! Your package have 4 items: ', self.list_package)


class Arms(Package):
    def add_arms(self, value):
        self.value = value
        if len(self.list_arms) < self.limit_arms:
            self.list_arms.append(self.value)
            print('Arms have -', self.list_arms)
        elif len(self.list_arms) == 2:
            print('Arms is busy. Item -', self.value, 'not added! Arms have 2 items -', self.list_arms)


max_bag = Arms()
max_bag.add_arms('Mac')
max_bag.add_arms('iPhone 8')
max_bag.add_arms('Apple TV')
max_bag.add_basket('AirPods')
max_bag.add_basket('AirPods red')
max_bag.add_package('Windows 7')
max_bag.show()

kate_bag = Arms()
kate_bag.add_arms('iPhone 7')
kate_bag.add_arms('MacBook Pro')
kate_bag.add_arms('iPhone 5')
kate_bag.add_package('Mac OS 10')
kate_bag.show()

nikita_bag = Package()
nikita_bag.add_package('Windows 10')
nikita_bag.show()