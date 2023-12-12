import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
segment=(17,27,22,23,24,25,5,6)
for segment in segment:
    GPIO.setup(segment,GPIO.OUT)
    GPIO.output(segment,GPIO.HIGH)
digits=(16,20,21,12)
for digit in digits:
    GPIO.setup(digit,GPIO.OUT)
    GPIO.setup(digit,GPIO.HIGH)

num={' ':(0,0,0,0,0,0,0),
     '0':(1,1,1,1,1,1,0),
     '1':(0,1,1,0,0,0,0),
     '2':(1,1,0,1,1,0,1),
     '3':(1,1,1,1,0,0,1),
     '4':(0,1,1,0,0,1,1),
     '5':(1,0,1,1,0,1,1),
     '6':(1,0,1,1,1,1,1),
     '7':(1,1,1,0,0,0,0),
     '8':(1,1,1,1,1,1,1),
     '9':(1,1,1,1,0,1,1),
    }

while True:
    n=time.(time()[11:13])+time.time()[14:16])
    s=str(n)
    for digit in range(4):
        for loop in range(0,7):
            if num[s[digit]][loop]==0:
                GPIO.OUTPUT(segments[loop],1)
            else:
                GPIO.OUTPUT(segments(loop),0)
            if int(time.(time()[18:19])%2==0)and(digit==1):
                GPIO.OUTPUT(6,0)
            else:
                GPIO.OUTPUT(6,1)
    GPIO.OUTPUT(digits[digit],1)
    time.sleep(0.001)
    GPIO.OUTPUT(digits[digits[digit]],0)
    
    
