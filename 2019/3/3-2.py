import numpy as np
import matplotlib.pyplot as plt

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

tabla = np.zeros((maxx-minx+1, maxy-miny+1), dtype=np.int16)

metszetek = []

i = 1
x1 = y1 = 0
x2 = y2 = 0
h1 = h2 = 0
while l1 or l2 or h1 or h2:
    if l1 or h1:
        if not h1:
            ir1, h1 = l1.pop(0)
        if ir1 == 'R':
            x1 += 1
        elif ir1 == 'L':
            x1 -= 1
        elif ir1 == 'U':
            y1 += 1
        elif ir1 == 'D':
            y1 -= 1
        if tabla[x1-minx][y1-miny] < 0:
            metszetek.append(i-tabla[x1-minx][y1-miny])
        else:
            tabla[x1-minx][y1-miny] += i
        h1 -= 1
    if l2 or h2:
        if not h2:
            ir2, h2 = l2.pop(0)
        if ir2 == 'R':
            x2 += 1
        elif ir2 == 'L':
            x2 -= 1
        elif ir2 == 'U':
            y2 += 1
        elif ir2 == 'D':
            y2 -= 1
        if tabla[x2-minx][y2-miny] > 0:
            metszetek.append(i+tabla[x2-minx][y2-miny])
        else:
            tabla[x2-minx][y2-miny] -= i
        h2 -= 1
    i += 1

print(metszetek)
print(min(metszetek))
plt.imshow(tabla, cmap="gray")
plt.show()
#print("\n".join(list(map(str, map(list, tabla)))))
