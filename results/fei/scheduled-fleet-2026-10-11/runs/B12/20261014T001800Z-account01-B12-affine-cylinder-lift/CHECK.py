#!/usr/bin/env python3
"""Deterministic controls for the affine-cylinder lifting theorem.

All Walsh transforms are computed from integer truth tables.  Floating point
is used only to evaluate logarithms after the exact dyadic spectra are known.
"""

from __future__ import annotations

import math
import random


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def raw_entropy_from_values(vals):
    n = int(math.log2(len(vals)))
    nums = fwht(vals)
    den = 1 << n
    ans = 0.0
    for z in nums:
        if z:
            u = (z / den) ** 2
            ans += u * math.log2(1.0 / u)
    return ans


def entropy_probability(weights):
    ans = 0.0
    for u in weights:
        if u > 0:
            ans += u * math.log2(1.0 / u)
    return ans


def influence(vals):
    n = int(math.log2(len(vals)))
    ans = 0.0
    for i in range(n):
        bit = 1 << i
        ans += sum((vals[x] - vals[x ^ bit]) ** 2 for x in range(len(vals))) / (4 * len(vals))
    return ans


def coordinate_influences(vals):
    n = int(math.log2(len(vals)))
    out = []
    for i in range(n):
        bit = 1 << i
        out.append(sum((vals[x] - vals[x ^ bit]) ** 2 for x in range(len(vals))) / (4 * len(vals)))
    return out


def linear_subspaces(m):
    """All subspaces of F_2^m; m<=4 in this checker."""
    universe = range(1 << m)
    out = []
    for mask in range(1 << (1 << m)):
        if not (mask & 1):
            continue
        size = mask.bit_count()
        if size & (size - 1):
            continue
        elems = [x for x in universe if (mask >> x) & 1]
        s = set(elems)
        if all((x ^ y) in s for x in elems for y in elems):
            out.append(tuple(elems))
    return out


def basis_of(V):
    basis = []
    pivots = []
    for x0 in V:
        x = x0
        for b, p in zip(basis, pivots):
            if (x >> p) & 1:
                x ^= b
        if x:
            p = x.bit_length() - 1
            for j in range(len(basis)):
                if (basis[j] >> p) & 1:
                    basis[j] ^= x
            basis.append(x)
            pivots.append(p)
    return basis


def point_from_label(label, basis):
    y = 0
    for j, b in enumerate(basis):
        if (label >> j) & 1:
            y ^= b
    return y


def signing_masks(size, seed):
    if size <= 8:
        return range(1 << size)
    rng = random.Random(seed)
    fixed = [0, (1 << size) - 1]
    fixed += [sum(1 << j for j in range(size) if (j >> k) & 1) for k in range(min(4, size.bit_length()))]
    sample = fixed + [rng.getrandbits(size) for _ in range(256)]
    return sorted(set(sample))


def check_case(t, m, V, sign_mask):
    basis = basis_of(V)
    d = len(basis)
    r = m - d
    p = 2.0 ** (-r)
    outer_points = [point_from_label(z, basis) for z in range(1 << d)]
    support_size = (1 << t) * (1 << d)
    signs = [1 if (sign_mask >> j) & 1 else -1 for j in range(support_size)]

    # b on t internal coordinates and m transverse coordinates.
    vals = [0] * (1 << (t + m))
    fibers = []
    for zi, y in enumerate(outer_points):
        fiber = []
        for x in range(1 << t):
            s = signs[zi * (1 << t) + x]
            fiber.append(s)
            vals[x | (y << t)] = s
        fibers.append(fiber)

    E_b = raw_entropy_from_values(vals)
    I_b = influence(vals)
    coord_I = coordinate_influences(vals)
    avg_I = sum(influence(g) for g in fibers) / len(fibers)
    avg_H = sum(raw_entropy_from_values(g) for g in fibers) / len(fibers)
    I_internal = sum(coord_I[:t])
    I_outer = sum(coord_I[t:])

    assert abs(I_internal - p * avg_I) < 1e-11
    assert abs(I_outer - m * p / 2) < 1e-11
    assert abs(I_b - I_internal - I_outer) < 1e-11

    # Joint quotient-spectrum law Q(S,lambda).
    q = []
    for S in range(1 << t):
        c = []
        for g in fibers:
            c.append(fwht(g)[S] / (1 << t))
        c_hat = fwht(c)
        c_den = 1 << d
        q.extend((z / c_den) ** 2 for z in c_hat)
    assert abs(sum(q) - 1.0) < 1e-11
    H_Q = entropy_probability(q)
    assert abs(E_b - (2 * r * p + p * H_Q)) < 2e-10
    assert H_Q <= avg_H + 2 * d + 2e-10

    fiber_ratios = []
    for g in fibers:
        ig = influence(g)
        hg = raw_entropy_from_values(g)
        if ig > 1e-14:
            fiber_ratios.append(hg / ig)
        else:
            assert abs(hg) < 1e-12
    C = max(fiber_ratios, default=0.0)
    rhs_split = C * I_internal + 4 * I_outer
    rhs_uniform = max(C, 4.0) * I_b
    assert E_b <= rhs_split + 2e-10
    assert E_b <= rhs_uniform + 2e-10
    return E_b, I_b, C, H_Q, avg_H, rhs_split


def main():
    cases = 0
    exhaustive = 0
    sampled = 0
    mixed_cylinders = 0
    max_ratio = 0.0
    max_joint_excess = -1e100
    for m in range(1, 5):
        for V in linear_subspaces(m):
            if any((1 << j) in V for j in range(m)):
                continue
            d = int(math.log2(len(V)))
            for t in range(0, 3):
                size = 1 << (t + d)
                if size > 16:
                    continue
                masks = signing_masks(size, seed=1000 * m + 100 * d + 10 * t + sum(V))
                is_exhaustive = size <= 8
                for mask in masks:
                    E_b, I_b, C, H_Q, avg_H, rhs_split = check_case(t, m, V, mask)
                    cases += 1
                    exhaustive += int(is_exhaustive)
                    sampled += int(not is_exhaustive)
                    mixed_cylinders += int(t > 0 and d > 0)
                    if I_b:
                        max_ratio = max(max_ratio, E_b / I_b)
                    max_joint_excess = max(max_joint_excess, H_Q - avg_H - 2 * d)

    # Exact sharpness control: one-point support in every tested dimension.
    sharp = []
    for n in range(1, 13):
        vals = [1] + [0] * ((1 << n) - 1)
        sharp.append(raw_entropy_from_values(vals) / influence(vals))
    assert all(abs(x - 4.0) < 2e-11 for x in sharp)

    print(f"verified_affine_cylinder_signings={cases}")
    print(f"exhaustive_signings={exhaustive}")
    print(f"deterministic_sampled_signings={sampled}")
    print(f"mixed_internal_oblique_cases={mixed_cylinders}")
    print(f"largest_observed_E_over_I={max_ratio:.15g}")
    print(f"largest_joint_entropy_slack={max_joint_excess:.15g}")
    print("point_support_constant_dimensions=1..12")
    print("sharp_uniform_constant=4")
    print("full_FEI=OPEN")
    print("PASS")


if __name__ == "__main__":
    main()
