"""
Advent of Code 2024 : Day 11
"""

import sys
import os

import tqdm

# Add the parent directory of `main.py` to `sys.path`
cur_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(cur_dir, '..'))
sys.path.insert(0, parent_dir)
import module

PATH = cur_dir + "/input.txt"
with open(PATH, "r", encoding="utf-8") as file:
    stones = file.read().strip().split(" ")

    for _ in tqdm.tqdm(range(25)):
        to_add = []
        for i, stone in enumerate(stones):
            if stone == "0":
                stones[i] = "1"
            elif (d := divmod(len(stone), 2))[1] == 0:
                stones[i] = stone[0:d[0]]
                to_add.append((i, "0" if (s := stone[d[0]:].lstrip("0")) == "" else s))
            else:
                stones[i] = str(2024*int(stone))

        
        for i, add in enumerate(to_add):
            stones.insert(i+add[0]+1, add[1])
    print(len(stones))
