from datetime import datetime
from random import randint
import time
import paho.mqtt.client as paho
from paho import mqtt
import AES_cipher as aes

def dump_pub(waktu, mess, messc, enctime):
   f = open('Publisher AES 256.csv', 'a')
   f.write(str(mess) + ";" + str(messc) + ";" + waktu + ";" + "{:.9f}".format(enctime) + "\n")

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

for j in range (10):    
	client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
	client.on_connect = on_connect

	client.username_pw_set("dw41y6", "rtX67vv09")
	client.connect("broker.mqttdashboard.com", 1883)

			# plaintex = 4 byte -> payload = 20 bytes
	b = 24  # plaintex = 14 byte -> payload = 30 bytes
			# plaintex = 24 byte -> payload = 40 bytes

	iv = 'HIwu5283JGHsi76H'
	key128 = 'Mu8weQyDvq1HlAzN'
	key192 = 'Mu8weQyDvq1HlAzNMu8weQyD'
	key256 = 'Mu8weQyDvq1HlAzNMu8weQyDvq1HlAzN'    

	message = {}
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

		curr = time.time_ns()
		now = "{:.5f}".format(curr)
		now = now[5:]

		messc = aes.main(mess,key256,iv,"MODE_ECB","ENC")
		enc_time = time.time_ns() - curr
	
		payload = "p:"+messc+ ";" + "t:"+now 

		client.publish("top/123", payload=payload, qos=1)
		print("Published > ", payload)

		dump_pub(now, mess, messc, enc_time)
    
		print(len(payload))
		time.sleep(2)

	client.disconnect()
	time.sleep(1)