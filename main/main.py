import tkinter as tk  # tkinter abkürzen mit tk
from tkinter import *  # Importierung der ttk-Widgets
from tkinter import messagebox
from datetime import datetime
from rfid import read
from db import write_db
from db import read_db
from camera import camera

from PIL import ImageTk,Image
import cv2


root = tk.Tk()  # Fenster erstellen
root.wm_title('Time-Control')  # Fenster - Titel
root.config(background='#ffdead')  # Hintergrundfarbe des Fensters
root.geometry('1200x800')  # GUI-Fenstergröße bestimmen


#%% ---GUI---

# Button 1
def chip_in():

    user_info = read.read_rfid_tag()
    id = user_info[0]
    #id = '803589853443'

    write_db.write_protocol(id, "kommen")

    name = read_db.get_name(id)

    datet = datetime.now()
    minute = str(datet.minute)
    length = 0
    for i in minute:
        length += 1
    if length == 1:
        minute = "0" + str(datet.minute)

    strdate = str(datet.day) + "." + str(datet.month) + "." + str(datet.year) + "  " + str(datet.hour) + ":" + str(minute)
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
    #id = '803589853443'

    write_db.write_protocol(id, "gehen")

    name = read_db.get_name(id)

    datet = datetime.now() #Klassenmethode importiert
    minute = str(datet.minute)
    length = 0
    for i in minute:
        length += 1
    if length == 1:
        minute = "0" + str(datet.minute)

    strdate = str(datet.day) + "." + str(datet.month) + "." + str(datet.year) + "  " + str(datet.hour) + ":" + str(minute)
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

        write_db.write_user(e1s, e2s, e3s, e4s, e5s, e6s, e7s, e8s)

        messagebox.showinfo(title=None, message="Mitarbeiter erfolgreich registriert!")
        popup.destroy()

    b1 = tk.Button(popup,
                   text='Bestätigen',
                   command=save)
    b1.grid(row=8, column=1)

    def picture():

        camera.take_picture()

        # Create a canvas
        canvas = Canvas(popup, width=600, height=400)
        canvas.grid(row=9, column=2)

        # Load an image in the script
        img = (Image.open("/home/pi/Technikerarbeit/camera/Pictures/image.jpg"))

        # Resize the Image using resize method
        resized_image = img.resize((200, 105), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)

        # Add image to the Canvas Items
        canvas.create_image(10, 10, anchor=CENTER, image=new_image)


    b2 = tk.Button(popup,
                   text='Foto',
                   command=picture)
    b2.grid(row=8, column=2)


# Button 3
registrieren = Button(root, text='Registrierung',
                 padx=20, pady=20,
                 command=register)
registrieren.pack(side='bottom', fill='x', padx=20, pady=30)


# Button 4
def get_protocol():
    popup_p = tk.Toplevel(root)

    result = read_db.get_protocol()

    #Zeilenkosmetik anpassen
    count = 0
    for row in result:
        count += 1
        name = str(row[0]) +" "+ str(row[1])
        datet = row[2]
        strdate = datet[:19]
        art = str(row[3])
        Label(popup_p, text=str(name)+"  "+str(strdate)+"  "+str(art)).grid(row=count)


protokoll = Button(root, text='Protokoll anzeigen',
                 padx=20, pady=20,
                 command=get_protocol)
protokoll.pack(side='top', fill='x', padx=20, pady=30)

root.mainloop()


"""
import tkinter as tk
from PIL import ImageTk, Image

# This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("640x480+100+100")
window.configure(background='grey')

path = "/home/pi/Technikerarbeit/camera/Pictures/image.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image=img)
panel1 = tk.Label(window, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

window.mainloop()
"""
"""
#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("750x270")

#Create a canvas
canvas= Canvas(win, width= 600, height= 400)
canvas.pack()

#Load an image in the script
img= (Image.open("/home/pi/Technikerarbeit/camera/Pictures/image.jpg"))

#Resize the Image using resize method
resized_image= img.resize((300,205), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)

win.mainloop()
"""