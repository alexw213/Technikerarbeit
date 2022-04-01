#from picamera import PiCamera
from time import sleep
#from PIL import ImageTk,Image
#import cv2

#camera = PiCamera()

def take_picture():
    camera.rotation = 270
    camera.start_preview()
    sleep(3)
    user_image = camera.capture('/home/pi/Technikerarbeit/camera/Pictures/image.jpg')
    camera.stop_preview()



