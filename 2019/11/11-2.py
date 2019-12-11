import subprocess
import matplotlib.pyplot as plt
import numpy as np

iranyok = [(0, 1), (1, 0), (0, -1), (-1, 0)]
poz = (0, 0)
ir = (0, 1)
d = {poz: 1}
s = subprocess.Popen(["python", ".\\2019\\11\\szamol.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

while s.poll() is None:
    s.stdin.write(f"{d.get(poz, 0)}\n".encode("ascii"))
    s.stdin.flush()
    try:
        d[poz] = int(s.stdout.readline())
    except ValueError:
        break
    fordul = int(s.stdout.readline())
    valt = -3 if fordul else -1
    uj_index = iranyok.index(ir) + valt
    ir = iranyok[uj_index]
    poz = (poz[0] + ir[0], poz[1] + ir[1])

print(len(d))
unzipped = list(zip(*d.keys()))
minx, miny = tuple(map(min, unzipped))
maxx, maxy = tuple(map(max, unzipped))

kep = np.zeros((maxy-miny+1, maxx-minx+1))
for (x, y), ert in d.items():
    kep[miny-y-1][x-minx] = ert

plt.imshow(kep)
plt.show()