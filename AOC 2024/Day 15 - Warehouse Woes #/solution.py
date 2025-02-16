"""
Advent of Code 2024 : Day 15
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
	warehouse, instructions = file.read().strip().split('\n\n')

inst_seq = ''
for line in instructions.split('\n'):
	inst_seq += line

warehouse = [line for line in warehouse.split('\n')]

n = len(warehouse)
m = len(warehouse[0])

walls = [[False for _ in range(m)] for _ in range(n)]
crates = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
	for j in range(m):
		match warehouse[i][j]:
			case "#":
				walls[i][j] = True
			case "O":
				crates[i][j] = True
			case "@":
				rob_pos = [i, j]

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

dir_map = {
	"^": DIRECTIONS[0],
	">": DIRECTIONS[1],
	"v": DIRECTIONS[2],
	"<": DIRECTIONS[3]
}

for c in inst_seq:
	dx, dy = dir_map[c]
	x = rob_pos[0] + dx
	y = rob_pos[1] + dy
	nb_crates = 0
	while module.in_map((x, y), n, m) and crates[x][y]:
		x += dx
		y += dy
		nb_crates += 1
	if module.in_map((x, y), n, m) and (not walls[x][y]):
		rob_pos[0] += dx
		rob_pos[1] += dy
		crates[x][y] = True
		crates[x - dx*nb_crates][y - dy*nb_crates] = False

""" string = ''
for i in range(n):
	for j in range(m):
		if rob_pos == [i, j]:
			string += "@"
		elif walls[i][j]:
			string += "#"
		elif crates[i][j]:
			string += "O"
		else:
			string += "."
	string += "\n"
print(string) """

GPS = 0
for i, line in enumerate(crates):
	for j, crate in enumerate(line):
		if crate:
			GPS += i*100 + j
print(GPS)


# Part 2 --------------------------------------------

new_warehouse = ["" for _ in range(n)]
for i in range(n):
	line = ""
	for c in warehouse[i]:
		match c:
			case "#":
				line += "##"
			case "O":
				line += "[]"
			case ".":
				line += ".."
			case "@":
				line += "@."
m = 2*m
walls = [[False for _ in range(m)] for _ in range(n)]
left_crates = [[False for _ in range(m)] for _ in range(n)]
right_crates = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
	for j in range(m):
		match new_warehouse[i][j]:
			case "#":
				walls[i][j] = True
			case "[":
				left_crates[i][j] = True
			case "]":
				right_crates[i][j] = True
			case "@":
				rob_pos = [i, j]

def no_walls_up(i, j, n=n, m=m, lc=left_crates, rc=right_crates, walls=walls, warehouse=warehouse):
	pass

def no_walls_right(i, j, n=n, m=m, lc=left_crates, rc=right_crates, walls=walls, warehouse=warehouse):
	x = i
	y = j + 1
	res = module.in_map((x, y), n, m)
	if res:
		if walls[x][y]:
			res = False
		elif left_crates[x][y]:
			res = no_walls_right(i, j + 2)
		else:
			res = True
	return res

def no_walls_down(i, j, n=n, m=m, lc=left_crates, rc=right_crates, walls=walls, warehouse=warehouse):
	pass

def no_walls_left(i, j, n=n, m=m, lc=left_crates, rc=right_crates, walls=walls, warehouse=warehouse):
	x = i
	y = j - 1
	res = module.in_map((x, y), n, m)
	if res:
		if walls[x][y]:
			res = False
		elif right_crates[x][y]:
			res = no_walls_right(i, j - 2)
		else:
			res = True
	return res

def no_walls_after(i, j, dx, dy, n=n, m=m, lc=left_crates, rc=right_crates, walls=walls, warehouse=warehouse):
	if dx == 0:
		x = i
		y = j + dy
		res = module.in_map((x, y), n, m) and warehouse[x][y] == "."
		if not res:
			if walls[x][y]:
				res = False
			elif left_crates[x][y]:
				res = no_walls_after(i, y + dy, dx, dy)

	return res

for c in inst_seq:
	dx, dy = dir_map[c]
	if dx == 0:
		pass
	else:
		x = rob_pos[0] + dx
		y = rob_pos[1]
		nb_crates = 0
		while module.in_map((x, y), n, m) and (left_crates[x][y] or right_crates[x][y]):
			x += dx
			nb_crates += 1
		if module.in_map((x, y), n, m) and (not walls[x][y]):
			rob_pos[0] += dx
			for i in range(nb_crates):
				z = x - dx
				if left_crates[z][y]:
					left_crates[x][y] = True
					left_crates[z][y] = False
					righ

			crates[x][y] = True
			crates[x - dx*nb_crates][y - dy*nb_crates] = False