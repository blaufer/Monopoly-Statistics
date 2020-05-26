import os,sys
from random import randrange

board = [[0 for i in range(40)] for j in range(40)]

for i in range(40):
    for j in range(10000):
        die1 = randrange(1,7)
        die2 = randrange(1,7)
        roll = die1 + die2
        move = i + roll
        if move > 39:
            move %= 40
        board[i][move] += 1

totals = [[j,0,0] for j in range(40)]
count = 0

for i in range(40):
    for j in range(40):
        totals[j][1] += board[i][j]
        count += board[i][j]

for i in range(40):
    totals[i][2] = totals[i][1] / count

for i in range(40):
    print(totals[i])
