"""
Advent of Code 2024 : Day 7
"""

def reduce(res, numbers):
    if ((len(numbers) == 1) or (res%numbers[-1] == 0)):
        equ = [res, numbers]
    else:
        equ = reduce(res-numbers[-1], numbers[:-1])
    return equ

def can_be_true(equation):
    res, numbers = equation
    res, numbers = reduce(res, numbers)

    size = len(numbers) - 1
    b = False
    if size == 0:
        ops = ''
        if res == numbers[0]:
            b = True
    else:
        for i in range(2**size):
            ops = format(i, f'0{size}b')
            s = numbers[0]
            for j, c in enumerate(ops):
                if c == '1':
                    s *= numbers[j+1]
                else:
                    s += numbers[j+1]
            
            if s == res:
                b = True
                break
    
    ops += '0'*(len(equation[1]) - len(numbers))
    result = 0
    if b:
        result = equation[0]
        print(equation, ops)
    return result

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

    s1 = 0
    for equ in equations:
        s1 += can_be_true(equ)
    print(s1)