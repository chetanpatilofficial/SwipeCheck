#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 03:11:00 2020

@author: chetan patil
"""

from confluent_kafka import Consumer, KafkaException
from datetime import datetime
import psycopg2 as pg
import logging
import random as random
import sys

class MessageConsumer:
    
    def consume_messages(self):
        try:
            consumer = Consumer({
                            'bootstrap.servers': 'localhost:9092',
                            'group.id': 'mygroup',
                            'auto.offset.reset': 'earliest'
                            })

            consumer.subscribe(['COMBINED_TRANSACTION_LOCATION'])
            
            
            while True:
                msg = consumer.poll(1.0)
                
                 # Create logger for consumer (logs will be emitted when poll() is called)
                logger = logging.getLogger('consumer')
                logger.setLevel(logging.DEBUG)
                handler = logging.StreamHandler()
                handler.setFormatter(logging.Formatter('%(asctime)-15s %(levelname)-8s %(message)s'))
                logger.addHandler(handler)
            
                if msg is None:
                    continue
                if msg.error():
                    print("Consumer error: {}".format(msg.error()))
                    print('Received message: {}'.format(msg.value().decode('utf-8')))
                else:
                    #record_value = msg.value().decode('utf-8')
                    #data = json.loads(record_value)
                    print('Received message: {}'.format(msg.value().decode('utf-8')))
                    combined_transaction_user_values = msg.value().decode('utf-8').split(",")
                    tloc_user_id = combined_transaction_user_values[0]
                    uloc_user_id = combined_transaction_user_values[1]
                    merchant_id = combined_transaction_user_values[2]
                    t_time_stamp = combined_transaction_user_values[3]
                    t_millis = combined_transaction_user_values[4]
                    amount = combined_transaction_user_values[5]
                    tloc_latitude = combined_transaction_user_values[6]
                    tloc_longitude = combined_transaction_user_values[7]
                    uloc_time_stamp = combined_transaction_user_values[8]
                    uloc_millis = combined_transaction_user_values[9]
                    uloc_latitude = combined_transaction_user_values[10]
                    uloc_longitude = combined_transaction_user_values[11]
                    distance = float(combined_transaction_user_values[12])
                    
                    
                    if distance == 0.0:
                        distance = random.uniform(2,8)
                    elif distance > 100.0:
                        distance = random.uniform(9,100)
                 
                    
                    conn = pg.connect(host="localhost", port="5432", database="datanodedb", user="datanode", password="password")
                    cursor = conn.cursor()
                    INSERT_STR = '''
                                 INSERT INTO COMBINED_TRANSACTION_LOCATION (tloc_user_id, uloc_user_id, merchant_id, 
                                 t_time_stamp,t_millis, amount, tloc_latitude, tloc_longitude, u_time_stamp, u_millis, 
                                 uloc_latitude, uloc_longitude, distance)
                                 values('{}','{}','{}','{}',{},{},{},{},'{}',{},{},{},{})'''
                    #combined_transaction_user_values = "U2394832,U2394832,M42438,2020-06-20 23:55:48,748,738.33,78.37343,111.282718,2020-06-20 23:55:48,748,78.37343,111.282718,0.0".split(",")
    
                    statement = INSERT_STR.format(tloc_user_id, uloc_user_id, merchant_id, t_time_stamp,
                                                  t_millis, amount, tloc_latitude, tloc_longitude,
                                                  uloc_time_stamp, uloc_millis, uloc_latitude, uloc_longitude,
                                                  distance)
                    cursor.execute(statement)
                    conn.commit()
        except KeyboardInterrupt:
            sys.stderr.write('%% Aborted by user\n')
        finally:
            # Leave group and commit final offsets
            consumer.close()

if __name__ == '__main__':
    cons = MessageConsumer()
    cons.consume_messages()
