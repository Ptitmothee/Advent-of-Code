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

    files = []
    free_space = []
    index = 0
    for i, c in enumerate(initial_sequence):
        nb = int(c)
        if i%2==0:
            files += [[index, nb]]
        else:
            free_space += [[index, nb]]
        index += nb

    for id in range(len(files)-1, -1, -1):
        f = files[id]
        for i, space in enumerate(free_space):
            if space[1] >= f[1] and space[0] < f[0]:
                free_space[i][1] -= f[1]
                files[id][0] = free_space[i][0]
                free_space[i][0] += f[1]
                free_space.pop()
                break
    
    checksum = 0
    for i, f in enumerate(files):
        index, nb = f
        for j in range(index, index+nb):
            checksum += i*j
    print(checksum)
    """
    i = 0
    j = sum(files)+sum(free_space)-1
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
    print(s) """