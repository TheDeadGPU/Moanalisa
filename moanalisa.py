import RPi.GPIO as GPIO
import os
import subprocess

# Constants
BUTTON_PIN = 17
BUTTON_STATE = 0  # 0 = Not Pressed, 1 = Pressed

# GPIO Setup
GPIO.setwarnings(False)  # Ignore warnings
GPIO.setmode(GPIO.BCM)  # Use GPIO Numbering
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set the button pin to be an input pin and set initial value to be pulled low

# Function to play a sound file
def play_sound(file_path):
    process = subprocess.Popen(['mpg321', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        print("The command has finished successfully.")
    else:
        print(f"The command has finished with an error code: {process.returncode}")

def main():
    global BUTTON_STATE
    BUTTON_STATE = BUTTON_STATE

    while True:  # Run forever
        button_state = GPIO.input(BUTTON_PIN)
        if button_state == GPIO.HIGH and button_state != BUTTON_STATE:
            print("Button was pushed!")
            play_sound("Moaning.mp3")
            BUTTON_STATE = button_state

if __name__ == "__main__":
    main()
