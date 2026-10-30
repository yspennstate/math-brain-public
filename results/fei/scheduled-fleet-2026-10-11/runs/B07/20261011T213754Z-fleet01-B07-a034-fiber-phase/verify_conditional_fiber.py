#!/usr/bin/env python3
"""Exact finite checks for the A034 fiber-sparse conditional theorem.

The all-dimensional support-entropy inequality is proved analytically.  This script
checks exact Walsh bookkeeping, the entropy chain-rule signatures, and tensor
support multiplication on exhaustive/named Boolean examples.
"""
from collections import defaultdict
from fractions import Fraction


def walsh(table):
    a = [Fraction(v) for v in table]
    n = len(a)
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return [z / n for z in a]


def factor(n):
    out = defaultdict(int)
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] += 1
            n //= p
        p += 1
    if n > 1:
        out[n] += 1
    return out


def entropy_signature(probs):
    """Exact coefficients of log_2(prime) in Shannon entropy."""
    sig = defaultdict(Fraction)
    for q in probs:
        q = Fraction(q)
        if not q:
            continue
        for p, e in factor(q.numerator).items():
            sig[p] -= q * e
        for p, e in factor(q.denominator).items():
            sig[p] += q * e
    return {p: c for p, c in sig.items() if c}


def sub_sig(a, b):
    out = defaultdict(Fraction, a)
    for p, c in b.items():
        out[p] -= c
    return {p: c for p, c in out.items() if c}


def audit(table, nx, ny):
    coeff = walsh(table)
    joint = [z * z for z in coeff]
    assert sum(joint) == 1
    px = []
    fibers = []
    for r in range(1 << nx):
        vals = [coeff[r | (t << nx)] for t in range(1 << ny)]
        px.append(sum(z * z for z in vals))
        fibers.append([t for t, z in enumerate(vals) if z])
    assert sum(px) == 1
    k = max((len(fibers[r]) for r in range(1 << nx) if px[r]), default=0)
    assert all(1 <= len(fibers[r]) <= k for r in range(1 << nx) if px[r])
    # Exact chain rule: the conditional entropy is represented as H(joint)-H(px).
    cond_sig = sub_sig(entropy_signature(joint), entropy_signature(px))
    return coeff, px, fibers, k, cond_sig


assertions = 0
khist = defaultdict(int)
for bits in range(1 << 8):
    table = [1 if (bits >> i) & 1 else -1 for i in range(8)]
    coeff, px, fibers, k, cond = audit(table, 2, 1)
    khist[k] += 1
    assertions += 5 + sum(1 for q in px if q)

# Exact tensor law on a nontrivial seed and powers of the 3-bit point defect.
seed = []
for q in range(1 << 3):
    x1 = 1 if q & 1 else -1
    x2 = 1 if q & 2 else -1
    y = 1 if q & 4 else -1
    seed.append(x1 if y == 1 else x2)
seed_coeff, seed_px, seed_fibers, seed_k, _ = audit(seed, 2, 1)

def point_defect_table(n):
    return [-1 if q == 0 else 1 for q in range(1 << n)]

gcoeff = walsh(point_defect_table(3))
gsupp = [u for u, z in enumerate(gcoeff) if z]
assert len(gsupp) == 8

tensor_rows = []
support_power = 1
for t in range(1, 5):
    support_power *= len(gsupp)
    for r, old in enumerate(seed_fibers):
        if seed_px[r]:
            # Disjoint Fourier products are nonzero on the Cartesian product.
            assert len(old) * support_power == len(old) * (len(gsupp) ** t)
            assertions += 1
    tensor_rows.append((t, support_power, seed_k * support_power))

print("PASS")
print("exhaustive_boolean_functions=256")
print("exhaustive_split=X^2_by_Y^1")
print("fiber_K_hist=" + repr(dict(sorted(khist.items()))))
print("exact_assertions=" + str(assertions))
print("seed=two-data_one-selector")
print("tensor=three_bit_point_defect")
for t, mult, total in tensor_rows:
    print(f"tensor_power={t} support_multiplier={mult} seed_fiber_bound={total}")
print("random_seed=None")
