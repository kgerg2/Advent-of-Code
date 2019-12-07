import subprocess
import itertools
from ast import literal_eval

maximum = 0
sorr = literal_eval(input())
ertek = b"0\n"
ert = 0
ek = []
for ph in sorr:
    if ek:
        ek.append(subprocess.Popen(["python", ".\\2019\\7\\szamol.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE))
    else:
        ek.append(subprocess.Popen(["python", ".\\2019\\7\\szamol.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE))
    ek[-1].stdin.write(f"{ph}\n".encode("ascii"))
    ek[-1].stdin.flush()
while ek[-1].poll() is None:
    for e in ek:
        e.stdin.write(ertek)
        e.stdin.flush()
        ertek = e.stdout.readline()
        if ertek:
            ert = int(ertek)
print(ert)