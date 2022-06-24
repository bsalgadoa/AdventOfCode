'''
--- Day 10: Syntax Scoring ---
--- Part Two ---
Now, discard the corrupted lines. The remaining lines are incomplete.

Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in the line.

You can only use closing characters (), ], }, or >), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.

In the example above, there are five incomplete lines:

[({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})].
[(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}).
(((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))).
{<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}>.
<{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}>.
Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the completion string character-by-character. Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:

): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.
So, the last completion string above - ])}> - would be scored as follows:

Start with a total score of 0.
Multiply the total score by 5 to get 0, then add the value of ] (2) to get a new total score of 2.
Multiply the total score by 5 to get 10, then add the value of ) (1) to get a new total score of 11.
Multiply the total score by 5 to get 55, then add the value of } (3) to get a new total score of 58.
Multiply the total score by 5 to get 290, then add the value of > (4) to get a new total score of 294.
The five lines' completion strings have total scores as follows:

}}]])})] - 288957 total points.
)}>]}) - 5566 total points.
}}>}>)))) - 1480781 total points.
]]}}]}]}> - 995444 total points.
])}> - 294 total points.
Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the middle score. (There will always be an odd number of scores to consider.) In this example, the middle score is 288957 because there are the same number of scores smaller and larger than it.

Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?

Your puzzle answer was 3969823589.
'''

## For each line will have 3 possible outcomes and for each one we'll take diferent action:
    # legal () -> discard
    # corrupted (] -> discard
    # incomplete (() -> calculate the points for the completing segment, accordingly with the rules given.

# First, to determine line outcome we call the function validBraces (inspired in CodeWars 6ku_valid_braces Kata solution, replaces the brace pairs until there is no more pairs to replace):
    # the function returns a string:
        # if it is empty -> discard.
        # if not, the line is incomplete or corrupted:
            # to determine what which one it is, we've created an incomplete bool function:
                # this function receives the string outcome from the def validBraces and checks if there's any closing brace in there:
                # if there is, it's a corrupted line (False), otherwise is an incomplete one (True).

# Now for each incomplete line we calculate its score and add it to total_score list:
    # first we set the line score to zero.
    # reverse the line. (otherwise we are "starting from the end" because we are not using the completing segment but the incompleted one).
    # apply the scoring rules (line score times 5 plus brace point).
    # add the line score to total score list.

# sort the total score list and return the middle value.

def solution():

    points = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
    }

    total_score = list()

    closing_braces = ')}]>'

    def validBraces(s):
        while '{}' in s or '()' in s or '[]' in s or '<>' in s:
            s=s.replace('{}','')
            s=s.replace('[]','')
            s=s.replace('()','')
            s=s.replace('<>','')
        return s

    def incomplete(s):
        return not any(brace in s for brace  in closing_braces)

    with open("010.txt", 'r') as f:

        for line in f:
            line = validBraces(line.strip())

            if line and incomplete(line): # if line not empty after removing the brace pairs and if it's incomplete and not corrupted:
                line_score = 0
                reversed_line = line[::-1]

                for brace in reversed_line:
                    line_score = (line_score * 5) + points[brace]

                total_score.append(line_score)

        total_score.sort()

    return total_score[int((len(total_score)/2))]

if __name__ == '__main__':
    import timeit as t
    #print(t.timeit(solution, number=2_0000))
    #solution()
    print("solution:", solution())
