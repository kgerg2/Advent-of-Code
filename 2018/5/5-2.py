import string
from subprocess import run, PIPE

with open(".\\2018\\5\\input.txt") as be:
    szoveg = be.read().strip()

print(len(szoveg))

for b, B in zip(string.ascii_lowercase, string.ascii_uppercase):
    uj = szoveg.replace(b, "").replace(B, "")
    e = run(["C:\\Users\\kgerg\\Documents\\GitHub\\Advent-of-Code\\2018\\5\\5-2.exe"], stdout=PIPE, input=uj, encoding='ascii')
    print(B, e.stdout)

print(run(["C:\\Users\\kgerg\\Documents\\GitHub\\Advent-of-Code\\2018\\5\\5-2.exe"], stdout=PIPE, input=szoveg, encoding='ascii').stdout)