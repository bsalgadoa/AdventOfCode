'''
--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?
'''

# For each new number that comes out
    # Save that number in a list
    # For every card that we have (5x5):
        # Check every line:
            # If there's any number that is not in the numbers list:
                # move to next line.
            # If not, store the count of numbers in list and if its 5, it means that that line is a bingo:
                # store that line and the card id in a winner list
    # If winner list is not empty, stop checking and return row and card.

#import numpy as np

with open('day4_giant_squid.txt', 'r') as fhand:
    all_numbers = list(map(int, fhand.readline().split(',')))
    #print(all_numbers)

    ## solution through matrix
    #boards = [np.mat(board.replace("\n", ";")) for board in fhand.read()[1:-1].split("\n\n")]
    ##boards = (line in fhand.read()[1:-1].split("\n\n"))
    #print (boards)

    # creates a list of every line
    boards = []
    for line in fhand:
        boards.append(list(map(int, line.split())))
    # remove blanck lines
    boards = list(filter(lambda item: item != [], boards))
    #print (boards)

    # create a list of every card
    boards_list = list()
    board_size = 5
    for i in range(0, len(boards), board_size):
        boards_list.append(boards[i:i+board_size])

#print(boards_list)



extracted_numbers = list()
winners_board = list()
winners_row = list()

for number in all_numbers:
    # add it to extracted_numbers list
    extracted_numbers.append(number)

    # for each extraction
    for extraction in extracted_numbers:
        # go to every board in board list
        for board in boards_list:
            # then to every row in each board
            for row in board:
                # set the counter to 0
                count = 0
                # for every number in row:
                for i in row:
                    # if that number is in the extracted_numbers list:
                    if i in extracted_numbers:
                        # add 1 to count
                        count += 1
                        # if the counter is at 5 we have a bingo and must store the row and the board and break all the loops
                        if count == 5:
                            winners_board.append(board)
                            winners_row.append(row)
                            break
                        else:
                            continue
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break

# we clean the winners_board format
winners_board = winners_board[0]

print('winner row',winners_row)
print('winner board',winners_board)
print('extracted_numbers ', extracted_numbers)

# now we need to know the unmarked numbers of the winning card to find the answer
unmarked_numbers = list()
for row in winners_board:
    for number in row:
        if number not in extracted_numbers:
            unmarked_numbers.append(number)

print('unmarked_numbers', unmarked_numbers)

# the answer is the unmarked_numbers times the last extraction
answer = sum(unmarked_numbers)*(extracted_numbers[-1])
print(answer)
