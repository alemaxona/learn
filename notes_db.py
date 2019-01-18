# -*- coding: utf-8 -*-


# ORM - object relations mapping -  прослойка между Python и СУБД (mysql, mssql, oracle, postgresql, sqlite(файловая бд)...)
# Модель(класс) в терминалогии ORM - по сути таблица
# Но модель к тому же - еще и python объект
# Свойство модели - столбец таблицы
# Объекты - строки
# SQLAlchemy - самая популярная ORM


import psycopg2  # Используется для подключения к PostgreSQL
import pyodbc, import pymssql, import pypyodbc  # Используются для подключения к Microsoft SQL Server
from flask_sqlalchemy import SQLAlchemy # Для Flask


# Examples
# mssql
import pypyodbc


connection = pypyodbc.Connection('Driver={SQL Server}; Server=msk1-tsql2sa21\sql2017; UID=login; pwd=pass;')
try:
    cursor = connection.cursor()
except Exception as a:
    print('ERROR: ', a)

query = ("""SELECT TOP (1000) [login], [pass] FROM [dba].[dbo].[loginpass];""")

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    login = row[0]
    pwd = row[1]
    print(login, ' | ', pwd)

connection.close()
