import tkinter
import tkinter as tk  # tkinter abkürzen mit tk
import sqlite3
from tkinter import *  # Importierung der ttk-Widgets
from tkinter import messagebox
from datetime import datetime
from rfid import read
from db import write_db
from db import read_db
#from setuptools._distutils.command.config import config


root = tk.Tk()  # Fenster erstellen
root.wm_title('Time-Control')  # Fenster - Titel
root.config(background='#ffdead')  # Hintergrundfarbe des Fensters
root.geometry('1200x800')  # GUI-Fenstergröße bestimmen


#%% ---GUI---

# Button 1
def chip_in():

    user_info = read.read_rfid_tag()
    id = user_info[0]

    write_db.write_protocol(id, "kommen")

    name = read_db.get_name(id)

    datet = datetime.now()
    strdate = str(datet.day) + "." + str(datet.month) + "." + str(datet.year) + "  " + str(datet.hour) + ":" + str(datet.minute)
    messagebox.showinfo(title=None, message="Einen schönen Arbeitstag " + name + "!" + "\n" + "Zeitpunkt: " + str(strdate) + " Uhr")

kommen = Button(root,
                 text='Kommen',
                 padx=50, pady=50,
                 bg='#00cd00',
                 command=chip_in)
kommen.pack(side='left', padx=20, pady=50)


# Button 2
def chip_out():

    user_info = read.read_rfid_tag()
    id = user_info[0]

    write_db.write_protocol(id, "gehen")

    name = read_db.get_name(id)

    datet = datetime.now() #Klassenmethode importiert
    strdate = str(datet.day) + "." + str(datet.month) + "." + str(datet.year) + "  " + str(datet.hour) + ":" + str(datet.minute)
    messagebox.showinfo(title=None, message="Einen schönen Feierabend " + name + "!" + "\n" + "Zeitpunkt: " + strdate + " Uhr")


gehen = Button(root, text='Gehen',
                 padx=50, pady=50,
                 bg='red',
                 command=chip_out)
gehen.pack(side='right', padx=20, pady=50)

#%% ---Registrierung im neuen Fenster---

# Button 3
def register():
    popup = tk.Toplevel(root)

    Label(popup, text='Vorname').grid(row=0)
    Label(popup, text='Nachname').grid(row=1)
    Label(popup, text='Geburtsdatum').grid(row=2)
    Label(popup, text='Familienstand').grid(row=3)
    Label(popup, text='Adresse').grid(row=4)
    Label(popup, text='Telefonnummer').grid(row=5)
    Label(popup, text='E-Mail').grid(row=6)
    Label(popup, text='RFID-Tag').grid(row=7)

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

    # Registriervorgang
    #def bestätigen():
       # print('Mitarbeiter ist registriert!')

    # %% --- RFID registration ---
    def save():

        e1s = e1.get()
        e2s = e2.get()
        e3s = e3.get()
        e4s = e4.get()
        e5s = e5.get()
        e6s = e6.get()
        e7s = e7.get()
        e8s = e8.get()

        connection = sqlite3.connect('db/data.db')
        cursor = connection.cursor()

        query2 = """Select * from user"""
        cursor.execute(query2)
        result = cursor.fetchall()
        connection.commit()

        for row in result:
            print(row)
            print("\n")

        query = """INSERT INTO user(pid, vorname, nachname, geburtsdatum, familienstand, adresse, telefonnummer, email,
         rfidtag)  VALUES (?, ?, ?, ?, ?, ?, ? ,?)"""
        cursor.execute(query, (str(e1s), str(e2s), str(e3s), str(e4s), str(e5s), str(e6s), str(e7s), str(e8s)))
        connection.commit()

        connection.close()

        messagebox.showinfo(title=None, message="Mitarbeiter erfolgreich registriert!")
        popup.destroy()

    b1 = tk.Button(popup,
                   text='Registrieren',
                   command=save)
    b1.grid(row=8, column=1)


registrieren = Button(root, text='Registrierung',
                 padx=20, pady=20,
                 command=register)
registrieren.pack(side='bottom', fill='x', padx=20, pady=30)

# Button 4
def get_protocol():

    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    query = "SELECT user.vorname user.nachname protocol.zeitpunkt protocol.reg_art" \
            " FROM user JOIN protocol ON user.rfidtag = protocol.rfidtag"
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()

    popup_p = tk.Toplevel(root)
    for row in result:
        Label(popup_p, text=row).grid(row=0)

    connection.close()

protokoll = Button(root, text='Protokoll anzeigen',
                 padx=20, pady=20,
                 command=get_protocol)
protokoll.pack(side='top', fill='x', padx=20, pady=30)


root.mainloop()

