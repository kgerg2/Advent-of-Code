import re

# python -c "import sys; sys.stdout.writelines((sorted(sys.stdin.readlines())))" < input.txt > rendezett.txt

őrök = {}

with open("rendezett.txt") as be:
    sorok = be.readlines()

alszik = False
for sor in sorok:
    if "#" in sor:
        ssz = int(re.search(r"#\d+", sor).group()[1:])
        if ssz not in őrök:
            őrök[ssz] = 0
    else:
        perc = int(re.search(r":\d+", sor).group()[1:])
        if not alszik:
            kezd = perc
        else:
            őrök[ssz] += perc-kezd
        alszik = not alszik

ssz = max([(x, y) for y, x in őrök.items()])[1]

percek = [0]*60

jo = False
alszik = False
for sor in sorok:
    if "#" in sor:
        jo = int(re.search(r"#\d+", sor).group()[1:]) == ssz
    elif jo:
        perc = int(re.search(r":\d+", sor).group()[1:])
        if not alszik:
            kezd = perc
        else:
            for i in range(kezd, perc):
                percek[i] += 1
        alszik = not alszik

print(ssz, percek.index(max(percek)))
print(ssz * percek.index(max(percek)))
