l = {}
s = {}

def tav(kezd, veg):
    if veg == kezd:
        return 0
    if kezd in s:
        szulo = s[kezd]
        l[szulo].remove(kezd)
    gyerekek = l.get(kezd, [])
    for gy in gyerekek:
        s.pop(gy)
    return min(min([tav(gy, veg) + 1 for gy in gyerekek] + [float("inf")]), float("inf") if kezd not in s else tav(szulo, veg) + 1)
    

with open(".\\2019\\6\\input.txt") as be:
    for sor in be.readlines():
        a, b = tuple(sor.strip().split(")"))
        s[b] = a
        if a in l:
            l[a].append(b)
        else:
            l[a] = [b]

print(tav(s["YOU"], s["SAN"]))