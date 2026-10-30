from fractions import Fraction
from itertools import permutations, combinations

PERMS = list(permutations(range(4)))
ID = (0, 1, 2, 3)
TRANS = []
for i, j in combinations(range(4), 2):
    p = list(ID)
    p[i], p[j] = p[j], p[i]
    TRANS.append(tuple(p))
V4 = [ID, (1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0)]


def comp(p, q):
    return tuple(p[q[i]] for i in range(4))


PAIR_CLASSES = [
    frozenset((frozenset((0, 1)), frozenset((2, 3)))),
    frozenset((frozenset((0, 2)), frozenset((1, 3)))),
    frozenset((frozenset((0, 3)), frozenset((1, 2)))),
]


def rho(p):
    out = []
    for C in PAIR_CLASSES:
        C2 = frozenset(frozenset(p[x] for x in e) for e in C)
        out.append(PAIR_CLASSES.index(C2))
    return tuple(out)


# Exact strict-support endpoint datum used only to falsify the claim that the
# new endpoint-geometry certificate is automatic.  It is NOT a MOC4
# counterexample.  The spectra are simple and real.
a = (-1, 2, 1, 0)
b = (-1, 1, -2, 2)


def endpoint(p):
    z = 1
    for i in range(4):
        z *= a[i] + b[p[i]]
    return Fraction(z)


H = {p: endpoint(p) for p in PERMS}
M = max(H.values())
m = sum(H.values(), Fraction(0)) / 24
fib = {}
for p in PERMS:
    fib.setdefault(rho(p), []).append(H[p])
Q = max(sum(v, Fraction(0)) / 4 for v in fib.values())
d = M - m
Delta = M - Q

Rroof = {}
gap = {}
for t in TRANS:
    Rroof[t] = max((H[p] + H[comp(t, p)]) / 2 for p in PERMS)
    gap[t] = 2 * M - 2 * Rroof[t]
G = sum(gap.values(), Fraction(0))

# Exact half-integer abstract orbit witness.  It is deliberately only a
# low-frequency/twirl-relaxation witness, not a true-unitary determinant
# orbit.  It proves that the V4 roof + six pair roofs + S4 low-frequency
# condition + same mean + orbit-maximum condition do not by themselves close
# the final 1/2 support gap for this endpoint datum.
twice = [
    73, 23, 7, 17, 3, 63,
    -1, -8, 19, 12, 9, 9,
    -33, -13, 53, 13, 63, 3,
    -48, -21, -11, -1, 9, -8,
]
f = {p: Fraction(v, 2) for p, v in zip(PERMS, twice)}

assert sum(f.values(), Fraction(0)) / 24 == m
assert f[ID] == M + Fraction(1, 2)
assert all(f[p] <= f[ID] for p in PERMS)

# Every transposition-pair roof is respected.
assert all(
    f[p] + f[comp(p, t)] <= 2 * Rroof[t]
    for p in PERMS for t in TRANS
)

# Every right V4-coset average respects the exact four-point fiber roof Q.
assert all(
    sum(f[comp(p, v)] for v in V4) / 4 <= Q
    for p in PERMS
)

# Low-frequency check.  For the central transposition adjacency operator A on
# S4, the irreducible eigenvalues are 6,2,0,-2,-6.  Thus
# A(A-2I)(A-6I) annihilates exactly the [4]+[31]+[22] sector used by the
# determinant subset expansion.
def Aop(x):
    return {p: sum(x[comp(p, t)] for t in TRANS) for p in PERMS}


Af = Aop(f)
A2 = Aop(Af)
A3 = Aop(A2)
assert all(A3[p] - 8 * A2[p] + 12 * Af[p] == 0 for p in PERMS)

assert M == 36
assert m == Fraction(29, 6)
assert Q == 15
assert d == Fraction(187, 6)
assert Delta == 21
assert G == 141
assert Delta + G / 2 - 3 * d == -2
assert (3 * d - Delta - G / 2) / 4 == Fraction(1, 2)

print('PASS MOC4-V4-PAIR-GAP-CEILING-v1')
print('M =', M, 'm =', m, 'Q =', Q, 'd =', d, 'Delta =', Delta, 'G =', G)
print('abstract_low_frequency_ceiling =', f[ID] - M)
print('endpoint_only_closure_slack =', Delta + G / 2 - 3 * d)
