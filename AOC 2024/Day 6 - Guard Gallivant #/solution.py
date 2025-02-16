"""
Advent of Code 2024 : Day 6
"""

from copy import deepcopy

import sys
import os

# Add the parent directory of `main.py` to `sys.path`
cur_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(cur_dir, '..'))
sys.path.insert(0, parent_dir)
import module

PATH = cur_dir + "/input.txt"
with open(PATH, "r", encoding="utf-8") as file:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    map_raw = file.read().strip().split('\n')
    n, m = len(map_raw), len(map_raw[0])
    map_obs = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if map_raw[i][j] == "^":
                print(i, j)
                x0 = i
                y0 = j
                d = 0
            map_obs[i][j] = map_raw[i][j] == "#"

    def visite_map_chemin(map_obs, p0):
        global directions
        x0, y0, d = p0
        map_vis = [[False for j in range(m)] for i in range(n)]
        chemin = [[d, (x0, y0)]]
        in_map = True
        while in_map:   
            map_vis[x0][y0] = True
            x1 = x0 + directions[d][0]
            y1 = y0 + directions[d][1]
            if x1 < 0 or y1 < 0 or x1 >= n or y1 >= m:
                in_map = False
            elif map_obs[x1][y1]:
                d = (d+1)%4
                chemin.append([d, (x0, y0)])
            else:
                x0 = x1
                y0 = y1
                chemin[-1].append((x0, y0))
        
        return map_vis, chemin

    map_vis, chemin = visite_map_chemin(map_obs, (x0, y0, d))

    s1 = 0
    for i in range(n):
        for j in range(m):
            s1 += map_vis[i][j]
    print(s1)

    def map_chemin_obs(map_obs, xi, yi, di):
        global directions
        x0, y0, d = xi, yi, di
        map_temp = deepcopy(map_obs)
        map_temp[x0 + directions[d][0]][y0 + directions[d][1]] = True
        in_map = True
        cycle = False
        chemin_temp = []
        while in_map and not cycle:
            chemin_temp.append((x0, y0, d))
            x1 = x0 + directions[d][0]
            y1 = y0 + directions[d][1]
            if (x1, y1, d) in chemin_temp:
                cycle = True
            elif x1 < 0 or y1 < 0 or x1 >= n or y1 >= m:
                in_map = False
            elif map_temp[x1][y1]:
                d = (d+1)%4
            else:
                x0 = x1
                y0 = y1
        
        return cycle

    pos_obs_cycle = [[False for j in range(m)] for i in range(n)]
    for i, segment in enumerate(chemin):
        for j in range(1, len(segment) -1):
            x0, y0 = segment[j]
            if not pos_obs_cycle[x0][y0]:
                if map_chemin_obs(map_obs, x0, y0, segment[0]):
                    pos_obs_cycle[x0][y0] = True
    
    s2 = 0
    for i in range(n):
        for j in range(m):
            s2 += pos_obs_cycle[i][j]
    print(s2)