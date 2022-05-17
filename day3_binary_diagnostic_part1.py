'''
--- Day 3: Binary Diagnostic ---
The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
'''

# open the file and read each line
# count the lines
# nest a loop to sum the value in each position in each line
# check for each position if the sum is greater than half of the line count.
    # if it is it means we have more 0 than 1
# use that to fine the gamma_rate
# epsilon_rate is the inverse
# convert them to decimal
# multiply and find the answer

# open the file and read each line
hfile = open("day3_binary_diagnostic.txt", "r")
#create an empty dict to store the sum of each position
position_dict = dict()

line_count = 0
for line in hfile:
    # count the lines
    line_count += 1
    striped_line = line.strip()
    # nest a loop to check in each position of the line and add the value to the dict.
    for i in range(0, len(striped_line)):
        if i in position_dict:
            position_dict[i] = int(position_dict.get(i, 0)) + int(striped_line[i])
        else: position_dict[i] = int(striped_line[i])

#print(position_dict)
#print(line_count)

bin_gamma_rate = ""
bin_epsilon_rate = ""

 # check for each position if the sum is greater than half of the line count.
     # if it is it means we have more 0 than 1
 # use that to fine the gamma_rate
 # epsilon_rate is the inverse
for i in position_dict:
    if position_dict[i] < (line_count/2):
        bin_gamma_rate += "0"
        bin_epsilon_rate += "1"
    else:
        bin_gamma_rate += "1"
        bin_epsilon_rate += "0"
#print(bin_gamma_rate)
#print(bin_epsilon_rate)

 # convert them to decimal
dec_gamma_rate = int(bin_gamma_rate, 2)
dec_epsilon_rate = int(bin_epsilon_rate, 2)

#print(dec_gamma_rate)
#print(dec_epsilon_rate)

 # multiply the decimals and find the answer
print(dec_gamma_rate * dec_epsilon_rate)
