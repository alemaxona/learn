# Иногда необходимо импортировать не вначале!
# Пример:

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Configuration


app = Flask(__name__)
db = SQLAlchemy(app)


# !!!
from model import *  # Этот импорт должен быть минимум тут! Так как если импортировать раньше,
# то не успеет создаться объкт db, и соответственно классы из модуля - model!
# Также необходимо импотировать все (*). Так как выскакивает ошибка. Видимо, зацикливание...


@app.route('/')
def index():
    return 'Hello world!'


if __name__ == "__main__":
    db.create_all()
