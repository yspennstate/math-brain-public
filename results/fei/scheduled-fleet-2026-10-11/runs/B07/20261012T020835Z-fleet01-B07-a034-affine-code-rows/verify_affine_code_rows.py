#!/usr/bin/env python3
"""Exact/interval checks for B07 A034 affine-code row theorem.

Standard library only.  Walsh transforms and code identities are exact
Fractions.  Entropy comparisons use outward rational logarithm intervals.
"""

from fractions import Fraction as F
from itertools import combinations


def walsh(values):
    a = [F(v) for v in values]
    n = len(a)
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return [z / n for z in a]


def parity(x):
    return x.bit_count() & 1


def rref(rows, n):
    rows = [x for x in rows if x]
    pivot = 0
    for col in range(n - 1, -1, -1):
        hit = next((j for j in range(pivot, len(rows)) if (rows[j] >> col) & 1), None)
        if hit is None:
            continue
        rows[pivot], rows[hit] = rows[hit], rows[pivot]
        for j in range(len(rows)):
            if j != pivot and ((rows[j] >> col) & 1):
                rows[j] ^= rows[pivot]
        pivot += 1
        if pivot == len(rows):
            break
    rows = [x for x in rows if x]
    return tuple(sorted(rows, reverse=True))


def span(basis):
    out = {0}
    for b in basis:
        out |= {x ^ b for x in list(out)}
    return out


def subspaces(n):
    seen = {()}
    nonzero = range(1, 1 << n)
    for k in range(1, n + 1):
        for rows in combinations(nonzero, k):
            rr = rref(rows, n)
            if len(rr) == k:
                seen.add(rr)
    return sorted(seen, key=lambda z: (len(z), z))


def atanh_log_interval(y, terms=80):
    y = F(y)
    assert 1 <= y <= 2
    z = (y - 1) / (y + 1)
    partial = F()
    for j in range(terms):
        partial += 2 * z ** (2 * j + 1) / (2 * j + 1)
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return partial, partial + tail


LN2 = atanh_log_interval(F(2))


def ln_interval(x):
    x = F(x)
    assert x > 0
    if x < 1:
        lo, hi = ln_interval(1 / x)
        return -hi, -lo
    shift = 0
    while x >= 2:
        x /= 2
        shift += 1
    lo, hi = atanh_log_interval(x)
    return shift * LN2[0] + lo, shift * LN2[1] + hi


def entropy_nats_interval(probs):
    lo = hi = F()
    for q in probs:
        q = F(q)
        if not q:
            continue
        lq, hq = ln_interval(q)
        lo -= q * hq
        hi -= q * lq
    return lo, hi


def affine_defect(n, basis, offset_bits):
    """-1 on {y: <basis_j,y>=offset_j}, +1 elsewhere."""
    return [
        -1 if all(parity(row & y) == ((offset_bits >> j) & 1)
                  for j, row in enumerate(basis)) else 1
        for y in range(1 << n)
    ]


def audit_defect(n, basis, offset):
    k = len(basis)
    W = span(basis)
    vals = affine_defect(n, basis, offset)
    coeffs = walsh(vals)
    delta = F(1, 1 << k)
    checks = 0

    assert coeffs[0] == 1 - 2 * delta
    checks += 1
    for t, c in enumerate(coeffs):
        if t == 0:
            continue
        assert (abs(c) == 2 * delta) == (t in W)
        checks += 1
    assert sum(c * c for c in coeffs) == 1
    checks += 1

    active = 0
    for j in range(n):
        count = sum((t >> j) & 1 for t in W)
        if count:
            assert count == 1 << (k - 1)
            active += 1
        checks += 1
    assert active >= k
    influence = sum(t.bit_count() * coeffs[t] ** 2 for t in range(1 << n))
    assert influence == 2 * active * delta
    checks += 2

    # Rigorous entropy inequality H <= 4 I, compared in nats.
    hlo, hhi = entropy_nats_interval([c * c for c in coeffs])
    assert hlo >= 0
    assert hhi <= 4 * influence * LN2[0]
    checks += 2

    # For positive-entropy defects, the square has non-affine minority density.
    if k >= 2:
        tensor_density = 2 * delta * (1 - delta)
        assert tensor_density.numerator > 1
        checks += 1
    return checks


subspace_count = coset_count = assertion_count = 0
dimension_histogram = {}
for n in range(1, 6):
    spaces = subspaces(n)
    dimension_histogram[n] = {k: 0 for k in range(n + 1)}
    for basis in spaces:
        k = len(basis)
        dimension_histogram[n][k] += 1
        subspace_count += 1
        if k == 0:
            continue
        for offset in range(1 << k):
            assertion_count += audit_defect(n, basis, offset)
            coset_count += 1


# Named full Boolean tensors f(x,y)=u(x)sigma(y): verify row normalization
# and the identity sum_R p_R I(sigma_R)=I_Y(f).
named = []


def majority3(x):
    bits = [1 if (x >> j) & 1 else -1 for j in range(3)]
    return 1 if sum(bits) > 0 else -1


def parity3(x):
    return -1 if parity(x) else 1


def point_defect3(x):
    return -1 if x == 0 else 1


for label, u in [("majority3", majority3), ("parity3", parity3),
                 ("point_defect3", point_defect3)]:
    nx, ny = 3, 5
    # Dense 3-dimensional dual code on all five Y coordinates.
    basis = rref((0b10101, 0b01110, 0b11100), ny)
    assert len(basis) == 3
    sigma = affine_defect(ny, basis, 0b101)
    uh = walsh([u(x) for x in range(1 << nx)])
    sh = walsh(sigma)
    full = walsh([u(z & 7) * sigma[z >> nx] for z in range(1 << (nx + ny))])
    iy = sum((mask >> nx).bit_count() * c * c for mask, c in enumerate(full))
    isigma = sum(t.bit_count() * c * c for t, c in enumerate(sh))
    weighted_rows = F()
    for r, ur in enumerate(uh):
        p = ur * ur
        for t, st in enumerate(sh):
            assert full[r | (t << nx)] == ur * st
            assertion_count += 1
        if p:
            weighted_rows += p * isigma
    assert weighted_rows == iy
    assertion_count += 1
    named.append((label, iy))

print("PASS")
print(f"linear_subspaces_n_le_5={subspace_count}")
print(f"affine_cosets_checked={coset_count}")
print(f"exact_and_interval_assertions={assertion_count}")
print(f"subspace_dimension_histogram={dimension_histogram}")
for label, iy in named:
    print(f"named_tensor={label} I_Y={iy}")
print("log_bounds=exact rational atanh intervals, 80 terms")
print("random_seed=None")
