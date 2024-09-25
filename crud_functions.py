import sqlite3

connection = sqlite3.connect('database_4.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')

for i in range(1, 5):
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   (f'Продукт{i}', f'Описание{i}', i * 100))
def get_all_products(data):
   cursor.execute("SELECT title, description, price FROM Products")
   data = cursor.fetchall()
   return data

connection.commit()
# connection.close()