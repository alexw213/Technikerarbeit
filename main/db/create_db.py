import sqlite3

connection = sqlite3.connect('data.db')
c = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns

create_table = "CREATE TABLE IF NOT EXISTS user (id INT AUTO_INCREMENT PRIMARY KEY, vorname text, nachname text," \
               " geburtsdatum date, familienstand text, adresse text, telefonnummer int, email text, rfidtag int)"
c.execute(create_table)
connection.commit()
connection.close()


