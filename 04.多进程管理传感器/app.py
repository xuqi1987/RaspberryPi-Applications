# -*- coding:utf8 -*-
import multiprocessing
import time
import os
from test import *
import pymongo
import random
from DHT11 import Sense_DHT11
from VOICES import Sense_Voice



if __name__ == "__main__":

    # Multi-process
    record = []

    lock = multiprocessing.Lock()

    process = Sense_DHT11(lock,[26])
    record.append(process)

    process = Sense_Voice(lock,[19])
    record.append(process)

    # start all progress
    for process in record:
        process.start()

    for process in record:
        process.join()



