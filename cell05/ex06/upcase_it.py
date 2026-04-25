#!/usr/bin/env python3
import sys

if len(sys.argv[1:]) == 0:
    print("none", end="\n")
else:
    print(sys.argv[1].upper())