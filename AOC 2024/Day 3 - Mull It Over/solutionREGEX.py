"""
Advent of Code 2024 : Day 3
"""
import re

import sys
import os

# Add the parent directory of `main.py` to `sys.path`
cur_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(cur_dir, '..'))
sys.path.insert(0, parent_dir)
import module

PATH = cur_dir + "/input.txt"
with open(PATH, "r", encoding="utf-8") as file:
    text = file.read().strip().split("do()")
    does = [t.split("don't()")[0] for t in text]
    mul = [match for d in does for match in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", d)]
    s = 0
    for m in mul:
        x = m.lstrip("mul(").rstrip(")").split(",")
        s += int(x[0])*int(x[1])
    print(s)