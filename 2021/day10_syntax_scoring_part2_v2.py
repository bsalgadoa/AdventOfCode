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

# New approach inspired in https://www.educative.io/answers/the-valid-parentheses-problem and kiwi feedback.

# To determine the outcome, for each striped line:
    # set an empty stack.
    # for each brace in line:
        # if it's an opening brace, we add it to the stack.
        # if not:
            # if stack not empty and brace value matches its key, pop the last one from stack.
            # else, means it's a corrupted line so we must break this loop and move on to the next line.
            # before we break the loop, we empty the stack.

    # Before we move on to the next line, if the stack its not empty, that means that we have an incomplete line.

    # For each incomplete line we calculate its score and add it to total_score list:
        # first we set the line score to zero.
        # reverse the line. (otherwise we are "starting from the end" because we are not using the completing segment but the incompleted one).
        # apply the scoring rules (line score times 5 plus brace point).
        # add the line score to total score list.

# sort the total score list and return the middle value.


def solution():

    total_score = list()

    points = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
    }

    brace_pairs = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
    }

    with open("010.txt", 'r') as f:

        for line in f:

            stack = list()

            for brace in line.strip():
                if brace in '({[<':
                        stack.append(brace)
                else:
                    # if stack not empty and
                    # if top of stack is the "opening brace" for the brace we are checking
                    if stack and stack[-1] == brace_pairs[brace]:
                        # we remove the top
                        stack.pop()

                    # otherwise we are in a corrupted line so
                    # we empty the stack and move on to the next line.
                    else:
                        stack = list()
                        break

            # after the loop, if the stack is not empty, the line is incomplete.
            # and we calculate the line score accordingly with the rules.
            if stack:
                line_score = 0
                reversed_line = stack[::-1]

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
