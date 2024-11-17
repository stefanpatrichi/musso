import matplotlib.pyplot as plt
import numpy as np
from decimal import *

getcontext().prec = 30

def musso_up_to(n, a, b):
    u = np.array([a])
    v = np.array([b])
    for i in range(n):
        u = np.append(u, (u[-1] + v[-1]) / 2)
        v = np.append(v, np.sqrt(u[-1] * v[-1]))
    return [u, v]

def agm_up_to(n, a, b):
    u = np.array([b])
    v = np.array([a])
    for i in range(n):
        u = np.append(u, (u[-1] + v[-1]) / 2)
        v = np.append(v, np.sqrt(u[-2] * v[-1]))
    return [u, v]


def diffs(n, u, v):
    d = np.array([])
    for i in range(n):
        d = np.append(d, (v[i + 1] - u[i + 1]) / (v[i] - u[i]))
    return d


# ------------------------------------------------------

n = int(input())
a = float(input())
b = float(input())

u, v = agm_up_to(n, a, b)

d = diffs(n - 1, u, v)
print(d)

# x = []
# for i in range(1, len(u) + 1):
#     x.append(i)

# plt.plot(x, u, '-')
# plt.plot(x, v, '-')
# plt.legend()
# plt.show()
