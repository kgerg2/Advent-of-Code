from math import gcd, copysign

toroltdb = 0

def szamol(l, x, y):
    global toroltdb
    kov = [[False]*len(l[0]) for _ in l]
    toroltek = [(i, j) for i, sor in enumerate(l) for j, e in enumerate(sor) if e]
    toroltdb += len(toroltek)

    def torol(l, x, y, i, j):
        nonlocal kov
        global toroltdb
        i -= x
        j -= y
        a = i // gcd(i, j)
        b = j // gcd(i, j)
        while True:
            i += a
            j += b
            if 0 <= x+i < len(l) and 0 <= y+j < len(l[x+i]):
                if l[x+i][y+j]:
                    l[x+i][y+j] = False
                    kov[x+i][y+j] = True
                    toroltdb -= 1
                    toroltek.remove((x+i, y+j))
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
    return toroltek, kov

with open(".\\2019\\10\\input.txt") as be:
    l = list(map(lambda x: [a == '#' for a in x.strip()], be.readlines()))

poz = (28, 22)
#poz = (13, 11)
while toroltdb < 200:
    t, l = szamol(l, *poz)
    print(t)

toroltdb -= len(t)
def f(p):
    y = poz[0] - p[0]
    x = p[1] - poz[1]
    fst = 2 if x == 0 and y > 0 else copysign(1, x)
    try:
        snd = y/x
    except ZeroDivisionError:
        snd = y*float("inf")
    return (fst, snd, *p, p[1]*100+p[0])

t.remove(poz)
t = sorted(map(f, t))
print(t)
print(t[-(200-toroltdb)])
# meredekség szerint csökkenő sorrendben először a pozitív, utána a negatív x koordinátájú pontok