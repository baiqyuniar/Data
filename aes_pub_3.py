from datetime import datetime
import json
from random import randint
import time
import paho.mqtt.client as paho
from paho import mqtt
import AES_cipher as aes

def pencatatan(i, waktu, mess):
   f = open('Publisher AES.csv', 'a')
   f.write( "Message ke-" +i+ ";" + str(mess) + ";" + waktu + "\n")
   

def dump_pub(waktu, mess, messc):
   f = open('Publisher AES.csv', 'a')
   #f.write( "Message ke-" +i+ ";" + str(mess) + ";" + waktu + "\n")
   f.write(str(mess) + ";" + str(messc) + ";" + waktu + "\n")

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)
    
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.username_pw_set("dw41y6", "rtX67vv09")
client.connect("broker.mqttdashboard.com", 1883)
#b = 4 # plaintex = 4 byte -> payload = 20 bytes
#b = 14 # plaintex = 14 byte -> payload = 30 bytes
b = 24 # plaintex = 24 byte -> payload = 40 bytes
key192 = 'Mu8weQyDvq1HlAzNMu8weQyD'
key256 = 'Mu8weQyDvq1HlAzNMu8weQyDvq1HlAzN'    
iv = 'HIwu5283JGHsi76H'

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

    messc = aes.main(mess,key192,iv,"MODE_ECB","ENC")
    #payload = "p:"+str(mess)+";"+"t:"+now
    payload = "p:"+messc+";"+"t:"+now 
    client.publish("test/1", payload=payload, qos=1)
    print("Published : ", payload)
    dump_pub(now, mess, messc)
    print(len(payload))
    time.sleep(2)
            
client.disconnect()