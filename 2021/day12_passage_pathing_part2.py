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

Your puzzle answer was 83475.

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

        def paths(node = 'start', allowed_visits = 2):

            total_paths = 0
            possible_paths = Queue()

            for node_conection in node_conections[node]:
                possible_paths.put([node, node_conection])

            while not possible_paths.empty():

                path = possible_paths.get()
                last_node = path[-1]

                for node_conection in node_conections[last_node]:

                    if node_conection == "end":
                        total_paths += 1
                        #print(path)

                    else:
                        if (node_conection.islower() and path.count(node_conection) < allowed_visits) or node_conection.isupper():

                            path_copy = path[:]
                            path_copy.append(node_conection)

                            # now before we add the copy to the Queue
                            # we'll check if there are more than a small cave visited_twice, if not, we added to Queue
                            # note ## is an alternative that keeps track of what small caves were already checked

                            visited_twice = 0
                            ##checked_nodes = list()
                            for node in path_copy:
                                if node.islower() and (path_copy.count(node) == 2):
                                ##if node not in checked_nodes and node.islower() and (path_copy.count(node) == 2):
                                    visited_twice += 1
                                    ##checked_nodes.append(node)

                            if visited_twice/2 < 2 :
                            ##if visited_twice < 2 :
                                possible_paths.put(path_copy)

            return total_paths
    return paths()

if __name__ == '__main__':
    #solution()
    #import timeit as t
    #print(t.timeit(solution, number=1))
    print("solution:", solution())
