'''
--- Part Two ---
Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539 lanternfish!

How many lanternfish would there be after 256 days?

Your puzzle answer was 1653250886439.

Both parts of this puzzle are complete! They provide two gold stars: **
'''
#from collections import defaultdict, Counter
#
# def solution_1():
#     with open("006.txt", 'r') as f:
#         fish = defaultdict(lambda: 0)
#         for i in f.readline().strip().split(','):
#             fish[i] +=1
#
#         return dict(fish)

def solution_2():
    with open("006.txt", 'r') as f:
        numbers = [int(i) for i in f.readline().strip().split(',')]
        #print(numbers)
        # create a list with the count of fish per day.
        fish = [numbers.count(i) for i in range(9)]
        #print(fish)

        for day in range(256):
            # the fish at 0 becomes 6
            #print(day, fish)
            fish[7] += fish[0]
            #print(fish)
            # the fish at 0 will generate the same amount at 8, so just rotate the list.
            fish.append(fish.pop(0))
            #print(fish)
            #print('-----')

        return sum(fish)

def solution_3():
    with open("006.txt") as f:
        counts = list(map(f.read().count, "012345678"))

    for i in range(256):
        counts[(i + 7) % 9] += counts[i % 9]
        #if i + 1 in (80,256):
    return (sum(counts))


if __name__ == '__main__':
    import timeit as t
    #print(t.timeit(solution_1, number=100))
    #print(solution_1())
    print(t.timeit(solution_2, number=100))
    print(solution_2())
    print(t.timeit(solution_3, number=100))
    print(solution_3())
