from datetime import datetime
import json
from random import randint
import time
import paho.mqtt.client as paho
from paho import mqtt

def pencatatan(i, waktu, mess):
   f = open('Publisher Plain.csv', 'a')
   f.write( "Message ke-" +i+ ";" + str(mess) + ";" + waktu + "\n")
   

def dump_pub(waktu, mess):
   f = open('Publisher Plain.csv', 'a')
   #f.write( "Message ke-" +i+ ";" + str(mess) + ";" + waktu + "\n")
   f.write(str(mess) + ";" + waktu + "\n")

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)
    
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.username_pw_set("dw41y6", "rtX67vv09")
client.connect("broker.mqttdashboard.com", 1883)
b = 24 # plaintex = 4 byte -> payload = 20 bytes
#b = 14 # plaintex = 14 byte -> payload = 30 bytes
#b = 24 # plaintex = 24 byte -> payload = 40 bytes
    
message = {}
for i in range (20) :
        # if("%s", rc == "Success"): 
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

    #now = str(datetime.now().timestamp())
    
    now = "{:.5f}".format(time.time())
    now = now[5:]
    
    #payload = "p:"+str(mess)+";"+"t:"+now
    payload = "p:"+mess+";"+"t:"+now 
    client.publish("test/1", payload=payload, qos=1)
    print("Published : ", payload)
    dump_pub(now, mess)
    print(len(payload))
    time.sleep(2)
            
client.disconnect()