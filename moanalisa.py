import RPi.GPIO as GPIO # Import Raspberry Pi GPIO Library
import os

#Variables
inputButtonPin = 17
lastButtonState = 0 # 0 = Not Pressed 1 = Pressed

#GPIO Setup
GPIO.setwarnings(False) # Ignore warnings
GPIO.setmode(GPIO.BCM) # Use GPIO Numbering
GPIO.setup(inputButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Set the button pin to be an input pin and set initial value to be pulled low

#Program Loop
while True: # Run forever
    buttonState = GPIO.input(inputButtonPin)
    if(buttonState == GPIO.HIGH) and (buttonState != lastButtonState):
        print("Button was pushed!")
        os.system("mpg321 Moaning.mp3 &")