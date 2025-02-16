"""
Advent of Code 2024 : Day 8
"""

from collections import defaultdict

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
    antennas = defaultdict(list)
    n = len(lines)
    m = len(lines[0])
    for i in range(n):
        for j, c in enumerate(lines[i]):
            if c != '.':
                antennas[c].append([i, j])
    antennas = dict(antennas)

    antinodes_1 = [[False for _ in range(m)] for _ in range(n)]
    antinodes_2 = [[False for _ in range(m)] for _ in range(n)]
    for antenna_type in antennas.keys():
        for i, ant_1 in enumerate(antennas[antenna_type]):
            for j, ant_2 in enumerate(antennas[antenna_type]):
                if i != j:
                    antinodes_2[ant_1[0]][ant_1[1]] = True
                    antinodes_2[ant_2[0]][ant_2[1]] = True
                    dx = ant_1[0] - ant_2[0]
                    dy = ant_1[1] - ant_2[1]
                    x, y = ant_1[0]+dx, ant_1[1]+dy
                    if module.in_map([x, y], n, m):
                        antinodes_1[x][y] = True
                        
                    while module.in_map([x, y], n, m):
                        antinodes_2[x][y] = True
                        x += dx
                        y += dy

                    x, y = ant_2[0]-dx, ant_2[1]-dy
                    if module.in_map([x, y], n, m):
                        antinodes_1[x][y] = True

                    while module.in_map([x, y], n, m):
                        antinodes_2[x][y] = True
                        x -= dx
                        y -= dy

    """ map = [list(line) for line in lines]
    for i in range(n):
        for j in range(m):
            if antinodes_1[i][j] and map[i][j] == '.':
                map[i][j] = '#'
        print(map[i]) """
    print(module.sum_bool_mat(antinodes_1))
    print(module.sum_bool_mat(antinodes_2))