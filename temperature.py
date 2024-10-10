from time import time
from alarm import *
from sense_hat import SenseHat
from time import sleep
from alarm import *
from gyroscope import *

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
    the high temperature threshold or if the temperature is high for a long period without movement.
    
    - If temperature exceeds 40°C, an alert is triggered immediately.
    - If temperature is above 26°C for more than the delay duration without movement, an alert is triggered.
    - If movement is detected, the alarm is prevented.
    """
    high_temp_threshold = 40  # Immediate alert if temperature exceeds 40°C
    delay_duration = 5  # Monitor for 15 seconds before triggering an alert if there's no movement
    consecutive_time = 0  # Time for which the temperature remains above the threshold
    check_interval = 1  # Check every 5 seconds
    flag_movement = 0  # A flag to track if no movement is detected

    while True:
        temp_data = read_temperature()
        
        # If the temperature is below the high threshold, monitor for movement
        if temp_data < high_temp_threshold:
            consecutive_time += check_interval
            print("No movement detected. Temp: " + str(temp_data) + "°C for " + str(consecutive_time) + " seconds.")
            
            if monitor_loop() == True or check_for_movement() == 'alarm' or monitor_loop() == 'impact': #Function returns alarm if no movement is detected
               print("alarm rings") 
               flag_movement += 1  # Increase the flag count if no movement is detected
            else:
                print("No alarm")
                flag_movement = 0  # Reset the flag if movement is detected
            
            # Check if the temperature has been high for the entire duration without movement
            if consecutive_time >= delay_duration:
                if flag_movement >= delay_duration / check_interval:
                    print("Temperature below threshold but no movement detected for the duration. Triggering alert.")
                    alert_protocol()  # Trigger alert when no movement for the set duration
                    break  # Exit the loop after triggering the alert
        else:
            # If temperature exceeds the high threshold, immediately trigger the alert
            print("High temperature detected: " + str(temp_data) + "°C. Triggering alert immediately.")
            alert_protocol()
            consecutive_time = 0
            break

        sleep(check_interval)  # Wait before the next check

if __name__ == "__main__":
    monitor_temperature()
