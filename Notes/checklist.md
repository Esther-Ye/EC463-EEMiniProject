# Thoughts on what to do next

1. Consider working on Bluetooth detection
   
   Specifically, the ble_scan.py currently prints the devices detected after a set amount of time right in the terminal. 
   Possible considerations include: 
   
   a) writing a loop to scan for devices over a more prolonged period of time
   
   b) representing the information in a graphical format (will likely be # of devices w.r.t. time)
   
2. Figure out the graphing scale of the wifi_plot.py file -- Current graph max is at 1 and min at 0
   
   Should probably add labels to the axes, not sure what the y-label will be but the x-label is time. 
   
   This shouldn't be difficult because the plots are done using matplotlib: command is xlabel('...')
