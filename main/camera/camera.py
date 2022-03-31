from picamera import PiCamera
from time import sleep
from PIL import ImageTk,Image
import cv2

camera = PiCamera()

def take_picture():
    camera.rotation = 270
    camera.start_preview()
    sleep(3)
    user_image = camera.capture('/home/pi/Technikerarbeit/camera/Pictures/image.jpg')
    camera.stop_preview()

    # Load an image in the script
    img = (Image.open("/home/pi/Technikerarbeit/camera/Pictures/image.jpg"))

    # Resize the Image using resize method
    resized_image = img.resize((300, 150), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)

    return new_image


