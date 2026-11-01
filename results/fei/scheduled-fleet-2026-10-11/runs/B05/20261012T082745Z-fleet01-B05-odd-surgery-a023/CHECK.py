#!/usr/bin/env python3
"""Deterministic checks for the odd point-surgery retained-child payment.

This is corroboration, not the analytic proof.  It verifies the exact shared-
selector identity against direct Walsh transforms in small dimensions and
checks the inequalities used in the general odd-m and special m=3 bounds.
"""

from __future__ import annotations

import math


def fwht(a):
    a = [float(x) for x in a]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    n = len(a)
    return [x / n for x in a]


def upper_caps(q, n):
    z = list(q)
    for bit in range(n):
        for mask in range(1 << n):
            if not (mask >> bit) & 1:
                z[mask] += z[mask | (1 << bit)]
    return z


def upper_u_from_spectrum(a, n):
    q = [x * x for x in a]
    cap = upper_caps(q, n)
    return sum(x * math.log2(y / x) for x, y in zip(q, cap) if x > 0)


def bent_truth(k):
    assert k % 2 == 0
    r = k // 2
    out = []
    for x in range(1 << k):
        dot = 0
        for j in range(r):
            dot ^= ((x >> j) & 1) & ((x >> (r + j)) & 1)
        out.append(-1.0 if dot else 1.0)
    return out


def surgery(g, points):
    h = list(g)
    for x in points:
        h[x] *= -1.0
    return h


def popcount(x):
    return x.bit_count()


def shared_identity(k, d, points, do_direct=True):
    g = bent_truth(k)
    h = surgery(g, points)
    a, b = fwht(g), fwht(h)
    p = 2.0 ** (-d)
    c = [(1 - p) * x + p * y for x, y in zip(a, b)]
    e = [y - x for x, y in zip(a, b)]
    A = upper_caps([x * x for x in a], k)
    B = upper_caps([x * x for x in b], k)
    D = upper_caps([x * x for x in e], k)

    base = 0.0
    for ct, At, Bt in zip(c, A, B):
        if ct:
            base += ct * ct * math.log2(((1 - p) * At + p * Bt) / (ct * ct))
    udiff = sum(x * x * math.log2(y / (x * x)) for x, y in zip(e, D) if x)
    norm_e = sum(x * x for x in e)
    identity_u = base + p * (1 - p) * udiff + (p * d / 2 - p * p * d) * norm_e

    # Direct truth table check (selector is active only on the all-one address).
    if do_direct:
        truth = []
        active = (1 << d) - 1
        for z in range(1 << d):
            truth.extend(h if z == active else g)
        direct_u = upper_u_from_spectrum(fwht(truth), k + d)
        identity_error = abs(identity_u - direct_u)
    else:
        identity_error = float("nan")

    Ug = upper_u_from_spectrum(a, k)
    Uh = upper_u_from_spectrum(b, k)
    J = identity_u - (1 - p) * Ug - p * Uh
    delta = 2.0 ** (-k)
    ictl = 2 * p * d * len(points) * delta

    # Exact Phi + K decomposition.
    scalar = 0.0
    for at, bt, ct, At, Bt in zip(a, b, c, A, B):
        u = Bt / At - 1
        v = bt * bt / delta - 1
        w = ct * ct / delta - 1
        phi = (1 + w) * math.log((1 + p * u) / (1 + w))
        phi -= p * (1 + v) * math.log((1 + u) / (1 + v))
        scalar += delta * phi / math.log(2)
    K = udiff - sum(x * x * (k - popcount(t)) for t, x in enumerate(e))
    decomposed = scalar + p * (1 - p) * K + (1 - 2 * p) * ictl

    return {
        "identity_error": identity_error,
        "decomposition_error": abs(J - decomposed),
        "J": J,
        "Ictl": ictl,
        "ratio": J / ictl,
        "K": K,
        "norm_e": norm_e,
        "max_abs_e": max(abs(x) for x in e),
        "min_abs_e": min(abs(x) for x in e),
    }


