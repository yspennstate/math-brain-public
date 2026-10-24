#!/usr/bin/env python3
"""Finite sanity checks for the B14 JS-absorbing influence potential.

Enumerates Boolean functions up to global sign for n <= 4.  This is not a
proof of FEI; the accompanying REPORT.md contains the analytic proof of the
potential inequalities checked here.
"""

import json
import math
import numpy as np

LN2 = math.log(2.0)
CSTAR = 2.0 / LN2


def h2(t):
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return -t * math.log2(t) - (1.0 - t) * math.log2(1.0 - t)


def jfun(s):
    s = min(max(float(s), 0.0), 0.5)
    z = 0.5 + math.sqrt(max(0.0, s * (1.0 - s)))
    return 1.0 - h2(z)


def eta(p):
    p = float(p)
    return jfun(min(p, 1.0 - p))


def walsh(f):
    a = np.asarray(f, dtype=float).copy()
    n = int(round(math.log2(len(a))))
    step = 1
    while step < len(a):
        for i in range(0, len(a), 2 * step):
            x = a[i : i + step].copy()
            y = a[i + step : i + 2 * step].copy()
            a[i : i + step] = x + y
            a[i + step : i + 2 * step] = x - y
        step *= 2
    return a / (1 << n)


def spectrum_stats(f):
    a = walsh(f)
    p = a * a
    n = int(round(math.log2(len(f))))
    H = sum(-x * math.log2(x) for x in p if x > 0.0)
    inf = []
    for i in range(n):
        mask = 1 << i
        inf.append(float(sum(p[s] for s in range(1 << n) if s & mask)))
    I = sum(inf)
    Phi = sum(eta(x) for x in inf)
    return H, I, Phi, inf, p


def restrict(f, i, bit):
    return np.asarray([f[x] for x in range(len(f)) if ((x >> i) & 1) == bit])


def coordinate_data(f, i):
    H, I, Phi, inf, p = spectrum_stats(f)
    f0 = restrict(f, i, 0)
    f1 = restrict(f, i, 1)
    H0, _, Phi0, inf0, _ = spectrum_stats(f0)
    H1, _, Phi1, inf1, _ = spectrum_stats(f1)
    dH = H - 0.5 * (H0 + H1)
    dPhi = Phi - 0.5 * (Phi0 + Phi1)

    mask = 1 << i
    B = 0.0
    for s in range(1 << int(round(math.log2(len(f))))):
        if s & mask:
            continue
        x, y = float(p[s]), float(p[s | mask])
        w = x + y
        if w > 0.0:
            B += w * h2(y / w)
    JS = dH - B

    gap_sum = 0.0
    gap_lower = 0.0
    n = int(round(math.log2(len(f))))
    for k in range(n):
        if k == i:
            continue
        kk = k if k < i else k - 1
        x, y = float(inf0[kk]), float(inf1[kk])
        gap = eta(inf[k]) - 0.5 * (eta(x) + eta(y))
        gap_sum += gap
        gap_lower += (x - y) ** 2 / (6.0 * LN2)

    rebate = eta(inf[i]) - JS + gap_sum
    return {
        "alpha": inf[i],
        "Delta_H": dH,
        "Delta_Phi": dPhi,
        "B": B,
        "JS": JS,
        "gap_sum": gap_sum,
        "gap_lower": gap_lower,
        "rebate": rebate,
        "corrected_identity_error": abs((dH - dPhi) - (B - rebate)),
    }


def main():
    out = {"cstar": CSTAR, "by_n": {}, "global": {}}
    global_min_absorb = float("inf")
    global_min_gap_surplus = float("inf")
    global_max_identity_error = 0.0
    total_relevant = 0

    for n in range(1, 5):
        N = 1 << n
        count = 0
        min_absorb = float("inf")
        min_gap_surplus = float("inf")
        max_identity_error = 0.0
        max_phi_over_I = 0.0
        max_corrected_over_I = -float("inf")

        # Fix f(0)=+1; global sign leaves all quantities invariant.
        for code in range(1 << (N - 1)):
            f = np.ones(N, dtype=float)
            for x in range(1, N):
                if (code >> (x - 1)) & 1:
                    f[x] = -1.0
            H, I, Phi, inf, _ = spectrum_stats(f)
            if I > 1e-14:
                max_phi_over_I = max(max_phi_over_I, Phi / I)
                max_corrected_over_I = max(max_corrected_over_I, (H - Phi) / I)
            for i, alpha in enumerate(inf):
                if alpha <= 1e-14:
                    continue
                count += 1
                q = coordinate_data(f, i)
                min_absorb = min(min_absorb, q["Delta_Phi"] - q["JS"])
                min_gap_surplus = min(min_gap_surplus, q["gap_sum"] - q["gap_lower"])
                max_identity_error = max(max_identity_error, q["corrected_identity_error"])

        out["by_n"][str(n)] = {
            "relevant_coordinate_cases": count,
            "min_DeltaPhi_minus_JS": min_absorb,
            "min_gap_minus_strong_concavity_lower_bound": min_gap_surplus,
            "max_corrected_identity_abs_error": max_identity_error,
            "max_Phi_over_I": max_phi_over_I,
            "max_H_minus_Phi_over_I": max_corrected_over_I,
        }
        total_relevant += count
        global_min_absorb = min(global_min_absorb, min_absorb)
        global_min_gap_surplus = min(global_min_gap_surplus, min_gap_surplus)
        global_max_identity_error = max(global_max_identity_error, max_identity_error)

    out["global"] = {
        "total_relevant_coordinate_cases": total_relevant,
        "min_DeltaPhi_minus_JS": global_min_absorb,
        "min_gap_minus_strong_concavity_lower_bound": global_min_gap_surplus,
        "max_corrected_identity_abs_error": global_max_identity_error,
        "status": "PASS" if global_min_absorb >= -1e-12 and global_min_gap_surplus >= -1e-12 else "FAIL",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
