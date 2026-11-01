"""Exact-rational checks for NEGATIVE_RHO_NEXT.md.

This is a deterministic finite-grid check, not a random-network simulation or
a proof of positive-time moving-corner phase selection.
"""

from fractions import Fraction as F
from itertools import product


def ceil_positive(x):
    assert x > 0
    return (x.numerator + x.denominator - 1) // x.denominator


def step(v, z, a, residual, gamma):
    x, y = v
    p, q = residual
    gate1, gate2 = x > 0, y > 0
    return (
        x + gamma * z * (p * gate1 - a * q * gate2),
        y + gamma * z * (-a * p * gate1 + q * gate2),
    )


def sector(v):
    return (v[0] > 0, v[1] > 0)


def frozen_positive_expected(v, w, a, residual, gamma):
    x, y = v
    p, q = residual
    if x <= 0 and y <= 0:
        return (False, False), 0
    if x > 0 and y <= 0:
        return (True, False), 0
    if x <= 0 and y > 0:
        return (False, True), 0
    if p < a * q:
        return (False, True), ceil_positive(x / (gamma * w * (a * q - p)))
    if q < a * p:
        return (True, False), ceil_positive(y / (gamma * w * (a * p - q)))
    return (True, True), 0


def negative_death_bound(v, w, a, residual, gamma):
    p, q = residual
    lower1 = min(v[0], -gamma * w * p)
    lower2 = min(v[1], -gamma * w * q)
    delta = gamma * w * (1 - a) * min(p, q)
    ratio = (sum(v) - lower1 - lower2) / delta
    return ratio.numerator // ratio.denominator + 1, (lower1, lower2), delta


def run_grid():
    correlations = (F(1, 4), F(1, 2), F(3, 4))
    residual_values = (F(1, 2), F(1), F(3))
    gammas = (F(1, 3), F(1))
    magnitudes = (F(1, 2), F(2))
    marks = (F(-2), F(-1, 3), F(0), F(1, 2), F(2))
    cases = positive_exits = negative_deaths = 0
    largest_death_bound = 0

    for a, p, q, gamma, w, x, y in product(
        correlations, residual_values, residual_values,
        gammas, magnitudes, marks, marks
    ):
        initial = (x, y)
        residual = (p, q)
        expected, entrance = frozen_positive_expected(
            initial, w, a, residual, gamma
        )
        v = initial
        for _ in range(entrance):
            v = step(v, w, a, residual, gamma)
        assert sector(v) == expected
        if expected == (False, False):
            assert v == initial
        for _ in range(8):
            v = step(v, w, a, residual, gamma)
            assert sector(v) == expected
        positive_exits += entrance > 0

        death_bound, lower, delta = negative_death_bound(
            initial, w, a, residual, gamma
        )
        v = initial
        for _ in range(death_bound):
            previous = v
            v = step(v, -w, a, residual, gamma)
            assert v[0] >= lower[0] and v[1] >= lower[1]
            if any(sector(previous)):
                assert sum(previous) - sum(v) >= delta
            else:
                assert v == previous
        assert sector(v) == (False, False)
        assert step(v, -w, a, residual, gamma) == v
        assert step(initial, -w, a, residual, gamma) == step(
            initial, w, a, (-p, -q), gamma
        )
        negative_deaths += 1
        largest_death_bound = max(largest_death_bound, death_bound)
        cases += 1

    return cases, positive_exits, negative_deaths, largest_death_bound


def check_corner():
    a, gamma = F(1, 2), F(1)
    v = (F(2), F(-2))
    original_invariant = v[1] + a * v[0]
    for changing_z, changing_r1 in (
        (F(1), F(1)), (F(1, 2), F(3, 4)), (F(2), F(-1, 4))
    ):
        assert sector(v) == (True, False)
        v = step(v, changing_z, a, (changing_r1, F(5)), gamma)
        assert v[1] + a * v[0] == original_invariant
    assert original_invariant == F(-1)

    survivor = (F(7, 10), F(-9, 20))
    dead = (F(9, 10), F(-11, 20))
    assert survivor[1] + a * survivor[0] == F(-1, 10)
    assert dead[1] + a * dead[0] == F(-1, 10)
    survivor_next = step(survivor, F(1), a, (F(-1), F(1)), gamma)
    dead_next = step(dead, F(1), a, (F(-1), F(1)), gamma)
    assert survivor_next == (F(-3, 10), F(1, 20))
    assert dead_next == (F(-1, 10), F(-1, 20))
    assert sector(survivor_next) == (False, True)
    assert sector(dead_next) == (False, False)

    reactivation = [(F(9, 10), F(-1, 10))]
    for _ in range(3):
        reactivation.append(step(reactivation[-1], F(-1), a, (F(1), F(1)), gamma))
    assert reactivation == [
        (F(9, 10), F(-1, 10)),
        (F(-1, 10), F(2, 5)),
        (F(2, 5), F(-3, 5)),
        (F(-3, 5), F(-1, 10)),
    ]
    return survivor_next, dead_next, reactivation


if __name__ == "__main__":
    cases, exits, deaths, bound = run_grid()
    survivor, dead, reactivation = check_corner()
    print(f"exact-rational parameter/mark cases: {cases}")
    print(f"positive-z ++ exits checked: {exits}")
    print(f"negative-z finite deaths checked: {deaths}; largest lower-barrier bound: {bound}")
    print(f"equal-invariant overshoot landings: survivor={survivor}, dead={dead}")
    print(f"negative-z gate-reactivation path: {reactivation}")
    print("PASS: classifier, lower barriers, decreasing sum, sign mirror, invariant, and overshoot")
