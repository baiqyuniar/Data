from datetime import datetime
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

        # plaintex = 4 byte -> payload = 20 bytes
b = 14  # plaintex = 14 byte -> payload = 30 bytes
        # plaintex = 24 byte -> payload = 40 bytes

def dump_sub(msg, timeSend):
	#now = str(datetime.now().timestamp())
	now = "{:.5f}".format(time.time())
	now = now[5:]
	f = open('Subscriber TLS.csv', 'a')
	f.write(msg + ";" + now + ";" + timeSend + "\n")


def on_message(client, userdata, msg):
    msg = msg.payload.decode("utf-8")
    mess=msg[2:]
    mess=mess.split(";")[0]
    timeSend = msg.split(";")[1]
    timeSend = timeSend[2:]
    dump_sub(mess, timeSend)
    print("Subscribed : ", msg)
    

client.on_message = on_message
client.subscribe("test/1", qos=1)

client.loop_forever()