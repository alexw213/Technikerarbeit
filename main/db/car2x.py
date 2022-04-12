"""
import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="caredb")
cursor = connection.cursor()
# some other statements  with the help of cursor

# SQL-Befehl ausführen
#SQLBefehl = 'SELECT * FROM care_person'
#cursor.execute(SQLBefehl)

#result = cursor.fetchall()

#for row in result:
print("Successful")


connection.close()
"""
