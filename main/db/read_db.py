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

    query2 = """Select * from user"""
    cursor.execute(query2)
    result = cursor.fetchall()
    connection.commit()

    for row in result:
        print(row)
        print("\n")

    connection.close()
