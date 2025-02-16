"""
Advent of Code 2024 : Day 10
"""

import sys
import os

# Add the parent directory of `main.py` to `sys.path`
cur_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(cur_dir, '..'))
sys.path.insert(0, parent_dir)
import module

from collections import deque

def add_neigh(p0, lines):
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n = len(lines)
    m = len(lines[0])
    i0, j0 = p0

    add_waiting = []

    for d in DIRECTIONS:
        i1 = i0 + d[0]
        j1 = j0 + d[1]
        if (module.in_map((i1, j1), n, m)) and (lines[i1][j1] == lines[i0][j0] + 1):
            add_waiting.append((i1, j1))
    
    return add_waiting


PATH = cur_dir + "/input.txt"
with open(PATH, "r", encoding="utf-8") as file:
    lines = [[int(c) for c in line] for line in file.read().strip().split("\n")]
    n = len(lines)
    m = len(lines[0])

    trailheads_score = [[[] for _ in range(m)] for _ in range(n)]
    trailheads_ratings = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if lines[i][j] == 0:
                waiting = deque()
                waiting += add_neigh((i, j), lines)

                while waiting:
                    pi, pj = waiting.popleft()
                    if lines[pi][pj] == 9:
                        trailheads_ratings[i][j] += 1
                        if (pi, pj) not in trailheads_score[i][j]:
                            trailheads_score[i][j].append((pi, pj))
                    else:
                        new_neigh = add_neigh((pi, pj), lines)
                        print(new_neigh)
                        waiting += add_neigh((pi, pj), lines)
    
    print(module.sum_mat(trailheads_score, function=len))
    print(module.sum_mat(trailheads_ratings))
                