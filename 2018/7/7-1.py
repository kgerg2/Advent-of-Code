felt = {}

with open(".\\2018\\7\\input.txt") as be:
    for sor in be.readlines():
        if sor[36] in felt:
            felt[sor[36]].add(sor[5])
        else:
            felt[sor[36]] = {sor[5]}
        if sor[5] not in felt:
            felt[sor[5]] = set()
        print(sor[5], sor[36])
print(felt)
while felt:
    lehetsegesek = [x for x, y in felt.items() if not y]
    kov = min(lehetsegesek)
    for x in felt:
        felt[x].discard(kov)
    felt.pop(kov)
    print(kov, end="")