'''
--- Day 9: Smoke Basin ---
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

# To solve this we have to:
# Find the clusters of numbers limeted by the number 9.
# Then for each cluster, save the area.
# Multiply the 3 biggest areas.


## First, to find clusters I found scipy library and scipy.ndimage package.
## this package contains various functions for multidimensional image processing and the labels in Measurements solve the problem very easily.
## source: https://docs.scipy.org/doc/scipy/reference/ndimage.html#module-scipy.ndimage
from scipy.ndimage import *
import numpy as np

def solution():
    with open("009.txt", 'r') as f:

        heightmap = list()
        ## using scipy.ndimage we need to have a list with 0 and 1 values to use.
        for line in f:
            item = list()
            for i in line.strip():
                ## knowing that our clusters are limeted by 9, we set 9 to 0 and all the others to 1.
                if i != "9":
                    item.append(1)
                else:
                    item.append(0)
            heightmap.append(item)
            #print (heightmap)

            ## at this point we have a 'matrix' of 0 and 1 where the 1 will be our clusters.

        ## now we use scipy.ndimage to label each cluster and give it a number.
        clusters, num = label(heightmap)
        #print ('Clusters:')
        #print(clusters)
        #print(num)

        ## now that we have all the different clusters, we'll find the area of each one
        ## using sum_labels from Measurements from scipy.ndimage.
        clusters_area = sum_labels(heightmap, clusters, index=np.arange(1, clusters.max() + 1)) #np.arange == range
        #print ('clusters_area :')
        #print (clusters_area)

        three_largest_basins = (np.sort(clusters_area)[-3:])
        #print('three_largest_basins :')
        #print(three_largest_basins)

    return int(np.prod(three_largest_basins))

if __name__ == '__main__':
    #solution()
    #import timeit as t

    print("solution:", solution())
    #print(t.timeit(solution, number=1_000))
