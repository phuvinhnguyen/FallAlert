from time import time
from .alarm import *

def read_temperature():
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
        
        time.sleep(1)