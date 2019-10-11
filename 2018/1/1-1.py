a = 0
with open("input.e") as be:
    fajl = be.readlines()
    for sor in fajl:
        a += int(sor)
print(a)