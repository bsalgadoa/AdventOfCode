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
#create an empty dict to store the sum of each position
position_dict = dict()


for line in hfile:
    striped_line = line.strip()
    # nest a loop to check in each position of the line and add the value to the dict.
    for i in range(0, len(striped_line)):
        if i in position_dict:
            position_dict[i] = int(position_dict.get(i, 0)) + int(striped_line[i])
        else: position_dict[i] = int(striped_line[i])

#print(position_dict)
#print(len(position_dict))


hfile = open("day3_binary_diagnostic.txt", "r")

bin_list = []
for line in hfile:
    bin_item = (line.strip())
    bin_list.append(list(bin_item))

for sub_list in bin_list:
    for i in range(0, len(sub_list)):
        sub_list[i] = int(sub_list[i])
#print (bin_list)


final_key = [sum((elts)) for elts in zip(*bin_list)]
print (final_key)
print("len: ",len(bin_list))


ox_list = bin_list
co2_list = bin_list
for i in range(0, len(final_key)):
    # if i == 0:
    #     if final_key[i] >= (len(bin_list))/2:
    #         for item in bin_list:
    #             if item[i] == 1:
    #                 ox_list.append(item)
    #             else:
    #                 co2_list.append(item)
    #     else:
    #         for item in bin_list:
    #             if item[i] == 0:
    #                 ox_list.append(item)
    #             else:
    #                 co2_list.append(item)
    #
    # if i>0:
        ox_key = [sum((elts)) for elts in zip(*ox_list)]
        co2_key = [sum((elts)) for elts in zip(*co2_list)]
        # print('i: ',i)
        # print('ox_list: ',ox_list)
        # print('len ox_list',len(ox_list))
        # print('ox_key: ',ox_key)
        # print('----------------------------------------------')
        #print('co2_key: ',co2_key)
        #print('len co2_list', len(co2_list))
        #print(co2_list)
        if ox_key[i] >= (len(ox_list))/2:
            ox_list =[item for item in ox_list if item[i] == 1]
            # print(ox_key[i], ">=", (len(ox_list))/2)
            # for item in ox_list:
            #     print(item)
            #     if item[i] == 0:
            #         print("i =", i,"item[i] =", item[i]," = 0")
            #         #if len(ox_list) > 1:


        else:
            ox_list =[item for item in ox_list if item[i] == 0]
            # print(ox_key[i], "<", (len(ox_list))/2)
            # for item in ox_list:
            #     if item[i] == 1:
            #         print("i =", i,"item[i] =", item[i]," = 1")
            #         #if len(ox_list) > 1:
            #         ox_list.remove(item)

        if co2_key[i] >= (len(co2_list))/2:
            co2_list =[item for item in co2_list if item[i] == 0]
            # print(co2_key[i], ">=", (len(co2_list))/2)
            # for item in co2_list:
            #     print(item)
            #     if item[i] == 0:
            #         print("i =", i,"item[i] =", item[i]," = 0")
            #         #if len(co2_list) > 1:


        else:
            co2_list =[item for item in co2_list if item[i] == 1]
            # print(co2_key[i], "<", (len(co2_list))/2)
            # for item in co2_list:
            #     if item[i] == 1:
            #         print("i =", i,"item[i] =", item[i]," = 1")
            #         #if len(co2_list) > 1:
            #         co2_list.remove(item)






#
#         Se o proximo item for >= total 2 (ou seja 1 predomina ou é empate) :
#             temos que ver item a item da lista ox e cortar 0
#             temos que ir irem a item da lisata co2 e cortar o 1
#
#         Se o proximo item < total/2 (ou seja o 0 predomina):
#             temos que ver item a item da lista ox e cortar 1
# #             temos que ir irem a item da lisata co2 e cortar o 0
#

print("ox_list", ox_list)
print("co2_list: ",co2_list)
