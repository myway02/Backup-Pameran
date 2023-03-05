import RPi.GPIO as GPIO
import time

# setting up GPIO for switch
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_Switch = 26
GPIO.setup(GPIO_Switch, GPIO.IN)

# main function
def main():
    while True:
        if GPIO.input(GPIO_Switch) == 1:
            print("Switch is ON")
        else:
            print("Switch is OFF")
        # delay before next loop iteration
        time.sleep(0.1)

# start the main function
main()
