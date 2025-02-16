"""
Advent of Code 2024 : Day 4
"""

import re

def test1(grid, i, j, d, c):
    n = len(grid)
    m = len(grid[0])

    x = i + d[0]
    y = j + d[1]

    return x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == c

def test2(grid, i, j, axis):
    n = len(grid)
    m = len(grid[0])

    res = True
    
    for a in axis:
        s = ''
        for x, y in a:
            xi = i + x
            yj = j + y
            if xi < 0 or yj < 0 or xi >= n or yj >= m:
                res = False
                break
            s += grid[xi][yj]
        
        if re.fullmatch(r'(MS|SM)', s) == None:
            res = False

        if not res:
            break

    return res

import sys
import os

# Add the parent directory of `main.py` to `sys.path`
cur_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(cur_dir, '..'))
sys.path.insert(0, parent_dir)
import module

PATH = cur_dir + "/input.txt"
with open(PATH, "r", encoding="utf-8") as file:
    lines = file.read().strip().split('\n')
    directions1 = [[i, j] for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)]
    res1 = 0
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c == 'X':
                for d in directions1:
                    if test1(lines, i, j, d, 'M'):
                        if test1(lines, i, j, [2*d[0], 2*d[1]], 'A'):
                            if test1(lines, i, j, [3*d[0], 3*d[1]], 'S'):
                                res1 += 1
    print(res1)

    res2 = 0
    axis = [[[-1, -1], [1, 1]], [[-1, 1], [1, -1]]]
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c == 'A':
                res2 += test2(lines, i, j, axis)
    print(res2)
