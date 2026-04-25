#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [value + 2 for value in original_array]

print(f"Original array: {original_array}")
print(f"New array: {new_array}")
for i in range(len(new_array)):
    new_array[i] = new_array[i] + 2