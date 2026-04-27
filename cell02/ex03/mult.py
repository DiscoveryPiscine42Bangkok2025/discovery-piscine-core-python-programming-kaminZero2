#!/usr/bin/env python3

first_number = int(input("Enter the first number:"))
second_number = int(input("Enter the second number:"))
total = first_number *  second_number

if total > 0:
    print ("The result is positive")
if total < 0:
    print ("The result is negative")
if total == 0:
    print("The result is positive and negative")