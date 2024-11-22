import matplotlib.pyplot as plt
from decimal import *
from sympy import *

PRECISION = 50

def sym_to_arr(arr):
    retval = []
    for x in arr:
        retval.append(N(x, PRECISION))
    return retval

def apm_lim(a, b):
    alpha = acos(a / b)
    return b * sin(alpha) / alpha

def asm_lim(a, b):
    alpha = acos(2 * a / b - 1)
    return b * sin(alpha) / alpha

def gm(a, b):
    return sqrt(a * b)

def hm(a, b):
    return 2 * a * b / (a + b)

def am(a, b):
    return (a + b) / 2

def qm(a, b):
    return sqrt((a * a + b * b) / 2)

def gaussian_iteration(n, mean1, mean2, a, b):
    u = [a]
    v = [b]
    for i in range(n):
        u.append(mean1(u[-1], v[-1]))
        v.append(mean2(u[-2], v[-1]))
    return [u, v]

def archimedean_iteration(n, mean1, mean2, a, b):
    u = [a]
    v = [b]
    for i in range(n):
        u.append(mean1(u[-1], v[-1]))
        v.append(mean2(u[-1], v[-1]))
    return [u, v]

def apm_up_to(n, a, b):
    return archimedean_iteration(n, am, gm, a, b)

def asm_up_to(n, a, b):
    return archimedean_iteration(n, gm, am, b, a)

def agm_up_to(n, a, b):
    return gaussian_iteration(n, gm, am, a, b)

def ham_up_to(n, a, b):
    return gaussian_iteration(n, hm, am, a, b)

def gqm_up_to(n, a, b):
    return gaussian_iteration(n, gm, qm, a, b)

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

def conv_rate2(n, u, v, ord):
    mu = []
    for i in range(n):
        mu.append(Abs(v[i + 1] - u[i + 1]) / Abs(v[i] - u[i])**ord)
    return mu

# ------------------------------------------------------

n = int(input())
a = sympify(input())
b = sympify(input())

u, v     = apm_up_to(n, a, b)
up, vp   = asm_up_to(n, a, b)
upp, vpp = agm_up_to(n, a, b)
print(sym_to_arr(upp))
print(sym_to_arr(conv_rate2(n - 2, u, v, 1)))
print(sym_to_arr(conv_rate2(n - 2, up, vp, 1)))
print(sym_to_arr(conv_rate(n - 2, vpp, upp[n - 1], 2)))
# d = diffs(n - 1, u, v)
# p = conv_order(n - 2, v, v[n - 1])
# print(v)
# print(sym_to_arr(test(n, v, musso_lim(a, b))))

x = []
for i in range(1, len(upp) + 1):
    x.append(i)

plt.plot(x, u, '-', label="APM u")
plt.plot(x, v, '-', label="APM v")
plt.plot(x, up, '-', label="ASM u")
plt.plot(x, vp, '-', label="ASM v")
plt.plot(x, upp, '-', label="AGM u")
plt.plot(x, vpp, '-', label="AGM v")
plt.legend()
plt.show()
