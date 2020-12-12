import subprocess
import sys
from sys import byteorder

print("---------------------------------")
print("|                               |")
print("|                               |")
print("|        Enumerate Plz          |")
print("|        Credit: L0uisJ0shua    |")
print("|                               |")
print("|                               |")
print("---------------------------------")

print()

print("The server is using " + byteorder + " endian!")

print("\n--------------------------------\n")

print("Enumerating information about system...\n")

print("System Information:")
subprocess.call("uname -ar", shell=True)
subprocess.call("hostname", shell=True)

print()

subprocess.call("cat /etc/*-release", shell=True)


print("\n--------------------------------\n")
print("User Information:")
try:
   user = subprocess.check_output("whoami", shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()
   userid = subprocess.check_output("id", shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()
   path = subprocess.check_output("echo $PATH", shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()
   term = subprocess.check_output("echo $TERM", shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()
   shell = subprocess.check_output("echo $SHELL", shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()

except subprocess.CalledProcessError:
   print("Execution of '%s' failed!") % cmd
   sys.exit(1)


print("Currently logged in as: ")
print(userid)
print("$PATH = " + path)
print("$TERM = " + term)
print("$SHELL = " + shell)


print("\n--------------------------------\n")

print("Network Information:")
subprocess.call("ip a", shell=True)
print()
subprocess.call("netstat -tulpn | grep LISTEN", shell=True)

print("\n----------------------------------\n")

print("Done")



