#!/usr/bin/env python3

import sys

def check_z():
    if len(sys.argv) != 2:
        print("none")
        return

    string_param = sys.argv[1]
    found_z = False

    for char in string_param:
        if char == 'z':
            print('z')
            found_z = True
    
    if not found_z:
        print("none")

if __name__ == "__main__":
    check_z()