import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def write_rfid_tag(name):
    reader = SimpleMFRC522()
    try:
        print("Halten Sie jetzt den RFID-Chip ans Lesegeraet")
        reader.write(name)
        print("Vorgang abgeschlossen")
    except:
        print('Geht nicht')
    finally:
        GPIO.cleanup()