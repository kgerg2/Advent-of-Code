import numpy as np

with open(".\\2018\\6\\input.txt") as be:
    pontok = [tuple([int(x)+100 for x in sor.split(",")]) for sor in be.readlines()]

ter = np.zeros((600, 600), dtype=np.int8)
db = np.zeros(50, dtype=np.int32)
print(ter.shape)

for i in range(600):
    for j in range(600):
        tavok = [(abs(j-a) + abs(i-b), k) for k, (a, b) in enumerate(pontok)]
        mintav = min(tavok)[0]
        jok = [k for tav, k in tavok if tav == mintav]
        if len(jok) > 1:
            ter[i][j] = -1
        else:
            ter[i][j] = jok[0]
            db[jok[0]] += 1
        if min(db) < 0:
            print(db)


print(db)
for i in range(600):
    db[ter[i][0]] = 0
    db[ter[i][599]] = 0
    db[ter[0][i]] = 0
    db[ter[599][i]] = 0

print(db)
print(max(db))
print(pontok)
print(ter)