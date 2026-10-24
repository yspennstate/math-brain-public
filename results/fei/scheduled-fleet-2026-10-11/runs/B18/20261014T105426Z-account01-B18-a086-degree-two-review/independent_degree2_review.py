#!/usr/bin/env python3
"""Independent reconstruction of B11-A052-DEGREE-TWO-EXTREMAL-v1.

Uses integer Walsh numerators and 100-digit Decimal logarithms.  The author
certificate supplies directed rational log enclosures; this independent
implementation checks the truth-table classification, all formulas, all
signs, sharp cases, and invariance under one added dummy variable.
"""
from decimal import Decimal, getcontext

getcontext().prec = 100
LN2 = Decimal(2).ln()
TOL = Decimal('1e-80')


def fwht_int(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def spectral(vals):
    n = len(vals).bit_length()-1
    N = len(vals)
    wnum = fwht_int(vals)
    den = N*N
    pnum = [x*x for x in wnum]
    pinum = pnum[:]
    for bit in range(n):
        for s in range(N):
            if not ((s >> bit) & 1):
                pinum[s] += pinum[s | (1 << bit)]
    I_num = sum(s.bit_count()*pnum[s] for s in range(N))
    U = Decimal(0)
    for p, pi in zip(pnum, pinum):
        if p:
            U += Decimal(p)/Decimal(den) * (Decimal(pi)/Decimal(p)).ln()/LN2
    H = Decimal(0)
    for p in pnum:
        if p:
            H += Decimal(p)/Decimal(den) * (Decimal(den)/Decimal(p)).ln()/LN2
    return wnum, pnum, pinum, Decimal(I_num)/Decimal(den), U, H


def restrict(vals, bit, value):
    return [v for x, v in enumerate(vals) if ((x >> bit) & 1) == value]


def metrics(vals):
    n = len(vals).bit_length()-1
    w, p, pi, I, U, H = spectral(vals)
    child = Decimal(0)
    for bit in range(n):
        for value in (0, 1):
            child += spectral(restrict(vals, bit, value))[4]/2
    return w, p, pi, I, U, Decimal(n)*U-child, H


def add_dummy(vals):
    # New highest bit is ignored.
    return list(vals) + list(vals)


cases = []
for mask in range(1 << 15):
    vals = [1] + [1 if ((mask >> (x-1)) & 1) else -1 for x in range(1, 16)]
    w = fwht_int(vals)
    if any(w[s] and s.bit_count() > 2 for s in range(16)):
        continue
    cases.append((mask, vals))

assert len(cases) == 111
eq_g = eq_h = 0
strict_g = strict_h = 0
min_g = None
min_h = None
dummy_checks = 0
worst_R = None
worst_mask = None

for mask, vals in cases:
    _, _, _, I, U, G, H = metrics(vals)
    sg = 2*I-G
    sh = 2*I-H
    assert sg > -TOL, (mask, sg)
    assert sh > -TOL, (mask, sh)
    if abs(sg) < TOL:
        eq_g += 1
    else:
        strict_g += 1
        min_g = sg if min_g is None else min(min_g, sg)
    if abs(sh) < TOL:
        eq_h += 1
    else:
        strict_h += 1
        min_h = sh if min_h is None else min(min_h, sh)
    R = G-4*I-Decimal(3)*U/Decimal(4)
    if worst_R is None or R > worst_R:
        worst_R, worst_mask = R, mask

    # Dummy coordinates must create no spectral mass, influence, U, or G.
    _, _, _, I5, U5, G5, H5 = metrics(add_dummy(vals))
    assert abs(I5-I) < TOL
    assert abs(U5-U) < TOL
    assert abs(G5-G) < TOL
    assert abs(H5-H) < TOL
    dummy_checks += 4

assert eq_g == 25 and strict_g == 86
assert eq_h == 25 and strict_h == 86
assert abs(min_g-Decimal(2)) < TOL
assert abs(min_h-Decimal(1)) < TOL
assert worst_R <= TOL

print('PASS_INDEPENDENT_RECONSTRUCTION')
print(f'degree_le_2_mod_sign_cases={len(cases)}')
print(f'G_equalities={eq_g}')
print(f'G_strict={strict_g}')
print(f'min_positive_2I_minus_G={min_g}')
print(f'H_equalities={eq_h}')
print(f'H_strict={strict_h}')
print(f'min_positive_2I_minus_H={min_h}')
print(f'worst_frozen_residual={worst_R}')
print(f'worst_frozen_residual_mask={worst_mask}')
print(f'dummy_variable_identity_checks={dummy_checks}')
print('decimal_precision=100')
print('random_seed=None')
