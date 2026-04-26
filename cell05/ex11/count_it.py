#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv)<2:
        print("none")
    else:
        for i in range(len(sys.argv) -1,0,-1):
            x= sys.argv[i]
            print(x + ":" , len(x))
main()
