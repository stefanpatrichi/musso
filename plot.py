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
    alpha = acos(a / b)
    return b * sin(alpha) / alpha

def asm_lim(a, b):
    alpha = acos(2 * a / b - 1)
    return b * sin(alpha) / alpha

def am(a, b):
    return (a + b) / 2

def gm(a, b):
    return sqrt(a * b)

def hm(a, b):
    return 2 * a * b / (a + b)

def musso_up_to(n, a, b):
    u = [a]
    v = [b]
    for i in range(n):
        u.append(am(u[-1], v[-1]))
        v.append(gm(u[-1], v[-1]))
    return [u, v]

def asm_up_to(n, a, b):
    u = [a]
    v = [b]
    for i in range(n):
        v.append(gm(u[-1], v[-1]))
        u.append(am(u[-1], v[-1]))
    return [u, v]

def agm_up_to(n, a, b):
    u = [b]
    v = [a]
    for i in range(n):
        u.append(am(u[-1], v[-1]))
        v.append(gm(u[-2], v[-1]))
    return [u, v]

def diffs(n, u, v):
    d = []
    for i in range(n):
        d.append(Abs(v[i + 1] - u[i + 1]) / Abs(v[i] - u[i]))
    return d

def conv_order(n, v, lim):
    p = []
    for i in range(n):
        p.append(log(Abs(v[i + 1] - lim)) / log(Abs(v[i] - lim)))
    return p

def conv_rate(n, v, lim, ord):
    mu = []
    for i in range(n):
        mu.append(Abs(v[i + 1] - lim) / Abs(v[i] - lim)**ord)
    return mu


# ------------------------------------------------------

n = int(input())
a = sympify(input())
b = sympify(input())

if a > b:
    a, b = b, a

u, v     = musso_up_to(n, a, b)
# up, vp   = asm_up_to(n, a, b)
# u, v = agm_up_to(n, a, b)
# print(sym_to_arr(up))
# print(sym_to_arr(u))
# d = diffs(n - 1, u, v)
# p = conv_order(n - 2, v, v[n - 1])
# print(v)
# r = conv_rate(n - 2, v, v[n - 1], 2)
# print(sym_to_arr(r))
print(sym_to_arr(test(n, v, musso_lim(a, b))))

# for i in range(len(u)):
#     print(N(u[i] + vp[i]) / 2)
#     print(N(up[i] + v[i]) / 2)

# x = []
# for i in range(1, len(upp) + 1):
#     x.append(i)

# plt.plot(x, u, '-', label="APM u")
# plt.plot(x, v, '-', label="APM v")
# plt.plot(x, up, '-', label="ASM u")
# plt.plot(x, vp, '-', label="ASM v")
# plt.plot(x, upp, '-', label="AGM u")
# plt.plot(x, vpp, '-', label="AGM v")
# plt.legend()
# plt.show()
