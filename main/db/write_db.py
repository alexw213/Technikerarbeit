import sqlite3
from datetime import datetime


def write_protocol(id, art):
    # Verbindungsaufbau Datenbank
    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    # Protokoll schreiben
    currentDateTime = datetime.now()  # Klassenmethode importiert
    query = "INSERT INTO protocol VALUES (?, ?, ?)"

    if art == "kommen":
        cursor.execute(query, (id, currentDateTime, "Kommen"))
    elif art == "gehen":
        cursor.execute(query, (id, currentDateTime, "Gehen"))

    connection.commit()
    connection.close()


def write_user(e1s, e2s, e3s, e4s, e5s, e6s, e7s, e8s):
    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    query = """INSERT INTO user(vorname, nachname, geburtsdatum, familienstand, adresse, telefonnummer, email,
     rfidtag)  VALUES (?, ?, ?, ?, ?, ?, ? ,?)"""
    cursor.execute(query, (str(e1s), str(e2s), str(e3s), str(e4s), str(e5s), str(e6s), str(e7s), str(e8s)))
    connection.commit()

    connection.close()

