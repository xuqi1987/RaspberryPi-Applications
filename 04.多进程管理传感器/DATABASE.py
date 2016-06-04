#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import datetime
import ConfigParser
import os

#获取config配置文件
def getConfig(conf,section, key):
    config = ConfigParser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/'+ conf
    config.read(path)
    return config.get(section, key)

class mongodatabase():
    def __init__(self,conf):
        self.conf = conf
        pass

    def connect(self,dbname):
        self.host = getConfig(self.conf,'database','dbhost')
        self.port = getConfig(self.conf,'database','dbport')
        self.client = pymongo.MongoClient(host=self.host,port=self.port)
        self.dbname = dbname
        self.db = None
    def get_db(self):
        # 建立连接
        self.db = self.client[self.dbname]
        #或者 db = client.example
        return self.db

