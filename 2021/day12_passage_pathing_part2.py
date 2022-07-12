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


def solution():

    with open("012.txt", 'r') as f:
        nodes_dict = defaultdict(lambda: [] )
        for line in f:
            a, b = line.strip().split("-")
            #print (a, b)
            if a != "end" and b != "start": nodes_dict[a].append(b)
            if b != "end" and a != "start": nodes_dict[b].append(a)

            #print (nodes_dict)

    def paths(node = "start", visited_nodes = set(), twice_visited_nodes = set()):

        node_conections = nodes_dict[node]

        if node == "end":
            return 1

        total_paths = 0

        for node in node_conections:

            if node == "end":
                total_paths +=1
                continue

            if node in twice_visited_nodes:
                continue

            if node in visited_nodes:
                twice_visited_nodes.add(node.lower())


            # add the node to the visited nodes list
            visited_nodes.add(node.lower())

            # if the node is not the end, keep looking for one.
            total_paths += paths(node, visited_nodes)

            # remove the node to the visited nodes list
            visited_nodes.discard(node)
            twice_visited_nodes.discard(node)

        return total_paths

    return paths("start")


if __name__ == '__main__':
    #solution()
    #import timeit as t
    #print(t.timeit(solution, number=1_000))
    print("solution:", solution())
