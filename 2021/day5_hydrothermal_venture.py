'''
1. Ler o ficheiro
2. Transformar cada linha do ficheiro num item de uma lista com a seguinte informação [x1, y1, x2, y2]
3. Iterar essa lista e para cada item fazer o modulo da diferença entre pontos do mesmo eixo.
4. Criar uma coordenada para cada um dos pontos dessa diferença.
5. Adicionar cada um desses pontos (x, y) a uma lista "mae"
6. Iterar a lista "mae" e fazer um dict "histogáfico".
'''


def solution():
    with open("005.txt", 'r') as f:
        line_extremes = list()
        for line in f:
            x1, y1, x2, y2 = list(map(int, line.replace(" -> ", ",").split(",")))
            if x1 == x2 or y1==y2:
                line_extremes.append((x1, y1, x2, y2))

        coordinates = list()

        for coordinate in line_extremes:

            x1 = coordinate[0]
            y1 = coordinate[1]
            x2 = coordinate[2]
            y2 = coordinate[3]

            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2)+1):
                    coordinates.append((x1, i))

            if y1 == y2:
                for i in range(min(x1, x2), max(x1, x2)+1):
                    coordinates.append((i, y1))

        coord_dict = dict()

        for coordinate in coordinates:
            # if the key is already in dict we update the value of the key by adding the new one
            if coordinate in coord_dict:
                coord_dict[coordinate] += 1
            # if the key is not in the dict we need to add it
            else: coord_dict[coordinate] = 1

        counter = 0
        for k, v in coord_dict.items():
            if v >= 2:
                counter += 1

    return counter

if __name__ == '__main__':
    print(solution())
