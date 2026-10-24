#!/usr/bin/env python3
"""Exact finite sanity checks for D0067 run 7.

The report proves the all-m prefix arguments analytically.  This script checks
representative exact integer geometry for the new delayed-first-contact family
W_m and verifies prefix incompatibility with the previously archived U/V/T
families through m,k <= 30 and all D4 orientations.
"""


def U(k):
    pts = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 2)]
    pts.extend((x, 2) for x in range(1, k + 1))
    pts.append((k, 3))
    return pts


def V(k):
    pts = [(0, 0), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    pts.extend((x, 0) for x in range(-2, -(k + 1) - 1, -1))
    pts.append((-(k + 1), 1))
    return pts


def T(k):
    pts = [(0, 0)]
    pts.extend((x, 0) for x in range(1, k + 1))
    pts.append((k, 1))
    pts.extend((x, 1) for x in range(k - 1, -1, -1))
    pts.extend([(-1, 1), (-1, 0), (-1, -1), (0, -1)])
    return pts


def W(m):
    # First extra neighbour of the root is (0,1), reached only at the final step.
    pts = [(0, 0)]
    pts.extend((x, 0) for x in range(1, m + 1))
    pts.extend([(m, 1), (m, 2)])
    pts.extend((x, 2) for x in range(m - 1, -1, -1))
    pts.append((0, 1))
    return pts


def d4_maps():
    maps = []
    seen = set()
    for reflect in (False, True):
        for rotations in range(4):
            def f(p, reflect=reflect, rotations=rotations):
                x, y = p
                if reflect:
                    x = -x
                for _ in range(rotations):
                    x, y = -y, x
                return (x, y)
            key = (f((1, 0)), f((0, 1)))
            if key not in seen:
                seen.add(key)
                maps.append(f)
    assert len(maps) == 8
    return maps


def transform(path, f):
    return [f(p) for p in path]


def is_saw(path):
    return (
        len(path) == len(set(path))
        and all(
            abs(path[i + 1][0] - path[i][0])
            + abs(path[i + 1][1] - path[i][1])
            == 1
            for i in range(len(path) - 1)
        )
    )


def is_prefix(a, b):
    return len(a) <= len(b) and a == b[: len(a)]


def extra_root_contact_times(path):
    first = path[1]
    extras = {(1, 0), (-1, 0), (0, 1), (0, -1)} - {first}
    return [i for i, p in enumerate(path) if i > 0 and p in extras]


G = d4_maps()

# Local exact geometry of W_m.
for m in range(1, 31):
    path = W(m)
    assert is_saw(path)
    assert len(path) - 1 == 2 * m + 3
    assert extra_root_contact_times(path) == [len(path) - 1]
    # Westward escape ray starts free at the final vertex (0,1).
    occupied = set(path)
    for j in range(1, 31):
        assert (-j, 1) not in occupied

# Exact D4 prefix checks against the earlier three families.
new = []
old = []
for m in range(1, 31):
    for gi, g in enumerate(G):
        new.append((m, gi, transform(W(m), g)))
for k in range(1, 31):
    for name, family in (("U", U), ("V", V), ("T", T)):
        for gi, g in enumerate(G):
            old.append((name, k, gi, transform(family(k), g)))

for i, (_, _, p) in enumerate(new):
    for _, _, q in new[i + 1 :]:
        assert not is_prefix(p, q)
        assert not is_prefix(q, p)
    for _, _, _, q in old:
        assert not is_prefix(p, q)
        assert not is_prefix(q, p)

print("PASS")
print(f"checked_W_oriented={len(new)}")
print(f"checked_old_oriented={len(old)}")
print("W_m length=2m+3; first extra root contact occurs exactly at the final step")
print("all checked W_m D4 images are prefix-incompatible with each other and U/V/T")
