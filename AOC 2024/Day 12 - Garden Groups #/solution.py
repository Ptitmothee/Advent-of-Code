"""
Advent of Code 2024 : Day 12
"""
import sys
import os
from collections import deque

# Add the parent directory of `main.py` to `sys.path`
cur_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(cur_dir, ".."))
sys.path.insert(0, parent_dir)
import module

PATH = cur_dir + "/input.txt"
with open(PATH, "r", encoding="utf-8") as file:
	lines = file.read().strip().split('\n')
	n = len(lines)
	m = len(lines[0])
	
	directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

	""" Doesn't work for enclosed fences
	fences = [[0 for _ in range(m)] for _ in range(n)]
	regions = {}
	for i, line in enumerate(lines):
		for j, plot in enumerate(line):
			if plot not in regions:
				regions[plot] = [(i, j)]
			else:
				regions[plot] += [(i, j)]

			for d in directions:
				x = i + d[0]
				y = j + d[1]
				if (not module.in_map((x, y), n, m)) or lines[x][y] != plot:
					fences[i][j] += 1
	
	perimeters = {}
	for region, plots in regions.items():
		perimeters[region] = 0
		for i, j in plots:
			perimeters[region] += fences[i][j]
	
	cost = 0
	for region, plots in regions.items():
		cost += len(plots)*perimeters[region]
		print(cost)
	print(cost) """

	def visit_region(i0, j0):
		global lines
		global checked
		global fences
		global directions
		global n
		global m
		visit = deque([(i0, j0)])
		region = []
		while visit:
			i, j = visit.popleft()
			region.append((i, j))
			checked[i][j] = True
			for d in directions:
				x = i + d[0]
				y = j + d[1]
				if (not module.in_map((x, y), n, m)) or lines[x][y] != lines[i][j]:
					fences[i][j] += 1
				elif (x, y) not in visit and not checked[x][y]:
					visit.append((x, y))
		return region

	checked = [[False for _ in range(m)] for _ in range(n)]
	fences = [[0 for _ in range(m)] for _ in range(n)]
	regions = []
	i = 0
	j = 0
	while j != m:
		regions.append(visit_region(i, j))
		while module.in_map((i, j), n, m) and checked[i][j]:
			if i == n-1:
				i = 0
				j += 1
			else:
				i += 1
	
	perimeters = []
	checksum = 0
	for region in regions:
		perimeter = 0
		for i,j in region:
			perimeter += fences[i][j]
		perimeters.append(perimeter)
		checksum += perimeter*len(region)
	print(regions)

