from fractions import Fraction
from itertools import product


def blocks(m):
    return [tuple(i for i in range(m) if (mask >> i) & 1) for mask in range(1 << m)]


def crossing(E, m, A):
    groups = {}
    for x in range(1 << m):
        z = tuple((x >> i) & 1 for i in A)
        hit, total = groups.get(z, (0, 0))
        groups[z] = (hit + (1 if x in E else 0), total + 1)
    c = Fraction(0)
    for hit, total in groups.values():
        u = Fraction(hit, total)
        if 2*u > 1:
            c += Fraction(total, 1 << m) * (2*u - 1)
    return Fraction(len(E), 1 << m), c


def envelope(t, p):
    if p == 0:
        return Fraction(0)
    if p <= Fraction(1, 2 ** (t + 1)):
        return Fraction(0)
    if p < Fraction(1, 2 ** t):
        return 2*p - Fraction(1, 2 ** t)
    return p


env_checks = env_equalities = env_violations = 0
max_gap = Fraction(0)
for m in range(1, 5):
    for mask in range(1 << (1 << m)):
        E = {x for x in range(1 << m) if (mask >> x) & 1}
        p = Fraction(len(E), 1 << m)
        if p > Fraction(1, 2):
            continue
        for A in blocks(m):
            p0, c = crossing(E, m, A)
            b = envelope(len(A), p0)
            env_checks += 1
            env_equalities += (c == b)
            env_violations += (c > b)
            max_gap = max(max_gap, b-c)


def coordinate_subcubes(m):
    for pat in product([None, 0, 1], repeat=m):
        F = tuple(i for i, v in enumerate(pat) if v is not None)
        Q = {x for x in range(1 << m)
             if all(v is None or ((x >> i) & 1) == v for i, v in enumerate(pat))}
        yield pat, F, Q


near_checks = near_equalities = near_violations = 0
for m in range(1, 4):
    cubes = list(coordinate_subcubes(m))
    for mask in range(1 << (1 << m)):
        E = {x for x in range(1 << m) if (mask >> x) & 1}
        p = Fraction(len(E), 1 << m)
        for _, F, Q in cubes:
            delta = Fraction(len(E.symmetric_difference(Q)), 1 << m)
            _, c = crossing(E, m, F)
            b = max(Fraction(0), p-delta)
            near_checks += 1
            near_equalities += (c == b)
            near_violations += (c < b)

print("crossing_envelope",
      "checks", env_checks,
      "violations", env_violations,
      "equalities", env_equalities,
      "max_gap", max_gap)
print("near_subcube_crossing",
      "checks", near_checks,
      "violations", near_violations,
      "equalities", near_equalities)
assert env_violations == 0
assert near_violations == 0
