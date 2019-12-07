l = {}

def osszeszamol(com, i):
    return sum(osszeszamol(h, i+1) for h in l.get(com, [])) + i

with open(".\\2019\\6\\input.txt") as be:
    for sor in be.readlines():
        a, b = tuple(sor.strip().split(")"))
        if a in l:
            l[a].append(b)
        else:
            l[a] = [b]

print(osszeszamol("COM", 0))