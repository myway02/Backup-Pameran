import RPi.GPIO as GPIO
import time
import telepot

GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

bot = telepot.Bot('5502929834:AAEKhzAz8I-38bygXDe83EjkHj4ZdpuITRk')

def handle_switch(channel):
    if GPIO.input(channel):
        bot.sendMessage('1124301975', 'Switch turned on')
    else:
        bot.sendMessage('1124301975', 'Switch turned off')

GPIO.add_event_detect(21, GPIO.BOTH, callback=handle_switch, bouncetime=200)

while True:
    time.sleep(1)
