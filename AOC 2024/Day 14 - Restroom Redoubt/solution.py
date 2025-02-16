"""
Advent of Code 2024 : Day 14
"""
import sys
import os
from copy import deepcopy

# Add the parent directory of `main.py` to `sys.path`
cur_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(cur_dir, ".."))
sys.path.insert(0, parent_dir)
import module
PATH = cur_dir + "/input.txt"
with open(PATH, "r", encoding="utf-8") as file:
	size, robs = file.read().strip().split("\n\n")
	size = size.lstrip("size=(").rstrip(")").split(", ")
	MAP_SIZE = (int(size[0]), int(size[1]))
	lines = robs.split("\n")
	robots = [line.split(" ") for line in lines]
	n = len(robots)
	robots_pos_init = [(0, 0) for _ in range(n)]
	robots_pos = [(0, 0) for _ in range(n)]
	robots_vel = [(0, 0) for _ in range(n)]
	for i in range(n):
		p, v = robots[i]
		p = p.lstrip("p=").split(",")
		v = v.lstrip("v=").split(",")

		robots_pos_init[i] = (int(p[0]), int(p[1]))
		robots_pos[i] = [int(p[0]), int(p[1])]
		robots_vel[i] = (int(v[0]), int(v[1]))
	
	def next(pos, robots_vel):
		robots_pos = deepcopy(pos)
		for i in range(n):
			x, y = robots_pos[i]
			robots_pos[i][0] = (x + robots_vel[i][0])%MAP_SIZE[0]
			robots_pos[i][1] = (y + robots_vel[i][1])%MAP_SIZE[1]
		return robots_pos

	def multinext(pos, robots_vel, nb):
		robots_pos = deepcopy(pos)
		for _ in range(nb):
			robots_pos = next(robots_pos, robots_vel)
		return robots_pos
	
	def affiche(pos):
		robots_map = [[0 for _ in range(MAP_SIZE[0])] for _ in range(MAP_SIZE[1])]
		for x, y in pos:
			robots_map[y][x] += 1
		
		for line in robots_map:
			string = ""
			for nb in line:
				if nb == 0:
					string += " "
				else:
					string += "#"
			print(string)
			string = "-"*MAP_SIZE[0]
		print(string)

	pat1 = [list(rob) for rob in robots_pos_init]
	pat1 = multinext(pat1, robots_vel, 11)
	pat2 = multinext(pat1, robots_vel, 78)

	for t in range(1000):
		pat2 = multinext(pat2, robots_vel, 103)

		# t = 61
		# 62 iterations
		# x = 89 + 103*62
		affiche(pat2)
		print(t)
		
		input()
""" 	
	quads_sum = [0 for _ in range(4)]
	mid_X = MAP_SIZE[0]//2
	mid_Y = MAP_SIZE[1]//2
	for x in range(MAP_SIZE[0]):
		for y in range(MAP_SIZE[1]):
			if x != mid_X and y != mid_Y:
				if x < mid_X and y < mid_Y:
					quads_sum[0] += robots_map[y][x]
				elif x > mid_X and y < mid_Y:
					quads_sum[1] += robots_map[y][x]
				elif x < mid_X and y > mid_Y:
					quads_sum[2] += robots_map[y][x]
				else:
					quads_sum[3] += robots_map[y][x]
	
	print(quads_sum)
	res1 = 1
	for fact in quads_sum:
		res1 *= fact
	print(res1) """