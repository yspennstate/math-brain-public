#!/usr/bin/env python3
"""Exact/direct audit for the aligned-nullity-two shield theorem.

Walsh numerators and influence counts are integer exact.  Entropy and U are
evaluated from the resulting exact dyadic masses; the written proof supplies
the all-parameter theorem.
"""

from fractions import Fraction
from itertools import product
from math import log2
from random import Random


SEED = 0xB01A0032
rng = Random(SEED)


def dot(a, b):
    return sum(x & y for x, y in zip(a, b)) & 1


def mat_vec(M, u):
    return tuple(dot(row, u) for row in M)


def rank2(M, r):
    rows = [sum(v << j for j, v in enumerate(row)) for row in M]
    rank = 0
    for j in range(r):
        p = next((i for i in range(rank, len(rows)) if (rows[i] >> j) & 1), None)
        if p is None:
            continue
        rows[rank], rows[p] = rows[p], rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> j) & 1):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def walsh_masses(table):
    keys = tuple(table)
    n = len(keys[0]) if keys else 0
    N = len(keys)
    out = {}
    for a in product((0, 1), repeat=n):
        num = sum(v * (-1 if dot(a, x) else 1) for x, v in table.items())
        if num:
            out[a] = Fraction(num * num, N * N)
    assert sum(out.values()) == 1
    return out


def entropy(masses):
    return sum(float(p) * log2(float(1 / p)) for p in masses.values())


def upper_U(masses):
    ans = 0.0
    for S, p in masses.items():
        cap = sum(q for T, q in masses.items() if all(not bit or T[i] for i, bit in enumerate(S)))
        ans += float(p) * log2(float(cap / p))
    return ans


def influence_vector(table):
    keys = tuple(table)
    n = len(keys[0]) if keys else 0
    N = len(keys)
    ans = []
    for j in range(n):
        changed = 0
        for x in keys:
            y = x[:j] + (x[j] ^ 1,) + x[j + 1 :]
            changed += table[x] != table[y]
        ans.append(Fraction(changed, N))
    return ans


def make_P(M, D, a, b, c, sign=0):
    s, r = len(M), len(M[0]) if M else len(b)
    out = {}
    for x in product((0, 1), repeat=s):
        for u in product((0, 1), repeat=r):
            for z in product((0, 1), repeat=2):
                phase = dot(x, mat_vec(M, u)) ^ dot(a, x) ^ dot(b, u) ^ dot(c, z) ^ sign
                out[x + u + z] = D[u + z] * (-1 if phase else 1)
    return out


def make_q_times_g(g):
    out = {}
    n = len(next(iter(g)))
    for x, u in product((0, 1), repeat=2):
        for z in product((0, 1), repeat=n):
            out[(x, u) + z] = (-1 if x & u else 1) * g[z]
    return out


def restrict_table(table, j, bit):
    return {
        x[:j] + x[j + 1 :]: v
        for x, v in table.items()
        if x[j] == bit
    }


def G_value(table):
    root = upper_U(walsh_masses(table))
    n = len(next(iter(table)))
    return sum(root - 0.5 * (
        upper_U(walsh_masses(restrict_table(table, j, 0)))
        + upper_U(walsh_masses(restrict_table(table, j, 1)))
    ) for j in range(n))


counts = {
    "two_bit_fibers": 0,
    "exhaustive_canonical_cores": 0,
    "oriented_matrix_samples": 0,
    "direct_walsh_atoms": 0,
    "direct_U_endpoint_checks": 0,
    "hardness_seed_identities": 0,
}
max_H_over_I = 0.0


# Every two-bit Boolean function is affine or affine times z1*z2.
zs = tuple(product((0, 1), repeat=2))
for vals in product((-1, 1), repeat=4):
    f = dict(zip(zs, vals))
    masses = walsh_masses(f)
    H = entropy(masses)
    I = sum(influence_vector(f), Fraction())
    assert H <= 2 * float(I) + 1e-12
    if len(masses) == 1:
        assert abs(H) < 1e-12
    else:
        assert len(masses) == 4 and set(masses.values()) == {Fraction(1, 4)}
        assert abs(H - 2) < 1e-12 and I == 1
    counts["two_bit_fibers"] += 1


