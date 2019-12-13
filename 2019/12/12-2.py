import re
from itertools import combinations
from functools import reduce
import numpy as np
from math import gcd

sk = [set() for _ in range(3)]
ism = [None]*3
uj = 0

class Hold:
    def __init__(self, poz):
        self.p = poz
        self.v = (0, 0, 0)

    def grav(self, masik):
        self.v = tuple(v + int(np.sign(m-s)) for v, s, m in zip(self.v, self.p, masik.p))

    def mozg(self):
        self.p = tuple(p + v for p, v in zip(self.p, self.v))

def gravitacio(holdak):
    for h1, h2 in combinations(holdak, 2):
        h1.grav(h2)
        h2.grav(h1)

def mozgatas(holdak):
    for h in holdak:
        h.mozg()

with open(".\\2019\\12\\input.txt") as be:
    l = [Hold(tuple(map(int, re.split(", .=", sor[3:-2])))) for sor in be.readlines()]

i = 0
while uj < 3:
    for j, s in enumerate(sk):
        if ism[j] is None:
            ert = (tuple(l[k].p[j] for k in range(4)), tuple(l[k].v[j] for k in range(4)))
            if ert not in s:
                s.add(ert)
            else:
                ism[j] = i
                uj += 1
    gravitacio(l)
    mozgatas(l)
    i += 1

print(ism)
print(reduce(lambda a, b: a*b // gcd(a, b), ism))