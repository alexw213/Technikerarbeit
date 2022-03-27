import sqlite3
from datetime import datetime

def write_protocol(id, art):
    # Verbindungsaufbau Datenbank
    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    # Protokoll schreiben
    currentDateTime = datetime.now()  # Klassenmethode importiert

    if art == "kommen":
        query = "INSERT INTO protocol VALUES (" + str(id) + "," + currentDateTime + ",Kommen)"
    elif art == "gehen":
        query = "INSERT INTO protocol VALUES (" + str(id) + "," + currentDateTime + ",Gehen)"

    cursor.execute(query)
    connection.commit()
    connection.close()