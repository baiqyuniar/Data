from datetime import datetime
import time
import paho.mqtt.client as paho
from paho import mqtt
import AES_cipher as aes

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.username_pw_set("dw41y6", "rtX67vv09")
client.connect("broker.mqttdashboard.com", 1883)

        # plaintex = 4 byte -> payload = 20 bytes
b = 14  # plaintex = 14 byte -> payload = 30 bytes
        # plaintex = 24 byte -> payload = 40 bytes

key128 = 'Mu8weQyDvq1HlAzN'
key192 = 'Mu8weQyDvq1HlAzNMu8weQyD'
key256 = 'Mu8weQyDvq1HlAzNMu8weQyDvq1HlAzN'
iv = 'HIwu5283JGHsi76H'

def dump_sub(msg, timeSend):
	now = "{:.5f}".format(time.time())
	now = now[5:]
	msg = aes.main(msg,key192,iv,"MODE_ECB","DEC")
	f = open('Subscriber AES.csv', 'a')
	f.write(msg + ";" + now + ";" + timeSend + "\n")

def on_message(client, userdata, msg):
    msg = msg.payload.decode("utf-8")
    mess=msg[2:]
    mess=mess.split(";")[0]
    timeSend = msg.split(";")[1]
    timeSend = timeSend[2:]
    dump_sub(mess, timeSend)
    print("Subscribed > ", msg)
    
client.on_message = on_message
client.subscribe("test/1", qos=1)

client.loop_forever()