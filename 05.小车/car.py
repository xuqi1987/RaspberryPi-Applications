import  RPi.GPIO as GPIO

import datetime
import time

class Wheel(object):
    def __init__(self,in_pin1,in_pin2,enable_pin1,enable_pin2):
        self.pin1 = in_pin1
        self.pin2 = in_pin2

        GPIO.setup(in_pin1,GPIO.OUT)
        GPIO.setup(in_pin2,GPIO.OUT)
        GPIO.setup(enable_pin1,GPIO.OUT)
        GPIO.setup(enable_pin2,GPIO.OUT)

        GPIO.output(enable_pin1,True)
        GPIO.output(enable_pin2,True)
        pass

    def forword(self):
        GPIO.output(self.pin1, True)
        GPIO.output(self.pin2, False)
        pass


    def backword(self):
        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, True)
        pass

    def stop(self):
        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, False)
        pass

class Car(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.left_wheel = Wheel(25,24)
        self.right_wheel = Wheel(23,18)
        pass

    def forword(self):
        self.left_wheel.forword()
        self.right_wheel.forword()
        pass

    def backword(self):
        self.left_wheel.backword()
        self.right_wheel.backword()
        pass

    def left(self):
        self.left_wheel.stop()
        self.right_wheel.forword()
        pass

    def rigth(self):
        self.left_wheel.forword()
        self.right_wheel.stop()
        pass

    def stop(self):
        self.left_wheel.stop()
        self.right_wheel.stop()
        pass

    def shutdown(self):
        self.stop()
        GPIO.cleanup()
        pass

    def test(self):
        pass


c = Car()

while True:
    c.forword()
    time.sleep(4)
    c.backword()
    time.sleep(4)
    c.left()
    time.sleep(4)
    c.rigth()
    time.sleep(4)
