'''
Temperature sensor monitoring

This module implements the protocol to detect high temperature and send help signal

The following functions are required to be implemented:

1. read_temperature() - To be implemented: Read temperature sensor data
   - This function return temperature sensor data (integer value)
   - Use Celsius unit
'''

from time import time
from .alarm import *

def read_temperature() -> int:
    # To be implemented: Read temperature sensor data
    pass

def monitor_temperature():
    while True:
        temp_data = read_temperature()

        if temp_data > 50:
            print("High temperature detected!")
            time.sleep(30)
            alert_protocol()
            break
        
        time.sleep(120)