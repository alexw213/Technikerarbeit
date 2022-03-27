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