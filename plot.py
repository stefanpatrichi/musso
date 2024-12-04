import matplotlib.pyplot as plt
import numpy as np
from decimal import *
from sympy import *

PRECISION = 50

def sym_to_arr(arr):
    retval = []
    for x in arr:
        retval.append(N(1/x, PRECISION))
    return retval

def gm(a, b):
    return sqrt(a * b)

def hm(a, b):
    return 2 * a * b / (a + b)

def am(a, b):
    return (a + b) / 2

def qm(a, b):
    return sqrt((a * a + b * b) / 2)


def apm_graph(a, x):
    retval = np.array([])
    for b in x:
        print("a")
        if a < b:
            retval = np.append(retval, sqrt(b**2 - a**2) / acos(a / b))
        elif a == b:
            retval = np.append(retval, a)
        else:
            retval = np.append(retval, sqrt(a**2 - b**2) / acosh(a / b))
    return retval

def asm_graph(a, x):
    retval = np.array([])
    for b in x:
        print("b")
        if a < b:
            retval = np.append(retval, sqrt(a * (b - a)) / acos(sqrt(a / b)))
        elif a == b:
            retval = np.append(retval, a)
        else:
            retval = np.append(retval, sqrt(b * (a - b)) / acosh(sqrt(a / b)))
    return retval

def agm_graph(a, x):
    retval = np.array([])
    t = Symbol('t')
    for b in x:
        print("c")
        retval = np.append(retval, pi / 2 * (integrate(1/sqrt(a**2 * cos(t)**2 + b**2 * sin(t)**2), (t, 0, pi / 2))) ** -1)
    return retval

def am_graph(a, x):
    retval = np.array([])
    for b in x:
        retval = np.append(retval, am(a, b))
    return retval

def gm_graph(a, x):
    retval = np.array([])
    for b in x:
        retval = np.append(retval, gm(a, b))
    return retval


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

# u, v     = asm_up_to(n, a, b)
# up, vp   = asm_up_to(n, a, b)
# upp, vpp = agm_up_to(n, a, b)
# print(sym_to_arr(u))
# print(sym_to_arr(v))
# print(sym_to_arr(conv_rate2(n - 2, u, v, 1)))
# print(sym_to_arr(conv_rate2(n - 2, up, vp, 1)))
# print(sym_to_arr(conv_rate(n - 2, vpp, upp[n - 1], 2)))
# d = diffs(n - 1, u, v)
# p = conv_order(n - 2, v, v[n - 1])
# print(v)
# print(sym_to_arr(test(n, v, musso_lim(a, b))))

# x = []
# for i in range(0, len(u)):
#     x.append(i)

# plt.plot(x, u, '-', label="u")
# plt.plot(x, v, '-', label="v")
# plt.plot(x, up, '-', label="u'")
# plt.plot(x, vp, '-', label="v'")
# plt.plot(x, upp, '-', label="x")
# plt.plot(x, vpp, '-', label="y")
# plt.xlabel("n")
# plt.legend()
# plt.show()

x = np.linspace(0.0, 2.5, 200)
# y1 = apm_graph(1, x)
# y2 = agm_graph(1, x)
y3 = asm_graph(1, x)
# y4 = am_graph(1, x)
# y5 = gm_graph(1, x)
# plt.plot(x, y1, label="APM")
# plt.plot(x, y2, label="AGM")
plt.plot(x, y3, label="ASM")
# plt.plot(x, y4, label="AM")
# plt.plot(x, y5, label="GM")
# plt.legend()
plt.show()