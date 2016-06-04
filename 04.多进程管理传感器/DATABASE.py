#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import datetime

class mongodatabase():
    def __init__(self):
        pass

    def connect(self,host,port,dbname):
        self.host = host
        self.port = port
        self.client = pymongo.MongoClient(host=host,port=port)
        self.dbname = dbname
        self.db = None
    def get_db(self):
        # 建立连接
        db = self.client[self.dbname]
        #或者 db = client.example
        return db

