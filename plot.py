import matplotlib.pyplot as plt
import math as np
from decimal import *

getcontext().prec = 30

def musso_up_to(n, a, b):
    u = [a]
    v = [b]
    for i in range(n):
        u.append((u[-1] + v[-1]) / Decimal(2))
        v.append(Decimal(u[-1] * v[-1]).sqrt())
    return [u, v]

def agm_up_to(n, a, b):
    u = [b]
    v = [a]
    for i in range(n):
        u.append((u[-1] + v[-1]) / Decimal(2))
        v.append(Decimal(u[-2] * v[-1]).sqrt())
    return [u, v]


def diffs(n, u, v):
    d = []
    for i in range(1, n + 1):
        d.append((v[i] - u[i]) / (v[i - 1] - u[i - 1]))
    return d


# ------------------------------------------------------

n = int(input())
a = Decimal(input())
b = Decimal(input())

u, v = agm_up_to(n, a, b)

d = diffs(n - 1, u, v)
print(d)

x = []
for i in range(1, len(u) + 1):
    x.append(i)

plt.plot(x, u, '-')
plt.plot(x, v, '-')
plt.legend()
plt.show()
