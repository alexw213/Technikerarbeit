import sqlite3

#%% ---Methode zum Namen auslesen---
def get_name(id): # Parameter id wird in die Methode eingefügt
    # Verbindungsaufbau Datenbank
    connection = sqlite3.connect('db/data.db')

    # User-Tabelle nach ID auslesen
    cursor = connection.cursor()
    query = "SELECT vorname, nachname FROM user WHERE rfidtag = " + str(id) # Vorname & Nachname wird aus User-Tabelle anhand des RFID-Tags ausgelesen
    cursor.execute(query) # quere wird ausgeführt

    result = cursor.fetchall() #Überträgt alle Tabellen-Einträge in die Tabellenvariable "result"

    vorname = ""
    nachname = ""
    for row in result:
        vorname = row[0]
        nachname = row[1]

    name = str(vorname) + " " + str(nachname)

    connection.close() # SQL-Verbindung wird geschlossen

    return name # Name wird zurückgegeben

#%% ---Methode zum Protokoll auslesen---
def get_protocol():
    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    # Tabelle "protocol" und "user" werden mit JOIN zusammengeführt
    query = "SELECT user.vorname, user.nachname, protocol.zeitpunkt, protocol.reg_art" \ 
            " FROM user JOIN protocol ON user.rfidtag = protocol.rfidtag" 
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    connection.close()

    return result # Ausgelesene Tabelleninhalt wird zurückgegeben

