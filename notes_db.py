# -*- coding: utf-8 -*-

import psycopg2  # Используется для подключения к PostgreSQL


# ORM - object relations mapping -  прослойка между Python и СУБД (mysql, mssql, oracle, postgresql, sqlite(файловая бд)...)
# Модель(класс) в терминалогии ORM - по сути таблица
# Но модель к тому же - еще и python объект
# Свойство модели - столбец таблицы
# Объекты - строки
# SQLAlchemy - самая популярная ORM

# Для Flask
from flask_sqlalchemy import SQLAlchemy
