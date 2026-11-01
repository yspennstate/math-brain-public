#!/usr/bin/env python3
"""Verify the signed U-collision cocycle and adaptive telescope on Boolean cubes."""

from functools import lru_cache
from fractions import Fraction
from itertools import product
from math import log2
import random

SEED = 0xB12A05803
TOL = 2e-10


@lru_cache(maxsize=None)
def fwht(values):
    a = [Fraction(x) for x in values]
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2 * step):
            for j in range(start, start + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return tuple(x / len(a) for x in a)


@lru_cache(maxsize=None)
def spectral_law(values):
    return tuple(c * c for c in fwht(values))


def upper_masses(p):
    z = list(p)
    n = len(p).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not (s & bit):
                z[s] += z[s | bit]
    return tuple(z)


@lru_cache(maxsize=None)
def u_value(values):
    p = spectral_law(values)
    pi = upper_masses(p)
    return sum(float(x) * log2(float(y / x))
               for x, y in zip(p, pi) if x)


@lru_cache(maxsize=None)
def influence(values):
    p = spectral_law(values)
    return sum(Fraction(s.bit_count()) * mass for s, mass in enumerate(p))


@lru_cache(maxsize=None)
def restrict(values, i, bit):
    n = len(values).bit_length() - 1
    return tuple(values[(z & ((1 << i) - 1)) | (bit << i) |
                        ((z >> i) << (i + 1))]
                 for z in range(1 << (n - 1)))


@lru_cache(maxsize=None)
def g_value(values):
    n = len(values).bit_length() - 1
    parent = u_value(values)
    return sum(parent - 0.5 * (u_value(restrict(values, i, 0)) +
                               u_value(restrict(values, i, 1)))
               for i in range(n))


def multiply(g, h):
    return tuple(x * y for x, y in zip(g, h))


def collision(g, h):
    return u_value(multiply(g, h)) - u_value(g) - u_value(h)


def local_collision_drift(g, h, i):
    return collision(g, h) - 0.5 * (
        collision(restrict(g, i, 0), restrict(h, i, 0)) +
        collision(restrict(g, i, 1), restrict(h, i, 1)))


def delta_u(values, i):
    return u_value(values) - 0.5 * (
        u_value(restrict(values, i, 0)) + u_value(restrict(values, i, 1)))


def adaptive_index(g, h):
    """A branch-data-dependent physical-coordinate choice."""
    n = len(g).bit_length() - 1
    score = sum((k + 1) * (x + 2 * y) for k, (x, y) in enumerate(zip(g, h)))
    return score % n


def adaptive_telescope(g, h):
    """Return sum of reach-weighted local drifts over a complete adaptive tree."""
    n = len(g).bit_length() - 1
    if n == 0:
        return 0.0, collision(g, h), 1
    i = adaptive_index(g, h)
    subtotal = local_collision_drift(g, h, i)
    left, left_terminal, left_nodes = adaptive_telescope(
        restrict(g, i, 0), restrict(h, i, 0))
    right, right_terminal, right_nodes = adaptive_telescope(
        restrict(g, i, 1), restrict(h, i, 1))
    return (subtotal + 0.5 * (left + right),
            0.5 * (left_terminal + right_terminal),
            1 + left_nodes + right_nodes)


def defect(values, a, b):
    return g_value(values) - a * float(influence(values)) - b * u_value(values)


def residual(g, h, a, b):
    f = multiply(g, h)
    laplacian = sum(local_collision_drift(g, h, i)
                    for i in range(len(g).bit_length() - 1))
    return (laplacian
            - a * float(influence(f) - influence(g) - influence(h))
            - b * collision(g, h))


def joint_pivotal(g, h):
    n = len(g).bit_length() - 1
    total = Fraction(0)
    for i in range(n):
        both = sum(g[x] != g[x ^ (1 << i)] and
                   h[x] != h[x ^ (1 << i)] for x in range(1 << n))
        total += Fraction(both, 1 << n)
    return total


def all_boolean_functions(n):
    return list(product((-1, 1), repeat=1 << n))


def main():
    exhaustive_pairs = 0
    cocycle_checks = 0
    adaptive_checks = 0
    max_cocycle_error = 0.0
    max_global_error = 0.0
    max_defect_error = 0.0
    max_telescope_error = 0.0
    min_collision = (float("inf"), None)
    max_collision = (-float("inf"), None)
    frozen_pairs = ((0.0, 0.0), (4.0, 0.5), (6.0, 0.25))

    for n in range(1, 4):
        functions = all_boolean_functions(n)
        for g in functions:
            for h in functions:
                f = multiply(g, h)
                c = collision(g, h)
                if c < min_collision[0]:
                    min_collision = (c, (n, g, h))
                if c > max_collision[0]:
                    max_collision = (c, (n, g, h))
                laplacian = 0.0
                for i in range(n):
                    lhs = delta_u(f, i) - delta_u(g, i) - delta_u(h, i)
                    rhs = local_collision_drift(g, h, i)
                    err = abs(lhs - rhs)
                    max_cocycle_error = max(max_cocycle_error, err)
                    assert err <= TOL
                    laplacian += rhs
                    cocycle_checks += 1
                global_err = abs(g_value(f) - g_value(g) - g_value(h) - laplacian)
                max_global_error = max(max_global_error, global_err)
                assert global_err <= TOL
                for a, b in frozen_pairs:
                    err = abs(defect(f, a, b) - defect(g, a, b) -
                              defect(h, a, b) - residual(g, h, a, b))
                    max_defect_error = max(max_defect_error, err)
                    assert err <= TOL
                telescoped, terminal, _ = adaptive_telescope(g, h)
                err = abs(c - (telescoped + terminal))
                max_telescope_error = max(max_telescope_error, err)
                assert err <= TOL
                assert abs(terminal) <= TOL  # complete restrictions are constants
                adaptive_checks += 1
                exhaustive_pairs += 1

    rng = random.Random(SEED)
    random_pairs = 2000
    maximum_dimension = 3
    maximum_tree_nodes = 0
    for _ in range(random_pairs):
        n = rng.randint(4, 8)
        g = tuple(rng.choice((-1, 1)) for _ in range(1 << n))
        h = tuple(rng.choice((-1, 1)) for _ in range(1 << n))
        c = collision(g, h)
        telescoped, terminal, nodes = adaptive_telescope(g, h)
        err = abs(c - (telescoped + terminal))
        max_telescope_error = max(max_telescope_error, err)
        assert err <= 5e-9
        assert abs(terminal) <= TOL
        maximum_dimension = max(maximum_dimension, n)
        maximum_tree_nodes = max(maximum_tree_nodes, nodes)

    # Exact sign-indefiniteness and failure of termwise product closure.
    witness_g = (-1, -1, -1, -1, -1, 1, 1, 1)
    witness_h = (-1, 1, 1, -1, -1, 1, 1, -1)  # character on bits 0,1
    witness_f = multiply(witness_g, witness_h)
    # C=(1/16)log_2((120^3*3^9)/2^25)>0, by an integer comparison.
    exact_numerator = 120 ** 3 * 3 ** 9
    exact_denominator = 2 ** 25
    assert exact_numerator > exact_denominator
    witness_c = collision(witness_g, witness_h)
    assert witness_c > 0
    assert all(abs(collision(restrict(witness_g, i, bit),
                                 restrict(witness_h, i, bit))) <= TOL
               for i in range(3) for bit in (0, 1))
    witness_lc = sum(local_collision_drift(witness_g, witness_h, i)
                     for i in range(3))
    assert abs(witness_lc - 3 * witness_c) <= TOL
    witness_j = joint_pivotal(witness_g, witness_h)
    assert witness_j == Fraction(1, 2)
    assert (influence(witness_f) - influence(witness_g) - influence(witness_h)
            == -2 * witness_j)
    # R_{a,b}=(3-b)C+a for this witness, positive for every a>=0,b<1.
    for a, b in frozen_pairs:
        assert abs(residual(witness_g, witness_h, a, b) -
                   ((3 - b) * witness_c + a)) <= TOL
        assert residual(witness_g, witness_h, a, b) > 0

    # Negative collision is immediate from g*h=1 when h=g and U(g)>0.
    assert collision(witness_g, witness_g) == -2 * u_value(witness_g) < 0

    min_c, min_witness = min_collision
    max_c, max_witness = max_collision
    print("STATUS PASS")
    print(f"seed={SEED}")
    print(f"exhaustive_pairs={exhaustive_pairs}")
    print(f"cocycle_checks={cocycle_checks}")
    print(f"adaptive_checks={adaptive_checks}")
    print(f"random_pairs={random_pairs}")
    print(f"maximum_dimension={maximum_dimension}")
    print(f"maximum_tree_nodes={maximum_tree_nodes}")
    print(f"max_cocycle_error={max_cocycle_error:.17g}")
    print(f"max_global_error={max_global_error:.17g}")
    print(f"max_defect_error={max_defect_error:.17g}")
    print(f"max_telescope_error={max_telescope_error:.17g}")
    print(f"minimum_collision={min_c:.17g}")
    print(f"minimum_collision_witness={min_witness}")
    print(f"maximum_collision={max_c:.17g}")
    print(f"maximum_collision_witness={max_witness}")
    print(f"certified_positive_collision={witness_c:.17g}")
    print(f"positive_sign_integer_test={exact_numerator}>{exact_denominator}")
    print(f"positive_witness_collision_laplacian={witness_lc:.17g}")
    print(f"positive_witness_joint_pivotal={witness_j}")
    print("termwise_product_residual_for_witness=(3-b)C+a>0_for_all_a>=0,b<1")
    print("collision_sign_definite=NO")
    print("universal_GU=OPEN")


if __name__ == "__main__":
    main()
