def jo(szam):
    elozo = szam % 10
    szam = szam // 10
    vanszomszedos = False
    szomszedhossz = 1
    for _ in range(5):
        if szam % 10 > elozo:
            return False
        if szam % 10 == elozo:
            szomszedhossz += 1
        else:
            if szomszedhossz == 2:
                vanszomszedos = True
            szomszedhossz = 1
        elozo = szam % 10
        szam = szam // 10
    return vanszomszedos or szomszedhossz == 2

print(len([True for x in range(130254, 678276) if jo(x)]))