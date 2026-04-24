#!/usr/bin/env python3

"""This script checks if a number is an integer or decimal."""
number = float(input("Give me a number: "))

if number == int(number):
    print("This number is an integer.")
else:
    print("This number is a decimal.")