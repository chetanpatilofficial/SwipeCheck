#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 02:42:30 2020

This class generates user location data i.e user_id, u_time_stamp, u_millis, u_latitude, u_longitude.

@author: Chetan Patil
"""

from datetime import datetime
from faker import Faker
import random as random
import application_config

class UserLocationMessageGenerator:
    
    def __init__(self):
        
        self.fake = Faker()
        self.user_id = ''
        self.u_time_stamp = ''
        self.u_millis = ''
        self.u_latitude = ''
        self.u_longitude = ''
    
    def create_user_location_msg(self, user_id, u_time_stamp, u_millis, u_latitude, u_longitude):
        """
        Args:
            user_id: string, 
            u_time_stamp: string, 
            u_millis:string,
            u_latitude:string, 
            u_longitude:string
        :rtype: dict
        """
        
        user_location_msg = {}
        user_location_msg[application_config.USER_LOCATION_MESSAGE_USER_ID] = user_id
        user_location_msg[application_config.USER_LOCATION_MESSAGE_TIMESTAMP] = u_time_stamp
        user_location_msg[application_config.USER_LOCATION_MESSAGE_MILLIS] = u_millis
        user_location_msg[application_config.USER_LOCATION_MESSAGE_LATITUDE] = u_latitude
        user_location_msg[application_config.USER_LOCATION_MESSAGE_LONGITUDE] = u_longitude
        return user_location_msg
    
    def get_current_timestamp(self):
        curr_time = datetime.now()
        curr_time = curr_time.strftime('%Y-%m-%d %H:%M:%S.%f')
        return curr_time
    
    def load_user_location_data(self, t_user_id, t_timestamp, t_millis, t_latitude, t_longitude):
        
        self.user_id = t_user_id
        self.u_time_stamp = t_timestamp
        self.u_millis = t_millis
        
        # Generate matching user location with probabilty greater than 0.015
        probability = random.uniform(0,1)
        if probability > 0.015:
            
            self.u_latitude = t_latitude
            self.u_longitude = t_longitude
            msg = self.create_user_location_msg(self.user_id, self.u_time_stamp, self.u_millis, self.u_latitude, 
                                                self.u_longitude)
        else:
            
            self.fake_latitude = str(self.fake.latitude())
            self.fake_longitude = str(self.fake.longitude())
            
            msg = self.create_user_location_msg(self.user_id, self.u_time_stamp, self.u_millis, self.fake_latitude, 
                                                self.fake_longitude)
        
        return msg
