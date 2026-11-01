#!/usr/bin/env python3
"""
P10/F0119 certificate at the binary-tree KS point lambda=1/sqrt(2).

Substantive checks:
1. PROVED PARTIAL finite-amplitude family: for every theta in [0,pi/3],
   the genuinely arbitrary-orbit diagonal family with complex magnetization
       m=(1/2) exp(i theta)
   satisfies K_*(p,p) <= Psi(p).  This includes three-distinct posteriors.
   The proof is computer-assisted: 128 outward interval cells cover the full
   Weyl-sector angular interval and use the exact edge-gap / normalization-
   entropy / polynomial-interaction decomposition from the accompanying report.

2. The proposed fixed-Euclidean-radius angular-extremality reduction is false.
   At rho=1/2, theta=pi/8 gives a strictly smaller KS gap than either
   reflection-axis endpoint theta=0, pi/3.

3. The still-stronger symmetrized tensorization inequality for Psi after the
   edge is also false.  The Bayes-plausible two-equal orbit p=(0,1/2,1/2)
   has a negative pure fusion-tensorization gap; the positive one-edge surplus
   is essential to the actual KS gap.

This is a research certificate, not an independent publication-level audit.
"""

import itertools
import math
import mpmath as mp

mp.mp.dps = 80
iv = mp.iv
SQ2 = iv.sqrt(2)
SQ3 = iv.sqrt(3)
PERMS = list(itertools.permutations(range(3)))


def _xlog3(X):
    """Outward enclosure of x log(3x) on a nonnegative interval."""
    lo = float(X.a)
    hi = float(X.b)
    if lo < -1e-7:
        raise RuntimeError((lo, hi))
    lo = max(0.0, lo)
    hi = max(0.0, hi)

    def f(t):
        return 0.0 if t == 0.0 else t * math.log(3.0 * t)

    vals = [f(lo), f(hi)]
    xc = 1.0 / (3.0 * math.e)
    if lo <= xc <= hi:
        vals.append(-1.0 / (3.0 * math.e))
    lower = min(vals)
    upper = max(vals)
    for _ in range(8):
        lower = math.nextafter(lower, -math.inf)
        upper = math.nextafter(upper, math.inf)
    return iv.mpf([lower, upper])


def _psi_vec(p):
    out = iv.mpf(0)
    for X in p:
        z = X - iv.mpf(1) / 3
        out += _xlog3(X) + iv.mpf(3) * z**3 / 2 - z**4
    return out


def _edge(p):
    one_third = iv.mpf(1) / 3
    return [one_third + (X - one_third) / SQ2 for X in p]


def _Pxy(x, y):
    # P(m)=Re(m^3)/3-2|m|^4/9 for m=x+iy.
    return (x**3 - 3 * x * y**2) / 3 - 2 * (x**2 + y**2) ** 2 / 9


def _transform(x, y, j, reflect):
    # D_3 action: m -> omega^j m and m -> omega^j conjugate(m).
    yy = -y if reflect else y
    if j == 0:
        return x, yy
    if j == 1:
        return -x / 2 - SQ3 * yy / 2, SQ3 * x / 2 - yy / 2
    return -x / 2 + SQ3 * yy / 2, -SQ3 * x / 2 - yy / 2


def _clip01(X):
    # On rho=1/2 and theta in [0,pi/3] the exact p(theta) is in the simplex.
    # Intersecting the dependency-widened coordinate interval with [0,1]
    # therefore preserves every exact value while sharply reducing wrapping.
    return iv.mpf([max(0.0, float(X.a)), min(1.0, float(X.b))])


def _Hdiag_half_radius(theta):
    """KS gap H(p,p) on |m|=1/2, using the exact decomposition."""
    R = iv.mpf(1) / 2
    x = R * iv.cos(theta)
    y = R * iv.sin(theta)

    p = [
        _clip01((1 + 2 * x) / 3),
        _clip01((1 - x + SQ3 * y) / 3),
        _clip01((1 - x - SQ3 * y) / 3),
    ]
    pe = _edge(p)
    edge_gap = _psi_vec(p) / 2 - _psi_vec(pe)

    # Exact arbitrary-orbit decomposition for p=q:
    # H = 2 E(p) + S - Delta_P.
    xe = x / SQ2
    ye = y / SQ2
    Pedge = _Pxy(xe, ye)
    S = iv.mpf(0)
    KP = iv.mpf(0)
    for j in range(3):
        for reflect in (False, True):
            nx, ny = _transform(x, y, j, reflect)
            bx = nx / SQ2
            by = ny / SQ2
            M = 1 + 2 * (xe * bx + ye * by)
            Nr = xe + bx + xe * bx - ye * by
            Ni = ye + by - xe * by - ye * bx
            weighted_P = (
                (Nr**3 - 3 * Nr * Ni**2) / (3 * M**2)
                - 2 * (Nr**2 + Ni**2) ** 2 / (9 * M**3)
            )
            S += M * iv.log(M)
            KP += weighted_P
    S /= 6
    KP /= 6
    Delta_P = KP - 2 * Pedge
    return 2 * edge_gap + S - Delta_P


def _posterior_from_xy(x, y):
    return [
        (1 + 2 * x) / 3,
        (1 - x + SQ3 * y) / 3,
        (1 - x - SQ3 * y) / 3,
    ]


