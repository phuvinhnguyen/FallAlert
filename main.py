import time
import threading
from .alarm import *
from .gyroscope import *
from .temperature import *

def monitor_fall():
    '''
    This function implements the protocol to detect fall and send help signal
    '''
    fall_detected = False
    start_time = None

    while True:
        gyro_data = read_gyroscope()
        
        if fall_detected and start_time:
            elapsed_time = time.time() - start_time
            if elapsed_time > 90:
                alert_protocol()
                break
        elif check_fall_condition(gyro_data):
            fall_detected = True
            start_time = time.time()
            print("Fall detected, starting timer.")

        time.sleep(1)

if __name__ == "__main__":
    # Start the fall and temperature monitoring in separate threads
    while True:
        fall_thread = threading.Thread(target=monitor_fall)
        temp_thread = threading.Thread(target=monitor_temperature)

        fall_thread.start()
        temp_thread.start()

        fall_thread.join()
        temp_thread.join()

        time.sleep(30)
