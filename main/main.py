
import tkinter as tk  # tkinter abkürzen mit tk
from tkinter import *  # Importierung der ttk-Widgets

root = tk.Tk()  # Fenster erstellen
root.wm_title("Time-Control")  # Fenster - Titel
root.config(background="#3399ff")  # Hintergrundfarbe des Fensters
root.geometry("1200x800")  # GUI-Fenstergröße bestimmen


#%% Buttons

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




#%% Registration-Entry
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


button3 = tk.Button(root,
                text="Registration",
                padx=20, pady=10,
                command=createNewWindow)
button3.pack(side="bottom", fill="x", pady=20)



"""
# Button 3
def createNewWindow():
    newWindow = tk.Toplevel(app)  # neues Fenster in root

button3 = ttk.Button(root, text="Registration", command=createNewWindow)
button3.pack(side="bottom", fill="x")


# Eingabefeld
def print_entry_input():
    print(entry1_popup.get())


entry1_popup = ttk.Entry(master=popup)
entry1_popup.pack()
"""
"""
button4 = ttk.Button(root, text = "Confirm", command=print_entry_input) #Gibt eingebene Daten aus
button4.pack(side="bottom", fill="x")

def delete_input():
    entry1.delete(0, tk.END)

button5 = ttk.Button(root, text = "Clear", command=delete_input) #Löscht eingegebene Daten
button5.pack(side="bottom", fill="x")

#for item in entry1.keys():
#    print(item, ": ", entry1[item])

for item in button5.keys():
    print(item, ": ", button5[item])
"""

root.mainloop()