def analytic_case(k, d, points, special_triple=False):
    m = len(points)
    assert m % 2 == 1
    g = bent_truth(k)
    h = surgery(g, points)
    a, b = fwht(g), fwht(h)
    p = 2.0 ** (-d)
    delta = 2.0 ** (-k)
    alpha = math.sqrt(delta)
    c = [(1 - p) * x + p * y for x, y in zip(a, b)]
    e = [y - x for x, y in zip(a, b)]
    A = upper_caps([x * x for x in a], k)
    B = upper_caps([x * x for x in b], k)
    D = upper_caps([x * x for x in e], k)

    us = [Bt / At - 1 for At, Bt in zip(A, B)]
    vs = [x * x / delta - 1 for x in b]
    ws = [x * x / delta - 1 for x in c]
    udiff = sum(x * x * math.log2(y / (x * x)) for x, y in zip(e, D))
    K = udiff - sum(x * x * (k - popcount(t)) for t, x in enumerate(e))

    # Odd parity: the signed sum defining every e_T is a nonzero odd integer.
    assert min(abs(x) for x in e) >= 2 * delta - 1e-14
    assert max(abs(x) for x in e) <= 2 * m * delta + 1e-14
    assert abs(sum(x * x for x in e) - 4 * m * delta) < 1e-11
    assert K <= 8 * m * delta * math.log2(m) + 1e-11

    if special_triple:
        assert m == 3 and k >= 10
        assert max(abs(x) for x in us) <= 14 * alpha + 1e-12
        assert max(abs(x) for x in vs) <= 14 * alpha + 1e-12
        assert max(abs(x) for x in ws) <= 13 * p * alpha + 1e-12
        C = 1 + 1327 / (6 * math.log(2)) + 4 * math.log2(3)
    else:
        assert m * alpha <= 1 / 32 + 1e-15
        assert max(abs(x) for x in us) <= 5 * m * alpha + 1e-12
        assert max(abs(x) for x in vs) <= 5 * m * alpha + 1e-12
        assert max(abs(x) for x in ws) <= 5 * p * m * alpha + 1e-12
        C = 1 + 99 * m / (2 * math.log(2)) + 4 * math.log2(m)
    return C, K, max(abs(x) for x in us), max(abs(x) for x in vs), max(abs(x) for x in ws)


def main():
    direct = []
    for k, d, pts in [
        (4, 1, [0, 1, 3]),
        (4, 2, [0, 5, 15]),
        (6, 1, [0, 21, 63]),
        (6, 3, [2, 17, 55]),
    ]:
        r = shared_identity(k, d, pts)
        assert r["identity_error"] < 2e-12
        assert r["decomposition_error"] < 2e-12
        direct.append((k, d, pts, r))

    triple = []
    for k in (10, 12, 14):
        N = 1 << k
        point_sets = ([0, 1, 3], [0, N // 3, N - 1], [2, N // 5, 4 * N // 5 + 1])
        for d in (1, 2, 4, 8):
            for pts in point_sets:
                C, K, mu, mv, mw = analytic_case(k, d, list(pts), special_triple=True)
                r = shared_identity(k, d, list(pts), do_direct=False)
                assert r["ratio"] < C + 1e-9
                triple.append((k, d, pts, r["ratio"], C, K, mu, mv, mw))

    general = []
    for m, k in ((1, 10), (3, 14), (5, 16), (7, 16)):
        N = 1 << k
        pts = [((j + 1) * (N // (m + 2)) + j * j) % N for j in range(m)]
        assert len(set(pts)) == m
        for d in (1, 2, 4):
            C, K, mu, mv, mw = analytic_case(k, d, pts)
            general.append((m, k, d, C, K, mu, mv, mw))

    print("DIRECT_IDENTITY_CASES", len(direct))
    for k, d, pts, r in direct:
        print(
            f"  k={k} d={d} points={pts} identity_err={r['identity_error']:.3e} "
            f"decomp_err={r['decomposition_error']:.3e} ratio={r['ratio']:.9f}"
        )
    print("TRIPLE_ANALYTIC_CASES", len(triple))
    print("  max_observed_ratio", f"{max(x[3] for x in triple):.9f}")
    print("  proved_uniform_constant", f"{max(x[4] for x in triple):.9f}", "(<327)")
    print("  max_K", f"{max(x[5] for x in triple):.9e}")
    print("GENERAL_ODD_M_CASES", len(general))
    for m in (1, 3, 5, 7):
        rows = [x for x in general if x[0] == m]
        print(
            f"  m={m} k={rows[0][1]} C_m={rows[0][3]:.9f} "
            f"max|u|={max(x[5] for x in rows):.6g} "
            f"max|v|={max(x[6] for x in rows):.6g} "
            f"max|w|={max(x[7] for x in rows):.6g}"
        )
    print("STATUS PASS")


if __name__ == "__main__":
    main()
