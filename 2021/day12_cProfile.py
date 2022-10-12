
from collections import defaultdict
from queue import Queue


def solution():

    with open("012.txt", 'r') as f:
        node_conections = defaultdict(lambda: [] )
        for line in f:
            a, b = line.strip().split("-")
            if a != "end" and b != "start": node_conections[a].append(b)
            if b != "end" and a != "start": node_conections[b].append(a)
    return node_conections
if __name__ == '__main__':
    solution()



node_conections = solution()

def alpha(node = "start", visited_nodes = set()):

    total_paths = 0

    for node in node_conections[node]:

        if node == "end":
            total_paths += 1
            continue

        if node in visited_nodes:
            continue
        # add the node to the visited nodes list
        if node.islower():
            visited_nodes.add(node)

        # if the node is not the end, keep looking for one.
        total_paths += alpha(node, visited_nodes)

        # remove the node to the visited nodes list
        visited_nodes.discard(node)

    return total_paths


def beta(node = 'start', allowed_visits = 1):

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

print ("alpha", alpha())
print ("beta", beta())

import timeit as t
#print(t.timeit(alpha, number=1_000))
#print(t.timeit(beta, number=1_000))

import cProfile
import re
cProfile.run("alpha()")
#cProfile.run("beta()")
cProfile.run("beta()", "beta.txt")

import pstats
from pstats import SortKey
p = pstats.Stats('beta.txt')
#p.strip_dirs().sort_stats(-1).print_stats()
p.sort_stats(SortKey.CUMULATIVE).print_stats(10)
#p.sort_stats(SortKey.TIME).print_stats(10)
