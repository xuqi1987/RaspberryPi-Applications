#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import multiprocessing
from DATABASE import mongodatabase
import datetime


# 将这个类定义成进程
class Sense_Voice(multiprocessing.Process):

    def __init__(self,lock,pins):
        multiprocessing.Process.__init__(self)
        self.pin = pins[0]
        self.lock = lock
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin,GPIO.IN)

        pass

    def update(self):
        n = 0
        while True:
            if GPIO.input(self.pin) == GPIO.HIGH:
                n = n +1
            else:
                n = n - 1

            if abs(n) > 0:
                break;

            time.sleep(0.01)

        return {"声音":n < 0}

    def run(self):

        client = mongodatabase('db.conf')
        client.connect("raspberry")
        self.db = client.get_db()
        print"%s连接数据库成功~"%self.__class__.name

        while True:
            try:
                data = self.update()
            except Exception,X:
                #print X
		        pass
            else:
                #print data
                #print self.db
                if data["声音"]:
                    print data
                    self.db.voice.insert(data)
                pass
            finally:
                time.sleep(0.1)
                pass