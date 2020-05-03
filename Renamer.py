#!/usr/bin/python

import os
import time

time.sleep(10)

for r, d, f in os.walk("/usb/media/"):
    for filename in f:
        print filename
	if filename.startswith("www.TamilRockers."):
        	os.rename(filename, filename[22:])
		

