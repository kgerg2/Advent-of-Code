import re
import numpy as np

with open("input.txt") as be:
    l = [tuple(map(int, re.split(r"\D+", sor)[2:-1])) for sor in be.readlines()]

mezo = np.zeros([1000, 1000])

for elem in l:
    for i in range(elem[2]):
        for j in range(elem[3]):
            mezo[elem[0] + i][elem[1] + j] += 1

#print(max([i[0] + i[2] for i in l]), max([i[1] + i[3] for i in l]))
print(sum(1 for i in mezo.flat if i > 1))