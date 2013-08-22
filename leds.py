import piface.pfio as pfio

pfio.init()

while True:
    
    # turn LED pins 1 to 10 on
    pfio.digital_write(1, 1)
    pfio.digital_write(2, 1)
    pfio.digital_write(3, 1)
    pfio.digital_write(4, 1)
    pfio.digital_write(5, 1)
    pfio.digital_write(6, 1)
    pfio.digital_write(7, 1)
    pfio.digital_write(8, 1)
    pfio.digital_write(9, 1)
    pfio.digital_write(10, 1)
    
    time.sleep(0.5) # LEDs stay on for half a second
    
    # turn LED pins 1 to 10 off
    pfio.digital_write(1, 0)
    pfio.digital_write(2, 0)
    pfio.digital_write(3, 0)
    pfio.digital_write(4, 0)
    pfio.digital_write(5, 0)
    pfio.digital_write(6, 0)
    pfio.digital_write(7, 0)
    pfio.digital_write(8, 0)
    pfio.digital_write(9, 0)
    pfio.digital_write(10, 0)
    
    time.sleeo(0.5) # LEDs stay off for half a second
