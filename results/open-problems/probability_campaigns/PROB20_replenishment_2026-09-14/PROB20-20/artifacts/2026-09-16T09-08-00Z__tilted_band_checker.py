#!/usr/bin/env python3
"""Finite bookkeeping checks for PROB20-20 tilted amplified-band algebra.

These are finite sanity checks only. They do not verify the asymptotic theorem.
"""

import math
from collections import defaultdict


def convolve_pmf(pi, n):
    d = {0: 1.0}
    for _ in range(n):
        nd = defaultdict(float)
        for s, p in d.items():
            for k, pk in enumerate(pi):
                if pk:
                    nd[s + k] += p * pk
        d = dict(nd)
    return d


def bisect(f, lo, hi, steps=120):
    flo = f(lo)
    fhi = f(hi)
    if flo * fhi > 0:
        raise RuntimeError("root not bracketed")
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        fm = f(mid)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2.0


def check_case(name, raw_pi, n, m, L, U, mu):
    total = sum(raw_pi)
    pi = [x / total for x in raw_pi]
    tail = sum(pi[L + 1:])

    def truncated_vals(t):
        M = tail
        Mp = 0.0
        for k, pk in enumerate(pi):
            if k <= L:
                e = math.exp(t * k)
                M += pk * e
                Mp += k * pk * e
        return M, Mp

    def root_eq(t):
        M, Mp = truncated_vals(t)
        return Mp / M - mu

    hi = 0.01
    while root_eq(hi) < 0:
        hi *= 2
        if hi > 100:
            raise RuntimeError("could not bracket saddlepoint")
    t = bisect(root_eq, 0.0, hi)
    M, Mp = truncated_vals(t)
    J = mu * t - math.log(M)

    full = convolve_pmf(pi, n)
    p = full.get(m, 0.0)
    if p <= 0:
        raise RuntimeError("inadmissible exact sum")

    pi_cap = [pk if k <= U else 0.0 for k, pk in enumerate(pi)]
    cap_p = convolve_pmf(pi_cap, n).get(m, 0.0)
    eta = cap_p / p
    if eta <= 0:
        raise RuntimeError("cap excludes exact-sum event")

    b = -math.log(p)
    lam = m / n
    F_U = sum(pk * math.exp(t * k) for k, pk in enumerate(pi) if k <= U)
    F_low = sum(pk * math.exp(t * k) for k, pk in enumerate(pi) if k <= L)
    B = F_U - F_low

    coefficient_floor = lam * t - b / n + math.log(eta) / n
    coeff_slack = math.log(F_U) - coefficient_floor

    exact_band_floor = math.exp(coefficient_floor) - M
    band_slack = B - exact_band_floor

    assert coeff_slack >= -1e-12
    assert band_slack >= -1e-12
    assert abs(Mp / M - mu) < 1e-11

    return {
        "name": name,
        "mean": sum(k * pk for k, pk in enumerate(pi)),
        "t": t,
        "J": J,
        "eta": eta,
        "B": B,
        "exact_band_floor": exact_band_floor,
        "coeff_slack": coeff_slack,
        "band_slack": band_slack,
    }


def main():
    cases = [
        ("A", [0.48, 0.30, 0.12, 0.05, 0.02, 0.01, 0.01, 0.005, 0.005],
         12, 24, 3, 7, 1.30),
        ("B", [0.55, 0.20, 0.10, 0.06, 0.035, 0.02, 0.015, 0.01, 0.005, 0.005],
         10, 22, 3, 8, 1.40),
        ("C", [0.58, 0.18, 0.09, 0.055, 0.035, 0.02, 0.015, 0.01, 0.007, 0.004, 0.004],
         9, 18, 2, 8, 1.15),
    ]
    out = [check_case(*c) for c in cases]
    print("PROB20-20 tilted-band finite checker")
    for row in out:
        print(
            row["name"],
            "mean=%.12g" % row["mean"],
            "t=%.12g" % row["t"],
            "J=%.12g" % row["J"],
            "eta=%.12g" % row["eta"],
            "B=%.12g" % row["B"],
            "floor=%.12g" % row["exact_band_floor"],
            "coeff_slack=%.12g" % row["coeff_slack"],
            "band_slack=%.12g" % row["band_slack"],
        )
    print("PASS")


if __name__ == "__main__":
    main()
