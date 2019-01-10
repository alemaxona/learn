# -*- coding: utf-8 -*-


# Паттерны проектирования
# Их очень много! Наследование, MVC(model-view-controller), decorator(обертки для функций),
# iterator(итерирование по коллекциям)...
# Идея сводится к постоянному изучению паттернов. В разработке - тщательное проектирование, которое съэкономит время
# написания кода!

# Пример


class Teacher:
    def say(self):
        print('Hello, Teacher')


class Student:
    def answer(self):
        print('Hello, student')


# Эти 2 класса выполняют одно и тоже, следовательно их можно спроектировать по другому:


class Teacher:
    obj = 'Teacher'
    def say(self):
        print('Hello, {}'.format(self.obj))


class Student(Teacher):
    obj = 'Student'


# Теперь мы не повторяемся, но жертвуем гибкостью, до этогго классы были независимы!
