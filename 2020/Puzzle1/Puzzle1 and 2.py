import math
import numpy as np


f = open("C:\\Users\\larsd\\OneDrive - Danmarks Tekniske Universitet\\DTU\\Programming Projects\\Python\\AOC\\Puzzle1\\Expenses.txt").read().split('\n')
print(f)

for i in f:
    for j in f:
        for k in f:
            if int(i) + int(j)  + int(k) == 2020:
                fresult = int(i) * int(j) * int(k)
                print(i, j, k, fresult)

