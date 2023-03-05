from gpiozero import Button
import telebot

# Telegram bot token
TOKEN = '5502929834:AAEKhzAz8I-38bygXDe83EjkHj4ZdpuITRk'

# Telegram chat ID to send messages to
CHAT_ID = '1124301975'

# Initialize Telegram bot
bot = telebot.TeleBot(TOKEN)

# Initialize switch
switch = Button(21)

# Define message function
def send_message(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

# Monitor switch state and send messages
while True:
    if switch.is_pressed:
        # Send message when switch is turned on
        message = 'Switch turned on!'
        send_message(message)

        # Wait for switch to be released
        while switch.is_pressed:
            pass

        # Send message when switch is turned off
        message = 'Switch turned off!'
        send_message(message)
