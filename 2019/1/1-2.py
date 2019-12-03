with open(".\\1\\input.e") as be:
    l = map(int, be.readlines())

def ua(t):
    uj = t//3-2
    if uj > 0:
        return uj + ua(uj)
    return 0

print(sum(map(ua, l)))