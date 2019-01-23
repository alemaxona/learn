# Язык шаблонов - jinja2
from jinja2 import Template


# {{ }} - Используется для вывода/ выражений
# {% %} - Содержит блоки кодов, таких как for, if
# Отступы(4 spases) внутри блока не обязательны
# {# ... #} - комментарии

# Примеры
def simple():
    t = Template('Hello {{ some }}!')
    result = t.render(some='World')
    print(result)

simple()
# Hello World!


# for
def simple2(iter=None):
    if iter == None:
        iter = range(1, 11)
        t = Template("""
        My numbers: 
        {% for i in array %}
        {{ i }}
        {% endfor %}""")
        result = t.render(array=iter)
        print(result)

simple2()
# 1
# 2
# 3

# Очень важно!
# Если записать шаблон в строку и без пробелов!
def simple2_1(iter=None):
    if iter == None:
        iter = range(1, 11)
        t = Template("""My numbers: {% for i in array %}{{ i }}{% endfor %}""")
        result = t.render(array=iter)
        print(result)

simple2_1()
# My numbers: 12345678910


# if
def simple3(value):
    t = Template("""
    {% if value %}
    True!
    {% else %}
    False!
    {% endif %}
    """)
    result = t.render(value=value)
    print(result)

simple3(1)
# True!

simple3('')
# False!
