import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def write_rfid_tag(name):
    reader = SimpleMFRC522()
    try:
        print("Halten Sie jetzt den RFID-Chip ans Lesegeraet")
        reader.write(name)
        id = reader.read()
        print("Vorgang abgeschlossen mit ID '{}'".format(id))
        return id
    except:
        print('Geht nicht')
    finally:
        GPIO.cleanup()