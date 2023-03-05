import telepot
import RPi.GPIO as GPIO
import time

# setting up GPIO for switch
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_Switch = 21
GPIO.setup(GPIO_Switch, GPIO.IN)

# bot setting up
bot = telepot.Bot('5502929834:AAEKhzAz8I-38bygXDe83EjkHj4ZdpuITRk')

# function to send notification to Telegram
def sendNotification():
    chat_id = '1124301975'
    bot.sendMessage(chat_id, 'Switch is ON')

# main function
def main():
    while True:
        if GPIO.input(GPIO_Switch) == 1:
            print("Switch is ON")
            sendNotification()
            # wait until the button is released
            while GPIO.input(GPIO_Switch) == 1:
                time.sleep(0.1)
        else:
            print("Switch is OFF")
        # delay before next loop iteration
        time.sleep(0.1)

# start the main function
main()
