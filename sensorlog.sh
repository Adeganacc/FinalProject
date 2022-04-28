#!/bin/bash

FILE=/home/$USER/sensorlog.txt

if [ ! -f "$FILE" ]; then
  touch /home/$USER/sensorlog.txt
fi


echo $(date)
