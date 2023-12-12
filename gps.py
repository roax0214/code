import time
import serial
import string
import pynmea2
port='/dw/ttyAMAO'
ser=Serial.serial(Port,baud rate=9600,timeout=0.5)
while(1):
    try:
        data=ser.readline()
        if data[0:6]=='$GPGGA':
            msg=pynmea2.parse(data)
            latval=msg.lat
            concatlat='lat:'+str(latval)
            print(concatlat)
            lonval:msg.lon
            concatlat='lon:'+str(lonval)
            print(concatlat)
        finally:
            print('loading')
