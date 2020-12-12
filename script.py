#!/usr/bin/python

# Shortcut script written to take in the hexcode payload and run it with the binary not sure if it works but use it at your own risk

import sys
import os

if len(sys.argv) != 3:
   print "payload.py <hexcode> <binary file>"
   sys.exit()
else:
   payload = sys.argv[1]
   print "You are using the following payload: \n" + payload
   print "Binary chosen to be run : \n" + sys.argv[2]
   print "Running Binary with Payload ... ...\n"

   os.system("./" + sys.argv[2] + " " + payload)
