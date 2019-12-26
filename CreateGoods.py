import sqlite3
 
# Создание/открытие базы данных irina.db
conn = sqlite3.connect("irina.db")
cursor = conn.cursor()
 
# Создание таблицы Goods
cursor.execute('create table if not exists goods(id integer primary key, category integer, name varchar(100), filename varchar(100), price integer)')

# Вставляем данные в таблицу
# cursor.execute('insert into goods(category, name, filename, price) values (1, "Apple iPhone 11", "iphone11.jpg", 1000)')
# cursor.execute('insert into goods(category, name, filename, price) values (1, "Samsung Galaxy S8", "galaxy8.jpg", 800)')
# cursor.execute('insert into goods(category, name, filename, price) values (1, "SONY Xperia XA1", "xperia.jpg", 300)')

cursor.execute('insert into goods(category, name, filename, price) values (2, "LG", "lg.jpg", 80)')
cursor.execute('insert into goods(category, name, filename, price) values (2, "PHILIPS", "philips.jpg", 90)')

cursor.execute('insert into goods(category, name, filename, price) values (3, "Panasonic", "panasonic.jpg", 80)')

cursor.execute('insert into goods(category, name, filename, price) values (4, "DEXP", "dexp.jpg", 10)')

conn.commit()
cursor.close()
conn.close()
 
