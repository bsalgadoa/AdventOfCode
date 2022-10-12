'''
--- Day 12: Passage Pathing ---
With your submarine's subterranean subsystems subsisting suboptimally, the only way you're getting out of this cave anytime soon is by finding a path yourself. Not just a path - the only way to know if you've found the best path is to find all of them.

Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves (your puzzle input). For example:

start-A
start-b
A-c
A-b
b-d
A-end
b-end
This is a list of how all of the caves are connected. You start in the cave named start, and your destination is the cave named end. An entry like b-d means that cave b is connected to cave d - that is, you can move between them.

So, the above cave system looks roughly like this:

    start
    /   \
c--A-----b--d
    \   /
     end
Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more than once. There are two types of caves: big caves (written in uppercase, like A) and small caves (written in lowercase, like b). It would be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them multiple times. So, all paths you find should visit small caves at most once, and can visit big caves any number of times.

Given these rules, there are 10 paths through this example cave system:

start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end
(Each line in the above list corresponds to a single path; the caves visited by that path are listed in the order they are visited and separated by commas.)

Note that in this cave system, cave d is never visited by any path: to do so, cave b would need to be visited twice (once on the way to cave d and a second time when returning from cave d), and since cave b is small, this is not allowed.

Here is a slightly larger example:

dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
The 19 paths through it are as follows:

start,HN,dc,HN,end
start,HN,dc,HN,kj,HN,end
start,HN,dc,end
start,HN,dc,kj,HN,end
start,HN,end
start,HN,kj,HN,dc,HN,end
start,HN,kj,HN,dc,end
start,HN,kj,HN,end
start,HN,kj,dc,HN,end
start,HN,kj,dc,end
start,dc,HN,end
start,dc,HN,kj,HN,end
start,dc,end
start,dc,kj,HN,end
start,kj,HN,dc,HN,end
start,kj,HN,dc,end
start,kj,HN,end
start,kj,dc,HN,end
start,kj,dc,end
Finally, this even larger example has 226 paths through it:

fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
How many paths through this cave system are there that visit small caves at most once?

'''

from queue import Queue
from collections import defaultdict

def solution():

    with open("012.txt", 'r') as f:
        nodes_dict = defaultdict(lambda: [] )
        for line in f:
            a, b = line.strip().split("-")
            #print (a, b)
            if a != "start" and b != "end": nodes_dict[b].append(a)
            nodes_dict[a].append(b)

        #print (nodes_dict)


    def paths(node = "start", visited_nodes = set(), path_counter = 0):
        print (f"function paths() called for node: {node}")
        list = nodes_dict[node]
        print (f"list of node {node}: {list}" )

        #path_counter = 0

        while list:
            print(f"poping 1 node from list {list}")
            node = list.pop()
            print("node", node)
            print (f"list {list}")

            if node == "end":
                print (f"found 1 End and will add it to path_counter : {path_counter}")
                path_counter += 1
                print (f"(EEEEEEENDNDDDDDDD +1 ) path_counter : {path_counter}")
                continue

            if node in visited_nodes:
                print (f"node {node} in visited_nodes {visited_nodes}")
                continue

            else:
                print(f"add node {node} to visited_nodes, so ")
                visited_nodes.add(node.lower())
                print("visited_nodes", visited_nodes)
                print (f"then call the function on the node: {node}")
                path_counter += paths(node, visited_nodes, path_counter)

            try:
                print (f"try remove node {node} from visited_nodes :{visited_nodes}")
                visited_nodes.remove(node)
                print ("node removed. ")
            except:
                print("node not in visited_nodes.")
                continue

        print(f"EMPTY LIST go back")
        return path_counter

    return paths("start")

    # def flashes(grid, i , j, flashed_position = 0):
    #     #print ("start flash: \n", np.array(grid))
    #     n = len(grid)
    #     m = len(grid[0])
    #     # set a counter
    #     flashes = 0
    #     # set an empty queue
    #     queue = Queue()
    #     # add the current coordinates pair i, j to the queue
    #     queue.put((i, j))
    #
    #     # while queue is not empty
    #     while not queue.empty():
    #         # we pick an item (coordinates pair)
    #         i, j = queue.get()
    #         # continue if it is out of limitis or the value is zero.
    #         if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0 :
    #             continue
    #         # otherwise we add 1
    #         grid[i][j] += 1
    #         # and:
    #         if grid[i][j] > 9:
    #             # mark the current_position as flashed
    #             grid[i][j] = flashed_position
    #             # add 1 flash to the counter
    #             flashes +=1
    #             # add its 8 neighbors to the queue
    #             queue.put((i+1, j))
    #             queue.put((i-1, j))
    #             queue.put((i, j+1))
    #             queue.put((i, j-1))
    #             queue.put((i+1, j+1))
    #             queue.put((i-1, j+1))
    #             queue.put((i+1, j-1))
    #             queue.put((i-1, j-1))
    #
    #     return flashes
    #
    # return all_flash(grid)

if __name__ == '__main__':
    #solution()
    #import timeit as t
    #print(t.timeit(solution, number=1_000))
    print("solution:", solution())
