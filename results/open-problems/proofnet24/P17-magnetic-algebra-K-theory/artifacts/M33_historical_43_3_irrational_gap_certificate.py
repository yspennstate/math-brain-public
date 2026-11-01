#!/usr/bin/env python3
"""
ProofNet24 P17 M33 certificate.

Historical nearest-neighbor Example 4.3.3, exact irrational source frequencies
    theta1=(3-sqrt(3))/2,
    theta2=(4-sqrt(5))/3,
with r=0.4.

The certificate has two layers.

(A) Rational full-C*-spectrum certificate at the closer approximants
    theta1'=989/1560, theta2'=939/1597.
    For each factor it validates all periodic/antiperiodic endpoint eigenvalues
    on an 8-point residual-hull grid by a posteriori Hermitian residual/polar
    bounds. Exact Jacobi coefficients are interval-enclosed with mpmath.iv.
    The residual hull interpolation budget is then added exactly as in M31/M32.

(B) A source-specific frequency-continuity theorem proved in the run report:
    for the one-dimensional source Jacobi spectrum Sigma(theta), for every
    integer L>=1,

      d_H(Sigma(theta),Sigma(theta'))
      <= pi*A/L + 4*pi*r*A*(2L+3)*|theta-theta'|,

    where A=exp(-(1-2r)).

    The script interval-encloses the two algebraic frequency errors and the
    corresponding bounds at L1=1148 and L2=1635. If the validated rational
    distance from each target interval exceeds the rational hull budget plus
    the two frequency-continuity budgets, the exact irrational spectrum is
    disjoint from that target interval throughout the straight parameter path.

Software trust boundary: IEEE-754 binary64 arithmetic under the standard gamma_k
model plus mpmath.iv outward interval semantics. NumPy eigendata are used only
as candidate dyadic data; no correctness or backward-stability theorem for the
eigensolver is assumed.
"""

import math
from decimal import Decimal
import numpy as np
import mpmath as mp
from mpmath.libmp import to_float

mp.iv.dps = 70
U = 2.0**-53
R = 0.4
NGRID = 8
L1 = 1148
L2 = 1635


def gamma(k):
    x = k * U
    if x >= 1:
        raise ValueError("gamma_k invalid")
    return x / (1 - x)


def jacobi(Q, p, alpha, beta_sign):
    """Binary64 midpoint matrix, used only to generate candidate eigendata."""
    theta = p / Q
    phi = alpha / Q
    n = np.arange(Q, dtype=float)
    t = np.exp(-(1 + R * (
        np.sin(2*np.pi*((n+1)*theta + phi))
        - np.sin(2*np.pi*(n*theta + phi)))))
    H = np.zeros((Q, Q), dtype=float)
    idx = np.arange(Q-1)
    H[idx, idx+1] = t[:-1]
    H[idx+1, idx] = t[:-1]
    H[Q-1, 0] = beta_sign * t[-1]
    H[0, Q-1] = beta_sign * t[-1]
    return H, t


def exact_weight_midpoint_error(Q, p, alpha_num, alpha_den, tfloat):
    """Outward upper bound for max |t_exact - tfloat|."""
    rr = mp.iv.mpf(2) / 5
    theta = mp.iv.mpf(p) / Q
    phi = (mp.iv.mpf(alpha_num) / alpha_den) / Q
    twopi = 2 * mp.iv.pi
    out = 0.0
    for n, tf in enumerate(tfloat):
        s1 = mp.iv.sin(twopi * (mp.iv.mpf(n+1)*theta + phi))
        s0 = mp.iv.sin(twopi * (mp.iv.mpf(n)*theta + phi))
        ti = mp.iv.exp(-(1 + rr*(s1-s0)))
        lo = to_float(ti._mpi_[0])
        hi = to_float(ti._mpi_[1])
        e = max(abs(tf-lo), abs(tf-hi))
        e = math.nextafter(e*(1+16*U) + 1e-30, math.inf)
        out = max(out, e)
    return out


