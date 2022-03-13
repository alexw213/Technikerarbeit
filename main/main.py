from tkinter import * # urspünglicher Import

import tkinter as tk # new gui
from tkinter import ttk # new gui

root = Tk() # Fenster erstellen
root.wm_title("Time-Control") # Fenster - Titel
root.config(background = "#3399ff") # Hintergrundfarbe des Fensters
root.geometry("1200x800")

#Button 1
def say_hello():
    print("Have a nice workday!")

button1 = ttk.Button(root, text = "Coming", padding=50, command=say_hello)
button1.pack(side="left")

for item in button1.keys():
    print(item, ": ", button1[item])

#Button 2
def say_bye():
    print("Have a nice closing time!")

button2 = ttk.Button(root, text = "Leaving", padding=50, command=say_bye)
button2.pack(side="right")

#Button 3
button3 = ttk.Button(root, text = "Registration", padding=20) # 3. Button mit Text "Registration" wird erstellt
button3.pack(side="bottom", fill="x")   # 3. Button wird unten dargestellt und füllt den restlichen Freiraum der x-Achse
                                        # aus

root.mainloop()
