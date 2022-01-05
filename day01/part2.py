#!/usr/bin/python
# Advent of Code 2021
# Day 1 Part 2

import sys

prev_window = 999999
c = 0
count_up = 0

for line in sys.stdin:
    if c == 0:
        pos1 = int(line.strip())
        c += 1
    elif c == 1:
        pos2 = int(line.strip())
        c += 1
    elif c >= 2:
        pos3 = int(line.strip())
        c += 1
  
        curr_window = pos1 + pos2 + pos3

        if prev_window < curr_window:
            count_up += 1

        prev_window = curr_window
        pos1 = pos2
        pos2 = pos3

print(count_up)
