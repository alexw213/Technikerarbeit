from picamera import PiCamera
from time import sleep

camera = PiCamera()

def take_picture():
    camera.start_preview()
    sleep(3)
    user_image = camera.capture('/home/pi/Technikerarbeit/camera/Pictures/image.jpg')
    camera.stop_preview()

    return user_image

