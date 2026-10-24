#!/usr/bin/env python3
"""Verify the grouped-root signed collision companion identity."""

from functools import lru_cache
from fractions import Fraction
from itertools import combinations, product
from math import log2
import random

SEED = 0xB12A05804
TOL = 4e-10


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
    return sum(Fraction(s.bit_count()) * mass
               for s, mass in enumerate(spectral_law(values)))


@lru_cache(maxsize=None)
def restrict_one(values, i, bit):
    n = len(values).bit_length() - 1
    return tuple(values[(z & ((1 << i) - 1)) | (bit << i) |
                        ((z >> i) << (i + 1))]
                 for z in range(1 << (n - 1)))


def restrict_many(values, coords, assignment):
    n = len(values).bit_length() - 1
    fixed = dict(zip(coords, assignment))
    free = [i for i in range(n) if i not in fixed]
    out = []
    for z in range(1 << len(free)):
        x = 0
        for i, bit in fixed.items():
            x |= bit << i
        for j, i in enumerate(free):
            x |= ((z >> j) & 1) << i
        out.append(values[x])
    return tuple(out)


def multiply(g, h):
    return tuple(x * y for x, y in zip(g, h))


@lru_cache(maxsize=None)
def collision(g, h):
    return u_value(multiply(g, h)) - u_value(g) - u_value(h)


@lru_cache(maxsize=None)
def g_value(values):
    n = len(values).bit_length() - 1
    return sum(u_value(values) - 0.5 * (
        u_value(restrict_one(values, i, 0)) +
        u_value(restrict_one(values, i, 1))) for i in range(n))


@lru_cache(maxsize=None)
def face_averages(g, h):
    """A_k: uniform average collision on all codimension-k faces."""
    n = len(g).bit_length() - 1
    ans = []
    for k in range(n + 1):
        total = 0.0
        count = 0
        for coords in combinations(range(n), k):
            for assignment in product((0, 1), repeat=k):
                total += collision(restrict_many(g, coords, assignment),
                                   restrict_many(h, coords, assignment))
                count += 1
        ans.append(total / count)
    return tuple(ans)


@lru_cache(maxsize=None)
def face_companion(g, h):
    n = len(g).bit_length() - 1
    if n == 0:
        return 0.0
    av = face_averages(g, h)
    return (n - 1) * av[0] - 2 * sum(av[1:n])


def expected_child_face_companion(g, h):
    n = len(g).bit_length() - 1
    if n == 0:
        return 0.0
    return sum(face_companion(restrict_one(g, i, bit),
                              restrict_one(h, i, bit))
               for i in range(n) for bit in (0, 1)) / (2 * n)


def collision_laplacian(g, h):
    n = len(g).bit_length() - 1
    c = collision(g, h)
    return sum(c - 0.5 * (
        collision(restrict_one(g, i, 0), restrict_one(h, i, 0)) +
        collision(restrict_one(g, i, 1), restrict_one(h, i, 1)))
               for i in range(n))


@lru_cache(maxsize=None)
def active_coords(g, h):
    n = len(g).bit_length() - 1
    return tuple(i for i in range(n)
                 if any(g[x] != g[x ^ (1 << i)] or
                        h[x] != h[x ^ (1 << i)]
                        for x in range(1 << n)))


def policy_coordinate(g, h):
    """Canonical branch-dependent policy: first currently active coordinate."""
    active = active_coords(g, h)
    return active[0] if active else None


@lru_cache(maxsize=None)
def policy_companion(g, h):
    """Cumulative all-coordinate surplus along the active physical policy."""
    i = policy_coordinate(g, h)
    if i is None:
        return 0.0
    child = 0.5 * (
        policy_companion(restrict_one(g, i, 0), restrict_one(h, i, 0)) +
        policy_companion(restrict_one(g, i, 1), restrict_one(h, i, 1)))
    return collision_laplacian(g, h) - collision(g, h) + child


def expected_policy_child(g, h):
    i = policy_coordinate(g, h)
    if i is None:
        return 0.0
    return 0.5 * (
        policy_companion(restrict_one(g, i, 0), restrict_one(h, i, 0)) +
        policy_companion(restrict_one(g, i, 1), restrict_one(h, i, 1)))


def add_dummy_coordinate(values):
    """Append one high-order coordinate on which the function is invariant."""
    return tuple(values) + tuple(values)


def joint_pivotal(g, h):
    n = len(g).bit_length() - 1
    total = Fraction(0)
    for i in range(n):
        count = sum(g[x] != g[x ^ (1 << i)] and
                    h[x] != h[x ^ (1 << i)] for x in range(1 << n))
        total += Fraction(count, 1 << n)
    return total


def defect(values, a, b):
    return g_value(values) - a * float(influence(values)) - b * u_value(values)


