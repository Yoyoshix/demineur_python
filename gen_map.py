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

def get_neighbour(values, x, y):
    res = 0
    for i in range( -(x != 0), 1 + (x != len(values) - 1)):
        for j in range( -(y != 0), 1 + (y != len(values[0]) - 1)):
            #print(res, x, y, x + i, y + j)
            res += (values[x + i][y + j] == -1)
    return (res)

#todo generate density
def generate_map(hei, wid, bomb):
    nb_cell = hei * wid
    values = np.zeros((hei, wid))
    nb = [i for i in range(nb_cell)]
    #bomb_pos = []
    #table_density = np.zeros((hei, wid))

    for i in range(bomb):
        #isok = False
        #while (isok == False):
        rdm = nb[np.random.random_integers(0, high = (nb_cell - i))]
        y = rdm // wid
        x = rdm % wid
        nb[rdm] = nb[nb_cell - i - 1]
        #isok = True #((table_density[y][x] / density) >
        values[y][x] = -1

        #for j in range(hei):
        #    for k in range(wid):
        #        table_density[j][k] = (1 - table_density[j][k]) ** (abs(j - y) + abs(k - x))

    #print(values, '\n')
    for i in range(hei):
        for j in range(wid):
            if (values[i][j] != -1):
                values[i][j] = get_neighbour(values, i, j)

    return (values)

print(generate_map(8, 8, int(8*8*0.2)))
