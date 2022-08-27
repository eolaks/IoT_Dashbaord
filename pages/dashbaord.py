# -*- coding: utf-8 -*-
"""

Created on Thu Dec  10 11:48:45 2021
#   - Code for dashbaord for the oil and gas pipeline parameters
@author: User
"""

import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

import pandas as pd
from datetime import datetime as dt
import plotly.express as px
import dash_daq as daq
import random

from urllib.request import urlopen
import json

import mysql.connector
from mysql.connector import Error


# read data from api 
def read_api():
    # Get the dataset
    #url = 'https://wireless.uir.ac.id/admin/monitoring/get_oil_pump'
    url = 'https://wireless.uir.ac.id/api/get_oil_pump'
    response = urlopen(url)
    # Convert bytes to string type and string type to dict
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    return json_obj


#Create a class to handle data 
class mydata:
    def __init__(self, json_obj):
        
        self.status = json_obj["oil_pump"]['sensorStatus']
        self.date = json_obj["oil_pump"]['value'][0]['date'] # 
        self.temperature_in = json_obj["oil_pump"]['value'][0]['temperature_in']
        self.temperature_out = json_obj["oil_pump"]['value'][0]['temperature_out']
        self.pressure_in = json_obj["oil_pump"]['value'][0]['pressure_in']
        self.pressure_out = json_obj["oil_pump"]['value'][0]['pressure_out']
        self.flow_in = json_obj["oil_pump"]['value'][0]['flow_in']
        self.flow_out = json_obj["oil_pump"]['value'][0]['flow_out']
        
    def get_temp_in(self):
        return self.temperature_in 
    
    def get_temp_out(self):
        return self.temperature_out
    
    def get_pressure_in(self):
        return self.pressure_in
    
    def get_pressure_out(self):
        return self.pressure_out
    
    def get_flow_in(self):
        return self.flow_in
    def get_flow_out(self):
        return self.flow_out
    def get_date(self):
        return self.date

#create a function to connect to database
def connect():
    json_obj =read_api()    
    a = mydata(json_obj)
    record = (a.get_date(),a.get_temp_in(), a.get_temp_out(), a.get_pressure_in(), a.get_flow_in(), a.get_flow_out())
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='mydb',
                                       user='root',
                                       password='abcd1234')
        if conn.is_connected():
            print('Connected to MySQL database')
# prepare a cursor object using cursor() method
            cursor = conn.cursor()
# execute SQL query using execute() method.
            cursor.execute("SELECT VERSION()")
            data = cursor.fetchone()
            print ("Database version : %s " % data)

            
# Prepare SQL query to INSERT a record into the database.
            sql = """INSERT INTO STATION_1(DATE,TEMPERATURE_IN, TEMPERATURE_OUT, PRESSURE,
                        FLOWRATE, SALINITY)
                     VALUES (%s, %s, %s, %s, %s, %s )"""

            cursor.execute(sql, record)
            
# Commit your changes in the database
            conn.commit()
            
    except Error as e:
        print(e)
    # Rollback in case there is any error
        conn.rollback()
    finally:
# disconnect from database
        conn.close()


dash.register_page(__name__, name='Dashboard')



# Create Page Layout
layout = html.Div(
    [
         dcc.Interval(
             id ='interval-component',
             interval= 60*1000, #milliseconds  -> 60 seconds
             n_intervals=0),
      # First row   
        dbc.Row([
            # First Row, col one 
            dbc.Col([
                daq.Gauge(
                size = 120,
                showCurrentValue=True,
                id='my-gauge-1',
                color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,100]}},
                label="Temperature-in",
                max=100,
                min=0,
                value=0)
                
                ]),
            # First Row, col two 
            dbc.Col([
                daq.Gauge(
                    size = 120,
                    showCurrentValue=True,
                    id='my-gauge-2',
                    color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,100]}},
                    label="Temperature-out",
                    max=100,
                    min=0,
                    value=0)
                
                ]),
            # First Row, col three 
            dbc.Col([
                daq.Gauge(
                    size = 120,
                    showCurrentValue=True,
                    id='my-gauge-3',
                    color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,100]}},
                    label="Flowrate",
                    max=100,
                    min=0,
                    value=0)
                
                ]),
            # FIrst Row, col four
            dbc.Col([
                daq.Gauge(
                    size = 120,
                    showCurrentValue=True,
                    id='my-gauge-4',
                    color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,100]}},
                    label="Pressure",
                    max=100,
                    min=0,
                    value=0)
                
                ]),
            # First Row, col five 
            dbc.Col([
                daq.Gauge(
                    size = 120,
                    showCurrentValue=True,
                    id='my-gauge-5',
                    color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,100]}},
                    label="Salinity",
                    max=100,
                    min=0,
                    value=0)
                
                ])
         
            ]),
   
    ]
)

@callback(
    Output('my-gauge-1', 'value'),
    Output('my-gauge-2', 'value'),
    [Input('interval-component', 'n_intervals')]
)

def update_gauge(n_intervals):
    json_obj =read_api()    
    a = mydata(json_obj)
    value = (a.get_temp_in())
    value1 = (a.get_temp_out())
    value  = float(value)
    value1 = float(value1)
    print(value)
    # save to database
    #connect()
    return value, value1


