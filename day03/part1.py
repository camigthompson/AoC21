#!/usr/bin/python3
# Cami Thompson
# Day 3 Part 1

import sys

zeros = [0] * 12
ones  = [0] * 12

for line in sys.stdin:

    for i, digit in enumerate(line):

        if digit == '0':
            zeros[i] += 1
        elif digit == '1':
            ones[i] += 1

gamma   = [0] * 12
epsilon = [0] * 12

for index in range(12):
    if zeros[index] > ones[index]:
        gamma[index] = '0'
        epsilon[index] = '1'
    elif ones[index] > zeros[index]:
        gamma[index] = '1'
        epsilon[index] = '0'

gamma = ''.join(gamma)
epsilon = ''.join(epsilon)

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)

power = gamma_dec * epsilon_dec

print(power)
