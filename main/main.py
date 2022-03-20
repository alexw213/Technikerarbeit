import tkinter as tk  # tkinter abkürzen mit tk
from tkinter import *  # Importierung der ttk-Widgets
root = tk.Tk()  # Fenster erstellen
root.wm_title('Time-Control')  # Fenster - Titel
root.config(background='#ffdead')  # Hintergrundfarbe des Fensters
root.geometry('1200x800')  # GUI-Fenstergröße bestimmen
"""
from rfid.read import read_rfid_tag
from rfid.write import write_rfid_tag
import sqlite3
from db.user import User
"""

#%% ---GUI---

# Button 1
def say_hello():
    print('Einen schönen Arbeitstag!')

kommen = Button(root,
                 text='Kommen',
                 padx=50, pady=50,
                 bg='#00cd00',
                 command=say_hello)
kommen.pack(side='left', padx=20, pady=50)


# Button 2
def say_bye():
    print('Einen schönen Feierabend!')

gehen = Button(root, text='Gehen',
                 padx=50, pady=50,
                 bg='red',
                 command=say_bye)
gehen.pack(side='right', padx=20, pady=50)

#%% ---Registrierung im neuen Fenster---

def onclick():
    popup = tk.Toplevel(root)

    Label(popup, text="Vorname").grid(row=0)
    Label(popup, text="Nachname").grid(row=1)
    Label(popup, text="Geburtsdatum").grid(row=2)
    Label(popup, text="Familienstand").grid(row=3)
    Label(popup, text="Adresse").grid(row=4)
    Label(popup, text="Telefonnummer").grid(row=5)
    Label(popup, text="E-Mail").grid(row=6)
    Label(popup, text="RFID-Tag").grid(row=7)


    e1 = Entry(popup)
    e2 = Entry(popup)
    e3 = Entry(popup)
    e4 = Entry(popup)
    e5 = Entry(popup)
    e6 = Entry(popup)
    e7 = Entry(popup)
    e8 = Entry(popup)


    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)
    e7.grid(row=6, column=1)
    e8.grid(row=7, column=1)

    # Registriersvorgang

    def bestätigen():
        print('Mitarbeiter ist registriert!')

    b1 = tk.Button(popup,
                text='Bestätigung',
                command=bestätigen)
    b1.grid(row=8, column=1)

registrieren = Button(root, text='Registrierung',
                 padx=20, pady=20,
                 command=onclick)
registrieren.pack(side='bottom', fill='x', padx=20, pady=50)

#%% --- RFID registration ---
def callback_register():
    user_info = write_rfid_tag(E1.get())
    print("Registered User:" + user_info[1])
    # try:
    #     if User.find_by_username(user_info[1]):
    #         print("Employee is already registered")
    # except:
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "INSERT INTO {'users'} VALUES (?, ?)"
    #     #cursor.execute(query, (user_info[0], user_info[1]))
    #     cursor.execute(query, (33, "Raum"))

    #     connection.commit()
    #     connection.close()    

def callback_reading():
    user_info = read_rfid_tag()
    print(user_info)
    # print("Registered User:" + user_info[1])
    #if User.find_by_id(user_info[0]):
    #    print("Employee registered")
    #print("Wer sind Sie?")


root.mainloop()

