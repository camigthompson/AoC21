#!/usr/bin/python
# Advent of Code 2021
# Day 2 Part 2

import sys

x = 0
y = 0
aim = 0

for line in sys.stdin:
    direction, amount = line.strip().split()

    if direction == 'forward':
        x += int(amount)
        y += aim * int(amount)
    elif direction == 'down':
        aim += int(amount)
    elif direction == 'up':
        aim -= int(amount)

print(x * y)
