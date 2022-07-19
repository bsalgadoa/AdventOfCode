'''
--- Day 14: Extended Polymerization ---
--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

'''

from collections import Counter, defaultdict

def solution():

    steps = 40

    with open("014.txt", 'r') as f:
        template = str(f.readline().strip())

        pair_insertion_rules = dict()
        for line in f.readlines()[1:]:
            [k, v] = line.strip().split(" -> ")
            pair_insertion_rules[k] = v


    pairs_dict = defaultdict(lambda: 0)
    for i in range(1, (len(template))):
        k = template[i-1] + template[i]
        pairs_dict[k] += 1


    for i in range(steps):
        pairs_counter_perstep = defaultdict(lambda: 0)

        for k in pairs_dict:
            k0, k1 = k

            first_new_pair = k0 + pair_insertion_rules[k]
            second_new_pair = pair_insertion_rules[k] + k1

            pairs_counter_perstep[first_new_pair] += pairs_dict[k]
            pairs_counter_perstep[second_new_pair] += pairs_dict[k]

        pairs_dict = pairs_counter_perstep


    letter_counter = defaultdict(lambda: 0)
    for k in pairs_counter_perstep:
        k0, k1 = k
        letter_counter[k1] += pairs_counter_perstep[k]

    letter_counter[template[0]] += 1

    letter_counter = Counter(letter_counter)
    qt_most_common = max(letter_counter.values())
    qt_least_common = min(letter_counter.values())

    return (qt_most_common - qt_least_common)

if __name__ == '__main__':
    #solution()
    print("solution:", solution())
    #import timeit as t
    #print(t.timeit(solution, number=1_00))

import cProfile
#cProfile.run("solution()")
#cProfile.run("solution()", "solution.txt")

import pstats
from pstats import SortKey
#p = pstats.Stats('solution.txt')
#p.strip_dirs().sort_stats(-1).print_stats()
#p.sort_stats(SortKey.CUMULATIVE).print_stats(10)
#p.sort_stats(SortKey.TIME).print_stats(10)
