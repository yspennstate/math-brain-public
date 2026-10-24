from fractions import Fraction
from itertools import permutations

# Exact stress instance from the current campaign-lead report.
a = (Fraction(-1), Fraction(2), Fraction(1), Fraction(0))
b = (Fraction(-1), Fraction(1), Fraction(-2), Fraction(2))
perms = list(permutations(range(4)))


def compose(p, q):
    """p after q."""
    return tuple(p[q[i]] for i in range(4))


def endpoint(p):
    z = Fraction(1)
    for i in range(4):
        z *= a[i] + b[p[i]]
    return z


H = {p: endpoint(p) for p in perms}

# Klein four subgroup of S_4.
V4 = [
    (0, 1, 2, 3),
    (1, 0, 3, 2),
    (2, 3, 0, 1),
    (3, 2, 1, 0),
]

seen = set()
fibers = []
for p in perms:
    if p in seen:
        continue
    C = {compose(p, v) for v in V4}
    assert len(C) == 4
    seen.update(C)
    fibers.append(C)
assert len(fibers) == 6 and len(seen) == 24

B = {}
for C in fibers:
    avg = sum((H[x] for x in C), Fraction(0)) / 4
    for x in C:
        B[x] = avg

M = max(H.values())
m = sum(H.values(), Fraction(0)) / 24
Q = max(B.values())
d = M - m
Delta = M - Q
Kstd = max(H[p] - B[p] for p in perms)

# Reproduce the lead's six pair-specific endpoint gaps.
taus = []
for i in range(4):
    for j in range(i + 1, 4):
        t = list(range(4))
        t[i], t[j] = t[j], t[i]
        taus.append(tuple(t))

gaps = []
for t in taus:
    R_t = max((H[p] + H[compose(t, p)]) / 2 for p in perms)
    gaps.append(2 * M - 2 * R_t)
G = sum(gaps, Fraction(0))
lead_ceiling = (3 * d - Delta - G / 2) / 4
standard_ceiling = Kstd - Delta

assert M == 36
assert m == Fraction(29, 6)
assert Q == 15
assert d == Fraction(187, 6)
assert Delta == 21
assert sorted(gaps) == [4, 9, 24, 32, 36, 36]
assert G == 141
assert lead_ceiling == Fraction(1, 2)
assert Kstd == 21
assert standard_ceiling == 0

print("PASS MOC4-STANDARD-CHANNEL-CEILING-v1")
print("M =", M)
print("m =", m)
print("Q =", Q)
print("d =", d)
print("Delta =", Delta)
print("pair_gaps =", ",".join(str(x) for x in gaps))
print("G =", G)
print("lead_V4_pair_ceiling =", lead_ceiling)
print("Kstd =", Kstd)
print("standard_channel_ceiling =", standard_ceiling)
