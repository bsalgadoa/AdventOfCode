# Kiwi solution of missing values problem:
# 2 lists, one as the same values of the otherbut 2 of them are missing.
# values in list are natural numbers from 1 to n, random, not sequential.
# which values are missing?

# this is an efficient solution from time and memory usage.
# Of course, there are a number of straightforward ways to solve this problem with algorithns and data structures
# but the point is to solve it in one pass.


import random as r
import math as m

complete = set()

# 100 random numbers
while len(complete) < 100:
    if (n := r.randint(1, 1_000_000)) not in complete:
        complete.add(n)

list_B = list(complete)

# Index to remove - first and last
print(f'First: {list_B[0]}')
print(f'Last: {list_B[-1]}')
list_A = list(list_B[1:-1])

# On the same single pass, we sum every number and every square for both lists
# This could be done with sum, going the long way for demonstration purposes
sum_A = 0
square_A = 0
for number in list_A:
    sum_A += number
    square_A += number * number

sum_B = 0
square_B = 0
for number in list_B:
    sum_B += number
    square_B += number * number


# Missing numbers are x and y. To solve a system for 2 unknown variables,
# you need two linearly independent equations (to get a single solution).
# Oh, we just happen to have two of them at hand.
# sum_A + x + y = sum_B
# square_A + x*x + y*y = square_B
# Let sum_B - sum_A be P and square_B - square_A be Q, as they are both natural numbers and their difference will also be
# a natural number. This makes it easier to reason through the equations.
# Replacing those in the above you get
# x + y = P
# x^2+ y^2 = Q
# And given that, you just need to solve it. I like doing x = P - y, but you do you.
# In the end you'll find a quadratic equation for y and x = P - y.
def solve_equations(sum_a: int, square_a: int, sum_b: int, square_b: int) -> tuple[int, int]:
    p = sum_b - sum_a
    q = square_b - square_a

    a = 2  # It will always be 2 - just here for readability
    b = -2 * p  # Same as above
    c = p ** 2 - q

    d = b * b - (4 * a * c)

    alfa = (-b - m.sqrt(d)) / 4
    beta = (-b + m.sqrt(d)) / 4

    # Plug back into x = P - y
    return int(p - alfa), int(p - beta)


print(solve_equations(4, 10, 10, 30))
