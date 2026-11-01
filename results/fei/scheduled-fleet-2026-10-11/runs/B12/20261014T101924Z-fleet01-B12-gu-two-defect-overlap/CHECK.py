#!/usr/bin/env python3
"""Verify the exact two-defect overlap kernel and GU class bounds."""

from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import log2

TOL = 8e-10


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


def character(n, mask, sign=1):
    return tuple(sign * (-1 if (x & mask).bit_count() % 2 else 1)
                 for x in range(1 << n))


def masked_defect(n, mask, point, sign=1):
    return tuple(sign * (-1 if (x & mask).bit_count() % 2 else 1) *
                 (-1 if x == point else 1) for x in range(1 << n))


def masked_two_defect(n, mask, z0, z1, sign=1):
    assert z0 != z1
    return tuple(sign * (-1 if (x & mask).bit_count() % 2 else 1) *
                 (-1 if x == z0 or x == z1 else 1)
                 for x in range(1 << n))


def delete_bit(x, i):
    return (x & ((1 << i) - 1)) | ((x >> (i + 1)) << i)


def expected_laws(n, mask, z0, z1):
    N = 1 << n
    D = z0 ^ z1
    p = Fraction((N - 4) ** 2, N * N)
    q = Fraction(16, N * N)
    law = []
    pi = []
    for T in range(N):
        if T == mask:
            law.append(p)
        elif ((T ^ mask) & D).bit_count() % 2 == 0:
            law.append(q)
        else:
            law.append(Fraction(0))
    for S in range(N):
        free_d = D & ~S
        if free_d:
            count = 1 << (n - S.bit_count() - 1)
        else:
            parity_ok = (D.bit_count() - (mask & D).bit_count()) % 2 == 0
            count = (1 << (n - S.bit_count())) if parity_ok else 0
        heavy = p - q if (S | mask) == mask else 0
        pi.append(q * count + heavy)
    return tuple(law), tuple(pi)


def predicted_g_from_children(n, mask, z0, z1):
    root = u_value(masked_two_defect(n, mask, z0, z1))
    D = z0 ^ z1
    out = n * root
    for i in range(n):
        m = delete_bit(mask, i)
        a, b = (z0 >> i) & 1, (z1 >> i) & 1
        if a != b:
            # Both physical children contain one defect.
            c0 = masked_defect(n - 1, m, delete_bit(z0 if a == 0 else z1, i))
            c1 = masked_defect(n - 1, m, delete_bit(z0 if a == 1 else z1, i))
            out -= 0.5 * (u_value(c0) + u_value(c1))
        else:
            # One child contains both defects; the other is a character.
            active = masked_two_defect(n - 1, m, delete_bit(z0, i),
                                       delete_bit(z1, i))
            terminal = character(n - 1, m)
            assert u_value(terminal) == 0.0
            out -= 0.5 * u_value(active)
    return out


def point_u(n):
    N = 1 << n
    p = (1 - 2 / N) ** 2
    return ((0.0 if p == 0 else p * log2(1 / p)) +
            4 / (N * N) * (n * (N / 2) - n))


def two_u(n, d):
    N = 1 << n
    p = (1 - 4 / N) ** 2
    q = 16 / (N * N)
    if d == 1:
        L = (n - 1) * (N / 4 - 1)
    else:
        L = ((n - 2) * N / 4 - (n - 1) +
             ((1 << (n - d)) if d % 2 == 0 else 0))
    return (0.0 if p == 0 else p * log2(1 / p)) + q * L


def two_i(n, d):
    return 4 * (n - 1) / (1 << n) if d == 1 else 4 * n / (1 << n)


def two_g(n, d):
    ans = n * two_u(n, d) - d * point_u(n - 1)
    if n > d:
        ans -= 0.5 * (n - d) * two_u(n - 1, d)
    return ans


def tensor(a, b):
    return tuple(x * y for y in b for x in a)


