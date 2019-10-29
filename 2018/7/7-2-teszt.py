def munkahossz(nev):
    return ord(nev)-ord('A')+1

felt = {}

with open(".\\2018\\7\\input-teszt.txt") as be:
    for sor in be.readlines():
        if sor[36] in felt:
            felt[sor[36]].add(sor[5])
        else:
            felt[sor[36]] = {sor[5]}
        if sor[5] not in felt:
            felt[sor[5]] = set()
        print(sor[5], sor[36])
print(felt)

hossz = 0
dolgozok = [[0, ''] for _ in range(2)]

while felt:
    keszek = [i for i, e in enumerate(dolgozok) if e[0] == 0]
    for i in keszek:
        for x in felt:
            felt[x].discard(dolgozok[i][1])
        felt.pop(dolgozok[i][1], None)
    for i in keszek:
        lehetsegesek = [x for x, y in felt.items() if not y and x not in (x[1] for x in dolgozok)]
        if lehetsegesek:
            kov = min(lehetsegesek)
            dolgozok[i] = [munkahossz(kov), kov]
        else:
            dolgozok[i] = [0, '']

    for i in range(2):
        dolgozok[i][0] = max(0, dolgozok[i][0]-1)

    print(kov, end="")
    hossz += 1
print(hossz)