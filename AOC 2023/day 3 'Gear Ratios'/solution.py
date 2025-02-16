"""
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he 

can bring you. You go inside.


It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't 

working right now; it'll still be a while before I can fix it." You offer to help.


The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part 

numbers in the engine schematic, it should be easy to work out which part is missing.


The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really 

understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) 

do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other 

number is adjacent to a symbol and so is a part number; their sum is 4361.


Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""

import sys
sys.path.insert(0, 'C:/Users/timot/Documents/Programmation/Python/Advent of code 2023')
import Functions as Fn

eng_lines = Fn.getlines("day 3 'Gear Ratios'/input.txt")

n = len(eng_lines)
p = len(eng_lines[0])

numbers = []
for i in range(n):
    line = eng_lines[i]
    j = 0
    while j < p:
        c = line[j]
        if c.isnumeric():
            nb = c
            k = j+1
            while k < p and line[k].isnumeric():
                nb += line[k]
                k += 1
            numbers.append([i, j, nb])
            j += len(nb)
        else:
            j += 1

validnumbers = []
for number in numbers:
    x, y, nb = number
    valid = False
    for z in range(len(nb)):
        digit = nb[z]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                else:
                    x1 = x+i
                    y1 = y+z+j
                    if x1 < 0 or x1 >= n or y1 < 0 or y1 >= p:
                        continue
                    else:
                        char = eng_lines[x1][y1]
                        if char == "." or char.isnumeric():
                            continue
                        else:
                            valid = True
                            break
            if valid:
                break
        if valid:
            break
    if valid:
        validnumbers.append(number)

SOLUTION_p1 = 0
for x, y, nb in validnumbers:
    SOLUTION_p1 += int(nb)

print(SOLUTION_p1)


"""
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready 

to ascend to the water source.


You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it 

up and the engineer answers.


Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving 

with the other. You're going so slowly that you haven't even left the station. You exit the gondola.


The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part 

numbers. Its gear ratio is the result of multiplying those two numbers together.


This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear 

is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up 

all of the gear ratios produces 467835.


What is the sum of all of the gear ratios in your engine schematic?
"""

stars = []
for i in range(n):
    for j in range(p):
        if eng_lines[i][j] == "*":
            stars.append([i, j])

gears = []
for star in stars:
    x, y = star
    nb_counter = 0
    digit_pos = []

    if x > 0:
        if eng_lines[x-1][y].isnumeric():
            nb_counter += 1
            digit_pos.append([x-1, y])
        else:
            if eng_lines[x-1][y-1].isnumeric():
                nb_counter += 1
                digit_pos.append([x-1, y-1])
            if eng_lines[x-1][y+1].isnumeric():
                nb_counter += 1
                digit_pos.append([x-1, y+1])
    
    if eng_lines[x][y-1].isnumeric():
        nb_counter += 1
        digit_pos.append([x, y-1])

    if eng_lines[x][y+1].isnumeric():
        nb_counter += 1
        digit_pos.append([x, y+1])
    
    if x < n-1:
        if eng_lines[x+1][y].isnumeric():
            nb_counter += 1
            digit_pos.append([x+1, y])
        else:
            if eng_lines[x+1][y-1].isnumeric():
                nb_counter += 1
                digit_pos.append([x+1, y-1])
            if eng_lines[x+1][y+1].isnumeric():
                nb_counter += 1
                digit_pos.append([x+1, y+1])
    
    if nb_counter == 2:
        gear_nbs = []
        for pos in digit_pos:
            for number in validnumbers:
                if pos[0] != number[0]:
                    continue
                else:
                    nb = number[2]
                    for k in range(len(nb)):
                        if pos[1] == number[1] + k:
                            gear_nbs.append(int(nb))
        gears.append(star + gear_nbs)
    

SOLUTION_p2 = 0
for gear in gears:
    SOLUTION_p2 += gear[2]*gear[3]
print(SOLUTION_p2)