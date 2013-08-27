# This scrip runs the motor out and then back in again by closing relay output 0
import piface.pfio as pfio # Import PiFace
from time import sleep
pfio.init() # initialise PiFace # Comment out if using as nested script

pfio.digital_write (0,1) # motor out
print "button pressed - motor out"
sleep (1) # hold time
pfio.digital_write (0,0) # release button
print "released"
sleep (3) # wait time
print "running"
pfio.digital_write (0,1) # motor stop
print "button pressed - motor stopped"
sleep (1) # hold time
pfio.digital_write (0,0) # release button
print "move in complete waiting"

sleep (10) # in dead waiting
print "waiting"

pfio.digital_write (0,1) # motor in
print "button pressed - motor in"
sleep (1) # hold time
pfio.digital_write (0,0) # release button
print "released"
sleep (4) # wait time
print "running"
pfio.digital_write (0,1) # motor stop
print "button pressed - motor stopped"
sleep (1) # hold time
pfio.digital_write (0,0) # release button
print "move out complete"
