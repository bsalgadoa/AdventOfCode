'''
--- Part Two ---
Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
If you only have one number left, stop; this is the rating value for which you are searching.
Otherwise, repeat the process, considering the next bit to the right.
The bit criteria depends on which type of rating value you want to find:

To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
Then, to determine the CO2 scrubber rating value from the same example above:

Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)

'''


# open the file and read each line
hfile = open("day3_binary_diagnostic.txt", "r")

# create an empty list to store the values of each line
bin_list = []
for line in hfile:
    bin_item = (line.strip())
    bin_list.append(list(bin_item))
#print (bin_list)

# convert each digit in item into int instead of str with a nested loop
for item in bin_list:
    for i in range(0, len(item)):
        item[i] = int(item[i])
#print (bin_list)

#now we sum the same index in each line ans store it into a key.
# we'll use this to determine wich number is more frequent in each index.
    #if the value in the key is less than half of the lenght, there are more zeros than ones, and vice-versa.
final_key = [sum((elts)) for elts in zip(*bin_list)]
#print (final_key)
#print("len: ",len(bin_list))

# create to lists that start as the original, in order to exclude items and find the final one.
ox_list = bin_list
co2_list = bin_list

# now we'll go the key an iterate to each position in order to determine what to do
for i in range(0, len(final_key)):
        # now we set a key for each list thath should be updated each time we remove items,
        # in order to determine what to do in the next position (i)
        ox_key = [sum((elts)) for elts in zip(*ox_list)]
        # now if 1 is dominant over 0, and we have more than one item in list:
        if ox_key[i] >= (len(ox_list))/2 and len(ox_list) != 1:
            # we build a list that excludes 0
            # which is building a list with items that only have "1" the position (i) we checked.
            ox_list = list(filter(lambda item: item[i] == 1, ox_list))

        # on the other hand if 0 is dominant over 1, and we have more than one item in list:
        if ox_key[i] < (len(ox_list))/2 and len(ox_list) != 1:
            # we build a list that excludes 1
            # which is building a list with items that only have "0" the position (i) we checked.
            ox_list = list(filter(lambda item: item[i] == 0, ox_list))

        # here we the same for co2 rules:
        co2_key = [sum((elts)) for elts in zip(*co2_list)]
        if co2_key[i] >= (len(co2_list))/2 and len(co2_list) != 1:
            co2_list = list(filter(lambda item: item[i] == 0, co2_list))
        if co2_key[i] < (len(co2_list))/2 and len(co2_list) != 1:
            co2_list = list(filter(lambda item: item[i] == 1, co2_list))

print("ox_list", ox_list)
print("co2_list: ",co2_list)

# the final binary item for every list is found.
# we need to convert it to an string so we can then convert the binary to decimal
ox_str = str()
for i in ox_list[0]:
    ox_str += str(i)
print(ox_str)
# convert the string into decimal integer
dec_ox = int(ox_str, 2)
print(dec_ox)

# the same for co2
co2_str = str()
for i in co2_list[0]:
    co2_str += str(i)
print(co2_str)
dec_co2 = int(co2_str, 2)
print(dec_co2)

# now that we have the decimal integer of each list, we can multiply them and find the answer:
print(dec_ox * dec_co2)
