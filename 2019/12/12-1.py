import re
import numpy as np
from itertools import combinations
from math import copysign

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

for _ in range(1000):
    gravitacio(l)
    mozgatas(l)

print(sum([sum(map(abs, h.p))*sum(map(abs, h.v)) for h in l]))
