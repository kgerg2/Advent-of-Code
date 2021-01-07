import subprocess

s = subprocess.Popen(["python", ".\\2019\\13\\szamol.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

db = 0
while s.poll() is None:
    s.stdout.readline()
    s.stdout.readline()
    try:
        if int(s.stdout.readline()) == 2:
            db += 1
    except ValueError:
        break

print(db)
    
