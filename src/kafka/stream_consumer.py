#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 02:42:30 2020

@author: chetanspatil03
"""

from confluent_kafka import Consumer, KafkaException
from datetime import datetime
import psycopg2 as pg
import sys
import json
import psycopg2 as pg
import application_config
import postgres_connector

class StreamConsumer:
    
    def __init__(self, combined_transaction_user_location_topic, postgres_connector_obj):
        self.combined_transaction_user_location_topic = combined_transaction_user_location_topic
        self.postgres_connector_obj = postgres_connector_obj
        
    def consume_messages(self):
        try:
            consumer = Consumer({
                            'bootstrap.servers': application_config.KAFKA_SERVERS_DEV,
                            'group.id': application_config.MY_CONSUMER_GROUP,
                            'auto.offset.reset': application_config.CONSUMER_OFFSET_RESET_EARLIEST,
                            'fetch.min.bytes' : 100000,
                            'enable.auto.commit' : True
                            })

            consumer.subscribe(self.combined_transaction_user_location_topic)
            
            while True:
                msg = consumer.poll(1.0)
            
                if msg is None:
                    continue
                if msg.error():
                    print("Consumer error: {}".format(msg.error()))
                    print('Received message: {}'.format(msg.value().decode('utf-8')))
                else:
                    combined_transaction_user_values = msg.value().decode('utf-8')
                    combined_transaction_user_json = json.loads(combined_transaction_user_values)
                    self.postgres_connector_obj.save_data_datanodedb(combined_transaction_user_json)
                    
        except KeyboardInterrupt:
            print('You cancelled the operation.')
        except KafkaException as kafka_error:
            print('StreamConsumer : KafkaException :: \n', kafka_error)
        except:
            sys.stderr.write("StreamConsumer : Exception Occurred \n")
        finally:
            # Leave group and commit final offsets
            consumer.close()

if __name__ == '__main__':
    postgres_connector = postgres_connector.PostgresConnector("localhost", "5432", "datanodedb", "datanode", "password")
    stream_consumer = StreamConsumer([application_config.COMBINED_TRANSACTION_USER_LOCATION_TOPIC_NAME], postgres_connector)
    stream_consumer.consume_messages()
