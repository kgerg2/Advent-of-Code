from collections import Counter

with open("input.txt") as be:
    lista = be.readlines()

l = list(map(Counter, lista))
print(sum(1 for elem in l if 2 in elem.values()) * sum(1 for elem in l if 3 in elem.values()))