from picamera import PiCamera
from time import sleep
from PIL import ImageTk,Image
import cv2

camera = PiCamera()

#%% ---Methode zum Foto machen---
def take_picture():
    camera.rotation = 270
    camera.start_preview() # Kamera einschalten
    sleep(5)
    user_image = camera.capture('/home/pi/Technikerarbeit/camera/Pictures/image.jpg') # Foto wird geschossen und gespeichert
    camera.stop_preview() # Kamera ausschalten



