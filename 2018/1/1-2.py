a = 0
ak = set()
with open(".\\2018\\1\\input (1).e") as be:
    fajl = list(map(int, be.readlines()))

while True:
    for sor in fajl:
        a += sor
        # print(a)
        if a in ak:
            print(a)
            exit()
        ak.add(a)
# print(ak)