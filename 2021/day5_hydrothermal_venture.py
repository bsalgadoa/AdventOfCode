'''
# Ler o ficheiro
# Transformar cada linha do ficheiro num item de uma lista com a seguinte informação [x1, y1, x2, y2],
# Caso o item seja uma linha vertical ou horizontal, adiconar a uma lista de extremos de retas.
# Criar uma coordenada para cada um dos pontos entre extremos
# Adicionar cada um desses pontos (x, y) a uma lista "mae"
# Iterar a lista "mae" e devolver o numero de vezes que há valores repetidos
'''

from collections import Counter

def solution():
    with open("005.txt", 'r') as f:
        line_extremes = list()
        for line in f:
            x1, y1, x2, y2 = list(map(int, line.replace(" -> ", ",").split(",")))
            if x1 == x2 or y1==y2:
                line_extremes.append((x1, y1, x2, y2))

        coordinates = list()
        for p in line_extremes:

            x1,y1,x2,y2 = p[0],p[1],p[2],p[3]

            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2)+1):
                    coordinates.append((x1, i))

            else: # y1 == y2:
                for i in range(min(x1, x2), max(x1, x2)+1):
                    coordinates.append((i, y1))


        return sum(int(v) >= 2 for v in Counter(coordinates).values())

    #     coord_dict = dict()
    #     for coordinate in coordinates:
    #         # if the key is already in dict we update the value of the key by adding the new one
    #         if coordinate in coord_dict:
    #             coord_dict[coordinate] += 1
    #         # if the key is not in the dict we need to add it
    #         else: coord_dict[coordinate] = 1
    #
    #     counter = 0
    #     for k, v in coord_dict.items():
    #         if v >= 2:
    #             counter += 1
    #
    # return coord_dict

if __name__ == '__main__':
    print(solution())
