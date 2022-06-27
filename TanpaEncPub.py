from datetime import datetime
import json
from random import randint
import time
import paho.mqtt.client as paho
from paho import mqtt

def pencatatan(i, waktu, mess):
   f = open('Publisher.csv', 'a')
   f.write( "Message ke-" +i+ ";" + str(mess) + ";" + waktu + "\n")

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)
    
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.username_pw_set("dw41y6", "rtX67vv09")
client.connect("broker.mqttdashboard.com", 1883)
    
message = {}
for i in range (100) :
        # if("%s", rc == "Success"): 
    mess = randint (1000,9999)
    now = str(datetime.now().timestamp())

    pencatatan(str(i), now, mess)
    message['order'] = i
    message['plaintext'] = mess
    message['datetime'] = now
    payload = json.dumps(message, indent=2) 
    client.publish("percobaan/data", payload=payload, qos=1)
    print("Published : ", mess)
    time.sleep(2)
            
client.disconnect()
