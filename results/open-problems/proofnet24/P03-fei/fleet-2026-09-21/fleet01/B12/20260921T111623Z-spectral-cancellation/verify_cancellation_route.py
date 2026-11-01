#!/usr/bin/env python3
"""Self-contained checks for the B12 spectral-cancellation FEI continuation.

This is a finite sanity checker only.  The analytic statements in REPORT.md do
not depend on the enumeration.
"""

import json
import math

BETA = 6.4547837


def fwht(values):
    a = [float(x) for x in values]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def analyze(values, n):
    N = 1 << n
    hats = [x / N for x in fwht(values)]
    p = [x * x for x in hats]

    # Upward zeta transform: u[A] = sum_{B superset A} p[B].
    u = p[:]
    for bit in range(n):
        for A in range(N):
            if not ((A >> bit) & 1):
                u[A] += u[A | (1 << bit)]

    H = sum(-x * math.log2(x) for x in p if x > 0.0)
    I = sum(A.bit_count() * p[A] for A in range(N))
    p0 = p[0]
    V = 1.0 - p0
    Bcan = sum(
        p[A] * math.log2(u[A] / p[A])
        for A in range(N)
        if p[A] > 0.0
    )

    correction = p0 * math.log2(1.0 / p0) if p0 > 0.0 else 0.0
    rhs = 2.0 * I - 2.0 * V - correction + 2.0 * Bcan

    granular_ok = True
    for A in range(1, N):
        if p[A] > 0.0:
            k = A.bit_count()
            lower = (2.0 ** (1 - k)) * math.sqrt(p[A])
            if u[A] + 1e-12 < lower:
                granular_ok = False
                break

    levels = {A.bit_count() for A, mass in enumerate(p) if mass > 1e-15}
    pure_positive_level = len(levels) == 1 and 0 not in levels

    return {
        "H": H,
        "I": I,
        "Bcan": Bcan,
        "reduction_rhs": rhs,
        "granular_ok": granular_ok,
        "reduction_ok": H <= rhs + 1e-10,
        "pure_positive_level": pure_positive_level,
    }


def shell_rows():
    rows = []
    for m in range(2, 9):
        n = math.floor(m * math.exp(2 * (m - 1)))
        ratio = math.log2(n) - math.lgamma(m + 1) / (math.log(2) * m)
        rows.append(
            {
                "m": m,
                "n": n,
                "ln_n_over_m": math.log(n / m),
                "pc_cap": 2 * (m - 1),
                "all_PC_certified_analytically": math.log(n / m) <= 2 * (m - 1),
                "U_over_I": ratio,
                "U_over_I_minus_beta": ratio - BETA,
            }
        )
    return rows


def enumerate_boolean():
    rows = []
    for n in range(1, 5):
        N = 1 << n
        number = 1 << (N - 1)  # fix f(0)=+1 to quotient global negation
        best_ratio = -1.0
        best_mask = None
        best_hi = None
        all_granular = True
        all_reduction = True
        pure_count = 0
        pure_max_Bcan = 0.0

        for mask in range(number):
            values = [1.0] * N
            for x in range(1, N):
                if (mask >> (x - 1)) & 1:
                    values[x] = -1.0
            st = analyze(values, n)
            all_granular = all_granular and st["granular_ok"]
            all_reduction = all_reduction and st["reduction_ok"]
            if st["pure_positive_level"]:
                pure_count += 1
                pure_max_Bcan = max(pure_max_Bcan, st["Bcan"])
            if st["I"] > 1e-12:
                ratio = st["Bcan"] / st["I"]
                if ratio > best_ratio + 1e-15:
                    best_ratio = ratio
                    best_mask = mask
                    best_hi = st["H"] / st["I"]

        rows.append(
            {
                "n": n,
                "functions_mod_global_sign": number,
                "max_Bcan_over_I": best_ratio,
                "maximizer_mask": best_mask,
                "H_over_I_at_max": best_hi,
                "granular_inequality_all_pass": all_granular,
                "entropy_reduction_all_pass": all_reduction,
                "pure_positive_level_count": pure_count,
                "pure_level_max_Bcan": pure_max_Bcan,
            }
        )
    return rows


def main():
    result = {
        "status": "finite_sanity_only_full_FEI_open",
        "beta": BETA,
        "sharp_target_cancellation_constant": BETA / 2.0 - 1.0,
        "shell_obstruction": shell_rows(),
        "boolean_enumeration": enumerate_boolean(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
