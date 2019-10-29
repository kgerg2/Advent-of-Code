osszeg = 0
with open(".\\2018\\8\\input.txt") as be:
    lista = list(map(int, be.read().split()))

lista.reverse()
def elemez():
    global lista
    global osszeg
    ert = 0
    gyereklista = []
    gyerekek = lista.pop()
    metaadatok = lista.pop()
    for _ in range(gyerekek):
        gyereklista.append(elemez())
    for _ in range(metaadatok):
        uj = lista.pop()
        if gyerekek == 0:
            ert += uj
        elif 0 < uj <= gyerekek:
            ert += gyereklista[uj-1]
    return ert

print(elemez())