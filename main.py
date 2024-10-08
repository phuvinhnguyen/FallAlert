from time import time, sleep
import threading
from alarm import *
from gyroscope import *
from temperature import *
from alarm import *
from gyroscope import *
from temperature import *

def monitor_fall():

    while True:
        status=monitor_loop()
        if status=='alarm':
            monitor_temperature()
        time.sleep(1)

if __name__ == "__main__":
    

    monitor_fall()
    # Start the fall and temperature monitoring in separate threads

  #  fall_thread = threading.Thread(target=monitor_fall)
   # temp_thread = threading.Thread(target=monitor_temperature)

    #fall_thread.start()
   # temp_thread.start()

    #fall_thread.join()
    #temp_thread.join()

    sleep(1)
