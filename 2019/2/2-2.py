with open(".\\2\\input.e") as be:
    lista = list(map(int, be.readline().split(',')))

#lista = list(map(int, input().split(',')))

def lep(i):
    global l
    if l[i] == 1:
        l[l[i+3]] = l[l[i+1]] + l[l[i+2]]
        lep(i+4)
    elif l[i] == 2:
        l[l[i+3]] = l[l[i+1]] * l[l[i+2]]
        lep(i+4)
    elif l[i] != 99:
        raise Exception

for i in range(100):
    for j in range(100):
        l = lista[:]
        l[1] = i
        l[2] = j
        lep(0)
        if l[0] == 19690720:
            print(i, j, 100*i+j)
            break
