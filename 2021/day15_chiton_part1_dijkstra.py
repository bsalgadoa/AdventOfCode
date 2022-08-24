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

'''
import heapq

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

    distance = [[0] * m for i in range(n)]

    pq = [(0, 0, 0)]
    heapq.heapify(pq)

    while pq:
        d, i, j = heapq.heappop(pq)

        if 0 < distance[i][j] < d: continue
        if not distance[i][j] or distance[i][j] > d : distance[i][j] = d

        if (i, j) == (n-1, m-1):
            return distance[i][j]

        # add neighbors to pq
        for (a, b) in [(1,0),(-1,0),(0,1),(0,-1)]:
            ii = i + a
            jj = j + b
            if 0 <= ii < n and 0 <= jj < m:
                heapq.heappush(pq, (grid[ii][jj] + d , ii, jj))


if __name__ == '__main__':
    #solution()
    print("solution:", solution())
    #import timeit as t
    #print(t.timeit(solution, number=1_00))

import cProfile
#cProfile.run("solution()")
#cProfile.run("solution()", "solution.txt")

import pstats
from pstats import SortKey
#p = pstats.Stats('solution.txt')
#p.strip_dirs().sort_stats(-1).print_stats()
#p.sort_stats(SortKey.CUMULATIVE).print_stats(10)
#p.sort_stats(SortKey.TIME).print_stats(10)
