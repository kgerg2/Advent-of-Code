from math import gcd
from copy import deepcopy
import matplotlib.pyplot as plt

def szamol(l, x, y):
    def torol(l, x, y, i, j):
        i -= x
        j -= y
        a = i // gcd(i, j)
        b = j // gcd(i, j)
        while True:
            i += a
            j += b
            if 0 <= x+i < len(l) and 0 <= y+j < len(l[x+i]):
                l[x+i][y+j] = False
            else:
                return
    for i in range(x+1, len(l)):
        for j in range(y, len(l[i])):
            if l[i][j]:
                torol(l, x, y, i, j)
    for i in range(x, len(l)):
        for j in range(y-1, 0, -1):
            if l[i][j]:
                torol(l, x, y, i, j)
    for i in range(x, 0, -1):
        for j in range(y+1, len(l[i])):
            if l[i][j]:
                torol(l, x, y, i, j)
    for i in range(x-1, 0, -1):
        for j in range(y, 0, -1):
            if l[i][j]:
                torol(l, x, y, i, j)
    # kep = [[{(True, True): 5, (False, True): 2}.get(e, 0) for e in zip(lsor, tsor)] for lsor, tsor in zip(l, t)]
    # kep[x][y] = 10
    # plt.imshow(kep)
    # plt.show()
    return sum(map(sum, l))-1

with open(".\\2019\\10\\input.txt") as be:
    l = list(map(lambda x: [a == '#' for a in x.strip()], be.readlines()))

eredm = []
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j]:
            eredm.append(szamol(deepcopy(l), i, j))

print(max(eredm))