def _kernel(p, q):
    r = _edge(p)
    total = iv.mpf(0)
    for perm in PERMS:
        qp = [q[j] for j in perm]
        s = _edge(qp)
        Z = sum((r[i] * s[i] for i in range(3)), iv.mpf(0))
        post = [r[i] * s[i] / Z for i in range(3)]
        total += 3 * Z * _psi_vec(post)
    return total / 6


def _gap(p, q):
    return (_psi_vec(p) + _psi_vec(q)) / 2 - _kernel(p, q)


def _xlogx(X):
    lo = float(X.a)
    hi = float(X.b)
    if lo < -1e-7:
        raise RuntimeError((lo, hi))
    lo = max(0.0, lo)
    hi = max(0.0, hi)

    def f(t):
        return 0.0 if t == 0.0 else t * math.log(t)

    vals = [f(lo), f(hi)]
    xc = 1.0 / math.e
    if lo <= xc <= hi:
        vals.append(-1.0 / math.e)
    lower = min(vals)
    upper = max(vals)
    for _ in range(8):
        lower = math.nextafter(lower, -math.inf)
        upper = math.nextafter(upper, math.inf)
    return iv.mpf([lower, upper])


def _F_likelihood(L):
    # Mean-one likelihood functional corresponding exactly to Psi.
    d = [X - 1 for X in L]
    return (
        sum((_xlogx(X) for X in L), iv.mpf(0)) / 3
        + sum((X**3 for X in d), iv.mpf(0)) / 18
        - sum((X**4 for X in d), iv.mpf(0)) / 81
    )


def _F_homogeneous(z):
    M = sum(z, iv.mpf(0)) / 3
    L = [X / M for X in z]
    d = [X - 1 for X in L]
    entropy = sum((X * iv.log(X / M) for X in z), iv.mpf(0)) / 3
    return (
        entropy
        + M * sum((X**3 for X in d), iv.mpf(0)) / 18
        - M * sum((X**4 for X in d), iv.mpf(0)) / 81
    )


def main():
    # A. Full finite-amplitude angular ring |m|=1/2.
    N = 128
    min_lower = float("inf")
    worst = None
    for k in range(N):
        theta = iv.pi * iv.mpf([k, k + 1]) / (3 * N)
        H = _Hdiag_half_radius(theta)
        lower = float(H.a)
        if lower < min_lower:
            min_lower = lower
            worst = (k, float(theta.a), float(theta.b), lower, float(H.b))
        if lower <= 0:
            print("RING_FAIL", k, theta, H)
            raise SystemExit(1)
    print("RING_PASS")
    print("ring_intervals", N)
    print("ring_worst", worst)

    # B. Fixed-radius angular extremality is false at an exact algebraic point.
    rho = iv.mpf(1) / 2
    p_plus = _posterior_from_xy(rho, iv.mpf(0))
    p_minus = _posterior_from_xy(rho / 2, SQ3 * rho / 2)
    c = iv.sqrt(2 + SQ2) / 2
    s = iv.sqrt(2 - SQ2) / 2
    p_interior = _posterior_from_xy(rho * c, rho * s)

    g_plus = _gap(p_plus, p_plus)
    g_minus = _gap(p_minus, p_minus)
    g_interior = _gap(p_interior, p_interior)
    d_plus = g_interior - g_plus
    d_minus = g_interior - g_minus
    print("axis_plus_gap", g_plus)
    print("axis_minus_gap", g_minus)
    print("interior_pi_over_8_gap", g_interior)
    print("interior_minus_axis_plus", d_plus)
    print("interior_minus_axis_minus", d_minus)
    if not (float(d_plus.b) < 0 and float(d_minus.b) < 0):
        print("ANGULAR_EXTREMALITY_CHECK_FAIL")
        raise SystemExit(1)
    print("ANGULAR_EXTREMALITY_REFUTED")

    # C. Pure symmetrized tensorization of Psi after the edge is false.
    p = [iv.mpf(0), iv.mpf(1) / 2, iv.mpf(1) / 2]
    A = [3 * X for X in _edge(p)]
    avg = iv.mpf(0)
    for perm in PERMS:
        B = [A[j] for j in perm]
        avg += _F_homogeneous([A[i] * B[i] for i in range(3)])
    avg /= 6
    tensor_gap = 2 * _F_likelihood(A) - avg
    edge_gap = _psi_vec(p) / 2 - _psi_vec(_edge(p))
    actual_gap_from_parts = 2 * edge_gap + tensor_gap
    actual_gap_direct = _gap(p, p)
    print("pure_tensorization_gap", tensor_gap)
    print("single_edge_surplus", edge_gap)
    print("actual_gap_from_parts", actual_gap_from_parts)
    print("actual_gap_direct", actual_gap_direct)
    if not float(tensor_gap.b) < 0:
        print("TENSORIZATION_CHECK_FAIL")
        raise SystemExit(1)
    if not float(actual_gap_from_parts.a) > 0:
        print("COMBINED_GAP_CHECK_FAIL")
        raise SystemExit(1)
    print("PURE_TENSORIZATION_REFUTED")
    print("OVERALL_PASS")


if __name__ == "__main__":
    main()
