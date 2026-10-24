#!/usr/bin/env python3
"""Finite-support consistency checks for the PROB20-14 factorial-replication report.

This is NOT proof evidence for the universal infinite-variance theorem. It checks
exact combinatorial identities/inequalities on a finite critical offspring law and
numerically checks one Chernoff bound used in the report.
"""

from collections import defaultdict
from fractions import Fraction
from math import exp, factorial, log

LAW = {
    0: Fraction(11, 20),
    1: Fraction(1, 5),
    2: Fraction(3, 20),
    5: Fraction(1, 10),
}
assert sum(LAW.values()) == 1
assert sum(x * p for x, p in LAW.items()) == 1


def joint_sum_count(n, A):
    dp = {(0, 0): Fraction(1)}
    for _ in range(n):
        nxt = defaultdict(Fraction)
        for (s, c), prob in dp.items():
            for x, px in LAW.items():
                nxt[(s + x, c + int(x in A))] += prob * px
        dp = dict(nxt)
    return dp


def sum_law(n):
    dp = {0: Fraction(1)}
    for _ in range(n):
        nxt = defaultdict(Fraction)
        for s, prob in dp.items():
            for x, px in LAW.items():
                nxt[s + x] += prob * px
        dp = dict(nxt)
    return dp


def falling(z, m):
    out = 1
    for j in range(m):
        out *= z - j
    return out


def Lambda(t):
    return log(sum(float(p) * exp(-t * (x - 1)) for x, p in LAW.items()))


def H_grid(y, step=0.0005, tmax=4.0):
    # A lower bound on the exact Legendre supremum H(y), sufficient for a
    # numerical consistency check of the corresponding Chernoff upper bound.
    best = 0.0
    best_t = 0.0
    m = int(tmax / step)
    for i in range(m + 1):
        t = i * step
        value = t * y - Lambda(t)
        if value > best:
            best = value
            best_t = t
    return best, best_t


def main():
    n = 18
    A = {2, 5}
    d = 2
    m = 2

    joint = joint_sum_count(n, A)
    central = sum(prob for (s, c), prob in joint.items() if s == n - 1)
    assert central > 0
    cond_count = {
        c: prob / central
        for (s, c), prob in joint.items()
        if s == n - 1
    }
    mu = sum(Fraction(c) * prob for c, prob in cond_count.items())
    factorial_moment = sum(
        Fraction(falling(c, m)) * prob for c, prob in cond_count.items()
    )

    assert mu >= 2 * m
    jensen_lower = (mu - m + 1) ** m
    assert factorial_moment >= jensen_lower

    residual = sum_law(n - m)
    threshold = n - 1 - m * d
    residual_lower_tail = sum(
        prob for s, prob in residual.items() if s <= threshold
    )
    pA = sum(LAW[x] for x in A)
    n_falling_m = Fraction(factorial(n), factorial(n - m))
    replication_upper = (
        n_falling_m * (pA ** m) * residual_lower_tail / central
    )
    assert factorial_moment <= replication_upper

    # Singleton exact factorial identity: selected degree values have deterministic
    # total md, so the residual local atom is exact rather than only a lower-tail bound.
    A_single = {2}
    joint_single = joint_sum_count(n, A_single)
    central_single = sum(
        prob for (s, c), prob in joint_single.items() if s == n - 1
    )
    assert central_single == central
    cond_single = {
        c: prob / central_single
        for (s, c), prob in joint_single.items()
        if s == n - 1
    }
    factorial_single = sum(
        Fraction(falling(c, m)) * prob for c, prob in cond_single.items()
    )
    exact_residual_atom = residual.get(n - 1 - m * 2, Fraction(0))
    exact_formula = (
        n_falling_m * (LAW[2] ** m) * exact_residual_atom / central
    )
    assert factorial_single == exact_formula

    # Numerical Chernoff consistency.
    N = n - m
    xdef = 1 + m * (d - 1)
    y = xdef / N
    hgrid, tstar = H_grid(y)
    lower_tail_float = float(residual_lower_tail)
    chernoff_grid_upper = exp(-N * hgrid)
    assert lower_tail_float <= chernoff_grid_upper + 1e-14

    lam = -log(float(central))
    lhs = log(float(mu / (2 * n * pA)))
    rhs_grid = lam / m - (N / m) * hgrid
    assert lhs <= rhs_grid + 1e-12

    q = 1.5
    lambda_ratios = []
    for t in (0.2, 0.1, 0.05, 0.025):
        lambda_ratios.append((t, Lambda(t) / (t ** q)))

    print("critical_mean=1")
    print(f"n={n} A={sorted(A)} m={m} d={d}")
    print(f"central_atom={float(central):.15g}")
    print(f"conditional_mu_A={float(mu):.15g}")
    print(f"factorial_moment={float(factorial_moment):.15g}")
    print(f"jensen_lower={float(jensen_lower):.15g}")
    print(f"replication_upper={float(replication_upper):.15g}")
    print(f"singleton_factorial_identity={float(factorial_single):.15g}")
    print(f"H_grid={hgrid:.15g} at t={tstar:.6g}")
    print(f"residual_lower_tail={lower_tail_float:.15g}")
    print(f"chernoff_grid_upper={chernoff_grid_upper:.15g}")
    print(f"replication_log_lhs={lhs:.15g}")
    print(f"replication_log_rhs_grid={rhs_grid:.15g}")
    print("Lambda(t)/t^q samples:")
    for t, val in lambda_ratios:
        print(f"  t={t:.6g}: {val:.15g}")
    print("ALL_ASSERTIONS_PASSED")


if __name__ == "__main__":
    main()
