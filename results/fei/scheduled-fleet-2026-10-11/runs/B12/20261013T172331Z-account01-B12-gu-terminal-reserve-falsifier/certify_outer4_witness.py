#!/usr/bin/env python3
"""High-precision certificate data for the four-input envelope witness.

The Walsh coefficients and all cap masses are exact Fractions.  Decimal logs
are evaluated at 100 digits.  This certifies the strict numerical separation
from constant 3 (but is not a machine-checked transcendental interval proof).
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import json

getcontext().prec = 100
D = Decimal
LN2 = D(2).ln()


def walsh(values):
    out = [Fraction(v) for v in values]
    n = len(out)
    step = 1
    while step < n:
        for base in range(0, n, 2 * step):
            for j in range(base, base + step):
                u, v = out[j], out[j + step]
                out[j], out[j + step] = u + v, u - v
        step *= 2
    return [x / n for x in out]


def upper(x):
    out = list(x)
    nbits = len(out).bit_length() - 1
    for bit in range(nbits):
        for mask in range(1 << nbits):
            if not ((mask >> bit) & 1):
                out[mask] += out[mask | (1 << bit)]
    return out


def dec(x):
    return D(x.numerator) / D(x.denominator)


def entropy(atoms, caps=None):
    caps = upper(atoms) if caps is None else caps
    ans = D(0)
    for p, cap in zip(atoms, caps):
        if p:
            ans += dec(p) * (dec(cap) / dec(p)).ln() / LN2
    return ans


def psi(mu):
    q = mu * mu
    if not q:
        return D(0)
    return dec(q) * (D(1) / dec(q)).ln() / LN2


OUTER_INDEX = 10439
BIT = 0
OUTER = [1 if (OUTER_INDEX >> r) & 1 else -1 for r in range(16)]
minus_rows = [r for r in range(16) if not ((r >> BIT) & 1)]
plus_rows = [r | (1 << BIT) for r in minus_rows]
av = [Fraction(OUTER[p] + OUTER[m], 2) for p, m in zip(plus_rows, minus_rows)]
bv = [Fraction(OUTER[p] - OUTER[m], 2) for p, m in zip(plus_rows, minus_rows)]
a = walsh(av)
b = walsh(bv)
b2 = [x * x for x in b]
beta = sum(b2, Fraction())
eb = entropy(b2)


def theta(mu):
    alpha2 = 1 - mu * mu
    c = [x + mu * y for x, y in zip(a, b)]
    c2 = [x * x for x in c]
    mixed = [x + alpha2 * y for x, y in zip(c2, b2)]
    return entropy(c2, upper(mixed)) + dec(alpha2) * eb - dec(beta) * psi(mu)


def theta_prime_at_minus_one():
    mu = Fraction(-1)
    c = [x + mu * y for x, y in zip(a, b)]
    c2 = [x * x for x in c]
    caps = upper(c2)
    # At mu=-1, derivative of c_R^2 + (1-mu^2)b_R^2 is 2 a_R b_R.
    cap_primes = upper([2 * x * y for x, y in zip(a, b)])
    ans = D(0)
    for x, y, cap, cp in zip(c, b, caps, cap_primes):
        if not x:
            continue
        xd, yd, cd, cpd = dec(x), dec(y), dec(cap), dec(cp)
        ans += 2 * xd * yd * (cd / (xd * xd)).ln() / LN2
        ans += xd * xd * (cpd / cd - 2 * yd / xd) / LN2
    # derivative of (1-mu^2) E_b at mu=-1
    ans += 2 * eb
    # psi'(-1)=2/ln 2
    ans -= dec(beta) * D(2) / LN2
    return ans


tm = theta(Fraction(-1))
tp = theta(Fraction(1))
tprime = theta_prime_at_minus_one()
endpoint_slope = tprime + (tm - tp) / 2
endpoint_ratio = endpoint_slope / (2 * dec(beta))

mu = Fraction(-127, 128)
centered = theta(mu) - (dec(1 - mu) * tm + dec(1 + mu) * tp) / 2
grid_ratio = centered / (dec(beta) * dec(1 - mu * mu))

def fs(xs):
    return [str(x) for x in xs]


result = {
    "status": "HIGH_PRECISION_CERTIFICATE_DATA",
    "outer_index": OUTER_INDEX,
    "outer_bit": BIT,
    "truth_table_row_order": OUTER,
    "a_exact": fs(a),
    "b_exact": fs(b),
    "beta_exact": str(beta),
    "E_b_decimal": str(eb),
    "theta_minus_one": str(tm),
    "theta_plus_one": str(tp),
    "theta_prime_minus_one": str(tprime),
    "endpoint_centered_slope": str(endpoint_slope),
    "endpoint_ratio_limit": str(endpoint_ratio),
    "endpoint_ratio_minus_3": str(endpoint_ratio - 3),
    "grid_mu_exact": str(mu),
    "grid_centered_theta": str(centered),
    "grid_ratio": str(grid_ratio),
    "grid_ratio_minus_3": str(grid_ratio - 3),
    "decimal_precision": getcontext().prec,
    "random_seed": None,
    "limitation": "Decimal logarithms are not outward-rounded interval arithmetic",
}
print(json.dumps(result, indent=2, sort_keys=True))
