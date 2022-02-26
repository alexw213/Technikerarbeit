import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def read_rfid_tag():
    reader = SimpleMFRC522()
    try:
        id, text = reader.read()
        return id
    finally:
        GPIO.cleanup()