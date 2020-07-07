#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 02:42:30 2020

This class generates credit card transaction data i.e merchant_id, user_id, transaction_ts, u_time_stamp, transaction_millis, 
amount, transaction_latitude, transaction_longitude.

@author: Chetan Patil
"""


from datetime import datetime
from confluent_kafka import Producer
from faker import Faker
from json import dumps
import random as random
import time
import application_config

class TransactionMessageGenerator:
    
    def __init__(self):
        self.fake = Faker()
        self.merchant_id = ''
        self.user_id = ''
        self.t_time_stamp = ''
        self.t_millis = ''
        self.amount = ''
        self.t_latitude = ''
        self.t_longitude = ''
    
    def create_transaction_msg(self, merchant_id, user_id, transaction_ts, transaction_millis, amount, transaction_latitude, transaction_longitude):
        """
        Args:
            merchant_id: string, 
            user_id: string, 
            transaction_ts:string,
            transaction_millis:string, 
            amount:string, 
            transaction_latitude:string, 
            transaction_longitude:string
        :rtype: dict
        """
        
        transaction_msg = {}
        transaction_msg[application_config.TRANSACTION_MESSAGE_MERCHANT_ID] = merchant_id
        transaction_msg[application_config.TRANSACTION_MESSAGE_USER_ID] = user_id
        transaction_msg[application_config.TRANSACTION_MESSAGE_TRANSACTION_TIMESTAMP] = transaction_ts
        transaction_msg[application_config.TRANSACTION_MESSAGE_TRANSACTION_MILLIS] = transaction_millis
        transaction_msg[application_config.TRANSACTION_MESSAGE_TRANSACTION_AMOUNT] = amount
        transaction_msg[application_config.TRANSACTION_MESSAGE_TRANSACTION_LATITUDE] = transaction_latitude
        transaction_msg[application_config.TRANSACTION_MESSAGE_TRANSACTION_LONGITUDE] = transaction_longitude
        return transaction_msg
    
    def get_current_timestamp(self):
        curr_time = datetime.now()
        curr_time = curr_time.strftime('%Y-%m-%d %H:%M:%S.%f')
        return curr_time
    
    def load_transactions_data(self):
        self.merchant_id = 'M' + str(random.randint(10000, 50000))
        self.user_id = 'U' + str(random.randint(1000000, 5000000))
        self.t_time_stamp = str(self.get_current_timestamp())
        self.t_millis = "%.3d" % (time.time() % 1 * 1000)
        self.amount =  str(round(random.uniform(1, 1000), 2))
        self.t_latitude = str(self.fake.latitude())
        self.t_longitude = str(self.fake.longitude())
        msg = self.create_transaction_msg(self.merchant_id, self.user_id, self.t_time_stamp, self.t_millis, 
                                                self.amount, self.t_latitude, self.t_longitude)
        return msg