# Exhaust every D(u,z), modulo output complement, for canonical r=0,1,2.
# This includes all 32,768 four-bit core representatives at r=2.
for r in range(3):
    s = max(1, r)
    if r == 0:
        M = tuple(() for _ in range(s))
    else:
        M = tuple(tuple(1 if i == j else 0 for j in range(r)) for i in range(s))
    uzs = tuple(product((0, 1), repeat=r + 2))
    for mask in range(1 << ((1 << (r + 2)) - 1)):
        vals = [1] + [1 if (mask >> (i - 1)) & 1 else -1 for i in range(1, 1 << (r + 2))]
        D = dict(zip(uzs, vals))
        P = make_P(M, D, (0,) * s, (0,) * r, (0, 0))
        masses = walsh_masses(P)
        H = entropy(masses)
        infl = influence_vector(P)
        I = sum(infl, Fraction())
        # Exact fiber identity, evaluated from exact dyadic fiber spectra.
        fiber_H = 0.0
        fiber_I = Fraction()
        for u in product((0, 1), repeat=r):
            f = {z: D[u + z] for z in zs}
            fiber_H += entropy(walsh_masses(f)) / (1 << r)
            fiber_I += sum(influence_vector(f), Fraction()) / (1 << r)
        assert abs(H - (2 * r + fiber_H)) < 2e-11
        assert sum(infl[s:s + r], Fraction()) == Fraction(r, 2)
        assert sum(infl[s + r:], Fraction()) == fiber_I
        assert I >= r + fiber_I
        assert H <= 2 * float(I) + 2e-11
        if I:
            max_H_over_I = max(max_H_over_I, H / float(I))
        # U <= H proves the endpoint analytically.  Direct cap evaluation is
        # sampled because it is quadratic in Fourier support size.
        if r < 2 or mask % 16 == 0:
            U = upper_U(masses)
            assert U <= H + 2e-11
            assert U <= 2 * float(I) + 2e-11
            counts["direct_U_endpoint_checks"] += 1
        counts["exhaustive_canonical_cores"] += 1
        counts["direct_walsh_atoms"] += len(masses)


# Sample every small full-column-rank physical orientation and affine phase.
for r in (1, 2):
    for s in range(r, 4):
        matrices = []
        for raw in product((0, 1), repeat=s * r):
            M = tuple(tuple(raw[i * r + j] for j in range(r)) for i in range(s))
            if rank2(M, r) == r:
                matrices.append(M)
        for M in matrices:
            for _ in range(12):
                D = {w: rng.choice((-1, 1)) for w in product((0, 1), repeat=r + 2)}
                a = tuple(rng.randrange(2) for _ in range(s))
                b = tuple(rng.randrange(2) for _ in range(r))
                c = tuple(rng.randrange(2) for _ in range(2))
                P = make_P(M, D, a, b, c, rng.randrange(2))
                H = entropy(walsh_masses(P))
                infl = influence_vector(P)
                I = sum(infl, Fraction())
                fiber_H = 0.0
                fiber_I = Fraction()
                for u in product((0, 1), repeat=r):
                    f = {z: D[u + z] * (-1 if dot(c, z) else 1) for z in zs}
                    fiber_H += entropy(walsh_masses(f)) / (1 << r)
                    fiber_I += sum(influence_vector(f), Fraction()) / (1 << r)
                assert abs(H - (2 * r + fiber_H)) < 3e-11
                assert I >= r + fiber_I
                assert H <= 2 * float(I) + 3e-11
                counts["oriented_matrix_samples"] += 1


# Directly verify the q_1 tensor identities underlying FEI/GU' hardness for
# every Boolean seed through four bits (output-complement representatives).
for n in range(1, 5):
    xs = tuple(product((0, 1), repeat=n))
    total = 1 << len(xs)
    all_masks = 1 << (len(xs) - 1)
    if n <= 3:
        masks = range(all_masks)
    else:
        masks = sorted({0, all_masks - 1, *(rng.randrange(all_masks) for _ in range(2048))})
    for mask in masks:
        vals = [1] + [1 if (mask >> (i - 1)) & 1 else -1 for i in range(1, len(xs))]
        g = dict(zip(xs, vals))
        F = make_q_times_g(g)
        mg, mf = walsh_masses(g), walsh_masses(F)
        Hg, Hf = entropy(mg), entropy(mf)
        Ug, Uf = upper_U(mg), upper_U(mf)
        Ig = sum(influence_vector(g), Fraction())
        If = sum(influence_vector(F), Fraction())
        Gg, Gf = G_value(g), G_value(F)
        assert abs(Hf - (2 + Hg)) < 3e-11
        assert abs(Uf - (1 + Ug)) < 3e-11
        assert If == 1 + Ig
        assert abs(Gf - (2 + Gg)) < 5e-10
        counts["hardness_seed_identities"] += 4


print("PASS")
print(f"seed={SEED}")
for k, v in counts.items():
    print(f"{k}={v}")
print(f"max_H_over_I={max_H_over_I:.12f}")
