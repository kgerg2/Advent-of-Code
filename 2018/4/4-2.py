import re

# python -c "import sys; sys.stdout.writelines((sorted(sys.stdin.readlines())))" < input.txt > rendezett.txt

with open("rendezett.txt") as be:
    sorok = be.readlines()

őrök = {}

alszik = False
for sor in sorok:
    if "#" in sor:
        ssz = int(re.search(r"#\d+", sor).group()[1:])
        if ssz not in őrök:
            őrök[ssz] = [0]*60
    else:
        perc = int(re.search(r":\d+", sor).group()[1:])
        if not alszik:
            kezd = perc
        else:
            for i in range(kezd, perc):
                őrök[ssz][i] += 1
        alszik = not alszik

maxssz = None
maxpercek = 0
for ssz, percek in őrök.items():
    if max(percek) > maxpercek:
        maxpercek = max(percek)
        maxssz = ssz

print(maxssz, őrök[maxssz].index(maxpercek))
print(maxssz * őrök[maxssz].index(maxpercek))