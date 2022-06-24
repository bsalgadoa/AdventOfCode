def solution():
with open("006.txt", "r") as f:
fish = list(map(int, f.readline().strip().split(",")))

# Naive solution will not work for 256 generations, obviously.
# We need to compute how much spawn does a fish generate giving his starting status
# If you spawn in k%7, your offspring will spawn for the first time in k+2%7

adults = [0, 0, 0, 0, 0, 0, 0]
nursery = [0, 0, 0, 0, 0, 0, 0]
juveniles = [0, 0, 0, 0, 0, 0, 0]

# Initial setup
for f in fish:
adults[f % 7] += 1

print("Starting point", adults)

generations = 0
goal = 255

while generations < goal:
generations += 1
# Determine who is spawning now
spawner = generations % 7
# We retrieve the juveniles from the previous round that are now ready to spawn
adults[spawner] += juveniles[spawner]
# We clear the juvenile tank
juveniles[spawner] = 0
# We spawn to the nursery
nursery[(spawner + 2) % 7] += adults[spawner]
# We replenish our juveniles
juveniles[spawner] += nursery[spawner]
# Clean the nursery
nursery[spawner] = 0

return sum(adults) + sum(nursery) + sum(juveniles)
