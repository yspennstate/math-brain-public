#!/usr/bin/env python3
"""Deterministic controls for the B12 uniform coherent-kernel envelope.

The all-real inequalities are proved analytically in UNIFORM_KERNEL_PAYMENT.tex.
This script checks a high-precision scalar mesh, all Boolean outer branch pairs
on two variables against all Boolean children through three variables, and the
previous genuine fixed-bias collision family.  No randomness is used.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product
import math

getcontext().prec = 70
D = Decimal


def dF(x):
    x = abs(D(x))
    return x * x * x.ln() if x else D(0)


def dk(r):
    r = abs(D(r))
    return dF(r + 1) + dF(abs(r - 1)) - 2 * dF(r)


def psi(x):
    x = float(x)
    z = x * x
    return z * math.log(1.0 / z) if z else 0.0


def k(r):
    r = abs(float(r))
    def F(x):
        return x * x * math.log(x) if x else 0.0
    return F(r + 1.0) + F(abs(r - 1.0)) - 2.0 * F(r)


def fwht(values):
    a = list(values)
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2 * step):
            for j in range(start, start + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return a


def hats(values):
    n = len(values)
    return [Fraction(x, n) for x in fwht(values)]


def scalar_mesh():
    points = {D(0), D("0.5"), D(1), D(2)}
    for exponent in range(-15, 16):
        for numerator in range(1, 41):
            points.add((D(10) ** exponent) * D(numerator) / 40)
    points = sorted(points)
    max_upper = (D("-Infinity"), None)
    max_lower = (D("-Infinity"), None)
    max_drop = (D("-Infinity"), None)
    previous = None
    for x in points:
        upper = dk(x) - (2 * (1 + x).ln() + 3)
        lower = (2 * (1 + x).ln() - 1) - dk(x)
        max_upper = max(max_upper, (upper, x))
        max_lower = max(max_lower, (lower, x))
        if previous is not None:
            max_drop = max(max_drop, (dk(previous) - dk(x), previous, x))
        previous = x
    assert max_upper[0] <= D("1e-45")
    assert max_lower[0] <= D("1e-45")
    assert max_drop[0] <= D("1e-25")

    # Deterministic cross-scale pairs for the difference inequality.
    pair_points = [D(0)]
    for exponent in range(-12, 13):
        for mantissa in (D("0.1"), D("0.3"), D(1), D(3), D(9)):
            pair_points.append(mantissa * (D(10) ** exponent))
    worst = (D("-Infinity"), None)
    for r in pair_points:
        for s in pair_points:
            value = dk(r) - dk(s) - 4 - 2 * (1 + abs(r - s)).ln()
            worst = max(worst, (value, r, s))
    assert worst[0] <= D("1e-45")
    return len(points), max_upper, max_lower, max_drop, len(pair_points) ** 2, worst


def remainder_and_envelope(a_hat, b_hat, mu, alpha, c=1.0):
    beta = abs(float(alpha))
    if beta == 0.0:
        return 0.0, 0.0, 0.0, 0.0
    s = float(mu) / beta
    remainder = 0.0
    near = 0.0
    near_bound = 0.0
    separated_slack_min = float("inf")
    q = 0.0
    reserve = 0.0
    for a, b in zip(a_hat, b_hat):
        if not b:
            continue
        af, bf = float(a), float(b)
        q += bf * bf
        r = (af / bf + float(mu)) / beta
        contribution = beta * beta * bf * bf * (k(r) - k(s))
        remainder += contribution
        scalar_bound = beta * beta * bf * bf * (
            4.0 + 2.0 * math.log1p(abs(af) / (beta * abs(bf)))
        )
        separated_slack_min = min(separated_slack_min, scalar_bound - contribution)
        if abs(af + float(mu) * bf) <= c * beta * abs(bf) + 1e-15:
            near += contribution
            near_bound += beta * beta * bf * bf * (k(c) - k(abs(s)))
        ratio = abs(af / bf)
        if ratio > 1.0:
            reserve += 2.0 * bf * bf * math.log(ratio)
    envelope = q * psi(beta) + (4.0 + 2.0 * math.log(2.0)) * q * beta * beta + reserve * beta * beta
    return remainder, envelope, near_bound - near, separated_slack_min


def boolean_splice_controls():
    branches = list(product((-1, 1), repeat=4))
    outer_pairs = []
    for plus in branches:
        for minus in branches:
            a_values = [Fraction(x + y, 2) for x, y in zip(plus, minus)]
            b_values = [Fraction(x - y, 2) for x, y in zip(plus, minus)]
            outer_pairs.append((hats(a_values), hats(b_values)))

    cases = 0
    min_envelope_slack = float("inf")
    min_near_slack = float("inf")
    min_separated_slack = float("inf")
    for n in range(1, 4):
        size = 1 << n
        for child in product((-1, 1), repeat=size):
            child_hat = hats(child)
            mu = child_hat[0]
            for coordinate in range(n):
                alpha = child_hat[1 << coordinate]
                for a_hat, b_hat in outer_pairs:
                    remainder, envelope, near_slack, separated_slack = remainder_and_envelope(
                        a_hat, b_hat, mu, alpha
                    )
                    min_envelope_slack = min(min_envelope_slack, envelope - remainder)
                    min_near_slack = min(min_near_slack, near_slack)
                    min_separated_slack = min(min_separated_slack, separated_slack)
                    cases += 1
    assert min_envelope_slack > -2e-13
    assert min_near_slack > -2e-13
    assert min_separated_slack > -2e-13
    return cases, min_envelope_slack, min_near_slack, min_separated_slack


def collision_family():
    a_hat = [Fraction(-1, 2), Fraction(-1, 4), Fraction(-1, 4), 0,
             Fraction(-1, 4), 0, 0, Fraction(1, 4)]
    b_hat = [Fraction(-1, 4), 0, 0, Fraction(1, 4),
             0, Fraction(1, 4), Fraction(1, 4), Fraction(-1, 2)]
    rows = []
    for n in range(4, 17):
        alpha = Fraction(-4, 1 << n)
        remainder, envelope, near_slack, separated_slack = remainder_and_envelope(
            a_hat, b_hat, Fraction(1, 2), alpha
        )
        assert remainder <= envelope + 1e-13
        assert near_slack >= -1e-13
        assert separated_slack >= -1e-13
        rows.append((n, alpha, remainder, envelope, near_slack))
    return rows


def main():
    print("seed=none; all meshes and Boolean enumerations are deterministic")
    points, upper, lower, drop, pairs, pair_worst = scalar_mesh()
    print(f"scalar_mesh_points={points}")
    print(f"max_upper_bound_violation={upper}")
    print(f"max_lower_bound_violation={lower}")
    print(f"max_monotonicity_drop={drop}")
    print(f"difference_pairs={pairs} worst_difference_violation={pair_worst}")
    print("scalar_kernel_controls=PASS")
    cases, envelope_slack, near_slack, separated_slack = boolean_splice_controls()
    print(f"actual_boolean_splice_cases={cases}")
    print(f"minimum_complete_envelope_slack={envelope_slack:.17g}")
    print(f"minimum_signed_near_slack={near_slack:.17g}")
    print(f"minimum_separated_scalar_slack={separated_slack:.17g}")
    print("boolean_splice_controls=PASS")
    for n, alpha, remainder, envelope, near_slack in collision_family():
        print(
            f"collision_n={n} mu=1/2 alpha={alpha} R={remainder:.17g} "
            f"envelope={envelope:.17g} near_slack={near_slack:.17g}"
        )
    print("collision_refund_controls=PASS")
    print("analytic_hierarchy_constant_without_reserve=4+2ln2+2/e="
          f"{4 + 2 * math.log(2) + 2 / math.e:.16f}")
    print("scope=finite controls only; universal inequalities are proved in UNIFORM_KERNEL_PAYMENT.tex")


if __name__ == "__main__":
    main()

