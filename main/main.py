import tkinter
import tkinter as tk  # tkinter abkürzen mit tk
import sqlite3
from tkinter import *  # Importierung der ttk-Widgets
from tkinter import messagebox
from rfid import read
root = tk.Tk()  # Fenster erstellen
root.wm_title('Time-Control')  # Fenster - Titel
root.config(background='#ffdead')  # Hintergrundfarbe des Fensters
root.geometry('1200x800')  # GUI-Fenstergröße bestimmen


#%% ---GUI---

# Button 1
def say_hello():
    print('Einen schönen Arbeitstag!')

    user_info = read.read_rfid_tag()
    id = user_info[0]


    connection = sqlite3.connect('data.db')
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

    messagebox.showinfo(title=None, message="Einen schönen Arbeitstag " + name)

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
    def register():
        #user_info = write_rfid_tag(E1.get())
        # print("Registered User:" + user_info[1])
        # try:
        #     if User.find_by_username(user_info[1]):
        #         print("Employee is already registered")
        # except:

        e1s = e1.get()
        e2s = e2.get()
        e3s = e3.get()
        e4s = e4.get()
        e5s = e5.get()
        e6s = e6.get()
        e7s = e7.get()
        e8s = e8.get()

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        create_table = "CREATE TABLE IF NOT EXISTS user (vorname text, " \
                       "nachname text, geburtsdatum date, familienstand text, adresse text, telefonnummer int, " \
                       "email text, rfidtag int, PRIMARY KEY (rfidtag))"
        cursor.execute(create_table)

        #query = 'INSERT INTO user VALUES (' + str(e1) + ',' + str(e2) + ',' + str(e3) + ',' + str(e4) + ',' +\
         #       str(e5) + ',' + str(e6) + ',' + str(e7) + ',' + str(e8) + ')'
        #query = "INSERT INTO user VALUES (" + str(e1) + "," + str(e2) + "," + str(e3) + "," + str(e4) + "," +\
              #  str(e5) + "," + str(e6) + "," + str(e7) + "," + str(e8) + ")"
        query = """INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ? ,?) """
        cursor.execute(query, (str(e1s), str(e2s), str(e3s), str(e4s), str(e5s), str(e6s), str(e7s), str(e8s)))
    #     cursor.execute(query, (33, "Raum"))
        connection.commit()

        query2 = """Select * from user"""
        cursor.execute(query2)
        result = cursor.fetchall()

        for row in result:
            print(row)
            print("\n")

        connection.close()

        messagebox.showinfo(title=None, message="Mitarbeiter erfolgreich registriert!")
        popup.destroy()

    b1 = tk.Button(popup,
                   text='Registrieren',
                   command=register)
    b1.grid(row=8, column=1)


# Button 3
registrieren = Button(root, text='Registrierung',
                 padx=20, pady=20,
                 command=onclick)
registrieren.pack(side='bottom', fill='x', padx=20, pady=30)


'''
def callback_reading():
    user_info = read_rfid_tag()
    print(user_info)
    # print("Registered User:" + user_info[1])
    #if User.find_by_id(user_info[0]):
    #    print("Employee registered")
    #print("Wer sind Sie?")
'''

root.mainloop()

