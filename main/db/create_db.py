import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns

create_table = "CREATE TABLE IF NOT EXISTS user (pid INT AUTO INCREMENT, vorname text, " \
               "nachname text, geburtsdatum date, familienstand text, adresse text, telefonnummer int, " \
               "email text, rfidtag int, PRIMARY KEY (pid))"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS protocol (rfidtag INT, datum DATE, zeit TIME, reg_art TEXT)"
cursor.execute(create_table)

connection.commit()
connection.close()


