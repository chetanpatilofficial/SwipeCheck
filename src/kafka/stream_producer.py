#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 02:42:30 2020

This class uses TransactionMessageGenerator and UserLocationMessageGenerator classes to produce transaction and user location streams
and write data to credit_card_transaction and user_location topic.

@author: Chetan Patil
"""

import sys
sys.path.insert(0, "/home/chetanspatil03/Insight-Data-Engineering/Credit-Card-Fraud-Detection-Project")
sys.path.insert(0, "/home/chetanspatil03/Insight-Data-Engineering/Credit-Card-Fraud-Detection-Project/src")


from confluent_kafka import Producer
from credit_card_transactions_generator import TransactionMessageGenerator
from user_locations_generator import UserLocationMessageGenerator
import application_config
from json import dumps

class StreamProducer:
    
    def __init__(self, credit_card_transaction_topic, user_location_topic):
        self.producer = Producer({'bootstrap.servers': application_config.KAFKA_SERVERS_DEV,
                                  'linger.ms': 1, 
                                  'batch.num.messages': 3000, 
                                  'queue.buffering.max.messages': 10000})
        self.credit_card_transaction_topic = credit_card_transaction_topic
        self.user_location_topic = user_location_topic
        self.credit_card_transactions_generator_obj = TransactionMessageGenerator()
        self.user_locations_generator_obj = UserLocationMessageGenerator()
    
    def produce_messages(self):
        
        while (True):
            
            if (self.credit_card_transactions_generator_obj is not None and self.user_locations_generator_obj is not None):
                
                # get transaction data
                transaction_message =  self.credit_card_transactions_generator_obj.load_transactions_data()
                
                # get user location data
                user_message = self.user_locations_generator_obj.load_user_location_data(transaction_message[application_config.TRANSACTION_MESSAGE_USER_ID],
                                                                                        transaction_message[application_config.TRANSACTION_MESSAGE_TRANSACTION_TIMESTAMP],
                                                                                        transaction_message[application_config.TRANSACTION_MESSAGE_TRANSACTION_MILLIS],
                                                                                        transaction_message[application_config.TRANSACTION_MESSAGE_TRANSACTION_LATITUDE],
                                                                                        transaction_message[application_config.TRANSACTION_MESSAGE_TRANSACTION_LONGITUDE])
                
                
                transaction_message = dumps(transaction_message)
                user_message = dumps(user_message)
                self.producer.produce(self.credit_card_transaction_topic, transaction_message.encode('utf-8'))
                self.producer.produce(self.user_location_topic, user_message.encode('utf-8'))
        
            self.producer.flush()

if __name__ == '__main__':
    stream_producer = StreamProducer(application_config.TRANSACTION_TOPIC_NAME, application_config.USER_TOPIC_NAME)
    stream_producer.produce_messages()
