import sqlite3
 
# Создание/открытие базы данных irina.db
conn = sqlite3.connect("irina.db")
cursor = conn.cursor()
 
# Создание таблицы Cart
cursor.execute('create table if not exists cart(id integer primary key, good integer, count integer)')

conn.commit()
cursor.close()
conn.close()
 
