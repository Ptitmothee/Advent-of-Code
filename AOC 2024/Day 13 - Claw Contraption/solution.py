"""
Advent of Code 2024 : Day 13
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
	file_read = file.read().strip()
	machines = file_read.split("\n\n")

	for i, machine in enumerate(machines):
		but_A, but_B, prize = machine.split("\n")
		but_A = but_A.lstrip("Button A: ").split(", ")
		but_B = but_B.lstrip("Button B: ").split(", ")
		prize = prize.lstrip("Prize: ").split(", ")

		but_A = [int(but_A[0].lstrip("X+")), int(but_A[1].lstrip("Y+"))]
		but_B = [int(but_B[0].lstrip("X+")), int(but_B[1].lstrip("Y+"))]
		prize = [int(prize[0].lstrip("X=")), int(prize[1].lstrip("Y="))]

		machines[i] = [but_A, but_B, prize]
	
	""" 
	Equations :
	xP = a*xA + b*xB
	yP = a*yA + b*yB
	tokens = 3*a + b

	P = [A B]*X
	X = ([A B]^(-1))*P

	M = [A B] = xA xB
			    yA yB
	M^-1 = 1/det(M) * [yB -xB]
					  [-yA xA]
	"""

	s = 0
	tok = 0
	for i, machine in enumerate(machines):
		but_A, but_B, prize = machine
		det = but_A[0]*but_B[1] - but_B[0]*but_A[1]
		
		a = (but_B[1]*prize[0] - but_B[0]*prize[1])//det
		get_prize = a >= 0 and a <= 100
		if get_prize:
			b = (-but_A[1]*prize[0] + but_A[0]*prize[1])//det
			get_prize = b >= 0 and b <= 100 and prize[0] == but_A[0]*a + but_B[0]*b and prize[1] == but_A[1]*a + but_B[1]*b
			if get_prize:
				s += 1
				tok += 3*a + b
	print(s, tok)

	s = 0
	tok = 0
	for i, machine in enumerate(machines):
		print(f"Machine {i} :")
		but_A, but_B, prize = machine
		prize[0] += 10000000000000
		prize[1] += 10000000000000
		det = but_A[0]*but_B[1] - but_B[0]*but_A[1]
		
		a = (but_B[1]*prize[0] - but_B[0]*prize[1])//det
		print(a)
		get_prize = a >= 0
		if get_prize:
			print(b)
			b = (-but_A[1]*prize[0] + but_A[0]*prize[1])//det
			get_prize = b >= 0 and prize[0] == but_A[0]*a + but_B[0]*b and prize[1] == but_A[1]*a + but_B[1]*b
			if get_prize:
				s += 1
				tok += 3*a + b
	print(s, tok)