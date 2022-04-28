#!/bin/python3

from gpiozero import DistanceSensor, LED
from time import sleep
import subprocess
import os.path

sensor = DistanceSensor (echo=23, trigger=24, max_distance=2.0)
red = LED(17)
green = LED(27)

if os.path.isFile('/home/$USER/sensorlog.txt') == False:
  open('/home/$USER/sensorlog.txt')
  
  else:
    pass

while True:
  distance = sensor.distance * 100
  print("Distance : %.1f" % distance)
  sleep(1)
  
  if distance <= 20:
        green.off()
        red.on()
        #subprocess.run(['date >> /home/$USER/sensorlog.txt'])
        with open("/home/$USER/sensorlog.txt", 'w') as logfile:
          logfile.write(subprocess.run(date))
        
  else:
        green.on()
        red.off()
