def jo(szam):
    elozo = szam % 10
    szam = szam // 10
    vanszomszedos = False
    for _ in range(5):
        if szam % 10 == elozo:
            vanszomszedos = True
        elif szam % 10 > elozo:
            return False
        elozo = szam % 10
        szam = szam // 10
    return vanszomszedos

print(jo(111111))
print(jo(112233))
print(jo(111220))
print(jo(135678))
print(len([True for x in range(130254, 678276) if jo(x)]))