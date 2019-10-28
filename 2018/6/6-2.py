import numpy as np

with open(".\\2018\\6\\input.txt") as be:
    pontok = [tuple([int(x)+100 for x in sor.split(",")]) for sor in be.readlines()]

ter = np.zeros((600, 600), dtype=np.int8)

for i in range(600):
    for j in range(600):
        tavok = [abs(j-a) + abs(i-b) for (a, b) in pontok]
        tav = sum(tavok)
        if tav < 10000:
            ter[i][j] = 1


print(pontok)
print(ter)

print(np.sum(ter))