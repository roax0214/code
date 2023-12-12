import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
list=[5,6,13,19,26]
while(true):
    for i in list:
        GPIO.OUTPUT(i,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.OUTPUT(i.GPIO.LOW)
        time.sleep(0.5)

        
    
