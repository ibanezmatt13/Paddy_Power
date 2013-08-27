# This script runs the motor out and then back in again by closing relay output 0
import piface.pfio as pfio # Import PiFace
from time import sleep
pfio.init() # initialise PiFace # Comment out if using as nested script

x = 0

while x <= 5:
    pfio.digital_write (0,1) # motor out
    print "button pressed - motor out"
    time.sleep(1) # hold time
    print "slept"
    pfio.digital_write (0,0) # release button
    print "released"
    x += 1 # increment counter each iteration
