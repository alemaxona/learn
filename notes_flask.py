# -*- coding: utf-8 -*-

# Framework - другое название библиотеки
# Flask Самый простой фрэймворк(micro (значит - очень маленький) framework) для web разработки (Соболев Н.)
# Django - огромный, полноценный фрэймворк.


__author__ = 'alemaxona'

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world!'


if __name__ == '__main__':
    app.run()
