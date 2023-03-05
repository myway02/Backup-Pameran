#library
import pynmea2
import serial
import requests
import time

TOKEN = "BBFF-uL9hKg0lIYKSroMuSuAPlyHXXMXpCP"  # Put your TOKEN here
DEVICE_LABEL = "MyWay"  # Put your device label here
VARIABLE_LABEL_1 = "position"  # Put your second variable label here

#setting up
def port_setup(port):
    ser = serial.Serial(port, baudrate=9600, timeout=2)
    return ser

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

#logic
if __name__ == "__main__":

    # access serial port
    gps_port = "/dev/ttyACM0"
    ser = port_setup(gps_port)

def build_payload(variable_1):
    # Creates two random values for sending data
    value_1 = parseGPSdata (ser)
    if value_1 is None:
        print ('no data found')
    else:
        payload = {variable_1 : {"lat": -7.54851436038116, "lng": 111.65035935912164}}
        return payload

def main():
    payload = build_payload(VARIABLE_LABEL_1)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")
    print ("======================================")

def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True

if __name__ == '__main__':
    while (True):
        main()
        time.sleep(2)

    # Print out GPS cordinates
    print("GPS coordinate Stream:")

    while True:
        try:
            gps_coords = parseGPSdata(ser)
            if gps_coords is None:  # if no valid data was received
                print("No Data")
            else:
                print(f"latitude: {gps_coords[0]} , longitude: {gps_coords[1]} ")
        except serial.SerialException as e:  # catch any serial communication errors
            print(f"\nERROR: {e}")
            print("... reconnecting to serial\n")
            ser = port_setup()

        except KeyboardInterrupt as e:  # Catch when user hits Ctrl-C and end program
            print("--- Program shutting down ---")
            break

