#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 02:42:30 2020

@author: Chetan Patil
"""

import psycopg2 as pg
import application_config
import random as random

class PostgresConnector:
    
    def __init__(self, hostname, port, dbname, dbusername, password):
        self.host_name = hostname
        self.port = port
        self.db_name = dbname
        self.db_user_name = dbusername
        self.password = password

    def save_data_datanodedb(self, combined_transaction_user_json):
        try:
            connection = pg.connect(host=self.host_name, 
                                    port=self.port, 
                                    database=self.db_name, 
                                    user=self.db_user_name, 
                                    password=self.password)
            cursor = connection.cursor()
            INSERT_STR = '''
                         INSERT INTO combined_transaction_location (tloc_user_id, uloc_user_id, merchant_id, 
                         t_time_stamp,t_millis, amount, tloc_latitude, tloc_longitude, u_time_stamp, u_millis, 
                         uloc_latitude, uloc_longitude, distance)
                         values('{}','{}','{}','{}',{},{},{},{},'{}',{},{},{},{})
                         '''
            
            tloc_user_id = combined_transaction_user_json[application_config.TLOC_MESSAGE_USER_ID]
            uloc_user_id = combined_transaction_user_json[application_config.ULOC_MESSAGE_USER_ID]
            merchant_id = combined_transaction_user_json[application_config.TLOC_MESSAGE_MERCHANT_ID]
            t_time_stamp = combined_transaction_user_json[application_config.TLOC_MESSAGE_TRANSACTION_TIME]
            t_millis = combined_transaction_user_json[application_config.TLOC_MESSAGE_TRANSACTION_MILLIS]
            amount = combined_transaction_user_json[application_config.TLOC_MESSAGE_AMOUNT]
            tloc_latitude = combined_transaction_user_json[application_config.TLOC_MESSAGE_TLOC_LATITUDE]
            tloc_longitude = combined_transaction_user_json[application_config.TLOC_MESSAGE_TLOC_LONGITUDE]
            uloc_time_stamp = combined_transaction_user_json[application_config.ULOC_MESSAGE_LOCATION_TIME]
            uloc_millis = combined_transaction_user_json[application_config.ULOC_MESSAGE_LOCATION_MILLIS]
            uloc_latitude = combined_transaction_user_json[application_config.ULOC_MESSAGE_ULOC_LATITUDE]
            uloc_longitude = combined_transaction_user_json[application_config.ULOC_MESSAGE_ULOC_LONGITUDE]
            distance = self.calculate_distance_thershold(combined_transaction_user_json)
            
            statement = INSERT_STR.format(tloc_user_id, 
                                          uloc_user_id, 
                                          merchant_id, 
                                          t_time_stamp,
                                          t_millis, 
                                          amount, 
                                          tloc_latitude, 
                                          tloc_longitude, 
                                          uloc_time_stamp, 
                                          uloc_millis, 
                                          uloc_latitude, 
                                          uloc_longitude, 
                                          distance)
            cursor.execute(statement)
            connection.commit()
        except pg.DatabaseError as error:
            print(error)
        except KeyboardInterrupt:
            print('You cancelled the operation.')
        except:
            print("PostgresConnector : Exception Occurred")
        finally:
            if connection is not None:
                connection.close()

    # This is the place where a data science model could implement more complex logic to calculate distance thershold
    def calculate_distance_thershold(self, combined_transaction_user_json):
        
        distance = float(combined_transaction_user_json[application_config.DISTANCE])

        if distance == 0.0:
            distance = random.uniform(0,8)
        elif distance > 100.0:
            distance = random.uniform(9,200)
        
        return distance
    