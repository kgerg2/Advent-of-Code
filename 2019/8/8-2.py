from functools import reduce
import matplotlib.pyplot as plt
import numpy as np

l = []
with open(".\\2019\\8\\input.txt") as be:
    while be:
        try:
            uj = list(map(int, list(be.read(25*6))))
            if uj:
                l.append(uj)
            else:
                break
        except ValueError:
            break

l = reduce(lambda x, y: list(map(lambda a: a[1] if a[0] == 2 else a[0], zip(x, y))), l)
print(l)
plt.imshow(np.reshape(l, (6, 25)))
plt.show()
