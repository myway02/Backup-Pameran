# libaries
import RPi.GPIO as GPIO
import time
from pygame import mixer
 
 
##GPIO pin setup for raspberry
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
##set GPIO Pins
#Depan 
GPIO_TRIG1 = 17
GPIO_ECHO1 = 18

#Belakang
GPIO_TRIG2 = 22
GPIO_ECHO2 = 23

#kanan
GPIO_TRIG3 = 19
GPIO_ECHO3 = 16

#kiri
GPIO_TRIG4 = 6
GPIO_ECHO4 = 12
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIG1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)

GPIO.setup(GPIO_TRIG2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)

GPIO.setup(GPIO_TRIG3, GPIO.OUT)
GPIO.setup(GPIO_ECHO3, GPIO.IN)

GPIO.setup(GPIO_TRIG4, GPIO.OUT)
GPIO.setup(GPIO_ECHO4, GPIO.IN)

##Sound Setting up
#initializing mixer
mixer.init () 

#inputing sound
halangan = mixer.Sound("/home/pi/SIC/Baru/music/halangan.wav")
TIT = mixer.Sound("/home/pi/SIC/Baru/music/TIT.wav")
KIRI = mixer.Sound("/home/pi/SIC/Baru/music/ke-kiri.wav")
KANAN = mixer.Sound("/home/pi/SIC/Baru/music/ke-kanan.wav")
PUTAR = mixer.Sound("/home/pi/SIC/Baru/music/putar-balik.wav")


##Main Ultra Function
#Bagian Depan 
def distance1():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIG1, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG1, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance1 = (TimeElapsed * 34300) / 2
 
    return distance1

#Bagian Belakang
def distance2():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIG2, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG2, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO2) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO2) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance2 = (TimeElapsed * 34300) / 2
 
    return distance2

#Bagian Kanan
def distance3():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIG3, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG3, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO3) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO3) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance3 = (TimeElapsed * 34300) / 2
 
    return distance3

##Bagian Kiri
def distance4():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIG4, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG4, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO4) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO4) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance4 = (TimeElapsed * 34300) / 2
 
    return distance4


#Detecting an object
#DEPAN
def object_detection_1 (distance1):
    # Jika jarak dibawah 200 cm maka status adalah bahaya
    status_depan = "aman"
    if distance1 < 500 :
        status_depan = "TIT"
    if distance1 <= 250 :
        status_depan = "ADA HALANGAN"
    return status_depan
      
#BELAKANG
def object_detection_2 (distance2):
    # Jika jarak dibawah 200 cm maka status adalah bahaya
    status_belakang = "aman"
    if distance2 <= 280 :
        status_belakang = "ada yang mendekat"
    if distance2 < 180 :
        status_belakang = "bahaya"
    return status_belakang
   
#KANAN
def object_detection_3 (distance3):
    # Jika jarak dibawah 200 cm maka status adalah bahaya
    status_kanan = "aman"
    if distance3 <= 150 :
        status_kanan = "bahaya"
    return status_kanan
    
#KIRI
def object_detection_4 (distance4):
    # Jika jarak dibawah 200 cm maka status adalah bahaya
    status_kiri = "aman"
    if distance4 <= 150 :
        status_kiri = "bahaya"
    return status_kiri
    
#Loop
if __name__ == "__main__":
    while True:
        try:
            #Distance detection
            dist_depan = distance1()
            print ("JARAK DEPAN = %.1f cm" % dist_depan)
            status1 = object_detection_1 (dist_depan)
            print ("status adalah : ", status1)
            
            dist_belakang = distance2()
            print ("JARAK BELAKANG = %.1f cm" % dist_belakang)
            status2 = object_detection_2 (dist_belakang)
            print ("status adalah : ", status2)
            
            dist_kanan = distance3()
            print ("JARAK KANAN = %.1f cm" % dist_kanan)
            status3 = object_detection_3 (dist_kanan)
            print ("status adalah : ", status3)
            
            dist_kiri = distance4()
            print ("JARAK KIRI = %.1f cm" % dist_kiri)
            status4 = object_detection_4 (dist_kiri)
            print ("status adalah : ", status4)
            
            #Sound output
            #Depan
            if status1 == 'TIT':
                TIT.play ()
            if status1 == "ADA HALANGAN" and status3 > status4:
                KANAN.play ()
            if status1 == "ADA HALANGAN" and status4 > status3:
                KIRI.play ()
            if status1 == "ADA HALANGAN" and status4 and status3 == "bahaya":
                PUTAR.play()
            
            #Belakang
            if status2 == 'ada yang mendekat':
                TIT.play ()
            if status2 == "bahaya":
                TIT.play ()
                
            #Kanan
            if status3 == 'bahaya':
                KANAN.play ()
                
            #Kiri
            if status4 == 'bahaya':
                KIRI.play ()
                
                
            print("================================")
            #Gap time for sound 
            time.sleep(5)
            
        except KeyboardInterrupt as e:  # Catch when user hits Ctrl-C and end program
            print("--- Program shutting down ---")
            break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        