import subprocess
import itertools


maximum = 0
for sorr in itertools.permutations(range(5)):
    ert = 0
    for ph in sorr:
        ert = int(subprocess.run(["python", ".\\2019\\7\\szamol.py"], input=f"{ph}\n{ert}", encoding="ascii", stdout=subprocess.PIPE).stdout.strip())
    maximum = max(maximum, ert)
print(maximum)