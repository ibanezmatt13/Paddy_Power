#!/bin/bash

while [ 1 ]; do # do  forever
{
/home/pi/flightcode.py; # execute the main tracker executable
/home/pi/camera_timelapse.py; # execute the camera timelapse
sleep 1 # delay for one second
}

done
