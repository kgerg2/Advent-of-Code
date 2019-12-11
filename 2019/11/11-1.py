import subprocess

iranyok = [(0, 1), (1, 0), (0, -1), (-1, 0)]
poz = (0, 0)
ir = (0, 1)
d = {}
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
