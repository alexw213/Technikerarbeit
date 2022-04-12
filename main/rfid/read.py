import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#%% ---Methode zum Auslesen des RFID-Chips---
def read_rfid_tag():
    reader = SimpleMFRC522()
    try:
        user_info = reader.read()
        return user_info
    finally:
        GPIO.cleanup()