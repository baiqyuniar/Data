from datetime import datetime
import json
from random import randint
import time
import paho.mqtt.client as paho
from paho import mqtt

def pencatatan(i, waktu, mess):
   f = open('Publisher.csv', 'a')
   f.write("Message ke-" + i + ";" + str(mess) + ";" + waktu + "\n")

message = {}
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)
    if("%s", rc == "Success"):
            for i in range (5) : 
                mess = randint (1000,9999)
                now = str(datetime.now().timestamp())

                pencatatan(str(i), now, mess)

                message['plaintext'] = mess
                message['datetime'] = now
                payload = json.dumps(message, indent=2) 
                client.publish("percobaan/data", payload=payload, qos=1)

                print("Published : ", mess)
            
client = paho.Client(client_id="clientId-7GWFTtedw0", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.username_pw_set("dw41y6", "rtX67vv09")
client.connect("broker.mqttdashboard.com", 1883)

client.loop_start()
time.sleep(5)
client.loop_stop()
