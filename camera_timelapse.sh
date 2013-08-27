
#!/bin/bash
 
while [ 1 ]; do # do forever
{
raspistill -o images/image/`date +%H%M%S` + ".jpg" # executing recording with some parameters
sleep 30 # delay for one second
}
 
done
