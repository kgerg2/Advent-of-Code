with open(".\\2019\\5\\input.txt") as be:
    l = list(map(int, be.readline().split(',')))

def lep(i):
    global l
    opcode = l[i] % 100
    if opcode == 1:
        a = l[i+1] if l[i] // 100 % 10 else l[l[i+1]]
        b = l[i+2] if l[i] // 1000 % 10 else l[l[i+2]]
        if l[i] // 10000:
            raise Exception
        l[l[i+3]] = a + b
        lep(i+4)
    elif opcode == 2:
        a = l[i+1] if l[i] // 100 % 10 else l[l[i+1]]
        b = l[i+2] if l[i] // 1000 % 10 else l[l[i+2]]
        if l[i] // 10000:
            raise Exception
        l[l[i+3]] = a * b
        lep(i+4)
    elif opcode == 3:
        if l[i] // 100:
            raise Exception
        l[l[i+1]] = int(input("> "))
        lep(i+2)
    elif opcode == 4:
        print(l[i+1] if l[i] // 100 % 10 else l[l[i+1]])
        lep(i+2)
    elif opcode != 99:
        raise Exception

lep(0)