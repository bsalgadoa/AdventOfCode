'''
--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?

Your puzzle answer was 22116.
'''

from collections import Counter

def solution():
    with open("005.txt", 'r') as f:
        # list of 2D lines.
        lines = list()
        for line in f:
            x1, y1, x2, y2 = list(map(int, line.replace(" -> ", ",").split(",")))
            #if x1 == x2 or y1==y2: Part 1 filter.
            #every line needs at least 2 points to be a line.
            lines.append((x1, y1, x2, y2))

        # list to add and save all the point coordinates that make each line.
        coordinates = list()

        for line in lines:
            # every number in line it's a coordinate.
            x1,y1,x2,y2 = line[0],line[1],line[2],line[3]

            # vertical lines
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2)+1):
                    coordinates.append((x1, i))

            # horizontal lines
            if y1 == y2:
                for i in range(min(x1, x2), max(x1, x2)+1):
                    coordinates.append((i, y1))

            # Diagonal descending line
            if (x1 > x2 and y1 < y2) or (x1 < x2 and y1 > y2):
                # create 2 lists of the x and y coordinates
                x_coord = (range(min(x1,x2), max(x1,x2)+1))
                y_coord = (range(max(y1,y2), min(y1,y2)-1, -1))
                # append the coordinates of each point to the main coordinates list
                for x, y in zip(x_coord, y_coord):
                    coordinates.append((x, y))

            # Diagonal ascending line
            if (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2):
                x_coord = (range(min(x1,x2), max(x1,x2)+1))
                y_coord = (range(min(y1,y2), max(y1,y2)+1))

                for x, y in zip(x_coord, y_coord):
                    coordinates.append((x, y))

        # return the number of points that are crossed by more than 1 line:
        return sum(int(v) >= 2 for v in Counter(coordinates).values())



if __name__ == '__main__':
    print(solution())
