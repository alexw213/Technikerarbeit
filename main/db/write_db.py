import sqlite3
from datetime import datetime

def write_protocol(id, art):
    # Verbindungsaufbau Datenbank
    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    # Protokoll schreiben
    datet = datetime.now()  # Klassenmethode importiert
    sec = str(datet.second)[:2]
    strdate = str(datet.year) + "-" + str(datet.month) + "-" + str(datet.day)
    strtime = str(datet.hour) + ":" + str(datet.minute) + ":" + str(sec)

    if art == "kommen":
        query = "INSERT INTO protocol VALUES (" + str(id) + "," + str(strdate) + "," + str(strtime) + ",Kommen)"
    elif art == "gehen":
        query = "INSERT INTO protocol VALUES (" + str(id) + "," + str(strdate) + "," + str(strtime) + ",Gehen)"

    cursor.execute(query)
    connection.commit()
    connection.close()