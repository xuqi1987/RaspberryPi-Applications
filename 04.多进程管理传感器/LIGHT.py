#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import multiprocessing
from DATABASE import mongodatabase
import datetime


# 将这个类定义成进程
class Sense_Light(multiprocessing.Process):

    def __init__(self,lock,pins):
        multiprocessing.Process.__init__(self)
        self.pin = pins[0]
        self.lock = lock
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin,GPIO.IN)

        pass

    def update(self):
        light = False
        last = False
        while True:
            if GPIO.input(self.pin) == GPIO.HIGH:
                light = False
            else:
                light = True

            if last != light:
                break
            time.sleep(0.5)

        return {"光线":light,"时间":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

    def run(self):

        client = mongodatabase('db.conf')
        client.connect("raspberry")
        self.db = client.get_db()
        print"%s连接数据库成功~"%self.__class__

        while True:
            try:
                data = self.update()
            except Exception,X:
                #print X
		        pass
            else:
                #print data
                #print self.db
                print "光线变化:%s,%s"%(data['光线'],datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                self.db.light.insert(data)
                pass
            finally:
                time.sleep(1)
                pass