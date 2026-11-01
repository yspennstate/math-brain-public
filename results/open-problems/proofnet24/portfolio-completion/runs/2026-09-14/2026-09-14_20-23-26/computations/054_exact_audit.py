#!/usr/bin/env python3
"""Independent exact checks supporting agents/054.md.

These finite checks do not prove the random-matrix theorem. They check the
algebraic identities and the conditioning/stopping bookkeeping used in its
written analytic proof. No third-party Python packages are required.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def recurrences():
    c, cap, ell, s, d = Q(1, 7), Q(5, 3), Q(2, 5), Q(2, 17), Q(3)
    initial = (Q(173), Q(11), Q(5))
    mass, medium, bad = initial
    for j in range(13):
        expected_medium = (initial[1] / initial[0]**2 * d
                           * (cap / c**2)**j * ell**(-4*j) * d**j)
        expected_bad = (initial[2] / initial[0]**2
                        * (cap / c**2)**j * ell**(-4*j) * s**(-j-1))
        assert d * medium / mass**2 == expected_medium
        assert bad / (s * mass**2) == expected_bad
        mass *= c * ell * s
        medium *= cap * ell**(-2) * d * s**2
        bad *= cap * ell**(-2) * s

    mass, bad = initial[0], initial[2]
    for j in range(13):
        assert bad / (s * mass**2) == (
            initial[2] / initial[0]**2 * (cap / c**2)**j * s**(-j-1))
        mass *= c * s
        bad *= cap * s
    # At the last pre-success index j=k-1, the exponent of 1/s is exactly k.
    for k in (1, 2, 3, 11, 101):
        assert (k - 1) + 1 == k
        assert k + 1 > k  # the unnecessary post-success invariant costs more
    print("PASS: two- and three-tier exact normalized recurrences, j=0,...,12")


def overlap_counts():
    cases = 0
    for m in range(2, 8):
        for n0 in range(m + 1, m + 4):
            first = frozenset(range(m - 1))
            empirical = Counter(
                m - len(first.intersection(second))
                for second in combinations(range(n0), m - 1)
            )
            predicted = {}
            for D in range(1, m + 1):
                j = D - 1
                predicted[D] = (comb(m - 1, j) * comb(n0 - m + 1, j)
                                if j <= n0 - m + 1 else 0)
            assert all(empirical[D] == predicted[D] for D in predicted)
            assert sum(empirical.values()) == comb(n0, m - 1)
            assert empirical[1] == 1  # the diagonal, excluded from graph edges
            cases += 1
    print(f"PASS: exact overlap-stratum formula in {cases} finite cases")


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), Q(0))


def mv(P, x):
    return [dot(row, x) for row in P]


def remove_row(P, x):
    z = mv(P, x)
    denom = dot(z, z)
    assert denom > 0
    return [[P[i][j] - z[i] * z[j] / denom
             for j in range(len(P))] for i in range(len(P))]


def projector_identity():
    ambient = 6
    P = [[Q(i == j) for j in range(ambient)] for i in range(ambient)]
    shared = [(0, 1, 1, 0, 0, 0), (0, 0, 0, 1, 1, 0)]
    private = [(1, 2, -1, 1, -1, 1),
               (2, -1, 2, -1, 1, 3),
               (1, 3, 0, 2, -1, -2)]
    for row in shared:
        P = remove_row(P, list(map(Q, row)))
    v = [Q(1)] + [Q(0)] * (ambient - 1)
    assert mv(P, v) == v
    product = Q(1)
    losses = []
    for row in private:
        x = list(map(Q, row))
        pv, px = mv(P, v), mv(P, x)
        previous_length = dot(pv, pv)
        loss = dot(pv, x)**2 / (previous_length * dot(px, px))
        assert 0 <= loss <= 1
        P = remove_row(P, x)
        after = dot(mv(P, v), mv(P, v))
        assert after == previous_length * (1 - loss)
        product *= 1 - loss
        losses.append(loss)
    assert sum(P[i][i] for i in range(ambient)) == 1
    assert product == dot(v, mv(P, v))
    assert 0 < product < 1
    print("PASS: exact sequential residual-projector product identity")
    print("  angular losses:", ", ".join(map(str, losses)))
    print("  final squared overlap:", product)


def adapted_scan():
    lower = Q(1, 5)
    tilt = Q(1, 2)
    horizon = 9
    for target in (1, 3, 5):
        paths = {(): Q(1)}
        for _ in range(horizon):
            following = {}
            for history, weight in paths.items():
                if sum(history) >= target:
                    probability = Q(1)  # forced bookkeeping after stopping
                else:
                    # Deliberately depends on the entire observed history.
                    tag = (sum((i + 1) * x for i, x in enumerate(history))
                           + len(history)) % 5
                    probability = lower + (1 - lower) * Q(tag, 5)
                assert lower <= probability <= 1
                for outcome, factor in ((0, 1 - probability), (1, probability)):
                    if factor:
                        following[history + (outcome,)] = weight * factor
            paths = following
        assert sum(paths.values()) == 1
        laplace = sum(weight * tilt**sum(history)
                      for history, weight in paths.items())
        failure = sum(weight for history, weight in paths.items()
                      if sum(history) < target)
        envelope = (1 - lower * (1 - tilt))**horizon
        assert laplace <= envelope
        assert failure <= tilt**(-target) * laplace
        print(f"PASS: adapted stopped scan, R={horizon}, k={target}, p=1/5")
    print("All exact checks passed; analytic and source dependencies remain explicit.")


if __name__ == "__main__":
    recurrences()
    overlap_counts()
    projector_identity()
    adapted_scan()
