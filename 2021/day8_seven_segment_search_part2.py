
'''

--- Part Two ---
Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3
Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?

'''

from collections import defaultdict

def solution():
    with open("008.txt", 'r') as f:
        n = 0
        counter = 0
        lenghts = {2: 1, 4: 4, 3: 7, 7: 8}

        # unique_signal = {
        # 'cdfbe': 5,
        # 'gcdfa': 2,
        # 'fbcad': 3,
        # 'cefabd': 9,
        # 'cdfgeb': 6,
        # 'cagedb': 0,
        # #'acedgfb': 8,'dab': 7,'eafb': 4,'ab': 1
        # }

        for line in f:
            n = n + 1

            unique_signal = defaultdict(lambda: 0)

            one_segment_up = str()
            one_segment_down = str()
            set_one = str()
            set_four = str()
            line_counter = str()

            unique_signal_patern = list(map(str, line.strip().replace(" | ", " ").split(" ")))[:10]
            #print('unique_signal_patern ', unique_signal_patern[:10])

            output_digits = list(map(str, line.strip().replace(" | ", " ").split(" ")))[-4:]
            #print('output_digits ', output_digits[-4:])

            #print('---')

            for signal in unique_signal_patern:

                if int(len(signal)) in lenghts.keys():
            	      unique_signal[signal] = lenghts[int(len(signal))]

                if int(len(signal)) == 2:
                    #one_segment_up = signal[0]
                    #one_segment_down = signal[-1]
                    set_one = signal
                    #print('set_one ', set_one)
                if int(len(signal)) == 4:
                    set_four = signal
                    #print('set_four ', set_four)



            for signal in unique_signal_patern:

                if int(len(signal)) == 6:

                    if not set(set_one).issubset(set(signal)):
                        unique_signal[signal] = 6

                    elif set(set_four).issubset(set(signal)):
                        unique_signal[signal] = 9
                        set_nine = signal

                    else:
                        unique_signal[signal] = 0

            for signal in unique_signal_patern:

                if int(len(signal)) == 5:

                    if set(set_one).issubset(set(signal)):
                        unique_signal[signal] = 3

                    elif set(signal).issubset(set(set_nine)):
                        unique_signal[signal] = 5

                    else:
                        unique_signal[signal] = 2


            #print('Dict ',dict(unique_signal))
            #print('one_segment_up ', one_segment_up)
            #print('one_segment_down ', one_segment_down)

            #print('----------')

            for digit in output_digits:

                for k in set(unique_signal.keys()):
                    if set(digit) >= set(k) and len(set(digit)) == len(set(k)):
                        line_counter += str(unique_signal[k])

            #print('line_counter ------------------->',n , line_counter)
            #print('counter ', counter)
            counter += int(line_counter)

    return counter



if __name__ == '__main__':
    #solution()
    import timeit as t

    print("solution:", solution())
    #print(t.timeit(solution, number=100))
