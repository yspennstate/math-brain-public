from itertools import product
from collections import Counter
from math import comb


def canon_sign(v):
    """Return canonical representative of {v,-v}: first nonzero entry positive."""
    for x in v:
        if x:
            return v if x > 0 else tuple(-y for y in v)
    raise ValueError("zero vector")


def primitive_subset_difference_normals(n):
    out = set()
    for v in product((-1, 0, 1), repeat=n):
        if 1 not in v or -1 not in v:
            continue
        out.add(canon_sign(v))
    return out


def orbit_type(v):
    a = sum(x == 1 for x in v)
    b = sum(x == -1 for x in v)
    if a > b:
        a, b = b, a
    c = len(v) - a - b
    return (a, b, c)


def formula(n):
    return (3**n - 2 * 2**n + 1) // 2


for n in range(2, 7):
    normals = primitive_subset_difference_normals(n)
    assert len(normals) == formula(n)
    print(f"n={n}: hyperplanes={len(normals)} formula={formula(n)} PASS")

n = 6
normals = primitive_subset_difference_normals(n)
orbits = Counter(orbit_type(v) for v in normals)
expected = {
    (1, 1, 4): 15,
    (1, 2, 3): 60,
    (1, 3, 2): 60,
    (1, 4, 1): 30,
    (1, 5, 0): 6,
    (2, 2, 2): 45,
    (2, 3, 1): 60,
    (2, 4, 0): 15,
    (3, 3, 0): 10,
}
assert dict(sorted(orbits.items())) == expected
assert sum(orbits.values()) == 301

print("depth6 orbit audit:")
for key in sorted(orbits):
    a, b, c = key
    # orbit size under coordinate permutations after identifying global sign
    raw = comb(n, a) * comb(n-a, b)
    orbit_size = raw if a < b else raw // 2
    assert orbit_size == orbits[key]
    print(f"  {key}: {orbits[key]} PASS")
print(f"orbit_types={len(orbits)} total={sum(orbits.values())} PASS")
print("OVERALL PASS")
