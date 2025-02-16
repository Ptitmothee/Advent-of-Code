"""
Advent of Code 2024 : Day 1
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
    content = file.read().strip()
    lines = content.split("\n")
    n = len(lines)
    L1 = [0]*n
    L2 = [0]*n
    for i in range(n):
        l = lines[i].split("   ")
        L1[i] = int(l[0])
        L2[i] = int(l[1])

    L1.sort()
    L2.sort()

    sum = 0
    for i in range(n):
        sum += abs(L1[i]-L2[i])

    print("Answer to part 1 :", sum)

    sum = 0
    c = 0
    i = 0
    j = 0
    while j < n:
        if L1[i] < L2[j]:
            sum += c*L1[i]
            i += 1
            c = 0
        elif L1[i] == L2[j]:
            c += 1
            j += 1
        else :
            j += 1
    
    print("Answer to part 2 :", sum)