import re
import numpy as np

with open("input.txt") as be:
    l = [tuple(map(int, re.split(r"\D+", sor)[2:-1])) for sor in be.readlines()]

mezo = np.zeros([1000, 1000])

for elem in l:
    for i in range(elem[2]):
        for j in range(elem[3]):
            mezo[elem[0] + i][elem[1] + j] += 1

jok = [True]*len(l)

for index, elem in enumerate(l):
    for i in range(elem[2]):
        for j in range(elem[3]):
            if mezo[elem[0] + i][elem[1] + j] > 1:
                jok[index] = False

print(jok.index(True)+1)