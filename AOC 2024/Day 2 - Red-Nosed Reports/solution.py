"""
Advent of Code 2024 : Day 2
"""

import sys
import os

# Add the parent directory of `main.py` to `sys.path`
cur_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(cur_dir, '..'))
sys.path.insert(0, parent_dir)
import module

def safe(l):
    res = True
    asc = True
    desc = True
    j = 0
    while j < len(l)-1 and res:
        d = l[j+1] - l[j]
        if (abs(d) > 3 or d == 0):
            res = False

        elif (d < 0):
            asc = False
            if not desc:
                res = False
            else:
                j += 1
        
        elif (d > 0):
            desc = False
            if not asc:
                res = False
            else:
                j += 1
        else:
            j += 1
    return res

def safe_sup(l):
    res = False
    if safe(l):
        res = True
    else:
        i = 0
        while (i < len(l) and not res):
            res = safe(l[:i]+l[i+1:])
            i += 1
    return res

PATH = cur_dir + "/input.txt"
with open(PATH, "r", encoding="utf-8") as file:
    lines = file.read().strip().split('\n')
    reports = [l.split(' ') for l in lines]
    rep_ints = [[int(r[j]) for j in range(len(r))] for r in reports]
    
    s = 0
    for r in rep_ints:
        s += safe_sup(r)
    print(s)
print("babc".split('a'))