def validated_eigh(Q, p, alpha_num, alpha_den, beta_sign):
    """Return candidate ordered eigenvalues and a rigorous common enclosure eta."""
    H, tfloat = jacobi(Q, p, alpha_num/alpha_den, beta_sign)
    D, Qm = np.linalg.eigh(H)

    Gf = Qm.T @ Qm
    max_def = float(np.max(np.abs(Gf - np.eye(Q))))
    gdot = gamma(2*Q + 4)
    col2 = np.sum(Qm*Qm, axis=0)
    smax = float(np.max(col2)) / (1 - gdot)
    gram_entry_round = gdot * smax
    delta = Q * (max_def + gram_entry_round + 4*U)
    delta = math.nextafter(delta*(1+16*U) + 1e-30, math.inf)
    assert delta < 1.0

    dmax = float(max(abs(D[0]), abs(D[-1])))
    tmax = float(np.max(np.abs(tfloat)))
    rf = np.empty_like(Qm)
    for j in range(Q):
        jm = (j-1) % Q
        jp = (j+1) % Q
        left = tfloat[jm] * (beta_sign if j == 0 else 1)
        right = tfloat[j] * (beta_sign if j == Q-1 else 1)
        rf[j, :] = left*Qm[jm, :] + right*Qm[jp, :] - D*Qm[j, :]
    rfro = float(np.linalg.norm(rf, ord='fro'))
    rfro *= (1 + gamma(2*Q*Q + 20))

    qfro = math.sqrt(Q * smax)
    sparse_round = gamma(10) * (2*tmax + dmax) * qfro + 8*U*Q
    rmid = rfro + sparse_round

    wt_err = exact_weight_midpoint_error(Q, p, alpha_num, alpha_den, tfloat)
    dA = 2 * wt_err
    rF = rmid + dA*qfro

    invsqrt = 1 / math.sqrt(1-delta)
    qnorm = math.sqrt(1+delta)
    polar_dev = invsqrt - 1
    eta = rF*invsqrt + 2*qnorm*dmax*polar_dev
    eta = math.nextafter(eta*(1+64*U) + 1e-30, math.inf)
    return D, eta, delta, rF, dA


def merge(intervals):
    out = []
    for a, b in sorted(intervals):
        if not out or a > out[-1][1]:
            out.append([a, b])
        else:
            out[-1][1] = max(out[-1][1], b)
    return [(a, b) for a, b in out]


def factor_grid_cover(Q, p):
    intervals = []
    stats = []
    for k in range(NGRID):
        dp, ep, gp, rp, ap = validated_eigh(Q, p, k, NGRID, +1)
        da, ea, ga, ra, aa = validated_eigh(Q, p, k, NGRID, -1)
        eta = max(ep, ea)
        stats.extend([(ep, gp, rp, ap), (ea, ga, ra, aa)])
        endpoints = np.sort(np.concatenate([dp, da]))
        for j in range(Q):
            lo = math.nextafter(float(endpoints[2*j] - eta), -math.inf)
            hi = math.nextafter(float(endpoints[2*j+1] + eta), math.inf)
            intervals.append((lo, hi))
    return merge(intervals), stats


def minkowski_cover(U1, U2):
    ints = []
    for a, b in U1:
        for c, d in U2:
            ints.append((math.nextafter(a+c, -math.inf),
                         math.nextafter(b+d, math.inf)))
    return merge(ints)


def decimal_interval(lo_s, hi_s):
    lo = math.nextafter(float(Decimal(lo_s)), -math.inf)
    hi = math.nextafter(float(Decimal(hi_s)), math.inf)
    return lo, hi


def interval_distance_lower(G, Uset):
    a, b = G
    ans = math.inf
    for c, d in Uset:
        if d >= a and c <= b:
            return 0.0
        if d < a:
            ans = min(ans, a-d)
        elif c > b:
            ans = min(ans, c-b)
    return math.nextafter(ans, -math.inf)


def iv_upper(x):
    return math.nextafter(to_float(x._mpi_[1]), math.inf)


def exact_frequency_error_uppers():
    th1 = (mp.iv.mpf(3) - mp.iv.sqrt(3)) / 2
    th2 = (mp.iv.mpf(4) - mp.iv.sqrt(5)) / 3
    r1 = mp.iv.mpf(989) / 1560
    r2 = mp.iv.mpf(939) / 1597
    d1 = r1 - th1
    d2 = r2 - th2
    d1u = max(abs(to_float(d1._mpi_[0])), abs(to_float(d1._mpi_[1])))
    d2u = max(abs(to_float(d2._mpi_[0])), abs(to_float(d2._mpi_[1])))
    return (math.nextafter(d1u, math.inf),
            math.nextafter(d2u, math.inf))


