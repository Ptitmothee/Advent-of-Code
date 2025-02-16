"""
Advent of Code 2024 : Day 9
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
    initial_sequence = file.read().strip()

    compressed_sequence = []
    id = 0
    for i, c in enumerate(initial_sequence):
        if i%2==0:
            compressed_sequence += [str(id)]*int(c)
            id += 1
        else:
            compressed_sequence += ['.']*int(c)

    print(compressed_sequence)
    i = 0
    j = len(compressed_sequence)-1
    while i < j:
        if compressed_sequence[i] == '.':
            x = compressed_sequence.pop()
            j -= 1
            while x == '.':
                x = compressed_sequence.pop()
                j -= 1
            if i < j:
                compressed_sequence[i] = x
            else:
                compressed_sequence.append(x)
        i += 1
    while compressed_sequence[-1] == '.':
        compressed_sequence.pop()
    compressed_sequence = [int(x) for x in compressed_sequence]

    print(compressed_sequence)
    s = 0
    for i, x in enumerate(compressed_sequence):
        s += i*int(x)
    print(s)