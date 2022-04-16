
import tkinter as tk  # tkinter abkürzen mit tk
from tkinter import *  # Importierung der ttk-Widgets
from tkinter import messagebox # Einfügen einer Messagebox in der GUI
from datetime import datetime # Zeitangabe einfügen
from rfid import read # Vom Ordner "RFID" wird die Klasse "read" eingefügt
from db import write_db # Vom Ordner "db" wird die Klasse "write_db" eingefügt
from db import read_db # Vom Ordner "db" wird die Klasse "read_db" eingefügt
from PIL import ImageTk,Image # Zum Verwenden des Bildes in der GUI
from camera import camera # Vom Ordner "camera" die Klasse "camera" einfügen
import cv2 # Importierung "open cv", um das Bild in der GUI anzeigen zu lassen

root = tk.Tk()  # Fenster erstellen
root.wm_title('Time-Control')  # Fenster - Titel
root.config(background='#ffdead')  # Hintergrundfarbe des Fensters
root.geometry('1200x800')  # GUI-Fenstergröße bestimmen


#%% ---Einchipen---
def chip_in():

    # RFID-Tag auslesen
    user_info = read.read_rfid_tag()
    id = user_info[0]

    # Einchipprotokoll schreiben (2 Parameter werden übergeben)
    write_db.write_protocol(id, "kommen")

    # Name des RFID-User auslesen
    name = read_db.get_name(id)

    # Aktuelle Zeit wird ausgelesen
    datet = datetime.now()

    # Minute kann mal einstellig sein, wenn dem so ist dann muss eine Null davor
    minute = str(datet.minute)
    length = 0
    for stelle in minute:
        length += 1
    if length == 1:
        minute = "0" + str(datet.minute)

    # Anzeigereihenfolge festsetzen in der Messagebox
    strdate = str(datet.day) + "." + str(datet.month) + "." + str(datet.year) + "  " + str(datet.hour) +\
              ":" + str(minute)


    messagebox.showinfo(title=None, message="Einen schönen Arbeitstag " + name + "!" + "\n" + "Zeitpunkt: " +
                                            str(strdate) + " Uhr")


kommen = Button(root,
                 text='Kommen',
                 padx=50, pady=50,
                 bg='#00cd00',
                 command=chip_in)
kommen.pack(side='left', padx=20, pady=50)


#%% ---Auschipen---
def chip_out():

    # RFID-Tag auslesen
    user_info = read.read_rfid_tag()
    id = user_info[0]

    # Auschipprotokoll schreiben (2 Parameter werden übergeben)
    write_db.write_protocol(id, "gehen")

    # Name des RFID-User auslesen
    name = read_db.get_name(id)

    # Aktuelle Zeit wird ausgelesen
    datet = datetime.now()

    # Minute kann mal einstellig sein, wenn dem so ist dann muss eine Null davor
    minute = str(datet.minute)
    length = 0
    for i in minute:
        length += 1
    if length == 1:
        minute = "0" + str(datet.minute)

    # Anzeigereihenfolge festsetzen in der Messagebox
    strdate = str(datet.day) + "." + str(datet.month) + "." + str(datet.year) + "  " +\
              str(datet.hour) + ":" + str(minute)

    messagebox.showinfo(title=None, message="Einen schönen Feierabend " + name + "!" + "\n" + "Zeitpunkt: " +
                                            strdate + " Uhr")

gehen = Button(root, text='Gehen',
                 padx=50, pady=50,
                 bg='red',
                 command=chip_out)
gehen.pack(side='right', padx=20, pady=50)


#%% ---Registrierung im neuen Fenster---
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
    Label(popup, text='PID-Nummer').grid(row=8)

    e1 = Entry(popup)
    e2 = Entry(popup)
    e3 = Entry(popup)
    e4 = Entry(popup)
    e5 = Entry(popup)
    e6 = Entry(popup)
    e7 = Entry(popup)
    e8 = Entry(popup)
    e9 = Entry(popup)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)
    e7.grid(row=6, column=1)
    e8.grid(row=7, column=1)
    e9.grid(row=8, column=1)

    # User anlegen/speichern
    def save():

        e1s = e1.get()
        e2s = e2.get()
        e3s = e3.get()
        e4s = e4.get()
        e5s = e5.get()
        e6s = e6.get()
        e7s = e7.get()
        e8s = e8.get()
        e9s = e9.get()

        # User in die Datenbank einpflegen
        write_db.write_user(e1s, e2s, e3s, e4s, e5s, e6s, e7s, e8s, e9s)
        popup.destroy()  # Registrierungfenster wird geschlossen

        messagebox.showinfo(title=None, message="Mitarbeiter erfolgreich registriert!")


    b1 = tk.Button(popup,
                   text='Bestätigen',
                   command=save)
    b1.grid(row=9, column=1)

    # Foto erstellen
    def picture():
        # Methode für den Schnappschuss
        camera.take_picture()

        # Das Bild wird geladen
        img = Image.open("/home/pi/Technikerarbeit/camera/Pictures/image.jpg")

        # Die Größe des Bildes verändern
        resized_image = img.resize((300, 150), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)

        # neues Foto im Registrierungspopup anzeigen
        panel = Label(popup, image=new_image) # Labelobjekt "panel" wird erstellt
        panel.image = new_image # In die Imagevariable wird das neue Bild eingefügt
        panel.grid(row=10, column=1)

    # Kamera wird ausgelöst
    b2 = tk.Button(popup,
                   text='Foto',
                   command=picture)
    b2.grid(row=9, column=2)


registrieren = Button(root, text='Registrierung',
                 padx=20, pady=20,
                 command=register)
registrieren.pack(side='bottom', fill='x', padx=20, pady=30)


#%% ---Protokoll-Anzeige---
def show_protocol():
    popup_p = tk.Toplevel(root)

    # Protokoll wird aus der Datenbank ausgelesen
    result = read_db.get_protocol()

    #Zeilenkosmetik anpassen
    count = 0
    for row in result:
        count += 1
        name = str(row[0]) +" "+ str(row[1]) # Name wird aus Vorname und Nachname zusammengesetzt
        datet = row[2] # 3. Zeile Zeitpunkt wird zugewiesen
        strdate = datet[:19] # Aus Zeitangabe wird die Sekunde auf 2 Stellen verkürzt
        reg_art = str(row[3])
        Label(popup_p, text=str(name)+"  "+str(strdate)+"  "+str(reg_art)).grid(row=count) # Einträge im Protokoll-Popup erstellen


protokoll = Button(root, text='Protokoll anzeigen',
                 padx=20, pady=20,
                 command=show_protocol)
protokoll.pack(side='top', fill='x', padx=20, pady=30)


root.mainloop()

