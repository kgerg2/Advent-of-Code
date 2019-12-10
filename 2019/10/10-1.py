from pprint import pprint
from math import gcd

def szamol(l, x, y):
    for i in range(x, len(l)):
        for j in range(y, len(l[i])):
            if l[i][j]:
                try:
                    a = i // gcd(i, j)
                    b = j // gcd(i, j)
                    k = 2
                    while True:
                        l[a*k][b*k] = False
                        k += 1
                except IndexError:
                    pass
    for i in range(x+1, len(l)):
        for j in range(y-1, 0, -1):
            if l[i][j]:
                try:
                    a = i // gcd(i, j)
                    b = j // gcd(i, j)
                    k = 2
                    while True:
                        l[a*k][b*k] = False
                        k += 1
                except IndexError:
                    pass
    for i in range(x-1, 0, -1):
        for j in range(y+1, len(l[i])):
            if l[i][j]:
                try:
                    a = i // gcd(i, j)
                    b = j // gcd(i, j)
                    k = 2
                    while True:
                        l[a*k][b*k] = False
                        k += 1
                except IndexError:
                    pass
    for i in range(x, 0, -1):
        for j in range(y, 0, -1):
            if l[i][j]:
                try:
                    a = i // gcd(i, j)
                    b = j // gcd(i, j)
                    k = 2
                    while True:
                        l[a*k][b*k] = False
                        k += 1
                except IndexError:
                    pass
    return sum(map(sum, l))-1

with open(".\\10\\input3.txt") as be:
    l = list(map(lambda x: [a == '#' for a in x.strip()], be.readlines()))

eredm = []
for i in range(len(l)):
    for j in range(len(l[i])):
        if(l[i][j]):
            eredm.append(szamol(l[:], i, j))

print("\n".join(map(str, l)))
print(max(eredm))