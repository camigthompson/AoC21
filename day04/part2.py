#!/usr/bin/python3
# Camila Thompson
# Advent of Code - Day 4 Part 2

import sys

numbers = sys.stdin.readline().split(",")

row_boards = []
col_boards = []

for line in sys.stdin:
    
    line = line.strip()

    if line == '':

        count = 0
        rows = []
        cols = [[],[],[],[],[]]
        continue

    count += 1
    line = list(map(int, line.split()))

    rows.append(line)
    for i in range(len(line)):
        cols[i].append(line[i])
    
    if count == 5:
        row_boards.append(rows)
        col_boards.append(cols)

removed = 0
winner = 0
for num in numbers:

    num = int(num)

    for i, board in enumerate(row_boards):
        if not isinstance(board, list):
            continue
        for row in board:
            if num in row:
                row.remove(num)
                if len(row) == 0:
                    row_boards[i] = sum(sum(row_boards[i],[]))
                    col_boards[i] = sum(sum(col_boards[i],[]))
                    removed += 1
                break

        if removed == len(row_boards):
            winner = row_boards[i]
            break

    for i, board in enumerate(col_boards):
        if not isinstance(board,list):
            continue
        for col in board:
            if num in col:
                col.remove(num)
                if len(col) == 0:
                    row_boards[i] = sum(sum(row_boards[i],[]))
                    col_boards[i] = sum(sum(col_boards[i],[]))
                    removed += 1
                break

        if removed == len(col_boards):
            winner = col_boards[i]
            break
    if winner:
        break

score = winner * int(num)
print(num)
print(winner)
print(score)
