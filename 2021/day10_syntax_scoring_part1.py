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

# to identify what outcome a line will have, we'll remove all the brace pairs (inspired in CodeWars 6ku_valid_braces Kata solution)
# so for each line, we'll replace the brace pairs until there is no more pairs to replace
    # when there is no more pairs to replace, the line will be empty or not
        # if it is empty, the line was legal -> discard.
        # if not empty, the line is incomplete or corrupted:
            # to determine what it is, we check each brace:
                # if we dectect a brance that is in points dict, the line is corrupted:
                    # we add the correspondent points to the counter and move to the next line (whitout checking the next braces).
                # if not, it was incomplete and we move on -> discard.

def solution():

    counter = 0

    points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
    }

    def validBraces(s):
        while '{}' in s or '()' in s or '[]' in s or '<>' in s:
            s=s.replace('{}','')
            s=s.replace('[]','')
            s=s.replace('()','')
            s=s.replace('<>','')

        return s

    with open("010.txt", 'r') as f:

        for line in f:

            line = validBraces(line.strip())

            if line: # "if line" means line == True which means line not empty.
                for brace in line:
                    if brace in points:
                        counter += points[brace]
                        break

    return counter

if __name__ == '__main__':
    #import timeit as t
    #print(t.timeit(solution, number=1_000))
    #solution()
    print("solution:", solution())
