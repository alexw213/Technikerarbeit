from tkinter import *
from rfid.read import read_rfid_tag
from rfid.write import write_rfid_tag
import sqlite3
from db.user import User 

#%% gui
root = Tk() # Fenster erstellen
root.wm_title("Zeiterfassung") # Fenster Titel
root.config(background = "#FFFFFF") # Hintergrundfarbe des Fensters


# Hier kommen die Elemente hin
leftFrame = Frame(root, width=200, height = 400)
leftFrame.grid(row=0, column=0, padx=10, pady=3)
 
leftLabel1 = Label(leftFrame, text="Platzhalter Text")
leftLabel1.grid(row=0, column=0, padx=10, pady=3)
leftLabel2 = Label(leftFrame, text="Dies ist ein Text\nmit mehreren Zeilen.")
leftLabel2.grid(row=1, column=0, padx=10, pady=3)
 
#imageEx = PhotoImage(file = '200x200')
#Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=3)
 
 
rightFrame = Frame(root, width=400, height = 400)
rightFrame.grid(row=0, column=1, padx=10, pady=3)
 
E1 = Entry(rightFrame, width=50)
E1.grid(row=0, column=0, padx=10, pady=3)
 
def callback_registrieren():
    user_info = write_rfid_tag(E1.get())

    try:
        if User.find_by_username(user_info[1]):
            print("Der Mitarbeiter wurde bereits registriert")
    except:
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        TABLE_NAME = 'users'
        query = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(table=self.TABLE_NAME)
        cursor.execute(query, (user_info[0], user_info[1]))

        connection.commit()
        connection.close()    

def callback_auslesen():
    user_info = read_rfid_tag()
    if User.find_by_id(user_info[0]):
        print("Der Mitarbeiter ist registriert")
    print("Wer sind Sie?")
 
buttonFrame = Frame(rightFrame)
buttonFrame.grid(row=1, column=0, padx=10, pady=3)
    
B1 = Button(buttonFrame, text="Registrieren", bg="#FF0000", width=15, command=callback_registrieren)
B1.grid(row=0, column=0, padx=10, pady=3)
 
B2 = Button(buttonFrame, text="Chip auslesen", bg="#FFFF00", width=15, command=callback_auslesen)
B2.grid(row=0, column=1, padx=10, pady=3)
 
Slider = Scale(rightFrame, from_=0, to=100, resolution=0.1, orient=HORIZONTAL, length=400)
Slider.grid(row=2, column=0, padx=10, pady=3)
 
 
root.mainloop() # GUI wird upgedatet. Danach keine Elemente setzen