#!/usr/bin/python

import os
import time

time.sleep(10)
#folders = []
#f = open("/media/pi/Sri/media/demofile2.txt", "a")
#f.write("Now the file has more content!")
#f.close()



for r, d, f in os.walk("/usb/media/"):
    for filename in f:
        print filename
	if filename.startswith("www.TamilRockers."):
        	os.rename(filename, filename[22:])
		

