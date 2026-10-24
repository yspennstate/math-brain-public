#!/usr/bin/env python3
"""Independent P26 dual/Fourier audit of P15-H64-BGS-2060-NEG-01.

This checker deliberately does NOT reproduce the owner's 9-coordinate
autocorrelation signature search or P14's 513-shift full-signature search.
It uses only two exact nontrivial character constraints in F_1543.

If X_1,...,X_4 were a (514;256,257,257,257;512) cyclic supplementary
difference family, then in the group ring
  sum_i X_i X_i^{-1} = 515 e + 512 G.
For every nontrivial character chi, therefore
  sum_i chi(X_i) chi(X_i^{-1}) = 515.
Modulo p=1543=3*514+1, zeta=125 has exact order 514, so the same necessary
identities hold at j=1 and j=2. We exhaust all H-invariant candidates and
show no quadruple satisfies even those two necessary identities.
"""
from itertools import combinations, combinations_with_replacement
from collections import Counter

v = 514
p = 1543
zeta = 125
hgen = 81
freqs = (1, 2)

# Exact primality and order checks.
assert p > 1 and all(p % d for d in range(2, int(p**0.5)+1))
assert pow(zeta, v, p) == 1
assert pow(zeta, v // 2, p) == p - 1   # not order 257
assert pow(zeta, 2, p) != 1             # not order 2

# H=<81> in Z_514^*.
H = []
x = 1
while x not in H:
    H.append(x)
    x = (x * hgen) % v
assert x == 1
assert len(H) == 64
assert pow(hgen, 32, v) == v - 1

# H-orbits on Z_514.
unseen = set(range(v))
orbits = []
while unseen:
    a = min(unseen)
    O = frozenset((a*h) % v for h in H)
    orbits.append(O)
    unseen -= O

profile = Counter(map(len, orbits))
assert profile == Counter({64: 8, 1: 2})
fixed = sorted(next(iter(O)) for O in orbits if len(O) == 1)
large = [O for O in orbits if len(O) == 64]
assert fixed == [0, 257]
assert len(large) == 8

# Size-256 H-invariant sets: four large orbits.
A = [
    frozenset().union(*(large[i] for i in I))
    for I in combinations(range(8), 4)
]
# Size-257 H-invariant sets: four large orbits plus one fixed point.
B = []
for I in combinations(range(8), 4):
    core = frozenset().union(*(large[i] for i in I))
    for f in fixed:
        B.append(core | {f})
assert len(A) == 70 and len(B) == 140
assert all(len(X) == 256 for X in A)
assert all(len(X) == 257 for X in B)

def chi(X, j):
    return sum(pow(zeta, (j*x) % v, p) for x in X) % p

def dual_sig(X):
    # chi_j(X) chi_{-j}(X) for the two selected nontrivial characters.
    return tuple((chi(X, j) * chi(X, -j)) % p for j in freqs)

AS = [dual_sig(X) for X in A]
BS = [dual_sig(X) for X in B]
assert len(set(AS)) == 38
assert len(set(BS)) == 43

# X2,X3,X4 are symmetric. Precompute every exact B+B dual fingerprint,
# allowing repetition; using all 140 candidate sets (not only distinct sigs)
# makes the coverage transparent.
pair_sums = {
    tuple((a+b) % p for a, b in zip(BS[i], BS[j]))
    for i, j in combinations_with_replacement(range(len(BS)), 2)
}
assert len(pair_sums) == 928

target = (515, 515)
hits = []
for ia, sa in enumerate(AS):
    for ib, sb in enumerate(BS):
        need = tuple((t-a-b) % p for t, a, b in zip(target, sa, sb))
        if need in pair_sums:
            hits.append((ia, ib, need))

assert not hits

# Independent structural sanity check: addition by 257 pairs the eight
# size-64 H-orbits. This is not needed for the dual proof.
paired = {}
for i, O in enumerate(large):
    shifted = frozenset((x + 257) % v for x in O)
    paired[i] = large.index(shifted)
assert all(paired[paired[i]] == i and paired[i] != i for i in range(8))
assert len({tuple(sorted((i, paired[i]))) for i in range(8)}) == 4

print("audit_claim=P15-H64-BGS-2060-NEG-01")
print("method=exact_dual_character_obstruction")
print("modulus_v=", v)
print("finite_field_p=", p)
print("zeta_order_514=", zeta)
print("H_generator=", hgen)
print("H_order=", len(H))
print("orbit_profile=", dict(sorted(profile.items())))
print("fixed_points=", fixed)
print("A_candidates=", len(A))
print("B_candidates=", len(B))
print("frequencies=", freqs)
print("distinct_A_dual_signatures=", len(set(AS)))
print("distinct_B_dual_signatures=", len(set(BS)))
print("distinct_B_plus_B_dual_signatures=", len(pair_sums))
print("required_nontrivial_character_value=", 515)
print("spectral_solution_hits=", len(hits))
print("order_two_orbit_pairs=", sorted({tuple(sorted((i, paired[i]))) for i in range(8)}))
print("P26_DUAL_EXACT_AUDIT_PASS")
