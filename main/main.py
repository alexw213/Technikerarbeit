import tkinter as tk  # tkinter abkürzen mit tk
from tkinter import *  # Importierung der ttk-Widgets
root = tk.Tk()  # Fenster erstellen
root.wm_title('Time-Control')  # Fenster - Titel
root.config(background='#ffdead')  # Hintergrundfarbe des Fensters
root.geometry('1200x800')  # GUI-Fenstergröße bestimmen

from rfid.read import read_rfid_tag
from rfid.write import write_rfid_tag
import sqlite3
from db.user import User


#%% --- GUI ---

# Button 1
def say_hello():
    print('Have a nice workday!')

button1 = Button(root,
                 text='Coming',
                 padx=50, pady=50,
                 bg='#00cd00',
                 command=say_hello)
button1.pack(side='left', padx=20, pady=50)


# Button 2
def say_bye():
    print('Have a nice closing time!')

button2 = Button(root, text='Leaving',
                 padx=50, pady=50,
                 bg='red',
                 command=say_bye)
button2.pack(side='right', padx=20, pady=50)


# Registration on a new window
def createNewWindow():
    popup = tk.Toplevel(root)

fields = 'Last Name', 'First Name', 'Date of Birth', 'Marital status' , 'Adress' , 'Phone number' , 'E-Mail' , 'RFID-Tag'

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text))

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
    popup = tk.Toplevel(root)
    ents = makeform(popup, fields)
    popup.bind('<Return>', (lambda event, e=ents: fetch(e)))

    b1 = Button(popup, text='Confirm',
          command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)

# when you put b2 it must open a new window with the entries above, but it doesn't work
    b2 = tk.Button(root,
                text='Registration',
                padx=20, pady=10,
                command=createNewWindow)
    b2.pack(side='bottom', fill='x', pady=20)

#here i wanted to try the RFID-registration, but it doesn't work
""" 
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
"""

root.mainloop()

