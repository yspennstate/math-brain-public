#!/usr/bin/env python3
"""Deterministic diagnostics for B10 half-tax candidate on two-bit gates.

The proof in REPORT.md reduces every nonlinear two-bit gate to the point-defect
formula used here. Decimal arithmetic is diagnostic, not interval arithmetic.
"""

from decimal import Decimal, getcontext
import json
import math

# 2^-512 is about 10^-154.  Keep enough guard digits that 1-p and the
# entropy cancellations remain resolved throughout the declared pilot.
getcontext().prec = 240
D = Decimal
LN2 = D(2).ln()


def h2d(x):
    x = D(x)
    if x == 0 or x == 1:
        return D(0)
    return (-x * x.ln() - (1 - x) * (1 - x).ln()) / LN2


def point_defect_decimal(p, q):
    p, q = D(p), D(q)
    s = 4 * q * (1 - q)
    c = 4 * q * q
    j = h2d(s * p) - p * h2d(s)
    den = 1 - s * p
    a = c * p * (1 - p) / den
    m = den * h2d(a) + s * p * h2d(p)
    e = min(p, 1 - p)
    delta = e * ((1 - e) / e).ln() / LN2
    return j, m, delta, j - m - delta / 2


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


def point_defect_float(p, q):
    s = 4 * q * (1 - q)
    c = 4 * q * q
    j = h2(s * p) - p * h2(s)
    den = 1 - s * p
    a = c * p * (1 - p) / den
    m = den * h2(a) + s * p * h2(p)
    e = min(p, 1 - p)
    delta = e * math.log2((1 - e) / e)
    return j, m, delta, j - m - delta / 2


def main():
    # A bounded interior pilot; it does not certify the continuum.
    interior_max = (-1e100, None)
    interior_ratio = (-1e100, None)
    n = 400
    for i in range(1, n):
        p = i / n
        for j0 in range(1, n):
            q = j0 / n
            j, m, delta, gap = point_defect_float(p, q)
            if gap > interior_max[0]:
                interior_max = (gap, (p, q))
            if delta and (j - m) / delta > interior_ratio[0]:
                interior_ratio = ((j - m) / delta, (p, q))

    # The asymptotically dangerous tube q=1/4+O(1/sqrt(log(1/p))).
    rare_max = (D("-1e1000"), None)
    rare_ratio = (D("-1e1000"), None)
    rare_count = 0
    for k in list(range(4, 65, 4)) + [96, 128, 192, 256, 384, 512]:
        p = D(2) ** (-k)
        offsets = [D(j) / (D(40) * D(k).sqrt()) for j in range(-20, 21)]
        qs = [D(1) / 4 + z for z in offsets]
        qs += [p, D(1) - p, D(1) / 2]
        for q in qs:
            if not 0 < q < 1:
                continue
            jv, mv, delta, gap = point_defect_decimal(p, q)
            rare_count += 1
            if gap > rare_max[0]:
                rare_max = (gap, (k, q))
            ratio = (jv - mv) / delta
            if ratio > rare_ratio[0]:
                rare_ratio = (ratio, (k, q))

    # The opposite revealed endpoint p=1-epsilon.
    upper_max = (D("-1e1000"), None)
    upper_count = 0
    for k in list(range(4, 65, 4)) + [96, 128, 192, 256]:
        p = 1 - D(2) ** (-k)
        for j0 in range(1, 100):
            q = D(j0) / 100
            _, _, _, gap = point_defect_decimal(p, q)
            upper_count += 1
            if gap > upper_max[0]:
                upper_max = (gap, (k, q))

    # Check the first nonzero term at the unique saturation point q=1/4.
    target = (D(1) / 2 - LN2) / LN2
    asymptotic = []
    for k in [16, 32, 64, 128, 256, 512]:
        p = D(2) ** (-k)
        _, _, _, gap = point_defect_decimal(p, D(1) / 4)
        asymptotic.append({
            "k": k,
            "gap_over_p": str(gap / p),
            "target": str(target),
            "absolute_error": str(abs(gap / p - target)),
        })

    out = {
        "status": "PASS_NUMERICAL_DIAGNOSTIC_ONLY",
        "candidate": "J_A <= M_A + Delta_A/2",
        "reduction": "nonlinear two-bit gates -> point defect",
        "interior_grid": {
            "box": "p,q in {1/400,...,399/400}",
            "instances": (n - 1) ** 2,
            "maximum_gap": interior_max,
            "maximum_ratio_(J-M)/Delta": interior_ratio,
        },
        "rare_tube": {
            "definition": "p=2^-k; q=1/4+j/(40 sqrt(k)), -20<=j<=20, plus joint q endpoints",
            "instances": rare_count,
            "maximum_gap": (str(rare_max[0]), (rare_max[1][0], str(rare_max[1][1]))),
            "maximum_ratio_(J-M)/Delta": (str(rare_ratio[0]), (rare_ratio[1][0], str(rare_ratio[1][1]))),
        },
        "upper_endpoint": {
            "definition": "p=1-2^-k; q=j/100",
            "instances": upper_count,
            "maximum_gap": (str(upper_max[0]), (upper_max[1][0], str(upper_max[1][1]))),
        },
        "saturation_second_term": asymptotic,
        "randomness": "NONE",
        "warning": "Decimal and binary64 evaluations are not rigorous interval enclosures.",
        "full_FEI": "OPEN",
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
