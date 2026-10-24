"""Independent exact-arithmetic checks of the forward filling recursion."""

from fractions import Fraction as F


def check(name, permutation, target, expected_residual):
    n = len(permutation)
    assert sorted(permutation) == list(range(n))
    assert sum(target) == n
    a = [F(1) for _ in range(n)]
    b = list(map(F, target))
    accepted = [F(0) for _ in range(n)]
    for step in range(40):
        m = [min(x, y) for x, y in zip(a, b)]
        accepted = [x + y for x, y in zip(accepted, m)]
        residual = [x - y for x, y in zip(a, m)]
        a_next = [F(0) for _ in range(n)]
        for i, j in enumerate(permutation):
            a_next[j] = residual[i]
        b = [x - y for x, y in zip(b, m)]
        a = a_next
        assert sum(a) == sum(b)
        assert [x + y for x, y in zip(accepted, b)] == list(map(F, target))
    mass = sum(a) / n
    assert mass == F(expected_residual)
    print(name, "residual_mass=", mass, "accepted_law=", [x / n for x in accepted])


check("one_orbit_with_zeros", [1, 2, 3, 0], [0, 0, 2, 2], 0)
check("two_balanced_orbits", [1, 0, 3, 2], [0, 2, 0, 2], 0)
check("two_unbalanced_orbits", [1, 0, 3, 2], [2, 2, 0, 0], F(1, 2))
