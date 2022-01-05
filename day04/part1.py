#!/usr/bin/python3
# Camila Thompson
# Advent of Code - Day 4 Part 1

import sys

numbers = sys.stdin.readline().split(",")

row_boards = []
col_boards = []

winner = []

for line in sys.stdin:
    
    line = line.strip()

    if line == '':

        count = 0
        rows = []
        cols = [[],[],[],[],[]]
        continue

    count += 1
    line = line.split()

    rows.append(line)
    for i in range(len(line)):
        cols[i].append(line[i])
    
    if count == 5:
        row_boards.append(rows)
        col_boards.append(cols)

for num in numbers:

    for board in row_boards:
        for row in board:
            if num in row:
                row.remove(num)
                if len(row) == 0:
                    winner = board
                break
        if winner != []:
            break
    if winner != []:
        break

    for board in col_boards:
        for col in board:
            if num in col:
                col.remove(num)
                if len(col) == 0:
                    winner = board
                break
        if winner != []:
            break

    if winner != []:
        break

wsum = 0
for b in winner:
    wsum += sum([int(i) for i in b])

score = wsum * int(num)
print(score)
