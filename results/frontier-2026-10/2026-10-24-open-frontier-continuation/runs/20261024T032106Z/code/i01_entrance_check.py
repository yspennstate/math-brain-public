"""Exact-rational checks for the same-sign frozen strict-gate classifier.

This is a finite-grid check of the deterministic theorem in agents/i01_entrance.md.
It uses Fraction throughout the dynamics and finite-step bounds. It makes no
claim about an infinite Poisson population or macroscopic network matching.
"""

from fractions import Fraction as F
from itertools import product


def positive(value):
    return value > 0


def step(v, z, residual, rho, gamma):
    x, y = v
    r1, r2 = residual
    g1, g2 = positive(x), positive(y)
    return (
        x + gamma * z * (r1 * g1 + rho * r2 * g2),
        y + gamma * z * (rho * r1 * g1 + r2 * g2),
    )


def ceil_nonnegative(value):
    assert value >= 0
    return (value.numerator + value.denominator - 1) // value.denominator


def growing_bound(v, w, residual, rho, gamma):
    assert w > 0 and all(r > 0 for r in residual)
    bounds = []
    for j in range(2):
        if v[j] > 0:
            bounds.append(0)
        else:
            delta = gamma * w * min(residual[j], rho * residual[1 - j])
            bounds.append((-v[j] // delta) + 1)
    return max(bounds)


def dying_bound(v, w, residual, gamma):
    assert w > 0 and all(r > 0 for r in residual)
    return max(
        ceil_nonnegative(max(v[j], F(0)) / (gamma * w * residual[j]))
        for j in range(2)
    )


def trajectory(v, z, residual, rho, gamma, length):
    result = [v]
    for _ in range(length):
        result.append(step(result[-1], z, residual, rho, gamma))
    return result


def check():
    rhos = (F(1, 4), F(1, 2), F(3, 4))
    gammas = (F(1, 3), F(1), F(5, 2))
    magnitudes = (F(1, 2), F(1), F(2))
    residuals = ((F(1), F(1)), (F(1), F(3)),
                 (F(3), F(1)), (F(1, 2), F(2)))
    coordinates = (F(-2), F(-1, 3), F(0), F(1, 2), F(2))

    cases = 0
    growing_survivors = 0
    initially_dead = 0
    dying_cases = 0
    exact_axis_terminal = 0
    max_bound = 0

    for rho, gamma, w, residual, x, y in product(
        rhos, gammas, magnitudes, residuals, coordinates, coordinates
    ):
        v0 = (x, y)
        cases += 1

        # Positive z with positive residual: both projections increase while
        # at least one gate is on. The negative-residual/negative-z mirror has
        # literally the same exact trajectory, not merely the same selector.
        grow_N = growing_bound(v0, w, residual, rho, gamma) if any(
            positive(t) for t in v0
        ) else 0
        grow = trajectory(v0, w, residual, rho, gamma, grow_N + 12)
        mirrored_grow = trajectory(
            v0, -w, tuple(-r for r in residual), rho, gamma, grow_N + 12
        )
        assert grow == mirrored_grow
        if any(positive(t) for t in v0):
            growing_survivors += 1
            assert all(t > 0 for t in grow[grow_N])
            assert all(all(t > 0 for t in state) for state in grow[grow_N:])
            assert all(
                grow[n + 1][j] > grow[n][j]
                for n in range(grow_N + 12) for j in range(2)
            )
        else:
            initially_dead += 1
            assert all(state == v0 for state in grow)

        # Negative z with positive residual: every positive coordinate
        # decreases at a uniform rate until both strict gates are off.
        die_N = dying_bound(v0, w, residual, gamma)
        dying = trajectory(v0, -w, residual, rho, gamma, die_N + 12)
        mirrored_dying = trajectory(
            v0, w, tuple(-r for r in residual), rho, gamma, die_N + 12
        )
        dying_cases += 1
        assert dying == mirrored_dying
        assert all(t <= 0 for t in dying[die_N])
        assert all(state == dying[die_N] for state in dying[die_N:])
        assert all(
            dying[n + 1][j] <= dying[n][j]
            for n in range(die_N + 12) for j in range(2)
        )
        exact_axis_terminal += any(t == 0 for t in dying[die_N])
        max_bound = max(max_bound, grow_N, die_N)

    rho, gamma, w, residual = F(1, 2), F(1), F(1), (F(1), F(1))
    axis_history = trajectory((F(1), F(-1)), w, residual, rho, gamma, 3)
    assert axis_history == [
        (F(1), F(-1)), (F(2), F(-1, 2)),
        (F(3), F(0)), (F(4), F(1, 2)),
    ]
    assert trajectory((F(1), F(1)), -w, residual, rho, gamma, 1)[1] == (
        F(-1, 2), F(-1, 2)
    )

    print(f"exact-rational parameter/mark cases: {cases}")
    print(f"growing survivors: {growing_survivors}; initially dead: {initially_dead}")
    print(f"dying cases: {dying_cases}; exact-axis terminal cases: {exact_axis_terminal}")
    print(f"largest proved finite-step bound used: {max_bound}")
    print(f"strict-gate axis history: {axis_history}")
    print("all finite bounds, absorption, persistence, monotonicity, and sign mirrors passed")


if __name__ == "__main__":
    check()
