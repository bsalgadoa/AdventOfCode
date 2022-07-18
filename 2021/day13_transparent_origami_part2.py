'''
--- Day 13: Transparent Origami ---
--- Part Two ---
Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?

Your puzzle answer was HKUJGAJZ.
'''

import numpy as np
import re

def solution():

    dots_counter = 0
    dots_set = set()

    with open("013.txt", 'r') as f:
        dots_data, folding_data = f.read().strip().split("\n\n")

    #set of tuples (x, y)
    for line in dots_data.strip().splitlines():
        i, j = map(int, line.strip().split(","))
        dots_set.add((i, j))

    # folding instructions
    folding_list = re.findall("[xy]=[0-9]+",folding_data)

    for folding in folding_list:
        axis, position = folding.strip().split("=")
        position = int(position)
        new_dots = set()

        if axis == "x":
            columns = position
            for dot in dots_set:
                i , j = dot[0], dot[1]
                if i > position:
                    new_dots.add((2*position - i, j))
                else:
                    new_dots.add((i, j))
        else:
            rows = position
            for dot in dots_set:
                i , j = dot[0], dot[1]
                if j > position:
                    new_dots.add((i,2*position - j))
                else:
                    new_dots.add((i, j))

        dots_set = new_dots
        dots_counter += len(dots_set)

    matrix = np.zeros((columns, rows))
    for dot in dots_set:
        x, y = dot[0], dot[1]
        matrix[x][y] = "11"

    print(matrix)
    print(np.transpose(matrix))

    return


if __name__ == '__main__':
    solution()
    #import timeit as t
    #print(t.timeit(solution, number=1_000))
    #print("solution: \n", solution())
