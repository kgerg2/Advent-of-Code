with open(".\\2019\\11\\input.txt") as be:
    l = list(map(int, be.readline().split(',')))
rb = 0

def get(i, mode):
    try:
        if mode == 0:
            return l[l[i]]
        elif mode == 1:
            return l[i]
        elif mode == 2:
            return l[l[i] + rb]
        else:
            raise Exception
    except IndexError:
        return 0

def put(i, a, mode):
    global l
    if mode == 0:
        i = l[i]
    elif mode == 2:
        i = l[i] + rb
    else:
        raise Exception
    try:
        l[i] = a
    except IndexError:
        l += [0]*(i-len(l)) + [a]

def lep(i):
    global l
    opcode = l[i] % 100
    if opcode == 1:
        a = get(i+1, l[i] // 100 % 10)
        b = get(i+2, l[i] // 1000 % 10)
        put(i+3, a+b, l[i] // 10000)
        return i+4
    elif opcode == 2:
        a = get(i+1, l[i] // 100 % 10)
        b = get(i+2, l[i] // 1000 % 10)
        put(i+3, a*b, l[i] // 10000)
        return i+4
    elif opcode == 3:
        put(i+1, int(input()), l[i] // 100)
        return i+2
    elif opcode == 4:
        print(get(i+1, l[i] // 100 % 10))
        return i+2
    elif opcode == 5:
        a = get(i+1, l[i] // 100 % 10)
        b = get(i+2, l[i] // 1000 % 10)
        if a:
            return b
        else:
            return i+3
    elif opcode == 6:
        a = get(i+1, l[i] // 100 % 10)
        b = get(i+2, l[i] // 1000 % 10)
        if not a:
            return b
        else:
            return i+3
    elif opcode == 7:
        a = get(i+1, l[i] // 100 % 10)
        b = get(i+2, l[i] // 1000 % 10)
        put(i+3, int(a < b), l[i] // 10000)
        return i+4
    elif opcode == 8:
        a = get(i+1, l[i] // 100 % 10)
        b = get(i+2, l[i] // 1000 % 10)
        put(i+3, int(a == b), l[i] // 10000)
        return i+4
    elif opcode == 9:
        global rb
        rb += get(i+1, l[i] // 100)
        return i+2
    elif opcode != 99:
        raise Exception
    return -1

i = 0
while -1 != (i := lep(i)):
    continue
