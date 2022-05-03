# FinalProject
Andrew_Degan_Final

Items needed
- 1 Rasberry Pi
- 1 Breadboard
- 2 220 Ohm resistors
- 1 330 resistor
- 1 470 resistor
- 1 Green LED
- 1 Red LED
- 1 Ultra-Sonic Distance Sensor (HC-SR04)
- 6 Male-to-Female Jumper wires
- 3 Male-to-Male Jumper wires

  The purpose of this device is to create a motion sensor that logs every time it is triggered in '/home/$USER'. 
Each time the motion sensor is triggered, a red LED will light up.
When there is nothing in the trigger range of the motion sensor a green LED will be lit.
 
  When I set out to make this device, the intended use case was to set up the device in a doorway of a room and log everytime the the sensor was tripped. The LEDs where added as a visual aid to quickly show whether or not the sensor has picked up anything. For stage 4; I was having trouble finding the proper syntax for python 3 to check if a file exists and write to it, or if it didn't exist have it create one then write to it. So I ended up writing a small bash script, 'sensorlog.sh', to preform that operation.

Stage 1: Turns on a distance sensor and prints out the distance.
  (4 Male-to-Female jumper wires, 1 330 Ohm resistor, 1 470 Ohm resistor, 1 Ulta-Sonic Distance Sensor)

Stage 2: If the distance is less than or equal to 20cm the red LED will light up.
  (Add on the red LED, 1 male-to-female jumper wire, 1 male-to-male jumper wire, and 1 220 Ohm resistor.)
  
Stage 3: Same as stage 2 but a green LED will be lit if the sensor does not detect anything within 20cm.
  (Add on the green LED, 1 male-to-female jumper wire, 1 male-to-male jumper wire, and 1 220 Ohm resistor.)
  
Stage 4: Print Time and Date in a log file in /home/$USER/sensorlog.txt each time the sensor detects anyhting within 20cm.
