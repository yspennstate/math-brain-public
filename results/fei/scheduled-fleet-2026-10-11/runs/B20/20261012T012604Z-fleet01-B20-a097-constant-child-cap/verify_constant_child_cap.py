#!/usr/bin/env python3
"""Exact finite audit of the constant-child transfer identities.

Entropy equalities are compared as rational linear combinations of log2(p)
over primes.  Influence equalities use Fraction throughout.  The universal
critical cap is proved analytically in CROSS_ROUTE_SUBSTITUTION.tex; this
script does not infer it from the finite sweep.
"""

from collections import defaultdict
from fractions import Fraction


def fwht(v):
    a = list(v)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def factors(n):
    out = defaultdict(int)
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] += 1
            n //= d
        d += 1
    if n > 1:
        out[n] += 1
    return out


def log_signature(x):
    """Exact coefficients of log2(prime) in log2(x)."""
    if x == 0:
        return {}
    out = defaultdict(Fraction)
    for p, e in factors(x.numerator).items():
        out[p] += e
    for p, e in factors(x.denominator).items():
        out[p] -= e
    return dict(out)


def add(a, b, scale=Fraction(1)):
    out = defaultdict(Fraction, a)
    for p, c in b.items():
        out[p] += scale * c
    return {p: c for p, c in out.items() if c}


def entropy_signature(vals):
    W = fwht(vals)
    den2 = len(vals) ** 2
    out = {}
    for w in W:
        if not w:
            continue
        mass = Fraction(w * w, den2)
        out = add(out, log_signature(mass), -mass)
    return out


def influence(vals):
    out = Fraction(0)
    for bit in range((len(vals)).bit_length() - 1):
        out += Fraction(sum(vals[x] != vals[x ^ (1 << bit)] for x in range(len(vals))), len(vals))
    return out


def packet_signature(p):
    """Exact prime-log signature of F(p)=p*c(p)."""
    if p in (0, 1):
        return {}
    q = 1 - p
    out = {2: 4 * p * q}  # rational constant r equals r*log2(2)
    out = add(out, log_signature(q), -2 * q * q)
    out = add(out, log_signature(p), -2 * p * p)
    r = abs(1 - 2 * p)
    if r:
        out = add(out, log_signature(r), r * r)
    return {prime: c for prime, c in out.items() if c}


checks = 0
functions = 0
for n in range(0, 5):
    N = 1 << n
    for mask in range(1 << N):
        D = [-1 if (mask >> z) & 1 else 1 for z in range(N)]
        p = Fraction(sum(v == -1 for v in D), N)
        # First half is the constant +1 child, second half the D child.
        K = [1] * N + D

        lhs = entropy_signature(K)
        rhs = add({}, entropy_signature(D), Fraction(1, 2))
        rhs = add(rhs, packet_signature(p))
        assert lhs == rhs
        checks += 1

        assert influence(K) == influence(D) / 2 + p
        checks += 1

        # The physical selector influence itself is exactly p.
        selector_pivots = Fraction(sum(K[z] != K[z + N] for z in range(N)), N)
        assert selector_pivots == p
        checks += 1
        functions += 1

print("scope constant-versus-Boolean physical selector splices")
print("dimensions 0..4")
print("boolean_children", functions)
print("exact_assertions", checks)
print("entropy_arithmetic rational prime-log signatures")
print("influence_arithmetic Fraction")
print("random_seed None")
print("universal_cap_source analytic substitution plus pinned C_star interval")
print("PASS")

