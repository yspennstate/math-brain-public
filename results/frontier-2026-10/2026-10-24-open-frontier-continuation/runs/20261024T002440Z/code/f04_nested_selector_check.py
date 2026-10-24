"""Supplementary randomized check of mixed-cone selectors and nested grids.

The proof is the ceiling inequality in reviews/MARGINAL_LAW_REVIEW.md.
This script is only a reproducible finite-sample consistency check.
"""

import math
import random
from fractions import Fraction


RHO = -0.5
GAMMA_COARSE = 1.0
GAMMA_FINE = 0.1
TRIALS = 100_000
SEED = 20261024


def analytic_selector(z, x, y, r1, r2, gamma):
    k = -RHO
    if z > 0:
        if y > 0:
            return 2
        if x <= 0:
            return 0
        a = -z * r1
        n_x = math.ceil(x / (gamma * a))
        return 2 if y + gamma * k * a * n_x > 0 else 0
    if x > 0:
        return 1
    if y <= 0:
        return 0
    b_abs = -z * r2
    n_y = math.ceil(y / (gamma * b_abs))
    return 1 if x + gamma * k * b_abs * n_y > 0 else 0


def direct_selector(z, x, y, r1, r2, gamma):
    for _ in range(5_000):
        if x <= 0 and y <= 0:
            return 0
        if z > 0 and x <= 0 and y > 0:
            return 2
        if z < 0 and x > 0 and y <= 0:
            return 1
        gate1 = x > 0
        gate2 = y > 0
        x, y = (
            x + gamma * z * (r1 * gate1 + RHO * r2 * gate2),
            y + gamma * z * (RHO * r1 * gate1 + r2 * gate2),
        )
    raise AssertionError("terminal sector was not reached")


def central_exact():
    x = Fraction(14, 100)
    y = Fraction(-12, 100)
    rho = Fraction(-1, 2)
    coarse = (x - 1, y - rho)
    fine1 = (x - Fraction(1, 10), y - rho / 10)
    fine2 = (fine1[0] - Fraction(1, 10), fine1[1] - rho / 10)
    assert coarse == (Fraction(-86, 100), Fraction(38, 100))
    assert fine1 == (Fraction(4, 100), Fraction(-7, 100))
    assert fine2 == (Fraction(-6, 100), Fraction(-2, 100))
    return coarse, fine1, fine2


def main():
    rng = random.Random(SEED)
    coarse_only = 0
    fine_only = 0
    for _ in range(TRIALS):
        z = rng.choice((-1.0, 1.0)) * 10 ** rng.uniform(-0.7, 0.5)
        x = rng.uniform(-2.0, 2.0)
        y = rng.uniform(-2.0, 2.0)
        r1 = -(10 ** rng.uniform(-0.3, 0.3))
        r2 = 10 ** rng.uniform(-0.3, 0.3)
        coarse = analytic_selector(z, x, y, r1, r2, GAMMA_COARSE)
        fine = analytic_selector(z, x, y, r1, r2, GAMMA_FINE)
        assert coarse == direct_selector(z, x, y, r1, r2, GAMMA_COARSE)
        assert fine == direct_selector(z, x, y, r1, r2, GAMMA_FINE)
        if fine and not coarse:
            fine_only += 1
        if coarse and not fine:
            coarse_only += 1
    assert fine_only == 0
    assert coarse_only > 0
    coarse, fine1, fine2 = central_exact()
    print(f"seed={SEED} trials={TRIALS} rho={RHO} gammas=({GAMMA_COARSE},{GAMMA_FINE})")
    print(f"analytic/direct selector mismatches=0")
    print(f"coarse-only escape={coarse_only}; fine-only escape={fine_only}")
    print(f"central coarse first={coarse}; fine first={fine1}; fine second={fine2}")
    mark = (0.14, -0.12)
    mid_escape = analytic_selector(1, *mark, -1, 1, 0.13)
    larger_dead = analytic_selector(1, *mark, -1, 1, 0.2)
    assert (mid_escape, larger_dead) == (2, 0)
    print("nonnested counterexample: gamma=0.13 escapes, gamma=0.2 dies")


if __name__ == "__main__":
    main()
