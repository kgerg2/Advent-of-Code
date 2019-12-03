with open(".\\2\\input2.e") as be:
    l = list(map(int, be.readline().split(',')))

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

lep(0)
print(l[0])