def frequency_bound_upper(delta, L):
    rr = mp.iv.mpf(2) / 5
    A = mp.iv.exp(-mp.iv.mpf(1)/5)
    dd = mp.iv.mpf(delta)
    val = mp.iv.pi*A/L + 4*mp.iv.pi*rr*A*(2*L+3)*dd
    return iv_upper(val)


def hull_budget_upper(Q1, Q2):
    rr = mp.iv.mpf(2) / 5
    c = 4*mp.iv.pi*rr*mp.iv.exp(-mp.iv.mpf(1)/5)
    return iv_upper(c/(Q1*NGRID) + c/(Q2*NGRID))


def main():
    Q1, p1 = 1560, 989
    Q2, p2 = 1597, 939
    U1, s1 = factor_grid_cover(Q1, p1)
    U2, s2 = factor_grid_cover(Q2, p2)
    full = minkowski_cover(U1, U2)

    hull = hull_budget_upper(Q1, Q2)
    dth1, dth2 = exact_frequency_error_uppers()
    freq1 = frequency_bound_upper(dth1, L1)
    freq2 = frequency_bound_upper(dth2, L2)
    freq = math.nextafter(freq1 + freq2, math.inf)

    targets = [
        decimal_interval('-1.18', '-1.00'),
        decimal_interval('-0.44', '-0.33'),
        decimal_interval('0.33', '0.44'),
        decimal_interval('1.00', '1.18'),
    ]

    print('rational approximants:', f'{p1}/{Q1}', f'{p2}/{Q2}')
    print('factor1 max eta =', max(x[0] for x in s1))
    print('factor2 max eta =', max(x[0] for x in s2))
    print('factor1 max Gram bound =', max(x[1] for x in s1))
    print('factor2 max Gram bound =', max(x[1] for x in s2))
    print('rational hull interpolation budget <=', hull)
    print('frequency errors <=', dth1, dth2)
    print('frequency bounds <=', freq1, freq2, 'sum <=', freq)
    print('factor cover components:', len(U1), len(U2), 'sum cover components:', len(full))
    print()

    final_margins = []
    for G in targets:
        d = interval_distance_lower(G, full)
        rat_margin = math.nextafter(d - hull, -math.inf)
        irr_margin = math.nextafter(rat_margin - freq, -math.inf)
        final_margins.append(irr_margin)
        print('target', G,
              'validated grid distance >=', d,
              'rational full-spectrum margin >=', rat_margin,
              'irrational full-spectrum margin >=', irr_margin)
        assert rat_margin > freq
        assert irr_margin > 0

    print('\nMIN IRRATIONAL MARGIN >=', min(final_margins))

    d1, e1, *_ = validated_eigh(Q1, p1, 0, NGRID, +1)
    d2, e2, *_ = validated_eigh(Q2, p2, 0, NGRID, +1)
    sums = np.sort((d1[:, None] + d2[None, :]).ravel())
    es = math.nextafter(e1 + e2, math.inf)
    energies = [-1.10, -0.385, 0.385, 1.10]
    labels = [(1,-1,-1,1), (-1,2,2,-3), (2,-2,-2,3), (0,1,1,-1)]
    print('\nvalidated rational Fermi ranks:')
    for E, lab in zip(energies, labels):
        rank = int(np.searchsorted(sums, E, side='left'))
        near = min(abs(sums[rank-1]-E) if rank else math.inf,
                   abs(sums[rank]-E) if rank < len(sums) else math.inf)
        assert near > es
        c0,c13,c24,c1234 = lab
        expected = (c0*Q1*Q2 + c13*p1*Q2 + c24*p2*Q1 + c1234*p1*p2)
        print('E', E, 'rank', rank, 'expected label rank', expected,
              'nearest candidate distance', near, 'validated sum error <=', es)
        assert rank == expected


if __name__ == '__main__':
    main()
