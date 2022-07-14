'''
--- Day 12: Passage Pathing ---
--- Part Two ---
After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. However, the caves named start and end can only be visited exactly once each: once you leave the start cave, you may not return to it, and once you reach the end cave, the path must end immediately.

Now, the 36 possible paths through the first example above are:

start,A,b,A,b,A,c,A,end
start,A,b,A,b,A,end
start,A,b,A,b,end
start,A,b,A,c,A,b,A,end
start,A,b,A,c,A,b,end
start,A,b,A,c,A,c,A,end
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,d,b,A,c,A,end
start,A,b,d,b,A,end
start,A,b,d,b,end
start,A,b,end
start,A,c,A,b,A,b,A,end
start,A,c,A,b,A,b,end
start,A,c,A,b,A,c,A,end
start,A,c,A,b,A,end
start,A,c,A,b,d,b,A,end
start,A,c,A,b,d,b,end
start,A,c,A,b,end
start,A,c,A,c,A,b,A,end
start,A,c,A,c,A,b,end
start,A,c,A,c,A,end
start,A,c,A,end
start,A,end
start,b,A,b,A,c,A,end
start,b,A,b,A,end
start,b,A,b,end
start,b,A,c,A,b,A,end
start,b,A,c,A,b,end
start,b,A,c,A,c,A,end
start,b,A,c,A,end
start,b,A,end
start,b,d,b,A,c,A,end
start,b,d,b,A,end
start,b,d,b,end
start,b,end
The slightly larger example above now has 103 paths through it, and the even larger example now has 3509 paths through it.

Given these new rules, how many paths through this cave system are there?

'''

from collections import defaultdict
from queue import Queue

def solution():

    with open("012.txt", 'r') as f:
        node_conections = defaultdict(lambda: [] )
        for line in f:
            a, b = line.strip().split("-")

            # Creates a dict of nodes as keys and its conections, as values.
            # Exclude conection start in values and node end as key.
            if a != "end" and b != "start": node_conections[a].append(b)
            if b != "end" and a != "start": node_conections[b].append(a)
            #print (node_conections)

        def paths(node = 'start', allowed_visits = 1):

            total_paths = 0

            possible_paths = Queue()

            for node_conection in node_conections[node]:
                possible_paths.put([node, node_conection])

            while not possible_paths.empty():

                path = possible_paths.get()

                last_node = path[-1]

                # just in case there's a: start-end.
                if node_conection == "end":
                    total_paths += 1
                    continue

                for node_conection in node_conections[last_node]:

                    if node_conection == "end":
                        total_paths += 1
                        #print(element)

                    else:
                        if ((node_conection.islower() and path.count(node_conection) < allowed_visits)) or node_conection.isupper():

                            path_copy = path[:]
                            path_copy.append(node_conection)
                            possible_paths.put(path_copy)

            return total_paths

    return paths()


if __name__ == '__main__':
    #solution()
    #import timeit as t
    #print(t.timeit(solution, number=1_000))
    print("solution:", solution())
