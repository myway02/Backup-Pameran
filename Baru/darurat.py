import telepot
import RPi.GPIO as GPIO
import time

# setting up GPIO for push button
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_Button = 21
GPIO.setup(GPIO_Button, GPIO.IN)

# bot setting up
bot = telepot.Bot('5502929834:AAEKhzAz8I-38bygXDe83EjkHj4ZdpuITRk')

# initialize chat_id as a global variable
chat_id = None

# Main function
def handle(msg):
    global chat_id
    chat_id = msg['chat']['id']
    telegramText = msg['text']

    print('Message received from ' + str(chat_id))

    # when program started, the main () goes on
    if telegramText == '/start':
        bot.sendMessage(chat_id, 'My Way siap membantu anda.')  # Put your welcome note here


def main():
    global chat_id  # use the global chat_id variable
    while True:
        if GPIO.input(GPIO_Button) == 1:
            print("Pengguna dalam bahaya")
            motion = 1
            # check if chat_id has been initialized
            if chat_id is not None:
                sendNotification(motion, chat_id)

        else:
            print('Pengguna aman')

        # delay before next loop iteration
        time.sleep(0.1)


# sending infinite notification to telegram
def sendNotification(motion, chat_id):
    bot.sendMessage(chat_id, 'Segera periksa Way-App. Pengguna sedang butuh bantuan !!!')
    time.sleep(5)


bot.message_loop(handle)

# start the main function
main()
