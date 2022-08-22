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

        #print(grid)

    def dijkstra(grid):
        ## set the grid size/limits:
        # number of rows
        n = len(grid)
        #number of columns
        m = len(grid[0])

        # tem que começar no canto sup esquerdo (0,0) e "don't count the risk level of your starting position"
        pq = [(0, 0, 0)] #-> 3-element list including the priority,
        #heapq.heapify(x) -> Transform list x into a heap, in-place, in linear time.
        heapq.heapify(pq)

        checked = list()

        while pq:
            #print (pq)
            # saco o elemento com soma mais baixa
            risk_level, i, j = heapq.heappop(pq)

            # se for o canto inf direito, devolve o risk_level + o seu valor
            if (i, j) == (n-1, m-1):
                print (f"FIM ({i}, {j})")
                return risk_level

            # se o que tiver sacado, estiver fora dos limites, passa ao próximo
            if (i, j) in checked or i < 0 or i == n or j < 0 or j == m:
                continue

            else:
                # adicionar o ponto aos já corridos.
                checked.append((i, j))

                # adicionar os vizinhos ao pq
                # mas e o custo???
                # heapq.heappush(pq, ((grid[i+1][j+1] + risk_level), i + 1, j + 1 ))
                # heapq.heappush(pq, ((grid[i+1][j-1] + risk_level), i + 1, j - 1 ))
                # heapq.heappush(pq, ((grid[i-1][j+1] + risk_level), i - 1, j + 1 ))
                # heapq.heappush(pq, ((grid[i-1][j-1] + risk_level), i - 1, j - 1 ))


                try:
                    heapq.heappush(pq, ((grid[i+1][j] + risk_level), i + 1, j ))
                except:
                    pass

                try:
                    heapq.heappush(pq, ((grid[i-1][j] + risk_level), i - 1, j))
                except:
                    pass

                try:
                    heapq.heappush(pq, ((grid[i][j+1] + risk_level), i, j + 1 ))
                except:
                    pass

                try:
                    heapq.heappush(pq, ((grid[i][j-1] + risk_level), i, j - 1 ))
                except:
                    pass




    return dijkstra(grid)


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



'''
# from: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
Pseudocode
 1    function Dijkstra(Graph, source):
 2
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8
 9      while Q is not empty:
10          u ← vertex in Q with min dist[u]
11          remove u from Q
12
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v] and dist[u] is not INFINITY:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]

'''