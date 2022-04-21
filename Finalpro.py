#!/bin/python3

from gpiozero import DistanceSensor, LED
from time import sleep
import subprocess

sensor = DistanceSensor (echo=23, trigger=24, max_distance=2.0)
led = LED(17)

while True:
  distance = sensor.distance * 100
  print("Distance : %.1f" % distance)
  sleep(5)
  
  if distance <= 20:
        subprocess.run(['echo date >> /home/$USER/sensorlog'])
        led.on()
  else:
        led.off()
        
