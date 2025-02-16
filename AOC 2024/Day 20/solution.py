"""
Advent of Code 2024 : Day 20
"""
import sys
import os

# Add the parent directory of `main.py` to `sys.path`
cur_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(cur_dir, ".."))
sys.path.insert(0, parent_dir)
import module
PATH = cur_dir + "/input.txt"
with open(PATH, "r", encoding="utf-8") as file:
	pass