def main():
    direct_cases = kernel_cases = recurrence_cases = 0
    max_kernel_error = max_recurrence_error = 0.0
    masked_max = (-1e100, None)

    # Exhaust every mask and unordered point pair through n=5.
    for n in range(2, 6):
        N = 1 << n
        for mask in range(N):
            for z0, z1 in combinations(range(N), 2):
                f = masked_two_defect(n, mask, z0, z1)
                ep, epi = expected_laws(n, mask, z0, z1)
                actual_p = spectral_law(f)
                actual_pi = upper_masses(actual_p)
                assert actual_p == ep and actual_pi == epi
                kernel_cases += 1

                pg = predicted_g_from_children(n, mask, z0, z1)
                err = abs(g_value(f) - pg)
                max_recurrence_error = max(max_recurrence_error, err)
                assert err <= TOL
                recurrence_cases += 1

                ii = float(influence(f))
                if ii:
                    ratio = g_value(f) / ii
                    if ratio > masked_max[0]:
                        masked_max = (ratio, (n, mask.bit_count(),
                                              (z0 ^ z1).bit_count()))
                    assert g_value(f) <= 32 * ii + TOL
                direct_cases += 1

    # Representative higher-dimensional exact reconstructions.
    for n in range(6, 10):
        for d in range(1, n + 1):
            D = (1 << d) - 1
            for r in range(n + 1):
                masks = {(1 << r) - 1, ((1 << r) - 1) << (n - r)}
                for mask in masks:
                    f = masked_two_defect(n, mask, 0, D)
                    ep, epi = expected_laws(n, mask, 0, D)
                    assert spectral_law(f) == ep
                    assert upper_masses(ep) == epi
                    assert abs(g_value(f) - predicted_g_from_children(
                        n, mask, 0, D)) <= TOL
                    assert g_value(f) <= 32 * float(influence(f)) + TOL
                    direct_cases += 1

    # Closed-form unmasked family and sharp imported point-defect constant.
    kappa = 0.25 + 2.25 * log2(16 / 9)
    unmasked_max = (-1e100, None)
    for n in range(2, 51):
        for d in range(1, n + 1):
            ratio = two_g(n, d) / two_i(n, d)
            if ratio > unmasked_max[0]:
                unmasked_max = (ratio, (n, d))
            assert ratio <= kappa + TOL
            if n <= 9:
                f = masked_two_defect(n, 0, 0, (1 << d) - 1)
                assert abs(u_value(f) - two_u(n, d)) <= TOL
                assert abs(g_value(f) - two_g(n, d)) <= TOL
                assert abs(float(influence(f)) - two_i(n, d)) <= TOL
    assert abs(unmasked_max[0] - kappa) <= TOL
    assert unmasked_max[1] == (4, 1)

    # Analytic entropy envelope used for every nonempty mask.
    for n in range(3, 101):
        rho = 4 / (1 << n)
        p = (1 - rho) ** 2
        q = rho * rho
        H = -p * log2(p) - ((1 << (n - 1)) - 1) * q * log2(q)
        assert n * H <= 32 * p + TOL

    # Exact tensor closure controls.
    factors = [masked_two_defect(3, 1, 0, 3),
               masked_two_defect(4, 5, 0, 7),
               masked_two_defect(2, 0, 0, 1)]
    F = factors[0]
    for f in factors[1:]:
        F = tensor(F, f)
    assert abs(u_value(F) - sum(u_value(f) for f in factors)) <= TOL
    assert abs(g_value(F) - sum(g_value(f) for f in factors)) <= TOL
    assert influence(F) == sum(influence(f) for f in factors)
    assert g_value(F) <= 32 * float(influence(F)) + TOL

    print("STATUS PASS")
    print(f"direct_two_defect_cases={direct_cases}")
    print(f"exhaustive_kernel_cases={kernel_cases}")
    print(f"physical_recurrence_cases={recurrence_cases}")
    print(f"maximum_recurrence_error={max_recurrence_error:.17g}")
    print(f"unmasked_max_G_over_I={unmasked_max[0]:.17g}")
    print(f"unmasked_max_location_n_d={unmasked_max[1][0]},{unmasked_max[1][1]}")
    print(f"exhaustive_masked_max_G_over_I={masked_max[0]:.17g}")
    print("masked_two_defect_pair=a:32,b:0")
    print("universal_GU=OPEN")


if __name__ == "__main__":
    main()
