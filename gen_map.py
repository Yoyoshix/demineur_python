import numpy as np

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

def generate_map(hei, wid, bomb, density):
    values = np.zeros((hei, wid))
    bomb_pos = np.empty((bomb))
    print(values)
    print(bomb_pos)

    for i in range(len(bomb)):
        tmp = np.random.random_integers(bomb - i)
    # todo generate bomb position with epic random algo

generate_map(10, 10, 0, 0)
