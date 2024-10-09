import time
from sense_hat import SenseHat
import math

# Initialize Sense HAT
sense = SenseHat()

# Thresholds for detecting a fall
GYRO_THRESHOLD = 100  # Angular velocity threshold (degrees per second)
ACC_THRESHOLD = 0.2   # Linear acceleration threshold (g-force)
ACC_LOW_THRESHOLD = 0.2  # Low acceleration after fall (impact)
GYRO_NO_MOVEMENT_THRESHOLD = 10  # Angular velocity threshold for no movement

# Time to wait after impact to detect no movement (seconds)
INACTIVITY_TIME = 15  

def read_gyroscope():
    """Reads gyroscope data (angular velocity) from the Sense HAT."""
    gyro = sense.get_gyroscope_raw()  # returns dict with x, y, z angular velocity
    x = gyro['x']
    y = gyro['y']
    z = gyro['z']
    return x, y, z

def read_accelerometer():
    """Reads accelerometer data (linear acceleration) from the Sense HAT."""
    acc = sense.get_accelerometer_raw()  # returns dict with x, y, z acceleration
    x = acc['x']
    y = acc['y']
    z = acc['z']
    # Calculate the magnitude of the acceleration vector
    magnitude = math.sqrt(x**2 + y**2 + z**2)
    return magnitude

def detect_fall(x_gyro, y_gyro, z_gyro, acc_magnitude):
    """Detects a fall based on gyroscope and accelerometer data."""
    # Check if any angular velocity exceeds the gyroscope threshold
    gyro_fall = abs(x_gyro) > GYRO_THRESHOLD or abs(y_gyro) > GYRO_THRESHOLD or abs(z_gyro) > GYRO_THRESHOLD
    
    # Check if acceleration exceeds the fall threshold
    acc_fall = acc_magnitude > ACC_THRESHOLD
    
    # Check for low acceleration after fall (impact)
    acc_low = acc_magnitude < ACC_LOW_THRESHOLD
    
    # Return True if a fall is detected
    if gyro_fall and acc_fall:
        return True  # Fall detected
    
    # Return 'impact' if low acceleration (impact) is detected
    if acc_low:
        return "impact"
    
    # Return False if no fall or impact is detected
    return False

def check_for_movement():
    """Checks for any movement using the gyroscope for 15 seconds."""
    start_time = time.time()
    while time.time() - start_time < INACTIVITY_TIME:
        # Read gyroscope data
        x_gyro, y_gyro, z_gyro = read_gyroscope()
        
        # If any movement is detected, return False (no alarm)
        if abs(x_gyro) > GYRO_NO_MOVEMENT_THRESHOLD or abs(y_gyro) > GYRO_NO_MOVEMENT_THRESHOLD or abs(z_gyro) > GYRO_NO_MOVEMENT_THRESHOLD:
            return False
        
        # Sleep for a short time before checking again
        time.sleep(0.1)
    
    # If no movement detected within the time limit, return 'alarm'
    return 'alarm'

def monitor_loop():
    """Main loop to monitor for falls and return flags."""
    # Read gyroscope and accelerometer data
    x_gyro, y_gyro, z_gyro = read_gyroscope()
    acc_magnitude = read_accelerometer()
    
    # Detect fall and return the status flag
    fall_status = detect_fall(x_gyro, y_gyro, z_gyro, acc_magnitude)
    
    if fall_status == True or fall_status == "impact":
        # If a fall or impact is detected, wait to see if there's no movement
        movement_status = check_for_movement()
        if movement_status == 'alarm':
            return 'alarm'
    
    return fall_status

def handle_fall_status(fall_status):
    """Handle the fall status based on the flag."""
    if fall_status == True:
        # Handle the detected fall (e.g., send alert)
        print("Fall detected! Handle accordingly.")
    elif fall_status == "impact":
        # Handle the impact event after fall
        print("Impact detected! Handle accordingly.")
    elif fall_status == "alarm":
        # Handle no movement after impact (trigger alarm)
        print("No movement detected for 15 seconds! Trigger alarm.")
    else:
        # No fall detected, normal operation
        print("No fall detected.")

if __name__ == "__main__":
    while True:
        print(monitor_loop())
        time.sleep(0.5)
        