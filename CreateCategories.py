import sqlite3
 
# Создание базы данных irina.db
conn = sqlite3.connect("irina.db")
cursor = conn.cursor()
 
# Создание таблицы Categories
cursor.execute('create table if not exists categories(id integer primary key, name varchar(50))')

# Вставляем данные в таблицу
cursor.execute('insert into categories(name) values ("Смартфоны")')
cursor.execute('insert into categories(name) values ("Кнопочные телефоны")')
cursor.execute('insert into categories(name) values ("Радиотелефоны")')
cursor.execute('insert into categories(name) values ("Стационарные телефоны")')

conn.commit()
cursor.close()
conn.close()
 
