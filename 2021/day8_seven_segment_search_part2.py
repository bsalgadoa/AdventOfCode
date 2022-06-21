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

Your puzzle answer was 1084606.

'''

from collections import defaultdict

def solution():
    with open("008.txt", 'r') as f:
        n = 0
        counter = 0
        lenghts = {2: 1, 4: 4, 3: 7, 7: 8}

        for line in f:

            unique_signal = defaultdict(lambda: 0)
            set_one = str()
            set_four = str()
            set_nine = str()
            line_counter = str()

            unique_signal_patern = list(map(str, line.strip().replace(" | ", " ").split(" ")))[:10]
            #print('unique_signal_patern ', unique_signal_patern[:10])

            output_digits = list(map(str, line.strip().replace(" | ", " ").split(" ")))[-4:]
            #print('output_digits ', output_digits[-4:])

            # for every line we'll have to build a unique signal dict to further decode the output digits.
            # to do so we start by looping once to first build the dict with the unique lenghts digits (1, 4, 7, 8)
            for signal in unique_signal_patern:

                if int(len(signal)) in lenghts.keys():
            	      unique_signal[signal] = lenghts[int(len(signal))]

                if int(len(signal)) == 2:
                    set_one = signal

                if int(len(signal)) == 4:
                    set_four = signal


            # now that we know the first ones we'll find the ones with lenght 6: 0, 6 and 9.
            # so we loop again and for 0, 6 and 9:
            for signal in unique_signal_patern:

                if int(len(signal)) == 6:
                    # the 6 is the only one that 1 is not in.
                    if not set(set_one).issubset(set(signal)):
                        unique_signal[signal] = 6
                    # the 9 has to have the 4 inside.
                    elif set(set_four).issubset(set(signal)):
                        unique_signal[signal] = 9
                        set_nine = signal
                    # 0 is the only one left or, if we want, the only that has lenght 6 and has 1 in it and not 4.
                    else:
                        unique_signal[signal] = 0

            # after doing this last loop, we can finally loop one more time for the numbers left, wich are the ones with lenght 5.
            for signal in unique_signal_patern:

                if int(len(signal)) == 5:
                    # last loop we know that the 3 has the 1 in it.
                    if set(set_one).issubset(set(signal)):
                        unique_signal[signal] = 3
                    # we also know that the 9 has the 5 in it.
                    elif set(signal).issubset(set(set_nine)):
                        unique_signal[signal] = 5
                    # and the 2 is the one left.
                    else:
                        unique_signal[signal] = 2


            # Use the unique signal dict to find the 4 digit output
            for digit in output_digits:

                for k in set(unique_signal.keys()):
                    if set(digit) >= set(k) and len(set(digit)) == len(set(k)):
                        line_counter += str(unique_signal[k])

            counter += int(line_counter)

    return counter



if __name__ == '__main__':
    #solution()
    #import timeit as t

    print("solution:", solution())
    #print(t.timeit(solution, number=100))
