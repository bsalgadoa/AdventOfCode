'''
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

Your puzzle answer was 600.

--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?

Your puzzle answer was 987840.
'''

## Trying a new approach with the flood fill algorithm instead of directly using scipy.ndimage library:
# references:
    # kiwi
    # https://en.wikipedia.org/wiki/Flood_fill#Walk-based_filling_(Fixed-memory_method)
    # https://www.youtube.com/watch?v=O-6Z4Yj1sFY
    # https://www.youtube.com/watch?v=VuiXOc81UDM

## Approach:
# 1 - read the file, make a grid (matrix/list of lists).
# 2 - set lists for lowest_points (part1) and clusters_areas (part2) to later return the solution for both parts.
# 3 - write a flood fill function:
    # this function receives a grid and
    # start going cell by cell and check if didn't hit a limit (9) or a cell that was visited before ('X'):
        # if not, it means that we are in a new cluster and we run the cluster_fill function:
            # this cluster_fill function receives a grid, 2 points: i and j, and eventually the new char/color that will replace the cells (if not, it's set to 'X').
            # sets the cluster area to zero
            # sets the bottom_point as the current_position
            # sets an empty queue
            # add the current point to that queue
            # while the queue is not empty, we take a point:
                # check it and if it is not a limit or a previous visited cell:
                    # check if this point lower than the actual bottom_point:
                        #if so, set the bottom_point to current position value
                    # increase area counter
                    # change the current_position content to 'X'
                    # add the 4 neighbors to the queue
                # move to next point
            # before returning to flood_fill, append bottom_point and current_area.
# 4 - calculate and return the solution based on lists set at #2.

from queue import Queue

def solution():

    with open("009.txt", 'r') as f:
        grid = list()
        for line in f:
            line_list = list()
            for i in line.strip():
                line_list.append((int(i)))
            grid.append(line_list)
        #print(grid)

    lowest_points = list()
    clusters_areas = list()

    def flood_fill(grid):
        ## set the grid size/limits:
        # number of rows
        n = len(grid)
        #number of columns
        m = len(grid[0])
        #print (np.array(grid))

        # start going row by row
        for i in range(n):
            # start going column by column
            for j in range(m):
                # if the point that we are is not a limit or a previous visited one
                if not grid[i][j] in [9,'X']:
                    # we are in a new cluster and start to fill it
                    cluster_fill(grid, i, j, 'X')

        #print (np.array(grid))
        #print ('END lowest_points :', lowest_points)
        #print ('END clusters_areas :', clusters_areas)

        part1_solution = sum(lowest_points) + len(lowest_points)
        print('Part 1 solution: ',part1_solution)

        top3_areas = sorted(clusters_areas)[-3:]
        part2_solution = top3_areas[0]*top3_areas[1]*top3_areas[2]
        print('Part 2 solution: ',part2_solution)


    def cluster_fill(grid, i , j, checked_position = 'X'):
        n = len(grid)
        m = len(grid[0])

        current_position = grid[i][j]
        # set the lowest point as the current_position
        bottom_point = current_position
        # set current cluster area to zero
        current_area = 0

        ## dont't need to check this condintion because, in this case, to enter def cluster_fill it was already checked.
        # if current_position == checked_position:
        #    return

        # set an empty queue
        queue = Queue()
        # add the current coordinates pair i, j to the queue
        queue.put((i, j))
        # while queue is not empty
        while not queue.empty():
            # we pick an item (coordinates pair)
            i, j = queue.get()
            # if we meet the grid limit, a border or if we find a position that was previous check, get the next item in queue
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] in [9, 'X']:
                continue

            # if not, that means that we are still in the same cluster
            else:
                # check if this point is a new bottom_point
                if grid[i][j] < bottom_point:
                    bottom_point = grid[i][j]
                # increase area counter
                current_area += 1
                # mark the current_position as checked
                grid[i][j] = checked_position
                # add its 4 neighbors to the queue
                queue.put((i+1, j))
                queue.put((i-1, j))
                queue.put((i, j+1))
                queue.put((i, j-1))

        ## after crossing the entire cluster:
        # add the bottom_point to the lowest_points list
        lowest_points.append(bottom_point)
        # add the cluster area to clusters_areas list
        clusters_areas.append(current_area)

    return flood_fill(grid)

if __name__ == '__main__':
    solution()
    #import timeit as t
    #print("solution:", solution())
    #print(t.timeit(solution, number=100))
