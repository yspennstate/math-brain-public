#!/usr/bin/env python3
"""Reconstruct the GU laws for same-variable parity-masked point defects."""

from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, log2

TOL = 3e-10


@lru_cache(maxsize=None)
def fwht(values):
    a = [Fraction(x) for x in values]
    h = 1
    while h < len(a):
        for start in range(0, len(a), 2 * h):
            for j in range(start, start + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return tuple(x / len(a) for x in a)


@lru_cache(maxsize=None)
def spectral_law(values):
    return tuple(x * x for x in fwht(values))


def upper_masses(p):
    z = list(p)
    n = len(p).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not (s & bit):
                z[s] += z[s | bit]
    return tuple(z)


@lru_cache(maxsize=None)
def u_value(values):
    p = spectral_law(values)
    pi = upper_masses(p)
    return sum(float(x) * log2(float(y / x))
               for x, y in zip(p, pi) if x)


@lru_cache(maxsize=None)
def influence(values):
    return sum(Fraction(s.bit_count()) * x
               for s, x in enumerate(spectral_law(values)))


@lru_cache(maxsize=None)
def restrict_one(values, i, bit):
    n = len(values).bit_length() - 1
    return tuple(values[(z & ((1 << i) - 1)) | (bit << i) |
                        ((z >> i) << (i + 1))]
                 for z in range(1 << (n - 1)))


@lru_cache(maxsize=None)
def g_value(values):
    n = len(values).bit_length() - 1
    return sum(u_value(values) - 0.5 * (
        u_value(restrict_one(values, i, 0)) +
        u_value(restrict_one(values, i, 1))) for i in range(n))


def masked_defect(n, mask, point=0, sign=1):
    return tuple(sign * (-1 if (x & mask).bit_count() % 2 else 1) *
                 (-1 if x == point else 1) for x in range(1 << n))


def formula_u(n, r):
    N = 1 << n
    tau = 2 / N
    q = tau * tau
    p = (1 - tau) ** 2
    pi_a = p + q * ((1 << (n - r)) - 1)
    out = 0.0 if p == 0 else p * log2(pi_a / p)
    for s in range(r):
        pi_s = p + q * ((1 << (n - s)) - 1)
        out += comb(r, s) * q * log2(pi_s / q)
    for s in range(n + 1):
        nonsubsets = comb(n, s) - (comb(r, s) if s <= r else 0)
        out += nonsubsets * q * (n - s)
    return out


def formula_i(n, r):
    N = 1 << n
    q = 4 / (N * N)
    p = (1 - 2 / N) ** 2
    return r * p + q * (n * (1 << (n - 1)) - r)


def formula_g(n, r):
    out = n * formula_u(n, r)
    if n > 1 and n - r:
        out -= 0.5 * (n - r) * formula_u(n - 1, r)
    if n > 1 and r:
        out -= 0.5 * r * formula_u(n - 1, r - 1)
    return out


def tensor(a, b):
    return tuple(x * y for y in b for x in a)


def main():
    cases = 0
    max_u_error = max_g_error = max_i_error = 0.0

    # Every mask through n=6, plus all mask sizes through n=8.  The defect
    # point and global sign are immaterial by cube translation/sign symmetry.
    for n in range(1, 7):
        for mask in range(1 << n):
            f = masked_defect(n, mask)
            r = mask.bit_count()
            eu = abs(u_value(f) - formula_u(n, r))
            eg = abs(g_value(f) - formula_g(n, r))
            ei = abs(float(influence(f)) - formula_i(n, r))
            max_u_error = max(max_u_error, eu)
            max_g_error = max(max_g_error, eg)
            max_i_error = max(max_i_error, ei)
            assert eu <= TOL and eg <= TOL and ei <= TOL
            cases += 1
    for n in (7, 8):
        for r in range(n + 1):
            mask = (1 << r) - 1
            for point, sign in ((0, 1), ((1 << n) - 1, -1)):
                f = masked_defect(n, mask, point, sign)
                assert abs(u_value(f) - formula_u(n, r)) <= TOL
                assert abs(g_value(f) - formula_g(n, r)) <= TOL
                assert abs(float(influence(f)) - formula_i(n, r)) <= TOL
                cases += 1

    # Exact class inequality through a broad scalar range.  The proof for all
    # n is analytic; this is only a reconstruction/control.
    max_ratio = (-1.0, None)
    for n in range(1, 101):
        for r in range(n + 1):
            ii = formula_i(n, r)
            gg = formula_g(n, r)
            if ii:
                ratio = gg / ii
                if ratio > max_ratio[0]:
                    max_ratio = (ratio, (n, r))
                assert gg <= 16 * ii + TOL

    # Tensor reconstruction for generated restriction-closed class.
    tensor_specs = [((3, 0), (4, 2)),
                    ((2, 2), (3, 1), (4, 4)),
                    ((1, 0), (3, 3), (5, 2))]
    tensor_cases = 0
    for specs in tensor_specs:
        factors = [masked_defect(n, (1 << r) - 1) for n, r in specs]
        F = factors[0]
        for f in factors[1:]:
            F = tensor(F, f)
        sum_u = sum(u_value(f) for f in factors)
        sum_g = sum(g_value(f) for f in factors)
        sum_i = sum(influence(f) for f in factors)
        assert abs(u_value(F) - sum_u) <= TOL
        assert abs(g_value(F) - sum_g) <= TOL
        assert influence(F) == sum_i
        assert g_value(F) <= 16 * float(influence(F)) + TOL
        tensor_cases += 1

    # Previously designated non-affine shared-coordinate collision control.
    positive_g = (-1, -1, -1, -1, -1, 1, 1, 1)
    positive_h = (-1, 1, 1, -1, -1, 1, 1, -1)
    positive_f = tuple(x * y for x, y in zip(positive_g, positive_h))
    positive_ratio = g_value(positive_f) / float(influence(positive_f))
    assert positive_ratio < 16

    sharp = 0.25 + 2.25 * log2(16 / 9)
    assert abs(max_ratio[0] - sharp) <= TOL
    assert max_ratio[1] == (3, 0)

    print("STATUS PASS")
    print(f"direct_masked_defect_cases={cases}")
    print(f"tensor_cases={tensor_cases}")
    print(f"maximum_U_formula_error={max_u_error:.17g}")
    print(f"maximum_G_formula_error={max_g_error:.17g}")
    print(f"maximum_I_formula_error={max_i_error:.17g}")
    print(f"scalar_dimensions_checked=100")
    print(f"maximum_G_over_I={max_ratio[0]:.17g}")
    print(f"maximum_location_n_r={max_ratio[1][0]},{max_ratio[1][1]}")
    print(f"positive_collision_G_over_I={positive_ratio:.17g}")
    print("masked_point_defect_pair=a:16,b:0")
    print("universal_GU=OPEN")


if __name__ == "__main__":
    main()
