with open(".\\2\\input2.e") as be:
    l1 = list(map(lambda x: (x[0], int(x[1:])), be.readline().split(',')))

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

print(minx, maxx, miny, maxy)