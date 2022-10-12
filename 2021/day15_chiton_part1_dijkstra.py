'''
--- Day 15: Chiton ---
You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.

The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

What is the lowest total risk of any path from the top left to the bottom right?

Your puzzle answer was 592.
'''

import heapq
from collections import defaultdict

def solution():

    with open("015.txt", 'r') as f:
        grid = list()
        for line in f:
            line_list = list()
            for i in line.strip():
                line_list.append((int(i)))
            grid.append(line_list)

    n = len(grid)
    m = len(grid[0])

    d_grid = [[0] * m for i in range(n)]
    d_dict = defaultdict(int)

    pq = [(0, 0, 0)]
    heapq.heapify(pq)

    while pq:
        d, i, j = heapq.heappop(pq)

        d_grid[i][j] = d

        for (a, b) in [(1,0),(0,1),(-1,0),(0,-1)]:
            ii = i + a
            jj = j + b

            # if node neighbors are inside matrix and
            if (0 <= ii < n and 0 <= jj < m):
                # if the neighbor was not visited yet or if was, but we now found a shorter path (lower distance)
                if not d_dict[(ii, jj)] or grid[ii][jj] + d < d_dict[(ii, jj)]:
                    # push neighbor to pq
                    heapq.heappush(pq, (grid[ii][jj] + d, ii, jj))
                    # update the neighbor distance value in dict
                    d_dict[(ii, jj)] = grid[ii][jj] + d

    return d_grid[n-1][m-1]

if __name__ == '__main__':
    #solution()
    print("solution:", solution())
    #import timeit as t
    #print(t.timeit(solution, number=1_00))

import cProfile
cProfile.run("solution()")
#cProfile.run("solution()", "solution.txt")

import pstats
from pstats import SortKey
#p = pstats.Stats('solution.txt')
#p.strip_dirs().sort_stats(-1).print_stats()
#p.sort_stats(SortKey.CUMULATIVE).print_stats(10)
#p.sort_stats(SortKey.TIME).print_stats(10)

## NOTES:
# also need to check the neighbor above (-1,0) and left (0,-1)
# otherwise it will miss the right solution when the shortest path is something like this for example:
# 19999
# 19111
# 11191
# 99991
#
# or
#
# 11111
# 99991
# 11111
# 19999
# 11111