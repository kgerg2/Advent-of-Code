with open(".\\1\\input.e") as be:
    l = map(int, be.readlines())

print(sum(map(lambda x: x//3-2, l)))