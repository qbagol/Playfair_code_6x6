import numpy as np

playfair_grid = np.chararray((6, 6))

def key_square_fill(key_simplefied):
    lit = 0
    for i in range(6):
        for j in range(6):
            if i * j > 25:
                break;
            else:
                playfair_grid[i, j] = key_simplefied[lit]
                lit = lit + 1

def coordinates(char):
    cord = np.zeros(2)
    for i in range(6):
        for j in range(6):
            x = char
            x = str.encode(x)
            if playfair_grid[i, j] == x:
                return i, j

def code(cord1, cord2):
    if cord1[0] == cord2[0]:
        c1 = cord1[1]
        c2 = cord2[1]
        if cord1[1] == 5:
            c1 = -1
        if cord2[1] == 5:
            c2 = -1
        char1 = playfair_grid[cord1[0], c1 + 1]
        char2 = playfair_grid[cord2[0], c2 + 1]
        text = char1.decode() + char2.decode()
    elif cord1[1] == cord2[1]:
        c1 = cord1[0]
        c2 = cord2[0]
        if cord1[0] == 5:
            c1 = -1
        if cord2[0] == 5:
            c2 = -1
        char1 = playfair_grid[c1 + 1, cord1[1]]
        char2 = playfair_grid[c2 + 1, cord2[1]]
        text = char1.decode() + char2.decode()
    else:
        char1 = playfair_grid[cord1[0], cord2[1]]
        char2 = playfair_grid[cord2[0], cord1[1]]
        text = char1.decode() + char2.decode()
    return text;

def decode(cord1, cord2):
    if cord1[0] == cord2[0]:
        c1 = cord1[1]
        c2 = cord2[1]
        if cord1[1] == 0:
            c1 = 6
        if cord2[1] == 0:
            c2 = 6
        char1 = playfair_grid[cord1[0], c1 - 1]
        char2 = playfair_grid[cord2[0], c2 - 1]
        text = char1.decode() + char2.decode()
    elif cord1[1] == cord2[1]:
        c1 = cord1[0]
        c2 = cord2[0]
        if cord1[0] == 0:
            c1 = 6
        if cord2[0] == 0:
            c2 = 6
        char1 = playfair_grid[c1 - 1, cord1[1]]
        char2 = playfair_grid[c2 - 1, cord2[1]]
        text = char1.decode() + char2.decode()
    else:
        char1 = playfair_grid[cord1[0], cord2[1]]
        char2 = playfair_grid[cord2[0], cord1[1]]
        text = char1.decode() + char2.decode()
    return text;