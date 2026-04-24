#!/usr/bin/env python3

number = int(input("Enter a number less than 25: "))
if number > 25:
    print(Error)
else:
    while number < 26:
        print("Inside the loop, my veriable is",number)
        number+=1
