#!/usr/bin/env python3
"""Deterministic checks for B12/A058 one-bit splice and affine-defect formulas."""

from itertools import combinations
from math import log2


def parity(x: int) -> int:
    return x.bit_count() & 1


def fwht(vals):
    out = list(vals)
    h = 1
    while h < len(out):
        for i in range(0, len(out), 2 * h):
            for j in range(i, i + h):
                a, b = out[j], out[j + h]
                out[j], out[j + h] = a + b, a - b
        h *= 2
    return out


def entropy_from_walsh(w):
    den2 = len(w) ** 2
    ans = 0.0
    for z in w:
        if z:
            q = z * z / den2
            ans += q * log2(1.0 / q)
    return ans


def influence_from_walsh(w):
    den2 = len(w) ** 2
    return sum(s.bit_count() * z * z for s, z in enumerate(w)) / den2


def rank_f2(rows):
    rows = list(rows)
    rank = 0
    while rows:
        pivot = max(rows)
        if pivot == 0:
            break
        rank += 1
        bit = 1 << (pivot.bit_length() - 1)
        rows = [x ^ pivot if x & bit else x for x in rows if x != pivot]
    return rank


def rowspace(rows):
    ans = {0}
    for r in rows:
        ans |= {x ^ r for x in tuple(ans)}
    return ans


pair_checks = 0
max_entropy_identity_error = 0.0
max_influence_identity_error = 0.0
min_boundary_credit_slack = float("inf")
min_boundary_domination_slack = float("inf")

for n in range(1, 4):
    N = 1 << n
    functions = []
    for table in range(1 << N):
        vals = [1 if (table >> x) & 1 else -1 for x in range(N)]
        functions.append((vals, fwht(vals)))
    for g, wg in functions:
        for h, wh in functions:
            d_num = sum(a != b for a, b in zip(g, h))
            d = d_num / N
            u = [(a + b) // 2 for a, b in zip(g, h)]
            v = [(a - b) // 2 for a, b in zip(g, h)]
            wu, wv = fwht(u), fwht(v)

            # F has u in the selector-free sector and v in the selector sector.
            # Selector bit is the high bit: branch values are u+v and u-v.
            F = [a + b for a, b in zip(u, v)] + [a - b for a, b in zip(u, v)]
            wF = fwht(F)
            expected = [2 * z for z in wu] + [2 * z for z in wv]
            assert wF == expected

            HF = entropy_from_walsh(wF)
            IF = influence_from_walsh(wF)
            Hu_sector = sum(
                (z * z / (N * N)) * log2(1.0 / (z * z / (N * N)))
                for z in wu if z
            )
            Hv_sector = sum(
                (z * z / (N * N)) * log2(1.0 / (z * z / (N * N)))
                for z in wv if z
            )
            Iu = sum(s.bit_count() * z * z for s, z in enumerate(wu)) / (N * N)
            Iv = sum(s.bit_count() * z * z for s, z in enumerate(wv)) / (N * N)
            max_entropy_identity_error = max(max_entropy_identity_error, abs(HF - Hu_sector - Hv_sector))
            max_influence_identity_error = max(max_influence_identity_error, abs(IF - (d + Iu + Iv)))

            if 0 < d <= 0.5:
                h2 = -d * log2(d) - (1 - d) * log2(1 - d)
                A = [a != b for a, b in zip(g, h)]
                J = 0.0
                for i in range(n):
                    J += sum(A[x] != A[x ^ (1 << i)] for x in range(N)) / N
                min_boundary_credit_slack = min(min_boundary_credit_slack, J - h2)
                min_boundary_domination_slack = min(
                    min_boundary_domination_slack, 2 * (Iu + Iv) - J
                )
                assert h2 <= J + 1e-12
                assert J <= 2 * (Iu + Iv) + 1e-12
            pair_checks += 1


affine_checks = 0
max_affine_entropy_error = 0.0
max_affine_influence_error = 0.0
min_four_slack = float("inf")

cases = []
for n in range(1, 6):
    masks = range(1, 1 << n)
    for r in (1, 2):
        if r > n:
            continue
        for rows in combinations(masks, r):
            if rank_f2(rows) == r:
                cases.append((n, rows))

# Add deterministic overlapping three-constraint systems, including n=6.
for n in (3, 4, 5, 6):
    taken = 0
    for rows in combinations(range(1, 1 << n), 3):
        if rank_f2(rows) == 3:
            cases.append((n, rows))
            taken += 1
            if taken == 80:
                break

for n, rows in cases:
    r = len(rows)
    V = rowspace(rows)
    support = 0
    for z in V:
        support |= z
    s = support.bit_count()
    p = 2.0 ** (-r)
    group = V | {z | (1 << n) for z in V}
    m = n + 1
    M = 1 << m
    for rhs in range(1 << r):
        vals = []
        for point in range(M):
            z = point & ((1 << n) - 1)
            selector = (point >> n) & 1
            in_A = all(parity(row & z) == ((rhs >> j) & 1) for j, row in enumerate(rows))
            vals.append(-1 if selector and in_A else 1)
        w = fwht(vals)
        assert w[0] == int(M * (1 - p))
        target_abs = int(M * p)
        for freq, coeff in enumerate(w):
            if freq == 0:
                continue
            if freq in group:
                assert abs(coeff) == target_abs
            else:
                assert coeff == 0

        H = entropy_from_walsh(w)
        I = influence_from_walsh(w)
        H_formula = (1 - p) ** 2 * log2(1 / (1 - p) ** 2) + (2 * p - p * p) * 2 * r
        I_formula = p * (s + 1)
        max_affine_entropy_error = max(max_affine_entropy_error, abs(H - H_formula))
        max_affine_influence_error = max(max_affine_influence_error, abs(I - I_formula))
        min_four_slack = min(min_four_slack, 4 * I - H)
        assert abs(H - H_formula) < 1e-12
        assert abs(I - I_formula) < 1e-12
        assert H <= 4 * I + 1e-12
        affine_checks += 1

print(f"ordered Boolean splice pairs checked: {pair_checks}")
print(f"max splice entropy identity error: {max_entropy_identity_error:.3e}")
print(f"max splice influence identity error: {max_influence_identity_error:.3e}")
print(f"minimum boundary-credit slack J-h2(d): {min_boundary_credit_slack:.15g}")
print(f"minimum domination slack 2(Iu+Iv)-J: {min_boundary_domination_slack:.15g}")
print(f"affine-defect instances checked: {affine_checks}")
print(f"max affine entropy formula error: {max_affine_entropy_error:.3e}")
print(f"max affine influence formula error: {max_affine_influence_error:.3e}")
print(f"minimum slack 4I-H: {min_four_slack:.15g}")
print("ALL_CHECKS_PASS")
