# -*- coding: utf-8 -*-

# Framework - другое название библиотеки
# Flask Самый простой фрэймворк(micro (значит - очень маленький) framework) для web разработки (Соболев Н.)
# Django - огромный, полноценный фрэймворк.
# Концепции WEB приложения: MVC - Model | View | Controller
# Model - хранит данные, View - отображает данные, Controller - котнотролирует отображение, хранение и т.д.
# (Flask) Routes - Устанваливает соотвествие мужу URL адресои и функцией виду View

# Подвид MVC: MVT - Model | View | Template

# Компоненты Flak:
# Web-server - Werkzeug (веркзоег) (библиотека которая лежит в основе Flask и работает с
# протоколом WSGI - (Web Server Gateway Interface)
# По сути можно использовать его и не сипользовать Flask, но он сложный(к примеру описывать Routes!)

# Протокол WSGI используется для общения Python-программы и сервера (Nginx, Apache) (PEP-3333)
# Используетс всеми web-фреймворками

# Дерево приложения (c virtualenv) (дполняется по мере изучения):
# venv/  # Папка виртуального окружения python
# app/  # Папка приложения
#   /main.py
#   /view.py  # Файлы приложения
#   /app.py
#   template/  # Подпапка для шаблонов приложения
#       /base.html
#       /index.html


from flask import Flask

app = Flask(__name__)  # app(в данном случае) - Controller, __name__ - собственно имя файла(notes_flask в данном случае)


@app.route('/')  # /test - http://127.0.0.1:5000/test
def home():
    return 'hello world!'  # 'Hello world' - В данном случае - это View


@app.route('/test/')  # Обязательно /test/ не /test
def home2():
    return 'hello User!'


@app.route('/hello/<user>')  # С параметром <имя параметра>
def home(user):
    return 'hello user: ' + user


@app.route('/<num1>,<num2>')
def usr_sum(num1, num2):
    rez = int(num1) + int(num2)
    return 'sum: ' + str(rez)


# Model(логины, пароли, отчеты...) тут нет, мы не храним данные, текст - это больше отображение (View)
if __name__ == '__main__':
    app.run()


# Конфигурация Flask
# Настройки завистят от окружения!!!

from flask import Flask

app = Flask(__name__)
# Очень внимательно включать на боевом сервере!
app.config['DEBUG'] = True  # Перезапускает сервер при изминении в файле, а также включает дебагер
# app.debug = True
app.config['SECRET_KEY'] = 'Some key'  # Секретный ключ!
# Секретный ключ необходимо прятать от чужих глаз! Пример одного из способов:
# В терминале:
# key = 'My best key' python notes_flask.py  # Создание переменной на момент запсука python
# В сценарии:
# import os
# app.config['SECRET_KEY'] = os.environ['key']  # os.environ - Переменные окружения

# или
# import os
# a = os.urandom(24)  # Генерит что-то типа: b'x\xc7{YV-l\x84\xfa@h\xfc\xf7\x81\xad\xf97z\xf8I\xa7\xa3+\xfc'


# Другая запись конфигурации:
app.config.update(
     DEBUG=True,
     SECRTE_KEY='Some key'  # *kwargs
)


# Запись конфигурации через объект:
# Файл - config.py:
class Configur(object):
    DEBUG = True


# Файл - app.py
from flask import Flask
from config import Configur

app = Flask(__name__)
app.config.from_object(Configur)  # from_object Другие доступные методы, например from_pyfile, можно посмотреть -  dir(app.config)
