#
#import piface.pfio as pfio # Import PiFace
from time import sleep
#pfio.init() # initialise PiFace # Comment out if using as nested script

x = 0

while x <= 5:
    print "statement 1"
    sleep (1) # hold time
    print "statement 2"
    sleep (2) # hold time
    print "statement 3"
    x += 1 # increment counter each iteration
