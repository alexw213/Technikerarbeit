import sqlite3
from datetime import datetime

def get_name(id):
    # Verbindungsaufbau Datenbank
    connection = sqlite3.connect('db/data.db')

    # User-Tabelle nach ID auslesen
    cursor = connection.cursor()
    query = "select vorname, nachname from user where rfidtag = " + str(id)
    cursor.execute(query)

    result = cursor.fetchall() #lese alle tabellen einträge in die tabellenvariable "result"

    vorname = ""
    nachname = ""
    for row in result:
        vorname = row[0]
        nachname = row[1]

    name = str(vorname) + " " + str(nachname)

    connection.close()

    return name

def get_protocol():
    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    query = "SELECT user.vorname, user.nachname, protocol.zeitpunkt, protocol.reg_art" \
            " FROM user JOIN protocol ON user.rfidtag = protocol.rfidtag"
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    connection.close()

    return result

def test_read():
    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    query = """Select * from user"""
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()

    for row in result:
        print(row)
        print("\n")

    connection.close()

def get_worktime(id):
    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    query = "SELECT protocol.zeitpunkt, protocol.reg_art FROM user JOIN protocol ON user.rfidtag = protocol.rfidtag" \
            " WHERE rfidtag = " + id
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()

    for row in result:
        if result[1] == "Kommen":
            startzeit = result[0]
        if result[1] == "Gehen":
            endzeit = result[0]

    time_1 = datetime.strptime(startzeit, "%H:%M:%S")
    time_2 = datetime.strptime(endzeit, "%H:%M:%S")

    time_interval = time_2 - time_1

    return time_interval
