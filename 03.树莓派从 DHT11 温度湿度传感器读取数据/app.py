# -*- coding:utf8 -*-
from DHT11 import Sense_DHT11
import time

dht = Sense_DHT11(26)

dht.start()

while dht.get_temperature() == None:
    time.sleep(0.1)

print dht.get_temperature()

