#!/usr/bin/python
# Advent of Code 2021
# Day 1 Part 1

import sys

prev = 999999
count_up = 0

for line in sys.stdin:
    curr = int(line.strip())
    if prev < curr:
        count_up += 1
    prev = curr

print(count_up)
