import sqlite3

connection = sqlite3.connect('data.db') # Verbindung zur Datenbank "data.db" wird aufgebaut
cursor = connection.cursor() # Objekt zur SQL Navigation wird erstellt

# User Tabelle wird erstellt
query = "CREATE TABLE IF NOT EXISTS user (pid INT AUTO INCREMENT, vorname text, " \
               "nachname text, geburtsdatum date, familienstand text, adresse text, telefonnummer int, " \
               "email text, rfidtag int, PRIMARY KEY (pid))"
cursor.execute(query) # Exexute-Methode wird aufgerufen und SQL Befehl "create_table" wird ausgeführt
connection.commit() # Vorherige Ausführungen werden bestätigt (nochmal googeln!!!)

# Protokolltabelle wird erstellt
query = "CREATE TABLE IF NOT EXISTS protocol (rfidtag INT, zeitpunkt TIMESTAMP, reg_art TEXT)"
cursor.execute(query)
connection.commit()

connection.close()


