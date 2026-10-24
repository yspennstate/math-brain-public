#!/usr/bin/env python3
"""Exact two-bit Boolean checks for the critical-pruning identity.

All entropies for two-bit Boolean functions are rational because their nonzero
squared Fourier masses are 1 or 1/4.  The all-dimensional result is analytic.
"""

from fractions import Fraction


def fwht(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def HI(vals):
    n = len(vals).bit_length() - 1
    ps = [Fraction(x * x, 1 << (2 * n)) for x in fwht(vals)]
    H = Fraction(0)
    for p in ps:
        if p == Fraction(1, 4):
            H += Fraction(1, 2)  # -(1/4) log2(1/4)
        elif p not in (0, 1):
            raise AssertionError((vals, p))
    I = sum(p * mask.bit_count() for mask, p in enumerate(ps))
    return H, I


def restrict(vals, n, i, bit):
    return [vals[x] for x in range(1 << n) if ((x >> i) & 1) == bit]


checks = 0


def check(x):
    global checks
    assert x
    checks += 1


critical_count = 0
for mask in range(1, 15):  # omit the two constant two-bit tables
    vals = [1 if (mask >> x) & 1 else -1 for x in range(4)]
    H, I = HI(vals)
    R = H / I
    child_ratios = []
    rows = []
    for i in range(2):
        kids = [restrict(vals, 2, i, b) for b in (0, 1)]
        his = [HI(k) for k in kids]
        Hbar = sum(x[0] for x in his) / 2
        Ibar = sum(x[1] for x in his) / 2
        d = I - Ibar
        Delta = H - Hbar
        check(Hbar - R * Ibar == R * d - Delta)
        if Ibar and d:
            check((Hbar / Ibar) - R == d * (R - Delta / d) / Ibar)
        for hk, ik in his:
            if ik:
                child_ratios.append(hk / ik)
        rows.append((Delta, d))
    is_critical = all(r <= R for r in child_ratios)
    if is_critical:
        critical_count += 1
        for Delta, d in rows:
            check(Delta >= R * d)

# Exact deficit and tensor-prime algebra over rational H/I data.
for C in [Fraction(1), Fraction(3, 2), Fraction(4)]:
    for Hg, Ig, Hh, Ih in [
        (Fraction(2), Fraction(3, 2), Fraction(0), Fraction(3)),
        (Fraction(7, 3), Fraction(2), Fraction(5, 4), Fraction(1, 2)),
    ]:
        check((Hg + Hh) - C * (Ig + Ih) == (Hg - C * Ig) + (Hh - C * Ih))

print(f"PASS: {checks} exact assertions")
print(f"two-bit descendant-critical truth tables: {critical_count} of 14")
print("scope: exact two-bit identity check; all-dimensional theorem is analytic")
