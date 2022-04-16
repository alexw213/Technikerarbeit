import sqlite3
from datetime import datetime

#%% ---Methode zum Schreiben des Protokolls---
def write_protocol(id, art):
    # Verbindungsaufbau Datenbank
    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    # Protokoll schreiben
    currentDateTime = datetime.now()  # Aktueller Zeitpunkt wird ausgelesen
    query = "INSERT INTO protocol VALUES (?, ?, ?)" # RFID-Tag, Zeitpunkt und Registrierungsart werden in "protocol" eingefügt

    #SQL-Befehl "Kommen" oder "Gehen" wird ausgeführt
    if art == "kommen":
        cursor.execute(query, (id, currentDateTime, "Kommen")) # query wird ausgeführt und die ? werden mit 3 Variablen befüllt
    elif art == "gehen":
        cursor.execute(query, (id, currentDateTime, "Gehen"))

    connection.commit()
    connection.close()

#%% ---Methode zum Speichern des Users in der Datenbank---
def write_user(e1s, e2s, e3s, e4s, e5s, e6s, e7s, e8s, e9s):
    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    query = """INSERT INTO user(vorname, nachname, geburtsdatum, familienstand, adresse, telefonnummer, email, rfidtag, pid)  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(query, (str(e1s), str(e2s), str(e3s), str(e4s), str(e5s), str(e6s), str(e7s), str(e8s), str(e9s))) # query wird ausgeführt und ? werden mit 9 Variablen befüllt
    connection.commit()

    connection.close()

