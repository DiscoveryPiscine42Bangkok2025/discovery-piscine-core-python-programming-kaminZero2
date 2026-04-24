#!/usr/bin/env python3

"""This script get a number and display its multiplication table."""
def main():
    """Main function to display multiplication table of a number."""
    i = 0
    j = 0
    while i < 11:
        while j < 11:
            print(i*j, end=" ")
            j += 1
        print()
        i += 1
        j = 0
main()
