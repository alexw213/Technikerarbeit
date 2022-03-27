import sqlite3

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

