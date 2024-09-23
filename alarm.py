'''
Alarm mechanism

The following functions are required to be implemented:

1. play_sound() - To be implemented: Play a sound alarm
2. trigger_light() - To be implemented: Trigger light as an alert

Those functions will be called by the main program (FallAlert/main.py) and other functions
'''

def play_sound():
    # To be implemented: Play a sound alarm
    pass

def trigger_light():
    # To be implemented: Trigger light as an alert
    pass

def alert_protocol() -> None:
    # Function to handle alert mechanism (play sound, trigger light, etc.)
    print("Alert triggered!")
    play_sound()
    trigger_light()