"""
Advent of Code 2024 : Day 5
"""

from collections import defaultdict, deque

import sys
import os

# Add the parent directory of `main.py` to `sys.path`
cur_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(cur_dir, '..'))
sys.path.insert(0, parent_dir)
import module

PATH = cur_dir + "/input.txt"
with open(PATH, "r", encoding="utf-8") as file:
    input = file.read().strip().split('\n\n')
    rules = [[int(x) for x in r.split('|')] for r in input[0].split('\n')]
    rules_dic = {}
    for rule in rules:
        if rule[0] not in rules_dic:
            rules_dic[rule[0]] = [rule[1]]
        else:
            rules_dic[rule[0]].append(rule[1])

    in_degree = defaultdict(int)

    for key, values in rules_dic.items():
        for value in values:
            in_degree[value] += 1
        # Ensure every key is initialized in in_degree
        if key not in in_degree:
            in_degree[key] = 0

    print([item for item in in_degree.items() if item[1] != 24])
    # Step 2: Perform topological sort using Kahn's algorithm
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in rules_dic[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    print(sorted_order)
    pages = [[int(x) for x in r.split(',')] for r in input[1].split('\n')]