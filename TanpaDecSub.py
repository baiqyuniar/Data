from datetime import datetime
import json
import time
import paho.mqtt.client as paho
from paho import mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

def pencatatan(msg, timeSend):
	now = str(datetime.now().microsecond)
	f = open('Subscriber.csv', 'a')
	f.write(msg + ";" + now + ";" + dateSend + "\n")

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode("utf-8"))
    msg = payload['plaintext']
    timeSend = payload['datetime']
    print("Subscribed : ", msg)
    
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.username_pw_set("dw41y6", "rtX67vv09")
client.connect("broker.mqttdashboard.com", 1883)

client.on_message = on_message
client.subscribe("percobaan/data", qos=1)

client.loop_forever()