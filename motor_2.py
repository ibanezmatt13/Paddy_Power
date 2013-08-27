# This scrip runs the motor out and then back in again by closing relay output 0
import piface.pfio as pfio # Import PiFace
from time import sleep
pfio.init() # initialise PiFace # Comment out if using as nested script

for x in range (0, 5): # loop x number of times
 pfio.digital_write (0,1) # motor out
 print "button pressed - motor out"
 sleep (1) # hold time
 pfio.digital_write (0,0) # release button
