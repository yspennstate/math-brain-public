#!/usr/bin/env python3
"""Exact formal log expression for the outer4 endpoint-ratio witness."""

from fractions import Fraction
from collections import defaultdict
from decimal import Decimal, getcontext

OUTER_INDEX = 10439
outer = [1 if (OUTER_INDEX >> r) & 1 else -1 for r in range(16)]


def walsh(v):
    out = [Fraction(x) for x in v]
    step = 1
    while step < len(out):
        for base in range(0, len(out), 2 * step):
            for k in range(base, base + step):
                x, y = out[k], out[k + step]
                out[k], out[k + step] = x + y, x - y
        step *= 2
    return [x / len(out) for x in out]


def upper(v):
    out = list(v)
    n = len(v).bit_length() - 1
    for bit in range(n):
        for mask in range(1 << n):
            if not ((mask >> bit) & 1):
                out[mask] += out[mask | (1 << bit)]
    return out


def factors(n):
    ans = defaultdict(int)
    p = 2
    while p*p <= n:
        while n % p == 0:
            ans[p] += 1
            n //= p
        p += 1
    if n > 1:
        ans[n] += 1
    return ans


class Expr:
    """sum_p coeff[p] log_2(p) + e_coeff log_2(e)."""
    def __init__(self):
        self.logs = defaultdict(Fraction)
        self.e = Fraction()

    def add_log_rational(self, coeff, q):
        assert q > 0
        for p, k in factors(q.numerator).items():
            self.logs[p] += coeff*k
        for p, k in factors(q.denominator).items():
            self.logs[p] -= coeff*k

    def __iadd__(self, other):
        for p, c in other.logs.items():
            self.logs[p] += c
        self.e += other.e
        return self

    def scale(self, q):
        z = Expr()
        z.logs.update({p: q*c for p, c in self.logs.items()})
        z.e = q*self.e
        return z

    def minus(self, other):
        return self.plus(other.scale(-1))

    def plus(self, other):
        z = self.scale(1)
        z += other
        return z

    def text(self):
        parts = [f"({c})*log2({p})" for p, c in sorted(self.logs.items()) if c]
        if self.e:
            parts.append(f"({self.e})*log2(e)")
        return " + ".join(parts) if parts else "0"

    def decimal(self, prec=80):
        getcontext().prec = prec
        d = Decimal
        ln2 = d(2).ln()
        ans = d(0)
        for p, c in self.logs.items():
            ans += d(c.numerator)/d(c.denominator) * d(p).ln()/ln2
        ans += d(self.e.numerator)/d(self.e.denominator) / ln2
        return ans


def entropy_expr(atoms, caps=None):
    caps = upper(atoms) if caps is None else caps
    z = Expr()
    for p, cap in zip(atoms, caps):
        if p:
            z.add_log_rational(p, cap/p)
    return z


minus = [r for r in range(16) if not (r & 1)]
plus = [r | 1 for r in minus]
a = walsh([Fraction(outer[p] + outer[m], 2) for p, m in zip(plus, minus)])
b = walsh([Fraction(outer[p] - outer[m], 2) for p, m in zip(plus, minus)])
b2 = [x*x for x in b]
beta = sum(b2, Fraction())
eb = entropy_expr(b2)


def theta_endpoint(mu):
    c2 = [(x+mu*y)**2 for x, y in zip(a, b)]
    return entropy_expr(c2)


def theta(mu):
    alpha2 = 1-mu*mu
    c2 = [(x+mu*y)**2 for x, y in zip(a, b)]
    mixed = [x+alpha2*y for x, y in zip(c2, b2)]
    z = entropy_expr(c2, upper(mixed))
    z += eb.scale(alpha2)
    q = mu*mu
    if q:
        psi_expr = Expr()
        psi_expr.add_log_rational(q, 1/q)
        z += psi_expr.scale(-beta)
    return z


c = [x-y for x, y in zip(a, b)]
c2 = [x*x for x in c]
caps = upper(c2)
cap_primes = upper([2*x*y for x, y in zip(a, b)])
tprime = Expr()
for x, y, cap, cp in zip(c, b, caps, cap_primes):
    if x:
        tprime.add_log_rational(2*x*y, cap/(x*x))
        tprime.e += x*x*(cp/cap - 2*y/x)
tprime += eb.scale(2)
tprime.e -= 2*beta

tm = theta_endpoint(-1)
tp = theta_endpoint(1)
slope = Expr()
slope += tprime
slope += tm.scale(Fraction(1, 2))
slope += tp.scale(Fraction(-1, 2))
ratio = slope.scale(Fraction(1, 1)/(2*beta))

mu = Fraction(-127, 128)
centered = theta(mu)
centered += tm.scale(-Fraction(1-mu, 2))
centered += tp.scale(-Fraction(1+mu, 2))
grid_ratio = centered.scale(1/(beta*(1-mu*mu)))


def integer_log_inequality(expr, constant):
    """Return exact integer comparison equivalent to expr > constant."""
    import math
    den = 1
    for c0 in list(expr.logs.values()) + [expr.e]:
        den = math.lcm(den, c0.denominator)
    assert not expr.e, "interior expression should contain no log2(e)"
    exponents = {p: int(c0*den) for p, c0 in expr.logs.items() if c0}
    exponents[2] = exponents.get(2, 0) - constant*den
    left = 1
    right = 1
    for p, exponent in exponents.items():
        if exponent >= 0:
            left *= p**exponent
        else:
            right *= p**(-exponent)
    return den, exponents, left, right

print("beta =", beta)
print("theta(-1) =", tm.text())
print("theta(1) =", tp.text())
print("theta'(-1+) =", tprime.text())
print("endpoint centered slope =", slope.text())
print("endpoint ratio =", ratio.text())
print("endpoint ratio numerical =", ratio.decimal())
print("endpoint ratio minus 3 =", ratio.decimal()-Decimal(3))
print("grid mu =", mu)
print("grid ratio =", grid_ratio.text())
print("grid ratio numerical =", grid_ratio.decimal())
den, exponents, left, right = integer_log_inequality(grid_ratio, 3)
print("grid strict proof denominator =", den)
print("grid strict proof prime exponents after subtracting 3 =", exponents)
print("grid strict proof left bit length =", left.bit_length())
print("grid strict proof right bit length =", right.bit_length())
print("grid strict proof exact comparison left>right =", left > right)
print("grid strict proof difference sign =", (left > right) - (left < right))
