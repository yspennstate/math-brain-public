#!/usr/bin/env python3
"""Point-defect test of a fixed-coefficient orbit lift under fair activation."""
from math import log, log2


def xr(x, y):
    return 0.0 if x == 0 else x * log2(y / x)


def T(a, b):
    return xr(a, a + b) + xr(b, a + b)


def caps(p):
    a = list(p)
    n = len(a).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(len(a)):
            if not s & bit:
                a[s] += a[s | bit]
    return a


def U4(p):
    return sum(xr(x, y) for x, y in zip(p, caps(p)))


def R(m):
    return U4([(1 + m) ** 2 / 4, (1 - m * m) / 4,
               (1 - m) ** 2 / 4, (1 - m * m) / 4]) - 0.5 * xr(m * m, 1)


def Bz(m):
    return (1 - m * m) / 2 + 0.25 * T((1 + m) ** 2, (1 - m) ** 2)


def C(m, p):
    return (-0.5 * T(m * m, p) + 0.25 * T((1 + m) ** 2, p)
            + 0.25 * T((1 - m) ** 2, p))


def P(m, a):
    return R(m) - 0.5 * (R(m - a) + R(m + a)) - C(m, a * a)


def q(t):
    return 0.0 if t == 0 else t * log2(1 / t) + 2 * t / log(2)


eta = 1.0
c = 29 / 2 + 2 / log(2)
lam = 2.0
print("eta=", eta, "c=", c, "lambda=", lam)
print("r eps residual residual/eps sumP/eps root/eps orbit/eps")
for r in range(2, 41):
    eps = 2 ** (1-r)
    m = 1 - eps
    J = eps / 2
    sumP = r * P(m, -eps)
    root = (2 + eta) * R(m) - Bz(m) - c * J
    orbit = lam * q(J) + lam * r * eps / 2
    residual = sumP + root + orbit
    print(r, f"{eps:.17g}", f"{residual:.17g}", f"{residual/eps:.12g}",
          f"{sumP/eps:.12g}", f"{root/eps:.12g}", f"{orbit/eps:.12g}")
