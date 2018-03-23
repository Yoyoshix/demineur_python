import numpy as np
import pygame

def verify_param(value, min, max, name):
    if (type(value) != type(0)):
        print(name, " must be an interger")
        return (0)
    if (value < min):
        print(name, " must be at least ", min)
        return (0)
    if (value > max):
        print(name, " must not exceed ", max)
        return (0)
    return (1)

def get_neighbour(cell_map, x, y):
    res = 0
    for i in range( -(x != 0), 1 + (x != len(cell_map) - 1)):
        for j in range( -(y != 0), 1 + (y != len(cell_map[0]) - 1)):
            #print(res, x, y, x + i, y + j)
            res += (cell_map[x + i][y + j] == -1)
    return (res)

#todo generate density
def generate_map(hei, wid, bomb):
    nb_cell = hei * wid
    cell_map = np.zeros((hei, wid))
    nb = [i for i in range(nb_cell)]

    for i in range(bomb):
        rdm = nb[np.random.random_integers(0, high=(nb_cell - i))]
        y = rdm // wid
        x = rdm % wid
        cell_map[y][x] = -1
        nb[rdm] = nb[nb_cell - i - 1]

    #print(cell_map, '\n')
    for i in range(hei):
        for j in range(wid):
            if (cell_map[i][j] != -1):
                cell_map[i][j] = get_neighbour(cell_map, i, j)

    return (cell_map)

print(generate_map(8, 8, int(8*8*0.2)))

tab = [0,1,2,3]
print(tab[-1])
