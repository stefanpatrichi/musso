import matplotlib.pyplot as plt
from decimal import *
from sympy import *

PRECISION = 50

def sym_to_arr(arr):
    retval = []
    for x in arr:
        retval.append(N(x, PRECISION))
    return retval

def musso_lim(a, b):
    return b * sin(acos(a / b)) / acos(a/b)

def musso_up_to(n, a, b):
    u = [a]
    v = [b]
    for i in range(n):
        u.append((u[-1] + v[-1]) / 2)
        v.append(sqrt(u[-1] * v[-1]))
    return [Array(u), Array(v)]

def agm_up_to(n, a, b):
    u = [b]
    v = [a]
    for i in range(n):
        u.append((u[-1] + v[-1]) / 2)
        v.append(sqrt(u[-2] * v[-1]))
    return [Array(u), Array(v)]

def diffs(n, u, v):
    d = []
    for i in range(n):
        d.append(Abs(v[i + 1] - u[i + 1]) / Abs(v[i] - u[i]))
    return Array(d)

def conv_order(n, v, lim):
    p = []
    for i in range(n):
        p.append(log(Abs(v[i + 1] - lim)) / log(Abs(v[i] - lim)))
    return Array(p)

def conv_rate(n, v, lim, ord):
    p = []
    for i in range(n):
        p.append(Abs(v[i + 1] - lim) / Abs(v[i] - lim)**ord)
    return Array(p)


# ------------------------------------------------------

n = int(input())
a = sympify(input())
b = sympify(input())

if a > b:
    a, b = b, a

_, v = musso_up_to(n, a, b)
# print(sym_to_arr(u))
# d = diffs(n - 1, u, v)
# p = conv_order(n - 2, v, v[n - 1])
# print(v)
r = conv_rate(n - 1, v, musso_lim(a, b), 1)
print(sym_to_arr(r))
# print(sym_to_arr(p))

# x = []
# for i in range(1, len(u) + 1):
#     x.append(i)

# plt.plot(x, u, '-')
# plt.plot(x, v, '-')
# plt.legend()
# plt.show()
