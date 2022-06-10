import numpy as np

data = [int(x) for x in open("007.txt", "r").read().split(",")]
print(data)
median = np.median(data)
print(f"Part 1: The shortest amount of fuel spend is {sum([abs(median - i) for i in data])}")

def sum_1_to_n(n): return n * (n + 1) / 2

mean = int(np.mean(data))
print(f"Part 2: The shortest amount of fuel spend is {sum([sum_1_to_n(abs(mean - i)) for i in data])}")
