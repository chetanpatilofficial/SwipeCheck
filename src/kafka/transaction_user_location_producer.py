#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 02:42:30 2020

@author: chetan patil
"""

from datetime import datetime
from faker import Faker
import random as random
from confluent_kafka import Producer
import time

class MessageProducer:
    
    fake = Faker()
    producer = Producer({'bootstrap.servers': 'localhost:9092'})
    
    def __init__(self, user_location_topic, transaction_topic):
        self.user_location_topic = user_location_topic
        self.transaction_topic = transaction_topic
    
    def get_timestamp(self):
        time = datetime.now()
        time = time.strftime('%Y-%m-%d %H:%M:%S.%f')
        return time
    
    def delivery_report(self, err, msg):
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
    
    def produce_messages(self):
        i = 0;
        while (True):
            i = i + 1
            # Generate Transaction Data.
            merchant_id = 'M' + str(random.randint(10000, 50000))
            user_id = 'U' + str(random.randint(1000000, 5000000))
            t_time_stamp = str(self.get_timestamp())
            t_millis = "%.3d" % (time.time() % 1 * 1000)
            amount =  str(round(random.uniform(1, 1000), 2))
            fake = Faker()
            t_latitude = str(fake.latitude())
            t_longitude = str(fake.longitude())
            transaction_message = ','.join((merchant_id, user_id, t_time_stamp,t_millis, amount, t_latitude, t_longitude))
            MessageProducer.producer.produce(self.transaction_topic, transaction_message.encode('utf-8'), callback=self.delivery_report)
            
            # Generate matching user location with probabilty greater than 0.015
            probability = random.uniform(0,1)
            if probability > 0.015:
                user_location_data = ','.join((user_id, t_time_stamp, t_millis, t_latitude, t_longitude))
                MessageProducer.producer.produce(self.user_location_topic, user_location_data.encode('utf-8'), callback=self.delivery_report)
            else:
                fraud_latitude = str(fake.latitude())
                fraud_longitude = str(fake.longitude())
                
                user_location_data = ','.join((user_id, t_time_stamp, t_millis, fraud_latitude, fraud_longitude))
                MessageProducer.producer.produce(self.user_location_topic, user_location_data.encode('utf-8'), callback=self.delivery_report)

        MessageProducer.producer.flush()


if __name__ == '__main__':
    prod = MessageProducer('location01', 'transaction01')
    prod.produce_messages()
