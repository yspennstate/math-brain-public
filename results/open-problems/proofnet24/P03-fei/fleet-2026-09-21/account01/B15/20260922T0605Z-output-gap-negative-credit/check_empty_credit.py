#!/usr/bin/env python3
"""Bounded diagnostic for the B15 empty-atom information-credit identities.

This is not part of the analytic proof.  It exhausts all pairs of Boolean
functions on two remaining variables at two product-bias vectors and four
pivot biases each, checking the source-exact identities/inequalities used in
REPORT.md.
"""

import itertools
import math


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def psi(z):
    z = max(0.0, min(1.0, z))
    return h2((1.0 - math.sqrt(max(0.0, 1.0 - z * z))) / 2.0)


def point_prob(x, ps):
    ans = 1.0
    for xi, p in zip(x, ps):
        ans *= p if xi else (1.0 - p)
    return ans


def truth_and_coeffs(bits, ps):
    xs = list(itertools.product((0, 1), repeat=len(ps)))
    vals = {x: (-1.0 if (bits >> k) & 1 else 1.0) for k, x in enumerate(xs)}
    coeff = {}
    for mask in range(1 << len(ps)):
        total = 0.0
        for x in xs:
            basis = 1.0
            for i, p in enumerate(ps):
                if (mask >> i) & 1:
                    basis *= (x[i] - p) / math.sqrt(p * (1.0 - p))
            total += point_prob(x, ps) * vals[x] * basis
        coeff[mask] = total
    return vals, coeff


def run():
    m = 2
    configs = [
        ([0.3, 0.6], [0.1, 0.37, 0.5, 0.83]),
        ([0.2, 0.8], [0.05, 0.25, 0.61, 0.95]),
    ]
    cases = 0
    min_hb_minus_psi = float("inf")
    min_isj_minus_i0 = float("inf")
    min_joint = float("inf")
    max_mu_error = 0.0

    for ps, pivot_biases in configs:
        funcs = [truth_and_coeffs(bits, ps) for bits in range(1 << (1 << m))]
        xs = list(itertools.product((0, 1), repeat=m))
        for vals0, a in funcs:
            for vals1, b in funcs:
                for t in pivot_biases:
                    q = 1.0 - t
                    V = 4.0 * t * q
                    T = {S: q * a[S] ** 2 + t * b[S] ** 2 for S in a}
                    theta = {
                        S: (0.0 if T[S] < 1e-15 else t * q * (b[S] - a[S]) ** 2 / T[S])
                        for S in a
                    }
                    mu = sum(T[S] * theta[S] for S in T)
                    hb = sum(
                        T[S] * h2(t * b[S] ** 2 / T[S])
                        for S in T
                        if T[S] > 1e-15
                    )
                    isj = h2(mu) - sum(T[S] * h2(theta[S]) for S in T)

                    delta = sum(point_prob(x, ps) for x in xs if vals0[x] != vals1[x])
                    r0 = sum(point_prob(x, ps) for x in xs if vals0[x] < 0)
                    r1 = sum(point_prob(x, ps) for x in xs if vals1[x] < 0)
                    d = abs(r1 - r0)
                    m0, m1 = 1.0 - 2.0 * r0, 1.0 - 2.0 * r1
                    s = q * m0 * m0 + t * m1 * m1

                    if s < 1e-12 or 1.0 - s < 1e-12:
                        i0 = 0.0
                    else:
                        theta0 = V * d * d / s
                        nu = V * (delta - d * d) / (1.0 - s)
                        i0 = h2(mu) - s * h2(theta0) - (1.0 - s) * h2(nu)

                    p = psi(math.sqrt(V) * abs(1.0 - 2.0 * delta))
                    min_hb_minus_psi = min(min_hb_minus_psi, hb - p)
                    min_isj_minus_i0 = min(min_isj_minus_i0, isj - i0)
                    min_joint = min(min_joint, hb + isj - p - i0)
                    max_mu_error = max(max_mu_error, abs(mu - V * delta))
                    cases += 1

    print("cases", cases)
    print("min_HB_minus_Psi", format(min_hb_minus_psi, ".17g"))
    print("min_ISJ_minus_I0", format(min_isj_minus_i0, ".17g"))
    print("min_joint_slack", format(min_joint, ".17g"))
    print("max_mu_identity_error", format(max_mu_error, ".17g"))
    print("collar_margin_exact", "13979/160000")
    print("collar_margin_decimal", format(13979 / 160000, ".12f"))

    tol = 1e-12
    assert min_hb_minus_psi >= -tol
    assert min_isj_minus_i0 >= -tol
    assert min_joint >= -tol
    assert max_mu_error <= tol
    print("PASS")


if __name__ == "__main__":
    run()
