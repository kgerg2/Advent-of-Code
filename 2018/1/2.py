a = 0
ak = set()
with open("input (1).e") as be:
    fajl = list(map(int, be.readlines()))

while True:
    for sor in fajl:
        a += sor
        # print(a)
        if a in ak:
            print(a)
            exit()
        ak = ak | {a}
# print(ak)