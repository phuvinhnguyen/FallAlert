import time
import smtplib
from sense_hat import SenseHat
from email.mime.text import MIMEText

'''
Alarm mechanism

1. play_sound() - To be implemented: Play a sound alarm
2. trigger_light() - To be implemented: Trigger light as an alert

Those functions will be called by the sensors
'''

# Flag to control alert state
alert_active = True

sense = SenseHat()

# Email credentials and configuration
SENDER_EMAIL = "fallalertacs@gmail.com"
SENDER_PASSWORD = "zjzl imww qrcq tuax"  # App password generated from Gmail
RECEIVER_EMAIL = "prakhar.d9@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# def play_sound():
#     # To be implemented: Play a sound alarm
#     pass

def send_email():
    try:
        # Set up the server connection
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        # Create the email content
        subject = "Fall Alert"
        body = "A fall has been detected! Please check up on your patient immediately."
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        
        # Send the email
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print(f"Alert email sent to {RECEIVER_EMAIL}")
        
        # Close the server connection
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

def trigger_led():
    global alert_active
    red = [255, 0, 0]
    
    # send an email when the alert is active
    send_email()  

    # Flash the LED matrix until alert is deactivated by joystick press
    while alert_active:
        sense.clear(red)
        time.sleep(0.5)
        sense.clear()  # Turn off the LEDs
        time.sleep(0.5)

    sense.clear()  # Clear the matrix when alert is deactivated

def joystick_event(event):
    global alert_active
    if event.action == 'pressed':  # When joystick is pressed
        print("Joystick pressed, stopping alert...")
        alert_active = False  # Set the alert_active flag to False to stop the alert


# def alert_protocol() -> None:
#     # Function to handle alert mechanism (play sound, trigger light, etc.)
#     print("Alert triggered!")
#     # play_sound() # 
#     trigger_light()


if __name__ == "__main__":
    # Register joystick event listener
    sense.stick.direction_any = joystick_event
    
    try:
        # Start the LED alert
        trigger_led()
    except KeyboardInterrupt:
        pass
    finally:
        # Clean up the LED display after stopping
        sense.clear()