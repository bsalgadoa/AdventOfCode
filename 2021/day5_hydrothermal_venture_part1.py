'''
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

Your puzzle answer was 6225.
'''


'''
# Ler o ficheiro
# Transformar cada linha do ficheiro num item de uma lista com a seguinte informação [x1, y1, x2, y2],
# Caso o item seja uma linha vertical ou horizontal, adiconar a uma lista de extremos de retas.
# Criar uma coordenada para cada um dos pontos entre extremos
# Adicionar cada um desses pontos (x, y) a uma lista "mae"
# Iterar a lista "mae" e devolver o numero de vezes que há valores repetidos
'''

from collections import Counter

def solution():
    with open("005.txt", 'r') as f:
        lines = list()
        for line in f:
            x1, y1, x2, y2 = list(map(int, line.replace(" -> ", ",").split(",")))
            if x1 == x2 or y1==y2:
                lines.append((x1, y1, x2, y2))

        coordinates = list()
        for p in lines:

            x1,y1,x2,y2 = p[0],p[1],p[2],p[3]

            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2)+1):
                    coordinates.append((x1, i))

            else: # y1 == y2:
                for i in range(min(x1, x2), max(x1, x2)+1):
                    coordinates.append((i, y1))


        return sum(int(v) >= 2 for v in Counter(coordinates).values())

    #     coord_dict = dict()
    #     for coordinate in coordinates:
    #         # if the key is already in dict we update the value of the key by adding the new one
    #         if coordinate in coord_dict:
    #             coord_dict[coordinate] += 1
    #         # if the key is not in the dict we need to add it
    #         else: coord_dict[coordinate] = 1
    #
    #     counter = 0
    #     for k, v in coord_dict.items():
    #         if v >= 2:
    #             counter += 1
    #
    # return coord_dict

if __name__ == '__main__':
    print(solution())
