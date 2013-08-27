# This script takes pictures and stamps them with the date
import os
import time
import datetime

while True: # Variable to ensure time lapse continues indefinitely 
	
	
	date = datetime.datetime.fromtimestamp(time.time()).strftime("_%Y-%m-%d_%H-%M-%S") # Define Date
	os.system("raspistill -o images/image" + date + ".jpg") # Run 'take picture' and save with date stamp
	time.sleep(30) # Wait time until repeat
