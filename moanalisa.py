import RPi.GPIO as GPIO
import os
import subprocess

# Variables
inputButtonPin = 17
lastButtonState = 0  # 0 = Not Pressed, 1 = Pressed

# GPIO Setup
GPIO.setwarnings(False)  # Ignore warnings
GPIO.setmode(GPIO.BCM)  # Use GPIO Numbering
GPIO.setup(inputButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set the button pin to be an input pin and set initial value to be pulled low

# Function that plays the moaning sound
def play_sound(file_path):
    # Run the command in the background
    process = subprocess.Popen(['mpg321', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for the process to finish
    process.wait()

    # Check if the process has finished
    if process.returncode == 0:
        print("The command has finished successfully.")
    else:
        print(f"The command has finished with an error code: {process.returncode}")

def main():
    global lastButtonState  # Declare lastButtonState as global
    while True:  # Run forever
        buttonState = GPIO.input(inputButtonPin)
        if buttonState == GPIO.HIGH and buttonState != lastButtonState:
            print("Button was pushed!")
            play_sound("Moaning.mp3")
            lastButtonState = buttonState

if __name__ == "__main__":
    main()
