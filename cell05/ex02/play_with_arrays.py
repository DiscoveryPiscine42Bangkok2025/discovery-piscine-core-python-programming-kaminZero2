#!/usr/bin/env python3

num =  "2 8 9 48 8 22 -12 2"
array = list(map(int, num.split()))
res = []

print(array)
for i in range(len(array)):
        res.append(array[i] + 2)
print(set(res))