#libaries
import serial
import pynmea2
import time
import pyrebase


##Firebase setup
config = {
    "apiKey": "AIzaSyC41ntynimqPmk4_3oWSfmXpJ0C3wgGr7I",
    "authDomain": "myway2023-790a8.firebaseapp.com",
    "databaseURL": "https://myway2023-790a8-default-rtdb.firebaseio.com",
    "projectId": "myway2023-790a8",
    "storageBucket": "myway2023-790a8.appspot.com",
    "messagingSenderId": "68073473672",
    "appId": "1:68073473672:web:d0c86be90a802d2265013d",
    "measurementId": "G-31T6CG2PDK"
};


#initializing database
firebase = pyrebase.initialize_app(config)

##Main GPS ffucntion
#setup port with serial
def port_setup(port):
    ser = serial.Serial(port, baudrate=9600, timeout=2)
    return ser

#get some data
def parseGPSdata(ser):
    keywords = ["$GPRMC","$GPGGA"]
    gps_data = ser.readline()
    gps_data = gps_data.decode("utf-8")  # transform data into plain string

    if len(gps_data) > 5:  # Check to see if the GPS gave any useful data
        if gps_data[0:6] in keywords:   # Check t see if the message code
            gps_msg = pynmea2.parse(gps_data)
            lat = gps_msg.latitude
            lng = gps_msg.longitude
            return (lat,lng)
        else:
            return None
    else:
        return None
    
#Loop
if __name__ == "__main__":
    # access serial port GPS 
    gps_port = "/dev/ttyACM0"
    ser = port_setup(gps_port)
    
    # Print out GPS cordinates
    print("GPS coordinate Stream:")
    while True:
        try:
            #Firebase storage setup
            storage = firebase.storage()
            database = firebase.database()
            
            #Position Storage Push
            gps_coords = parseGPSdata(ser)
            if gps_coords is None:  # if no valid data was received
                print("No Data")
            else:
                print(f"latitude: {gps_coords[0]} , longitude: {gps_coords[1]} ")
                database.child("Lokasi")
                dt = {"lokasi" : (f"http://maps.google.com/?q={gps_coords[0]},{gps_coords[1]}")}
                database.set(dt)
                database.child("Storage Lokasi")
                database.push(dt)
            
        except serial.SerialException as e: # catch any serial communication errors
            print(f"\nERROR: {e}")
            print("... reconnecting to serial\n")
            ser = port_setup()

        except KeyboardInterrupt as e:  # Catch when user hits Ctrl-C and end program
            print("--- Program shutting down ---")
            break