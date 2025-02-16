"""
Advent of Code 2024 : Day 7
"""

def is_valid(target, ns):
    if len(ns) == 1:
        b = ns[0] == target
    else:
        b = is_valid(target, [ns[0] + ns[1]] + ns[2:]) or is_valid(target, [ns[0] * ns[1]] + ns[2:]) or is_valid(target, [int(str(ns[0])+str(ns[1]))] + ns[2:])
    return b

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
    equ_str = [line.split(': ') for line in lines]
    equations = [[int(equ[0]), [int(x) for x in equ[1].split(' ')]] for equ in equ_str]

    s = 0
    for target, numbers in equations:
        if is_valid(target, numbers):
            s += target
    print(s)