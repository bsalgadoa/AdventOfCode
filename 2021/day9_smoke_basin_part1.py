'''
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

Your puzzle answer was 600.

'''


def solution():
    with open("009.txt", 'r') as f:
        counter = int()
        L = list()

        for line in f:
            L.append(list((line.strip())))

        #neste ponto temos um lista L em cada item é uma linha.
        #print (L)

        # agora vamos ver linha a linha ou item a item.
        for n in range(0, len(L)):
            l = L[n]
            #print (l)
            print ('line :', n)

            # --------------------
            # em todas as linhas excepto primeiro e última.
            if n > 0 and n < len(L)-1:
                #print ('line : ', n)
                for i in range(0, len(l)):
                    print (i)
                    # se não for o primeiro nem o ultimo elemento
                    if i > 0 and i < len(l)-1:
                        print ('midle numbers')
                        # vamos comparar com os vizinhos na mesma linha :
                        if l[i] < l[i-1] and l[i] < l[i+1]:
                            #print ('i ', i)
                            #print ('l[i] ', l[i])
                            #print ('l[i-1] ', l[i-1])
                            #print ('l[i+1] ', l[i+1])

                            # e, se for menor, comparamos com a linha acima e abaixo:
                            if l[i] < L[n-1][i] and l[i] < L[n+1][i]:
                                #print ('i ', i)
                                #print ('l[i] ', l[i])
                                #print ('L[n-1][i] ', L[n-1][i])
                                #print ('L[n+1][i] ', L[n+1][i])

                                #print('counter :', counter)
                                #print ('l[i] :', l[i])
                                counter += int(l[i]) + 1
                                #print('counter += int(l[i]) + 1 : ', counter)

                    # se for o primeiro elemento:
                    elif i == 0:
                        print ("elif")
                        # compara com o elemento seguinte e, se for menor, com o elemento na posição acima e abaixo.
                        if l[i] < l[i+1]:
                            # e, se for menor, comparamos com a linha acima e abaixo:
                            if l[i] < L[n-1][i] and l[i] < L[n+1][i]:
                                counter += int(l[i]) + 1

                    # se for o ultimo elemento:
                    #if i == len(l)-1:
                    else:
                        print ("else")
                        # compara com o elemento anterior e, se for menor, com o elemento na posição acima e abaixo.
                        if l[i] < l[i-1]:
                            # e, se for menor, comparamos com a linha acima e abaixo:
                            if l[i] < L[n-1][i] and l[i] < L[n+1][i]:
                                counter += int(l[i]) + 1



            # ------------------------------------------------------------------
            # primeira linha / primeiro item em L.

            elif n == 0:
                #print ('first line : ', n)
                # para cada elemento da primeira linha:
                for i in range(0, len(l)):

                    # se não for o primeiro nem o ultimo elemento
                    if i > 0 and i < len(l)-1:
                        # vamos comparar com os vizinhos na mesma linha :
                        if l[i] < l[i-1] and l[i] < l[i+1]:

                            # e, se for menor, comparamos com a linha abaixo:
                            if l[i] < L[1][i]:
                                counter += int(l[i]) + 1
                                print(l[i])

                    # se for o primeiro elemento:
                    elif i == 0:
                        # compara com o elemento seguinte e, se for menor, com o elemento na posição abaixo.
                        if l[i] < l[i+1] and l[i] < L[1][0]:
                            # então, acordo com as instruções, se for menor que os vizinhos, temos que guardar este numero e adicionar 1
                            counter += int(l[i]) + 1
                            print(l[i])

                    # se for o ultimo elemento:
                    #if i == len(L)-1:
                    else:
                        # compara com o elemento anterior e, se for menor, com o elemento na posição abaixo.
                        if l[i] < l[i-1] and l[i] < L[1][-1]:
                            # então, acordo com as instruções, se for menor que os vizinhos, temos que guardar este numero e adicionar 1
                            counter += int(l[i]) + 1
                            print(l[i])



            # ------------------------------------------------------------------
            # ultima linha / ultimo item em L.
            #if n == len(L)-1:
            else:
                #print ('last line : ', n)
                # para cada elemento da ultima linha:
                for i in range(len(l)):
                    #print('i ', i)
                    #print('n ', n)
                    #print('len l ', len(l))

                    # se não for o primeiro nem o ultimo elemento
                    if i > 0 and i < len(l)-1:
                        # vamos comparar com os vizinhos na mesma linha :
                        if l[i] < l[i-1] and l[i] < l[i+1]:
                            #print ('i ', i)
                            #print ('l[i] ', l[i])
                            #print ('l[i-1] ', l[i-1])
                            #print ('l[i+1] ', l[i+1])
                            # e, se for menor, comparamos com a linha acima:
                            if l[i] < L[-2][i]:
                                counter += int(l[i]) + 1
                                print(l[i])

                    # se for o primeiro elemento:
                    elif i == 0:
                        # compara com o elemento seguinte e, se for menor, com o elemento na posição abaixo.
                        if l[i] < l[i+1] and l[i] < L[-2][0]:
                            # então, acordo com as instruções, se for menor que os vizinhos, temos que guardar este numero e adicionar 1
                            counter += int(l[i]) + 1
                            print(l[i])

                    # se for o ultimo elemento:
                    #elif i == len(L)-1:
                    else:
                        # compara com o elemento anterior e, se for menor, com o elemento na posição acima.
                        if l[i] < l[i-1] and l[i] < L[-2][-1]:
                            # então, acordo com as instruções, se for menor que os vizinhos, temos que guardar este numero e adicionar 1
                            counter += int(l[i]) + 1
                            print(l[i])



            print ("counter :", counter)
            print ('-----------------')



    return counter



if __name__ == '__main__':
    solution()
    #import timeit as t

    #print("solution:", solution())
    #print(t.timeit(solution, number=100))
