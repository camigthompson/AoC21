#!/usr/bin/python
# Advent of Code 2021
# Day 2 Part 1

import sys

x = 0
y = 0

for line in sys.stdin:
    direction, amount = line.strip().split()

    if direction == 'forward':
        x += int(amount)
    elif direction == 'down':
        y += int(amount)
    elif direction == 'up':
        y -= int(amount)

print(x * y)
