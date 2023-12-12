from picamera import PiCamera
from time import sleep
camera=PiCamera()
camera.start_preview()
time.sleep(5)
camera.capture('/home/raspberryPi/1.jpg')
camera.stop_preview()
