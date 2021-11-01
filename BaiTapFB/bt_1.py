import numpy as np
l = [[0]] * 5
l[0].append(5)
a = np.array(l)

print(a)

arr = [[0] for _ in range(5)]
r = arr.append(5)
s = np.array(r)
print(s)
