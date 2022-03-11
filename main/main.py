from tkinter import * # urspünglicher Import

import tkinter as tk # new gui
from tkinter import ttk # new gui

root = Tk() # Fenster erstellen
root.wm_title("Time-Control") # Fenster - Titel
root.config(background = "#3399ff") # Hintergrundfarbe des Fensters
root.geometry("1200x800")

button1 = ttk.Button(root, text = "Coming")
button1.pack(side="left")

button2 = ttk.Button(root, text = "Leaving")
button2.pack(side="right")

#button3 = ttk.Button(root, text = "Registration")
#button3.pack(side="")

root.mainloop()
