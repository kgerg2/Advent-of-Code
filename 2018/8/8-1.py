osszeg = 0
with open(".\\2018\\8\\input.txt") as be:
    lista = list(map(int, be.read().split()))

lista.reverse()
def elemez():
    global lista
    global osszeg
    gyerekek = lista.pop()
    metaadatok = lista.pop()
    for _ in range(gyerekek):
        elemez()
    for _ in range(metaadatok):
        osszeg += lista.pop()

elemez()
print(osszeg)
