#Libraries
import paho.mqtt.client as paho
from paho import mqtt
from pygame import mixer

# mendefinisikan variable
# broker = "localhost" # for local connection
broker = "industrial.api.ubidots.com"  # for online version
port = 1883
timeout = 60

##Sound setting up
#Initialize Mixer / turning on sound
mixer.init ()
pulang = mixer.Sound ("/home/pi/SIC/Baru/music/panggil.wav")

#Ubidots User & Pass setup
username = 'BBFF-EU3E0E9usx81Q0hcNc7MFmomOY144i'
password = 'BBFF-EU3E0E9usx81Q0hcNc7MFmomOY144i'


## subscribing topic for Ubidots
switch_topic = '/v1.6/devices/myway/tombol/lv'


# waiting for callback 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    client.subscribe(switch_topic)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload.decode('utf-8')))
    payload_decoded = msg.payload.decode('utf-8')
            
     #Main       
    if msg.topic == switch_topic:
        print ('dipanggil tuh !!!')
        pulang.play ()
        
        
# Create an MQTT client and attach our routines to it.
client = paho.Client()
# client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username=username,password=password)
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(broker, port, timeout)

client.loop_forever()
