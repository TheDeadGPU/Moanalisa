import RPi.GPIO as GPIO
import os
import subprocess
import time
from pathlib import Path

# Constants
PHOTORESISTOR_PIN = 26
TRIGGER_STATE = 0  # 0 = Not Triggered, 1 = Triggered

# GPIO Setup
GPIO.setwarnings(False)  # Ignore warnings
GPIO.setmode(GPIO.BCM)  # Use GPIO Numbering

# Function to play a sound file
def play_sound(file_path):
    global TRIGGER_STATE
    TRIGGER_STATE = TRIGGER_STATE
    process = subprocess.Popen(['mpg321', file_path])
    process.wait()
    if process.returncode == 0:
        print("The command has finished successfully.")
    else:
        print(f"The command has finished with an error code: {process.returncode}")
    TRIGGER_STATE = 0
    

def main():
    global TRIGGER_STATE
    TRIGGER_STATE = TRIGGER_STATE
    global PHOTORESISTOR_PIN
    PHOTORESISTOR_PIN = PHOTORESISTOR_PIN
    print(Path.cwd())

    while True:  # Run forever
        #Compute the amout of time it takes our 1 uF capacitor to charge through the photo resistor
        GPIO.setup(PHOTORESISTOR_PIN, GPIO.OUT)
        GPIO.output(PHOTORESISTOR_PIN, GPIO.LOW)
        time.sleep(0.1)
        GPIO.setup(PHOTORESISTOR_PIN, GPIO.IN)
        currentTime = time.time()
        differenceTime = 0

        while(GPIO.input(PHOTORESISTOR_PIN) == GPIO.LOW):
            differenceTime = (time.time() - currentTime) * 1000
        if(differenceTime < 10 and TRIGGER_STATE !=  1):
            print("MOANING!")
            play_sound((Path.cwd() + "/Moaning.mp3"))
            TRIGGER_STATE = 1

if __name__ == "__main__":
    main()
