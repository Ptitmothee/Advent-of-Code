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

def blink(stone):
    if stone == "0":
        return ["1"]
    elif (d := divmod(len(stone), 2))[1] == 0:
        return [stone[0:d[0]], "0" if (s := stone[d[0]:].lstrip("0")) == "" else s]
    else:
        return [str(2024*int(stone))]
    
def memoized_blink(stone, remain_it, memo={}):
    #if not (result := remain_it == 0):
    result = 0
    if remain_it == 0:
        result = 1
    else:
        if (stone, remain_it) in memo:
            result = memo[(stone, remain_it)]
        else:
            stones = blink(stone)
            for s in stones:
                result += memoized_blink(s, remain_it-1, memo)
            memo[(stone, remain_it)] = result
    return result

PATH = cur_dir + "/input.txt"
with open(PATH, "r", encoding="utf-8") as file:
    stones = file.read().strip().split(" ")

    nb_stones = 0
    iterations = 75
    for stone in tqdm.tqdm(stones):
        nb_stones += memoized_blink(stone, iterations)
    print(nb_stones)
