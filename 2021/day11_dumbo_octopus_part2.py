'''
--- Day 11: Dumbo Octopus ---
--- Part Two ---
It seems like the individual flashes aren't bright enough to navigate. However, you might have a better option: the flashes seem to be synchronizing!

In the example above, the first time all octopuses flash simultaneously is step 195:

After step 193:
5877777777
8877777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777

After step 194:
6988888888
9988888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888

After step 195:
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern. What is the first step during which all octopuses flash?

Your puzzle answer was 273.

'''

from queue import Queue
#import numpy as np

def solution():

    with open("011.txt", 'r') as f:
        grid = list()
        for line in f:
            line_list = list()
            for i in line.strip():
                line_list.append((int(i)))
            grid.append(line_list)

    #print ("First grid : \n", (np.array(grid)))

    def all_flash(grid):
        # number of rows
        n = len(grid)
        # number of columns
        m = len(grid[0])
        # step counter
        step = 0
        # flashes per step counter
        step_flashes = 0

        #for step in range(1, steps+1):
        while step_flashes != 100:

            step_flashes = 0
            # first increase energy level by 1:
            grid = [[grid[i][j] + 1 for i in range(n)] for j in range(m)]

            # next check for flashes
            # start going row by row
            for i in range(n):
                # start going column by column
                for j in range(m):
                    # if a energy level is at flashing point:
                    if grid[i][j] > 9:
                        # we deal with it:
                        step_flashes += flashes(grid, i, j, 0)
            step += 1
        return step


    def flashes(grid, i , j, flashed_position = 0):
        #print ("start flash: \n", np.array(grid))
        n = len(grid)
        m = len(grid[0])
        # set a counter
        flashes = 0
        # set an empty queue
        queue = Queue()
        # add the current coordinates pair i, j to the queue
        queue.put((i, j))

        # while queue is not empty
        while not queue.empty():
            # we pick an item (coordinates pair)
            i, j = queue.get()
            # continue if it is out of limitis or the value is zero.
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0 :
                continue
            # otherwise we add 1
            grid[i][j] += 1
            # and:
            if grid[i][j] > 9:
                # mark the current_position as flashed
                grid[i][j] = flashed_position
                # add 1 flash to the counter
                flashes +=1
                # add its 8 neighbors to the queue
                queue.put((i+1, j))
                queue.put((i-1, j))
                queue.put((i, j+1))
                queue.put((i, j-1))
                queue.put((i+1, j+1))
                queue.put((i-1, j+1))
                queue.put((i+1, j-1))
                queue.put((i-1, j-1))

        return flashes

    return all_flash(grid)

if __name__ == '__main__':
    #solution()
    #import timeit as t
    #print(t.timeit(solution, number=1_000))
    print("solution:", solution())
