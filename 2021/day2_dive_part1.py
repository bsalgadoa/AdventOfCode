'''
--- Day 2: Dive! ---
Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2
Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
'''

# first read the .txt
# take lines and convert it into list
# make an histogram

#convert each line into item in list:

file = open("day2_dive.txt", "r")
directions_list = []
for line in file:
    direction = line.strip()
    directions_list.append(direction)

# split each item in list into sub list:
new_list = []
for i in directions_list:
    new_list.append(i.split())

#print(new_list)


def directions(directions_list):
# create a new dict with to update the 3 keys.
    directions_dict = dict()
# nest a loop in directions_list:
    for direction in directions_list:
        # if the key is already in dict we update the value of the key by adding the new one
        if direction[0] in directions_dict:
            directions_dict[direction[0]] = int(directions_dict.get(direction[0], 0)) + int(direction[-1])

        # if the key is not in the dict we need to add it
        else: directions_dict[direction[0]] = int(direction[-1])

    return directions_dict

print(directions(new_list))

final_directions = directions(new_list)

# find the position by reading the values in the final directions dict.
horizontal_position = final_directions["forward"]
print(horizontal_position)
depth_position = final_directions["down"] - final_directions["up"]
print(depth_position)

# find the answer to the question asked:
print(horizontal_position * depth_position)
print((horizontal_position * depth_position)* horizontal_position)
