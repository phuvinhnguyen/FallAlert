import time
import threading
from alarm import *
from gyroscope import *
from temperature import *

def monitor_fall():

    while True:
        monitor_loop()
        time.sleep(3)

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