def main():
    exhaustive_pairs = 0
    identity_checks = 0
    max_identity_error = 0.0
    max_defect_error = 0.0
    min_p = (float("inf"), None)
    max_p = (-float("inf"), None)
    max_policy_error = 0.0
    max_dummy_error = 0.0
    frozen_pairs = ((0.0, 0.0), (4.0, 0.5), (6.0, 0.25))

    for n in range(1, 4):
        functions = list(product((-1, 1), repeat=1 << n))
        for g in functions:
            for h in functions:
                c = collision(g, h)
                face_p = face_companion(g, h)
                face_rp = expected_child_face_companion(g, h)
                lc = collision_laplacian(g, h)
                err = abs(lc - (c + face_p - face_rp))
                max_identity_error = max(max_identity_error, err)
                assert err <= TOL
                p = policy_companion(g, h)
                rp = expected_policy_child(g, h)
                policy_error = abs(lc - (c + p - rp))
                max_policy_error = max(max_policy_error, policy_error)
                assert policy_error <= TOL
                dummy_error = abs(p - policy_companion(
                    add_dummy_coordinate(g), add_dummy_coordinate(h)))
                max_dummy_error = max(max_dummy_error, dummy_error)
                assert dummy_error <= TOL
                if p < min_p[0]:
                    min_p = (p, (n, g, h))
                if p > max_p[0]:
                    max_p = (p, (n, g, h))
                f = multiply(g, h)
                j = float(joint_pivotal(g, h))
                for a, b in frozen_pairs:
                    raw = defect(f, a, b) - defect(g, a, b) - defect(h, a, b)
                    grouped = (1 - b) * c + 2 * a * j + p - rp
                    derr = abs(raw - grouped)
                    max_defect_error = max(max_defect_error, derr)
                    assert derr <= TOL
                assert abs(face_averages(g, h)[-1]) <= TOL
                exhaustive_pairs += 1
                identity_checks += 1

    rng = random.Random(SEED)
    random_pairs = 500
    maximum_dimension = 3
    for _ in range(random_pairs):
        n = rng.randint(4, 7)
        g = tuple(rng.choice((-1, 1)) for _ in range(1 << n))
        h = tuple(rng.choice((-1, 1)) for _ in range(1 << n))
        c = collision(g, h)
        face_p = face_companion(g, h)
        face_rp = expected_child_face_companion(g, h)
        lc = collision_laplacian(g, h)
        err = abs(lc - (c + face_p - face_rp))
        max_identity_error = max(max_identity_error, err)
        assert err <= 2e-8
        p = policy_companion(g, h)
        rp = expected_policy_child(g, h)
        policy_error = abs(lc - (c + p - rp))
        max_policy_error = max(max_policy_error, policy_error)
        assert policy_error <= 2e-8
        dummy_error = abs(p - policy_companion(
            add_dummy_coordinate(g), add_dummy_coordinate(h)))
        max_dummy_error = max(max_dummy_error, dummy_error)
        assert dummy_error <= 2e-8
        maximum_dimension = max(maximum_dimension, n)

    # Previous certified obstruction: the companion absorbs the multiplicity.
    witness_g = (-1, -1, -1, -1, -1, 1, 1, 1)
    witness_h = (-1, 1, 1, -1, -1, 1, 1, -1)
    wc = collision(witness_g, witness_h)
    wp = policy_companion(witness_g, witness_h)
    wrp = expected_policy_child(witness_g, witness_h)
    assert abs(wp - 2 * wc) <= TOL
    assert abs(wrp) <= TOL
    assert abs(collision_laplacian(witness_g, witness_h) - 3 * wc) <= TOL

    print("STATUS PASS")
    print(f"seed={SEED}")
    print(f"exhaustive_pairs={exhaustive_pairs}")
    print(f"identity_checks={identity_checks}")
    print(f"random_pairs={random_pairs}")
    print(f"maximum_dimension={maximum_dimension}")
    print(f"max_grouped_identity_error={max_identity_error:.17g}")
    print(f"max_policy_identity_error={max_policy_error:.17g}")
    print(f"max_grouped_defect_error={max_defect_error:.17g}")
    print(f"max_dummy_invariance_error={max_dummy_error:.17g}")
    print(f"minimum_companion={min_p[0]:.17g}")
    print(f"minimum_companion_witness={min_p[1]}")
    print(f"maximum_companion={max_p[0]:.17g}")
    print(f"maximum_companion_witness={max_p[1]}")
    print(f"prior_witness_C={wc:.17g}")
    print(f"prior_witness_P={wp:.17g}")
    print(f"prior_witness_expected_child_P={wrp:.17g}")
    print("companion_sign_definite=NO")
    print("universal_GU=OPEN")


if __name__ == "__main__":
    main()
