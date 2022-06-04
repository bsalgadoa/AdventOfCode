def solution():
    with open("day4_giant_squid.txt", 'r') as f:
        numbers = f.readline().split(',')
        data = list()
        temp = list()
        # We are getting a 5x5 matrix
        for line in f:
            # if line is empty
            if not line.strip():
                # Se o temp for verdadeiro, ou seja, tiver conteudo
                if temp:
                    # adicionas os temp à data
                    data.append(temp)
                # voltas a colocar o temp vazio
                temp = list()
            # se a linha não for vazia
            else:
                # adiconas ao temp, os numeros na linha.
                temp.append(line.strip().split())

        # aqui estás a adiconar a ultima lista temp criada, à lista data.
        if temp:
            data.append(temp)

        # feito esta iteração de leitura vamos ter uma lista
        # data = [[temp], [temp], [..], [temp]]
        # temp = cartão do bingo
        # temp = [[n, n1, n2, n4, n5],[l2],[l3],[l4],[l5]]

    # a função recebe um cartão e o numero que saiu
    def mark_number(matrix, number):
        # para cada linha na matriz
        for row in matrix:
            # se o numero que saiu estiver na linha
            if number in row:
                # substituimos esse numero do cartão, por um espaço vazio.
                row[row.index(number)] = ''

    # funçao recebe uma matrix de devolve Bool
    def check_matrix(matrix):
        # para cada linha da matrix
        for row in matrix:
            # se for false, ou seja, se todos os items da linha forem ""
            if not any(row):
                # temos linha, o cartão passa a True
                return True
        # o mesmo mas para cada coluna.
        for entry in zip(*matrix):
            if not any(entry):
                return True
        # se não tivermos linha nem coluna, o cartão continua False
        return False

    #marker é uma lista em que cada false é um cartão de bingo
    marker = [False] * len(data)

    # para cada numero que sai
    for n in numbers:
        print(f'Calling {n}')

        # vamos a cada cartão de bingo
        for d in data:
            # passamos o cartão e o numero que saiu pela função mark_number
            mark_number(d, n)

        # ainda dentro do numero que saiu e depois de verificar todos os carões, vamos verificar...
        # para isso
        # vamos atribuir um indice a cada cartao (0, temp1), (1, temp2)
        for index, d in enumerate(data):
            # Se o cartão que estamos a ver ainda for false mas depois de verificar a tiver passado a true
            if not marker[index] and check_matrix(d):
                # significa que com esta extração tivemos uma linha ou uma coluna
                # como tal passamos o cartão a True
                marker[index] = True


            #PARTE 2
            # That was the last one!
            # se todos os cartões forem True, estás no ultimo que deu true.
            if all(marker):
                # asism sendo
                #devolves a ultima saida (int(n)) vezes a soma de todos os numeros desse cartão que ainda não sairam:
                # ou seja para cada linha do cartão, soma o valor de cada posição na linha e se o valor na posição for vazio soma 0.
                return int(n) * sum([sum(map(lambda x: int(x) if x else 0, row)) for row in d])


if __name__ == '__main__':
    print(solution())
