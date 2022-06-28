'''
--- Day 10: Syntax Scoring ---
You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:

Syntax error in navigation subsystem on line: all of them
All of them?! The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).

The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

If a chunk opens with (, it must close with ).
If a chunk opens with [, it must close with ].
If a chunk opens with {, it must close with }.
If a chunk opens with <, it must close with >.
So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.

Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]). Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

For example, consider the following navigation subsystem:

[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

{([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
[[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
[{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
[<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
<{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.
Stop at the first incorrect closing character on each corrupted line.

Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

): 3 ,
]: 57 points.
}: 1197 points.
>: 25137 points.
In the above example, an illegal ) was found twice (2*3 = 6 points), an illegal ] was found once (57 points), an illegal } was found once (1197 points), and an illegal > was found once (25137 points). So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!

Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?

Your puzzle answer was 265527.
'''

## For each line will have 3 possible outcomes and for each one we'll take diferent action:
    # legal () -> discard
    # incomplete (() -> discard
    # corrupted (] -> identify the brace that corrupted the line and add the correspondent points to a counter.

# New approach inspired in https://www.educative.io/answers/the-valid-parentheses-problem and kiwi feedback.

# For each striped line:
    # set an empty stack.
    # for each brace in line:
        # if it's an opening brace, add it to the stack.
        # if not:
            # if stack not empty and brace value matches its key, pop the last one from stack.
            # else, means it's a corrupted line so we must add the correspondent points and move on to the next line.


def solution():

    counter = 0

    points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
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
                    # if top of stack is diferent from "opening brace" of the brace we are checking:
                    if stack and stack.pop() != brace_pairs[brace]:
                        # we get the correspondent points for the invalid brace
                        # and move on to the next line.
                        counter += points[brace]
                        break

                    ## note: by checking stack.pop() in the if statement, we are "poping" the top of the stack
                    ## and that's why it also works when brace that we are checkig matches the last one.

        return counter


if __name__ == '__main__':
    #import timeit as t
    #print(t.timeit(solution, number=1_000))
    #solution()
    print("solution:", solution())
