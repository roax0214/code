import RPI.GPIO as GPIO
import time
import telepot
from telepot.loop import Messageloop
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led=13
GPIO.setup(13,GPIO.out)
GPIO.output(13,GPIO.low)

def action(msg):
    chat_id=msg['chat']['id']
    command=msg['text']
    print('received':command)
    if 'on' in command:
        message:'turned on'
        if 'led' in command:
            GPIO.output(13,GPIO.HIGH)
            message=message+'led'
        telegram_bot.sendMessage(chat_id,messsage)
    if 'off' in command:
        message:'turned off'
        if 'led' in command:
            GPIO.output(13,GPIO.LOW)
            message=message+'led'
        telegram_bot.sendMessage(chat_id,messsage)
telegram_bot=telepot.Bot(' ')
print(telegram_bot.getMe())
MessageLoop(telegram_bot,action).run_as_thread()
print('up and running________')
while(1):
    time.sleep(10)
