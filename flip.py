#!/usr/bin/python3

# Credits to @benjaminwongweien (https://github.com/benjaminwongweien)
### Use this to flip your memory address. Used to quickly flip memory adddresses that we want to write into during debugging
### Very useful for Little Endian Systems


def flip(arg):
    if arg[:2] != "0x":
        return False

    arg = arg[2:]

    while len(arg) < 8:
            arg = "0" + arg

    return "".join([r"\x"+arg[x:x+2] for x in range(0,len(arg),2)][::-1])

def main(*args):
    for x in args:
        print(flip(x))

if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])
