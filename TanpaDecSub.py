from datetime import datetime
import json
import time
import paho.mqtt.client as paho
from paho import mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("rinii", "Kediri28")
client.connect("92dd0db1a8e54522903c9bd581917a5f.s1.eu.hivemq.cloud", 8883)

def pencatatan(i, msg, timeSend):
	now = str(datetime.now().timestamp())
	f = open('Subscriber.csv', 'a')
	f.write( "Message ke-" +i+ ";" + msg + ";" + now + ";" + timeSend + "\n")

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode("utf-8"))
    i = payload['order']
    msg = payload['plaintext']
    timeSend = payload['datetime']
    pencatatan(str(i), str(msg), timeSend)
    print("Subscribed : ", msg)
    

client.on_message = on_message
client.subscribe("percobaan/data", qos=1)

client.loop_forever()