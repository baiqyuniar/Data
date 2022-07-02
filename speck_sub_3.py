from datetime import datetime
from random import randint
import time
import paho.mqtt.client as paho
from paho import mqtt
from speck import SpeckCipher

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.username_pw_set("dw41y6", "rtX67vv09")
client.connect("broker.mqttdashboard.com", 1883)

        # plaintex = 4 byte -> payload = 20 bytes
b = 14  # plaintex = 14 byte -> payload = 30 bytes
        # plaintex = 24 byte -> payload = 40 bytes

key128 = 0x1f1e1d1c1b1a19181716151413121110
key192 = 0x1f1e1d1c1b1a191817161514131211100f0e0d0c0b0a0908
key256 = 0x1f1e1d1c1b1a191817161514131211100f0e0d0c0b0a09080706050403020100

cipher = SpeckCipher(key256, 256, 128, 'ECB')

def dump_sub(msg, timeSend):
	now = "{:.5f}".format(time.time())
	now = now[5:]
	f = open('Subscriber Speck.csv', 'a')
	f.write(msg + ";" + now + ";" + timeSend + "\n")

def on_message(client, userdata, msg):
    msg = msg.payload.decode("utf-8")
    mess=msg[2:]
    mess1=mess.split(";")[0]
    coba = int(mess1)
    msg1 = cipher.decrypt(coba)
    print(msg1)
    timeSend = msg.split(";")[1]
    timeSend1 = timeSend[2:]
    dump_sub(str(msg1), timeSend1)
    print("Subscribed > ", msg)
    
client.on_message = on_message
client.subscribe("test/1", qos=1)

client.loop_forever()