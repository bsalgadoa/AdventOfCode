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

'''

## To solve this we have to find the the lowest numbers
# we'll have 3 different cases: first line, last line and all the others.
# in each line we'll also have 3 cases: first element, last element and all the others in the middle.
# for every one of these we'll have to check different "neighbors"
# we set the rules for each and
# everytime we found a low point, just add it to a counter + 1.
# return the counter.

def solution():
    with open("009.txt", 'r') as f:
        counter = int()
        L = list()

        for line in f:
            L.append(list((line.strip())))

        # at this point we have a list L where each item is a sublist of each line in file

        # now we'll check line by line or item by item:
        for n in range(0, len(L)):
            l = L[n]

            # all lines/items except the first and the last ones.
            if n > 0 and n < len(L)-1:

                # i = 0
                # while i < len(l): --->> the point was: if we just added a lower point to the counter, we don't need to check the next element because it wont be smaller, so we can just skip i+= 2.
                # howerver this while aproach is 20% slower than the first one.

                for i in range(0, len(l)):

                    # for all the elements except the first  and the last one:
                    if i > 0 and i < len(l)-1:

                        # we'll check it against its neighbors on the same line:
                        if l[i] < l[i-1] and l[i] < l[i+1]:

                            # and if it's smaller, we then check it against its neighbors above and below:
                            if l[i] < L[n-1][i] and l[i] < L[n+1][i]:

                                # if so, we add it to counter + 1
                                counter += int(l[i]) + 1
                                #i += 2

                    # if it's the first one in the line/item:
                    elif i == 0:

                        # we just compare it to the following one:
                        if l[i] < l[i+1]:

                            # and again if it's smaller, we then check it against its neighbors above and below:
                            if l[i] < L[n-1][i] and l[i] < L[n+1][i]:

                                # if so, we add it to counter + 1
                                counter += int(l[i]) + 1
                                #i += 2

                    # now we only have the last element to check:
                    #if i == len(l)-1:
                    else:

                        # at the last one we just have to check it against its previous one:
                        if l[i] < l[i-1]:
                            # and again if it's smaller, we then check it against its neighbors above and below:
                            if l[i] < L[n-1][i] and l[i] < L[n+1][i]:

                                # if so, we add it to counter + 1
                                counter += int(l[i]) + 1
                                #i += 2

                    #i += 1


            # Now we'll check the first line: (the first line purposely apears at this point)
            elif n == 0:

                # for every element in first line:
                for i in range(0, len(l)):

                    # if it's not the first or the last element:
                    if i > 0 and i < len(l)-1:
                        # we check it against its neighbors:
                        if l[i] < l[i-1] and l[i] < l[i+1]:
                            # if it's smaller, we then check it against the element below:
                            if l[i] < L[1][i]:
                                counter += int(l[i]) + 1


                    # if it's the first:
                    elif i == 0:
                        # we just compare it to the following one and the one below:
                        if l[i] < l[i+1] and l[i] < L[1][0]:
                            counter += int(l[i]) + 1

                    # the last element in first line:
                    #if i == len(L)-1:
                    else:
                        if l[i] < l[i-1] and l[i] < L[1][-1]:
                            counter += int(l[i]) + 1

            # Last line/item in L, we repeat the same principle above.
            #if n == len(L)-1:
            else:
                for i in range(len(l)):

                    if i > 0 and i < len(l)-1:
                        if l[i] < l[i-1] and l[i] < l[i+1]:
                            if l[i] < L[-2][i]:
                                counter += int(l[i]) + 1

                    elif i == 0:
                        if l[i] < l[i+1] and l[i] < L[-2][0]:
                            counter += int(l[i]) + 1

                    else:
                        if l[i] < l[i-1] and l[i] < L[-2][-1]:
                            counter += int(l[i]) + 1

    return counter

if __name__ == '__main__':
    #solution()
    #import timeit as t
    print("solution:", solution())
    #print(t.timeit(solution, number=100))
