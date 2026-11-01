#!/usr/bin/env python3
"""Exact rational-log certificate for the rank-three orbit-lift failure.

The certified quantity is ln(2) times
  [L_{c,1}(A f)+2 Theta_{X+z}(A f)
   - (L_{c,1}(f)+2 Theta_X(f))/2]
for the three-bit point defect, X=[3], c=29/2+2/ln(2).
"""
from fractions import Fraction as F


class E:
    def __init__(self, const=F(0), logs=None):
        self.const = F(const)
        self.logs = dict(logs or {})
        self._clean()

    def _clean(self):
        self.logs = {p: c for p, c in self.logs.items() if c}
        return self

    def __add__(self, other):
        other = other if isinstance(other, E) else E(other)
        d = self.logs.copy()
        for p, c in other.logs.items():
            d[p] = d.get(p, F(0)) + c
        return E(self.const + other.const, d)

    __radd__ = __add__

    def __neg__(self):
        return E(-self.const, {p: -c for p, c in self.logs.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, E) else E(-other))

    def __rsub__(self, other):
        return E(other) - self

    def __mul__(self, a):
        a = F(a)
        return E(a * self.const, {p: a * c for p, c in self.logs.items()})

    __rmul__ = __mul__

    def __truediv__(self, a):
        return self * (F(1) / F(a))


def factors(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def ln_rat(x):
    x = F(x)
    assert x > 0
    d = {}
    for p, k in factors(x.numerator).items():
        d[p] = d.get(p, F(0)) + k
    for p, k in factors(x.denominator).items():
        d[p] = d.get(p, F(0)) - k
    return E(0, d)


LN2 = ln_rat(F(2))


def xr(x, y):
    x, y = F(x), F(y)
    return E() if x == 0 else x * ln_rat(y / x)


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
    return sum((xr(x, y) for x, y in zip(p, caps(p))), E())


def R(m):
    return U4([(1 + m) ** 2 / 4, (1 - m * m) / 4,
               (1 - m) ** 2 / 4, (1 - m * m) / 4]) - xr(m * m, 1) / 2


def Bz(m):
    return ((1 - m * m) / 2) * LN2 + T((1 + m) ** 2, (1 - m) ** 2) / 4


def C(m, p):
    return -T(m * m, p) / 2 + T((1 + m) ** 2, p) / 4 + T((1 - m) ** 2, p) / 4


def P(m, a):
    return R(m) - (R(m - a) + R(m + a)) / 2 - C(m, a * a)


def q(t):
    t = F(t)
    return E() if t == 0 else t * ln_rat(1 / t) + 2 * t


def ln_integer_interval(n, terms=80):
    # n=2^k*x with x in [1,2); ln x=2*atanh((x-1)/(x+1)).
    k = n.bit_length() - 1
    x = F(n, 1 << k)
    z = (x - 1) / (x + 1)

    def atanh_bounds(w):
        s = F(0)
        power = w
        for j in range(terms):
            s += power / (2 * j + 1)
            power *= w * w
        lo = 2 * s
        tail = 2 * power / ((2 * terms + 1) * (1 - w * w))
        return lo, lo + tail

    l2, u2 = atanh_bounds(F(1, 3))
    lx, ux = atanh_bounds(z)
    return k * l2 + lx, k * u2 + ux


def interval(expr):
    lo = hi = expr.const
    for p, c in expr.logs.items():
        lp, up = ln_integer_interval(p)
        if c >= 0:
            lo += c * lp
            hi += c * up
        else:
            lo += c * up
            hi += c * lp
    return lo, hi


r = 3
eps = F(1, 4)
m = 1 - eps
J = eps / 2
eta = F(1)
lam = F(2)

sumP = r * P(m, -eps)
# Multiplication by ln(2) converts the dimensionless cI term exactly:
# (29/2+2/ln2) J * ln2 = (29/2)J ln2 + 2J.
root = (2 + eta) * R(m) - Bz(m) - F(29, 2) * J * LN2 - 2 * J
orbit = lam * q(J) + (lam * r * eps / 2) * LN2
residual = sumP + root + orbit
lo, hi = interval(residual)

print("quantity=ln(2)*orbit_lift_residual")
print("exact_constant=", residual.const)
print("exact_log_coefficients=", sorted(residual.logs.items()))
print("lower_fraction=", lo)
print("upper_fraction=", hi)
print("lower_decimal=", float(lo))
print("upper_decimal=", float(hi))
print("residual_bits_lower=", float(lo / ln_integer_interval(2)[1]))
print("status=", "CERTIFIED_POSITIVE" if lo > 0 else "NOT_CERTIFIED")
