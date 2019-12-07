import subprocess
import itertools

maximum = 0
for sorr in itertools.permutations(range(5, 10)): #[(5, 7, 9, 6, 8,)]:
    r = subprocess.run(["python", ".\\2019\\7\\ciklus_szamol.py"], input=str(sorr), encoding="ascii", stdout=subprocess.PIPE)
    maximum = max(maximum, int(r.stdout))
print(maximum)