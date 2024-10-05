from time import time
from alarm import *
from sense_hat import SenseHat
from time import sleep

"""
Temperature sensor monitoring

This module implements the protocol to detect high temperature and send help signal.
The following functions are required to be implemented:

   - read_temperature() - Read temperature sensor data
   - This function returns temperature sensor data (integer value).
   - Use Celsius unit.
"""

def read_temperature():
    """
    Read temperature sensor data from the Sense HAT sensor.
    Return an integer value representing the temperature in Celsius.
    """
    sense = SenseHat()
    sense.clear()

    # Get the temperature in Celsius
    temp = sense.get_temperature()
    print("Current temperature: °C")
    
    # Return the temperature as an integer
    return int(temp)

def monitor_temperature():
    """
    Monitor the temperature from the sensor and trigger alert if temperature exceeds 
    26°C for more than 3 minutes.
    """
    high_temp_threshold = 40  # temperature threshold in Celsius
    delay_duration = 0  # 3 minutes in seconds
    consecutive_time = 0  # how long the temperature stays above the threshold
    check_interval = 5  # check every 5 seconds

    while True:
        temp_data = read_temperature()

        if temp_data > high_temp_threshold:
            consecutive_time += check_interval
            print("High temperature detected: " + str(temp_data) + "°C for "+ str(consecutive_time) + " seconds")

            if consecutive_time >= delay_duration:
               #TODO: If the gyroscope and accelerometer readings go back to normal, do not trigger the alarm_protocol
                alert_protocol()
                break  # Exit the loop after triggering the alert
        else:
            # Reset if temperature drops below the threshold
            print("Temperature dropped to " + str(temp_data) + "°C. Resetting timer.")
            consecutive_time = 0

        sleep(check_interval)
