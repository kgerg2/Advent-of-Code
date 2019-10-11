from collections import Counter

with open("input.txt") as be:
    lista = map(lambda x: x.strip(), be.readlines())

l = set()

for elem in lista:
    for i in range(len(elem)-1):
        uj = "{}-{}".format(elem[:i], elem[i+1:])
        if uj in l:
            print(uj)
            exit()
        l.add(uj)
    #print(elem)
    #print(l)