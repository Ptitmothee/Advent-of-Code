"""
Advent of Code 2024 : Day 3
"""

import sys
import os

# Add the parent directory of `main.py` to `sys.path`
cur_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(cur_dir, '..'))
sys.path.insert(0, parent_dir)
import module

PATH = cur_dir + "/input.txt"
with open(PATH, "r", encoding="utf-8") as file:
    does = file.read().strip().split('do()')
    does_dont = [d.split("don't()") for d in does]
    final_does = [dd[0] for dd in does_dont]

    bits = []
    for fd in final_does:
        fd_split = fd.split("mul(")
        for i in range(1, len(fd_split)):
            bits.append(fd_split[i])
    
    s = 0
    for i in range(len(bits)):
        x = bits[i].split(',')
        if len(x) >= 2:
            n = x[0]
            if n != '' and len(n) <= 3 and n.isnumeric():
                m = x[1].split(')')[0]
                if m != '' and len(m) <= 3 and m.isnumeric() and x[1] != m:
                    if x[1].lstrip(m)[0] == ')':
                        s += int(n)*int(m)
    print(s)
