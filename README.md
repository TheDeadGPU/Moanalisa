# Moanalisa
## _The stupidest project I've ever come up with, Ever_

Moanalisa is a Python application that runs on the Raspberry Pi and gives the device the ability to moan in the presense of light.

## Installation
Pull down the repository and run the ScriptInstall.sh file. This install script will set up a service that runs on login of the Pi user and check for the presense of light that will trigger the play of the Moaning.mp3 file.

```sh
./ScriptInstall.sh
```

## Hardware Setup
In order to make this project work, you need to create a photo resistor circuit that will interact with the Moanalisa program. Below are th required materials.

#### Materials
- RPi (With USB)
- Speaker or Sounds Bar (USB)
- Perf Board or Breadboard
- 3 Female to Male Pin Jumper Wires
- Photo Resistor
- 1uF Capacitor


## Assembling the Circuit
![image](https://github.com/TheDeadGPU/Moanalisa/assets/12623002/781ef8ce-68c4-4a12-a162-c9e7725c1dac)



1. Connect a red positive wire to the 3.3V rail on the RPi and attach the other side of the wire to the positive terminal of the photoresistor.
2. Connect the negative side of the photoresistor to the positive side of the 1uF capacitor.
3. Connect the Green GPIO wire to the positive side of the capacitor and connect the other side to GPIO Pin 26.
4. Connect the ground wire to the negative side of the capacitor and the other side to the ground GPIO pin.
5. Done

## Testing Moanalisa
To run the program and test your photoresistor circuit, do the following.
1. Clone the Git repo.
2. Navigate to the local copy of the Git repo.
3. Run the following
``` sh
python Moanalisa.py
```
