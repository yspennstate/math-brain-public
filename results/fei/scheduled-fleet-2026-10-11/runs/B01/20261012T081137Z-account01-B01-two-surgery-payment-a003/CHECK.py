#!/usr/bin/env python3
"""Checks for the two-surgery shared-selector payment.

The all-parameter theorem is analytic.  This script independently checks
the exact shared-selector identity against direct truth tables in small
dimensions and tests the scalar decomposition/bounds on larger bent cores.
"""

from itertools import combinations
from math import log2, log


LN2 = log(2.0)
TOL = 3e-10


def fwht(vals):
    a = list(map(float, vals))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                u, v = a[j], a[j + h]
                a[j], a[j + h] = u + v, u - v
        h *= 2
    n = len(a)
    return [x / n for x in a]


def upper(vals):
    a = list(vals)
    n = (len(a)).bit_length() - 1
    for bit in range(n):
        step = 1 << bit
        for s in range(len(a)):
            if not s & step:
                a[s] += a[s | step]
    return a


def U_from_coeffs(coeff):
    q = [x * x for x in coeff]
    cap = upper(q)
    return sum(x * log2(y / x) for x, y in zip(q, cap) if x > 0.0)


def U(truth):
    return U_from_coeffs(fwht(truth))


def bent_truth(k):
    ans = []
    for x in range(1 << k):
        q = 0
        for j in range(0, k, 2):
            q ^= ((x >> j) & 1) & ((x >> (j + 1)) & 1)
        ans.append(-1 if q else 1)
    return ans


def flip2(g, x, y):
    h = list(g)
    h[x] *= -1
    h[y] *= -1
    return h


def switch_truth(g, h, d):
    out = []
    cmask = (1 << d) - 1
    for w in range(len(g) << d):
        out.append(h[w >> d] if (w & cmask) == 0 else g[w >> d])
    return out


def udiff(dvec):
    q = [x * x for x in dvec]
    cap = upper(q)
    return sum(x * log2(y / x) for x, y in zip(q, cap) if x > 0.0)


def shared_identity(g, h, dsel):
    p = 2.0 ** (-dsel)
    a, b = fwht(g), fwht(h)
    dv = [y - x for x, y in zip(a, b)]
    c = [(1 - p) * x + p * y for x, y in zip(a, b)]
    A = upper([x * x for x in a])
    B = upper([x * x for x in b])
    first = 0.0
    for ct, at, bt in zip(c, A, B):
        q = ct * ct
        if q > 0.0:
            first += q * log2(((1 - p) * at + p * bt) / q)
    second = p * (1 - p) * udiff(dv)
    third = (p * dsel / 2 - p * p * dsel) * sum(x * x for x in dv)
    return first + second + third


def decomposition(g, h, dsel):
    k = (len(g)).bit_length() - 1
    delta = 2.0 ** (-k)
    alpha = delta ** 0.5
    p = 2.0 ** (-dsel)
    a, b = fwht(g), fwht(h)
    dv = [y - x for x, y in zip(a, b)]
    c = [(1 - p) * x + p * y for x, y in zip(a, b)]
    A = upper([x * x for x in a])
    B = upper([x * x for x in b])
    D = upper([x * x for x in dv])
    scalar = 0.0
    corr_L = 0.0
    assertions = 0
    max_box = 0.0
    max_phi_ratio = 0.0
    for t, (at, bt, ct, cap_a, cap_b, cap_d, dt) in enumerate(zip(a, b, c, A, B, D, dv)):
        u = cap_b / cap_a - 1
        v = bt * bt / delta - 1
        w = ct * ct / delta - 1
        assert abs(u) <= 9 * alpha + 1e-12
        assert abs(v) <= 9 * alpha + 1e-12
        assert abs(w) <= 8.5 * p * alpha + 1e-12
        max_box = max(max_box, abs(u) / alpha, abs(v) / alpha,
                      abs(w) / (p * alpha))
        phi = ((1 + w) * log((1 + p * u) / (1 + w))
               - p * (1 + v) * log((1 + u) / (1 + v)))
        assert phi <= 780 * p * delta + 1e-12
        max_phi_ratio = max(max_phi_ratio, phi / (p * delta))
        scalar += delta * phi / LN2
        L = k - t.bit_count()
        corr_L += dt * dt * L
        assertions += 4
    diff_correction = p * (1 - p) * (udiff(dv) - corr_L)
    assert diff_correction <= 1e-11
    disagreement = sum(x != y for x, y in zip(g, h)) / len(g)
    ictl = 2 * p * dsel * disagreement
    rhs = scalar + diff_correction + (1 - 2 * p) * ictl
    J = shared_identity(g, h, dsel) - (1 - p) * U(g) - p * U(h)
    assert abs(J - rhs) < TOL
    assert J <= 283 * ictl + 1e-10
    assertions += 3
    return assertions, J / ictl, max_box, max_phi_ratio


def main():
    assertions = direct_cases = theorem_cases = 0
    max_direct_error = 0.0
    max_ratio = 0.0
    max_box = 0.0
    max_phi_ratio = 0.0

    # Direct truth-table reconstruction, independent of the selector formula.
    for k in (2, 4, 6):
        g = bent_truth(k)
        pairs = list(combinations(range(1 << k), 2))
        if k == 6:
            pairs = pairs[::7]
        for x, y in pairs:
            h = flip2(g, x, y)
            for dsel in (1, 2, 3):
                direct = U(switch_truth(g, h, dsel))
                formula = shared_identity(g, h, dsel)
                err = abs(direct - formula)
                assert err < TOL
                max_direct_error = max(max_direct_error, err)
                assertions += 1
                direct_cases += 1

    # All phase/distance types are sampled in the theorem range.
    for k in (8, 10, 12):
        g = bent_truth(k)
        n = 1 << k
        masks = [1, 2, 3, 5, 7, 15, 31, (1 << (k // 2)) - 1, n - 1]
        xs = [0, 1, 3, n // 5, n // 3, n // 2, n - 1]
        for x in xs:
            for mask in masks:
                y = x ^ (mask & (n - 1))
                if y == x:
                    continue
                h = flip2(g, x, y)
                for dsel in (1, 2, 4, 8):
                    a, ratio, box, phir = decomposition(g, h, dsel)
                    assertions += a
                    theorem_cases += 1
                    max_ratio = max(max_ratio, ratio)
                    max_box = max(max_box, box)
                    max_phi_ratio = max(max_phi_ratio, phir)

    print(f"direct_truth_cases={direct_cases}")
    print(f"theorem_cases={theorem_cases}")
    print(f"assertions={assertions}")
    print(f"max_direct_identity_error={max_direct_error:.4e}")
    print(f"max_observed_J_over_Ictl={max_ratio:.12f}")
    print(f"max_normalized_box_coordinate={max_box:.12f}")
    print(f"max_observed_Phi_over_pdelta={max_phi_ratio:.12f}")
    print("status=PASS")


if __name__ == "__main__":
    main()
