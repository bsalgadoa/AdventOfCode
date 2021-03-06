'''
How many measurements are larger than the previous measurement?

For example, suppose you had the following report:

199
200
208
210
200
207
240
269
260
263
This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?

'''

# we first need to make a list of the measurement imputs:

file = open("Day1_Sonar_Sweep_measurements.txt", "r")
ls = []
for line in file:
    numbers = int(line.strip())
    ls.append(numbers)

# then we need to create a function that evaluates if the previous number is smaller than the present measure:
# counter to store how many are bigger.
    # counter note: starts at 1 because the challenge considers that the first measure is bigger.

def larger_than_previous (measurement_list):
    counter = 1
    for i in list(range(1, len(measurement_list))):
        if measurement_list[i-1] < measurement_list[i]:
            counter += 1
    return counter

measurement_list = ls
print(larger_than_previous(measurement_list))
