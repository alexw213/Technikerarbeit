import sqlite3
""""
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("INSERT INTO protocol VALUES(803589853443, '2022-03-31 08:30:00', 'Kommen')")
cursor.execute("INSERT INTO protocol VALUES(803589853443, '2022-03-31 16:30:00', 'Gehen')")
connection.commit()

cursor.execute("select * from protocol")
result = cursor.fetchall()
print(result)
connection.close()
""""