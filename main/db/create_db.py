import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns

create_table = "CREATE TABLE IF NOT EXISTS user (pid INT AUTO INCREMENT, vorname text, " \
               "nachname text, geburtsdatum date, familienstand text, adresse text, telefonnummer int, " \
               "email text, rfidtag int, PRIMARY KEY (pid))"
cursor.execute(create_table)
connection.commit()

create_table = "CREATE TABLE IF NOT EXISTS protocol (rfidtag INT, datum DATE, zeit TIME, reg_art TEXT)"
cursor.execute(create_table)
connection.commit()

cursor.execute("INSERT INTO user VALUES(1, 'Josef', 'Schefer', 1991-09-26, 'ledig', 'Harthäuserweg 43', 017661972415, 'jossa.s@)web.de', 9328342122)")
connection.commit()

connection.close()


