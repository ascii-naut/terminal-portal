#!/usr/bin/env python3
import os
import time

#the landing location the script checks if new files are added
source = "/portal-entry/"
#the exit location where the file ends
exitLocation = "/portal-exit"
files1 = os.listdir(source)

while True:
    time.sleep(5)
    files2 = os.listdir(source)

    # Check for files
    new = [f for f in files2 if all([not f in files1])]
    # if new files exist:
    for f in new:
	os.system('mv ' + source + f + ' ' + exitLocation)

    files1 = files2
