import numpy as np

with open(".\\2019\\3\\input.e") as be:
    l1 = list(map(lambda x: (x[0], int(x[1:])), be.readline().split(',')))
    l2 = list(map(lambda x: (x[0], int(x[1:])), be.readline().split(',')))

maxx = maxy = minx = miny = 0

x = y = 0

for ir, h in l1:
    if ir == 'R':
        x += h
    elif ir == 'L':
        x -= h
    elif ir == 'U':
        y += h
    elif ir == 'D':
        y -= h
    maxx = max(x, maxx)
    maxy = max(y, maxy)
    minx = min(x, minx)
    miny = min(y, miny)

x = y = 0

for ir, h in l2:
    if ir == 'R':
        x += h
    elif ir == 'L':
        x -= h
    elif ir == 'U':
        y += h
    elif ir == 'D':
        y -= h
    maxx = max(x, maxx)
    maxy = max(y, maxy)
    minx = min(x, minx)
    miny = min(y, miny)

print(minx, maxx, miny, maxy)

tabla = np.zeros((maxx-minx+1, maxy-miny+1), dtype=np.byte)

metszetek = []

x = y = 0
for ir, h in l1:
    for i in range(h):
        if ir == 'R':
            x += 1
        elif ir == 'L':
            x -= 1
        elif ir == 'U':
            y += 1
        elif ir == 'D':
            y -= 1
        tabla[x-minx][y-miny] += 1

x = y = 0
for ir, h in l2:
    for i in range(h):
        if ir == 'R':
            x += 1
        elif ir == 'L':
            x -= 1
        elif ir == 'U':
            y += 1
        elif ir == 'D':
            y -= 1
        tabla[x-minx][y-miny] += 1
        if tabla[x-minx][y-miny] == 2:
            metszetek.append((abs(x) + abs(y), (x, y)))

print(min(metszetek))