from tkinter import *
from rfid.read import read_rfid_tag
from rfid.write import write_rfid_tag
import sqlite3
from db.user import User 

#%% gui
root = Tk() # Fenster erstellen
root.wm_title("Time-Control") # Fenster Titel
root.config(background = "#3399ff") # Hintergrundfarbe des Fensters


# Hier kommen die Elemente hin
rightFrame = Frame(root, width=2000, height = 3000)
rightFrame.grid(row=0, column=1, padx=10, pady=3)
 
E1 = Entry(rightFrame, width=50)
E1.grid(row=0, column=0, padx=10, pady=3)
 
def callback_registrieren():
    user_info = write_rfid_tag(E1.get())
    print("Registrierter Nutzer:" + user_info[1])
    # try:
    #     if User.find_by_username(user_info[1]):
    #         print("Der Mitarbeiter wurde bereits registriert")
    # except:
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "INSERT INTO {'users'} VALUES (?, ?)"
    #     #cursor.execute(query, (user_info[0], user_info[1]))
    #     cursor.execute(query, (33, "Raum"))

    #     connection.commit()
    #     connection.close()    

def callback_auslesen():
    user_info = read_rfid_tag()
    print(user_info)
    # print("Registrierter Nutzer:" + user_info[1])
    #if User.find_by_id(user_info[0]):
    #    print("Der Mitarbeiter ist registriert")
    #print("Wer sind Sie?")
 
buttonFrame = Frame(rightFrame)
buttonFrame.grid(row=1, column=0, padx=10, pady=3)
    
B1 = Button(buttonFrame, text="Registrieren", bg="#FF0000", width=15, command=callback_registrieren)
B1.grid(row=0, column=0, padx=10, pady=3)
 
B2 = Button(buttonFrame, text="Chip auslesen", bg="#FFFF00", width=15, command=callback_auslesen)
B2.grid(row=0, column=1, padx=10, pady=3)


root.mainloop() # GUI wird upgedatet. Danach keine Elemente setzen