# This script flashes output 2 LED's
from time import sleep
import piface.pfio as pfio
pfio.init() # Initialise PiFace #Comment out if used as nested PiFace Script

while(True): # Variable to ensure the script runs indefinatly
  pfio.digital_write (2,1) # LED On
  sleep (0.5) # Wait Time
  pfio.digital_write (2,0) # LED off
  sleep (0.5) # Wait time
