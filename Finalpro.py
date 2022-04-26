#!/bin/python3

from gpiozero import DistanceSensor, LED
from time import sleep

sensor = DistanceSensor (echo=23, trigger=24, max_distance=2.0)
red = LED(17)

while True:
  distance = sensor.distance * 100
  print("Distance : %.1f" % distance)
  sleep(1)
