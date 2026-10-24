#!/usr/bin/env python3
"""Deterministic standard-library diagnostic for RM3-LOWLEVEL-BARRIER-v1.

This checker evaluates the exact influence/entropy/I-projection formulas for
recursive ternary majority and the labelled level-<=2 KL projection.  The
analytic theorem is proved in REPORT.md; this file is supporting arithmetic.
"""

import math

C_SHAPE = 6.55844529582746
DEPTHS = (3, 4, 5, 6, 8, 10, 12, 16, 20)


def h2(x: float) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return (-x * math.log(x) - (1.0 - x) * math.log1p(-x)) / math.log(2.0)


def positive_c(depth: int) -> float:
    """Positive root of 1-c=(1-c*2^-m)^(3^m), by monotone bisection."""
    n = 3 ** depth
    r = 2.0 ** (-depth)

    def f(c: float) -> float:
        return 1.0 - c - math.exp(n * math.log1p(-c * r))

    lo, hi = 1e-12, 1.0
    for _ in range(220):
        mid = (lo + hi) / 2.0
        if f(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def row(depth: int):
    n = 3 ** depth
    r = 2.0 ** (-depth)
    mu = n * r
    c = positive_c(depth)
    t = c * r
    hmax = (n * h2(t) - h2(c)) / c
    demand = hmax - C_SHAPE * (mu - 1.0)

    # Recursive majority has exactly N singleton atoms, each of mass 4^-m.
    alpha = (3.0 / 4.0) ** depth
    log_p1 = -depth * math.log(4.0)

    # Q(S)=c^(|S|-1) r^|S| (1-cr)^(N-|S|), for S nonempty.
    log_q1 = math.log(c * r) + (n - 1) * math.log1p(-c * r) - math.log(c)
    log_q2 = 2.0 * math.log(c * r) + (n - 2) * math.log1p(-c * r) - math.log(c)

    log_beta1 = math.log(n) + log_q1
    log_beta2 = math.log(n) + math.log(n - 1) - math.log(2.0) + log_q2
    beta1 = 0.0 if log_beta1 < -745.0 else math.exp(log_beta1)
    beta2 = 0.0 if log_beta2 < -745.0 else math.exp(log_beta2)
    beta = beta1 + beta2

    # P has no level-2 atoms.  Pi_2 therefore has N singleton symbols plus tail.
    singleton_kl = alpha * (log_p1 - log_q1) / math.log(2.0)
    tail_kl = (1.0 - alpha) * math.log((1.0 - alpha) / (1.0 - beta), 2.0)
    delta2 = singleton_kl + tail_kl
    ratio = None if demand <= 0.0 else delta2 / demand

    # Exact recursive-majority identities used in the report.
    h_true = 4.0 * (mu - 1.0)
    residual_true = C_SHAPE * (mu - 1.0) - h_true
    assert c >= 0.5 - 1e-12
    assert residual_true > 0.0
    assert delta2 >= -1e-12
    return depth, n, mu, c, hmax, demand, delta2, ratio, alpha, beta


def main() -> None:
    print("RM3_LOWLEVEL_PROJECTION_DIAGNOSTIC")
    print(f"C_shape={C_SHAPE:.14f}")
    print("m N I c Hmax demand Delta2 ratio alpha beta")
    rows = []
    for m in DEPTHS:
        out = row(m)
        rows.append(out)
        m, n, mu, c, hmax, demand, delta2, ratio, alpha, beta = out
        ratio_s = "NA" if ratio is None else f"{ratio:.12g}"
        print(
            f"{m} {n} {mu:.12g} {c:.12g} {hmax:.12g} {demand:.12g} "
            f"{delta2:.12g} {ratio_s} {alpha:.12g} {beta:.12g}"
        )

    positive = [r for r in rows if r[7] is not None and r[0] >= 5]
    ratios = [r[7] for r in positive]
    assert all(ratios[i + 1] < ratios[i] for i in range(len(ratios) - 1))
    assert ratios[-1] < 3.1e-4
    print("PASS")


if __name__ == "__main__":
    main()
