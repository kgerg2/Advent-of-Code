import numpy as np

l = []
with open(".\\2019\\8\\input.txt") as be:
    while True:
        try:
            l.append(tuple(np.unique(list(map(int, list(be.read(6*25)))), return_counts=True)[1]))
        except ValueError:
            break

m = min(l)
print(m)
print(m[1]*m[2])