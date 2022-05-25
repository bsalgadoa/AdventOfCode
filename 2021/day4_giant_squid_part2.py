'''
--- Day 4: Giant Squid ---
--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?


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
#print(len(boards_list))


extracted_numbers = list()



for number in all_numbers:
    #print(number)
    extracted_numbers.append((number))
    #print('---------------------------extracted_numbers: ', extracted_numbers)
    if (len(boards_list) > 1):
        for board in boards_list:
            #print('board in boards_list: ', board)
            for row in board:
                #print("row in board: ", row)
                count = 0
                #print('count: ',count)
                for digit in row:
                    #print('number in row: ', digit)
                    if (digit in extracted_numbers):
                        count = count + 1
                        #print('count + 1 : ', count)
                        if count == 5:
                            last_extraction = number
                            winner_board = board
                            winners_row = row
                            boards_list.remove(board)
                            print('updated board list : ',boards_list)
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

    else:
        continue





# # we clean the winners_board format
# #last_winner_board = winners_board[-1]
#
print('winner row',winners_row)
print('winner board',winner_board)
print('last_extraction ', last_extraction)
print('extracted_numbers',extracted_numbers)
# now we need to know the unmarked numbers of the winning card to find the answer
unmarked_numbers = list()
for row in winner_board:
 for number in row:
     if number not in extracted_numbers:
         unmarked_numbers.append(number)

print('unmarked_numbers', unmarked_numbers)

#the answer is the unmarked_numbers times the last extraction
answer = sum(unmarked_numbers)*(last_extraction)
print(answer)
