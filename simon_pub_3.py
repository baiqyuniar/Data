from datetime import datetime
from random import randint
import time
import paho.mqtt.client as paho
from paho import mqtt
from simon import SimonCipher

def dump_pub(waktu, mess, messc):
   f = open('Publisher Simon.csv', 'a')
   f.write(str(mess) + ";" + str(messc) + ";" + waktu + "\n")

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)
    
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.username_pw_set("dw41y6", "rtX67vv09")
client.connect("broker.mqttdashboard.com", 1883)

            # plaintex = 4 byte -> payload = 20 bytes
b = 24      # plaintex = 14 byte -> payload = 30 bytes
            # plaintex = 24 byte -> payload = 40 bytes

key128 = 0x1f1e1d1c1b1a19181716151413121110
key192 = 0x1f1e1d1c1b1a191817161514131211100f0e0d0c0b0a0908
key256 = 0x1f1e1d1c1b1a191817161514131211100f0e0d0c0b0a09080706050403020100

cipher = SimonCipher(key256, 256, 128, 'ECB')

for i in range (10) :
    mess = "0"
    if b == 4:
        pl = randint (1000,9999)
        mess = str(pl)
    elif b == 14:
        pl = randint (10000,99999)
        mess = str(pl)
        pl = randint (10000,99999)
        mess = mess + str(pl)
        pl = randint (1000,9999)
        mess = mess + str(pl)
    elif b == 24:
        pl = randint (10000,99999)
        mess = str(pl)
        pl = randint (10000,99999)
        mess = mess + str(pl)
        pl = randint (10000,99999)
        mess = mess + str(pl)
        pl = randint (10000,99999)
        mess = mess + str(pl)
        pl = randint (1000,9999)
        mess = mess + str(pl)

    now = "{:.5f}".format(time.time())
    now = now[5:]

    pt = int(mess)
    messc = cipher.encrypt(pt)
    payload = "p:"+str(messc)+";"+"t:"+now 

    client.publish("test/1", payload=payload, qos=1)
    print("Published > ", payload)

    dump_pub(now, mess, messc)

    print(len(str(payload)))

    time.sleep(2)
            
client.disconnect()
