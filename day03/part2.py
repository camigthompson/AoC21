#!/usr/bin/python3
# Cami Thompson
# Day 3 Part 2

import sys

oxy_possible = []
co2_possible = []

for line in sys.stdin:

    oxy_possible.append(line.strip())
    co2_possible.append(line.strip())

# oxy - remove elements that do not match
for i in range(12):

    zeros = 0
    ones = 0
    oxy = ' '
    for o in oxy_possible:
        if o[i] == '0':
            zeros += 1
        elif o[i] == '1':
            ones += 1

    if zeros > ones:
        oxy = '0'
    else:
        oxy = '1'

    oxy_possible = [o for o in oxy_possible if o[i] == oxy]

    if len(oxy_possible) == 1:
        oxygen = oxy_possible[0]
        break
    
# co2 - remove elements that do not match
for i in range(12):

    zeros = 0
    ones = 0
    co2 = ' '
    for c in co2_possible:
        if c[i] == '0':
            zeros += 1
        elif c[i] == '1':
            ones += 1

    if zeros > ones:
        co2 = '1'
    else:
        co2 = '0'

    co2_possible = [c for c in co2_possible if c[i] == co2]

    if len(co2_possible) == 1:
        carbon = co2_possible[0]
        break

print("binary oxy: ", oxygen)
print("binary co2: ", carbon)

oxygen = int(oxygen,2)
carbon = int(carbon,2)

print("oxygen: ", oxygen)
print("carbon: ", carbon)

life_support = oxygen * carbon

print("life support: ", life_support)
