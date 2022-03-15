
import tkinter as tk  # tkinter abkürzen mit tk
from tkinter import *  # Importierung der ttk-Widgets

root = tk.Tk()  # Fenster erstellen
root.wm_title("Time-Control")  # Fenster - Titel
root.config(background="#3399ff")  # Hintergrundfarbe des Fensters
root.geometry("1200x800")  # GUI-Fenstergröße bestimmen


#%% --- GUI ---

# Button 1
def say_hello():
    print("Have a nice workday!")

button1 = Button(root,
                 text="Coming",
                 padx=50, pady=50,
                 command=say_hello)
button1.pack(side="left", padx=20, pady=50)


# Button 2
def say_bye():
    print("Have a nice closing time!")

button2 = Button(root, text="Leaving",
                 padx=50, pady=50,
                 command=say_bye)
button2.pack(side="right", padx=20, pady=50)




#%% Registration on a new window
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
    b1 = Button(popup, text='Show',
          command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(popup, text='Quit', command=popup.quit)
    b2.pack(side=LEFT, padx=5, pady=5)

    b3 = tk.Button(root,
                text="Registration",
                padx=20, pady=10,
                command=createNewWindow)
    b3.pack(side="bottom", fill="x", pady=20)


root.mainloop()
