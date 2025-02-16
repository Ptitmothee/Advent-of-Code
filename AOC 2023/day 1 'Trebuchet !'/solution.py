""" 
Part 1 : 
You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map 

looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") 

when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").


As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf 

who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.


The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves 

now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a 

single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""

import sys
sys.path.insert(0, 'C:/Users/timot/Documents/Programmation/Python/Advent of code 2023')
import Functions as Fn

calib_lines = Fn.getlines("day 1 'Trebuchet !'/input.txt")

# Solution 1 : 57346
def part1(lines):
    n = len(lines)
    calib_values_digits = [""]*n
    for i in range(n):
        for char in lines[i]:
            if 49 <= ord(char) and ord(char) <= 57:
                calib_values_digits[i] += char

    calib_values = [0]*n
    for i in range(n):
        value_str = calib_values_digits[i]
        m = len(value_str)
        calib_values[i] = int(value_str[0] + value_str[-1])

    return sum(calib_values)

SOLUTION_p1 = part1(calib_lines)
print(SOLUTION_p1)


"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: 

one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".


Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

# Solution 2 : 57345
def part2(lines):
    valid_digits = [str(i) for i in range(1, 10)] + ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    sum = 0
    for line in lines:
        digits = ""
        i = 0
        n = len(line)
        while i < n:
            for d_str in valid_digits:
                m = len(d_str)

                if n-i-m < 0:
                    continue

                else:
                    isdigit = True
                    for j in range(m):
                        if line[i+j] != d_str[j]:
                            isdigit = False
                            break

                    if isdigit:
                        if m == 1:
                            digits += d_str
                        else:
                            match d_str:
                                case "one":
                                    digits += "1"
                                case "two":
                                    digits += "2"
                                case "three":
                                    digits += "3"
                                case "four":
                                    digits += "4"
                                case "five":
                                    digits += "5"
                                case "six":
                                    digits += "6"
                                case "seven":
                                    digits += "7"
                                case "eight":
                                    digits += "8"
                                case "nine":
                                    digits += "9"

                        break

            i += 1

        value = int(digits[0] + digits[-1])
        print(line, value)
        sum += value

    return sum

SOLUTION_p2 = part2(calib_lines)
print(SOLUTION_p2)