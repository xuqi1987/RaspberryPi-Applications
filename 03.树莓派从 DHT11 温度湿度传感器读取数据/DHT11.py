# -*- coding:utf8 -*-
import RPi.GPIO as GPIO
import time

class Sense_DHT11():
    def __init__(self,out_pin):
        self.pin = out_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(out_pin,GPIO.OUT)
        GPIO.output(out_pin,GPIO.HIGH)

    def start(self):
        # 主机复位信号
        #发送开始信号
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin,GPIO.LOW)
        #至少等待18us
        time.sleep(0.01)

        #拉高20-40 us
        GPIO.output(self.pin,GPIO.HIGH)

        GPIO.setup(self.pin,GPIO.IN)


        # 等待低电平
        while GPIO.input(self.pin)==1:
            continue
        # 等待高电平
        while GPIO.input(self.pin)==0:
            continue

        # 等待低电平,数据开始
        while GPIO.input(self.pin)==1:
            continue
        # 数据位
        j = 0
        data = []
        # 前40位是数据位
        while j < 40:
            k = 0
            # 所有数据位都是以低电平开始的
            while GPIO.input(self.pin) == 0:
                continue

            while GPIO.input(self.pin) == 1:
                k+=1
                if k > 100:break;

            # 可能时间会不一样,所以可以改一下3这个值
            if k < 3:
                # 数字1表示的时间为26-28us
                data.append(0)
            else:
                # 数字0表示的时间为116-118us
                data.append(1)

            j += 1
        # 湿度整数位
        humidity_bit=data[0:8]
        # 湿度小数位
        humidity_point_bit=data[8:16]
        # 温度整数位
        temperature_bit=data[16:24]
        # 温度小数位
        temperature_point_bit=data[24:32]
        # 效验位
        check_bit=data[32:40]

        humidity=0
        humidity_point=0
        temperature=0
        temperature_point=0
        check=0
        # 转成10进制
        for i in range(8):
            humidity+=humidity_bit[i]*2**(7-i)
            humidity_point+=humidity_point_bit[i]*2**(7-i)
            temperature+=temperature_bit[i]*2**(7-i)
            temperature_point+=temperature_point_bit[i]*2**(7-i)
            check+=check_bit[i]*2**(7-i)

        #进行效验
        tmp=humidity+humidity_point+temperature+temperature_point
        if check==tmp:
            return (humidity,humidity_point,temperature,temperature_point)
        else:
            print "something is worong the humidity,humidity_point,temperature,temperature_point,check is",humidity,humidity_point,temperature,temperature_point,check

    def __del__(self):
        pass