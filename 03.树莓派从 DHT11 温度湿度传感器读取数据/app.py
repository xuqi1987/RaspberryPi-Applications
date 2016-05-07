# -*- coding:utf8 -*-
from DHT11 import Sense_DHT11
import time

dht = Sense_DHT11(26)
while True:
    print dht.start()
    time.sleep(1)
