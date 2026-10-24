#!/usr/bin/env python3
"""Formal logarithmic and exact integer certificate for the outer5 witness."""

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
import math

U_INDEX = 22338
V_INDEX = 38505
U = [1 if (U_INDEX >> r) & 1 else -1 for r in range(16)]
V = [1 if (V_INDEX >> r) & 1 else -1 for r in range(16)]


def walsh(v):
    out = [Fraction(x) for x in v]
    step = 1
    while step < len(out):
        for base in range(0, len(out), 2*step):
            for k in range(base, base+step):
                x, y = out[k], out[k+step]
                out[k], out[k+step] = x+y, x-y
        step *= 2
    return [x/len(out) for x in out]


def upper(v):
    out = list(v)
    n = len(v).bit_length()-1
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
    """sum_p c_p log2(p) + c_e log2(e)."""
    def __init__(self):
        self.logs = defaultdict(Fraction)
        self.e = Fraction()

    def add_log_q(self, coefficient, q):
        assert q > 0
        for p, k in factors(q.numerator).items():
            self.logs[p] += coefficient*k
        for p, k in factors(q.denominator).items():
            self.logs[p] -= coefficient*k

    def __iadd__(self, other):
        for p, c in other.logs.items():
            self.logs[p] += c
        self.e += other.e
        return self

    def scale(self, q):
        z = Expr()
        z.logs.update({p:q*c for p, c in self.logs.items()})
        z.e = q*self.e
        return z

    def text(self):
        parts = [f"({c})*log2({p})" for p, c in sorted(self.logs.items()) if c]
        if self.e:
            parts.append(f"({self.e})*log2(e)")
        return " + ".join(parts) if parts else "0"

    def decimal(self, precision=80):
        getcontext().prec = precision
        d, ln2 = Decimal, Decimal(2).ln()
        ans = d(0)
        for p, c in self.logs.items():
            ans += d(c.numerator)/d(c.denominator)*d(p).ln()/ln2
        ans += d(self.e.numerator)/d(self.e.denominator)/ln2
        return ans


def entropy_expr(atoms, caps=None):
    caps = upper(atoms) if caps is None else caps
    z = Expr()
    for p, c in zip(atoms, caps):
        if p:
            z.add_log_q(p, c/p)
    return z


uh, vh = walsh(U), walsh(V)
a = [(x+y)/2 for x, y in zip(uh, vh)]
b = [(y-x)/2 for x, y in zip(uh, vh)]
b2 = [x*x for x in b]
beta = sum(b2, Fraction())
eb = entropy_expr(b2)


def theta(mu):
    alpha2 = 1-mu*mu
    c2 = [(x+mu*y)**2 for x, y in zip(a, b)]
    mixed = [x+alpha2*y for x, y in zip(c2, b2)]
    z = entropy_expr(c2, upper(mixed))
    z += eb.scale(alpha2)
    q = mu*mu
    if q:
        ps = Expr()
        ps.add_log_q(q, 1/q)
        z += ps.scale(-beta)
    return z


tm, tp = theta(Fraction(-1)), theta(Fraction(1))
mu = Fraction(-1, 2)
centered = theta(mu)
centered += tm.scale(-Fraction(1-mu, 2))
centered += tp.scale(-Fraction(1+mu, 2))
ratio = centered.scale(1/(beta*(1-mu*mu)))


def integer_comparison(expr, constant):
    assert not expr.e
    den = 1
    for c in expr.logs.values():
        den = math.lcm(den, c.denominator)
    exponents = {p:int(c*den) for p, c in expr.logs.items() if c}
    exponents[2] = exponents.get(2, 0)-constant*den
    left = right = 1
    for p, exponent in exponents.items():
        if exponent >= 0:
            left *= p**exponent
        else:
            right *= p**(-exponent)
    return den, exponents, left, right


den, exponents, left, right = integer_comparison(ratio, 4)
print("beta =", beta)
print("mu =", mu)
print("normalized finite ratio =", ratio.text())
print("normalized finite ratio numerical =", ratio.decimal())
print("ratio minus 4 numerical =", ratio.decimal()-Decimal(4))
print("strict proof denominator =", den)
print("strict proof prime exponents after subtracting 4 =", exponents)
print("strict proof left bit length =", left.bit_length())
print("strict proof right bit length =", right.bit_length())
print("strict proof exact comparison left>right =", left > right)
print("strict proof difference sign =", (left > right)-(left < right))
