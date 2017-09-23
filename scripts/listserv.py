#!/usr/bin/python3
import sys
if len(sys.argv) < 4:
    print ("Usage: <file path> <command> <list name>")
    exit(1)
names = open (sys.argv[1], 'r')
for name in names:
    print ("approve raydio", sys.argv[2], sys.argv[3], name, end="")
