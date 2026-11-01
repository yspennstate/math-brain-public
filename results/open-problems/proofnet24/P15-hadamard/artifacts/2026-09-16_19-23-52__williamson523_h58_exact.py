#!/usr/bin/env python3
"""Exact restricted-family checker for order-523 Williamson quadruples.

Family: each ±1 sequence is invariant under the unique multiplicative subgroup
K <= F_523^* of order 58. Because -1 in K, every such sequence is symmetric.
The program enumerates all normalized K-invariant sequences, computes exact
periodic-autocorrelation signatures, and checks the Williamson four-sum by an
exact meet-in-the-middle. It also prints the simpler row-sum obstruction.

This is a restricted-family checker only. It does not decide existence of an
unrestricted Williamson quadruple of order 523 or an unrestricted Hadamard
matrix of order 2092.
"""
from itertools import product

P = 523
G = 2
D = 58


def mod_order(a, p):
    x = 1
    for k in range(1, p):
        x = (x * a) % p
        if x == 1:
            return k
    raise AssertionError("order not found")


assert mod_order(G, P) == P - 1
HGEN = pow(G, (P - 1) // D, P)
K = []
x = 1
for _ in range(D):
    K.append(x)
    x = (x * HGEN) % P
assert x == 1
assert len(set(K)) == D
assert (P - 1) in K  # -1, hence invariant sequences are symmetric.

unseen = set(range(1, P))
orbits = []
while unseen:
    a = min(unseen)
    orb = sorted({(a * h) % P for h in K})
    assert len(orb) == D
    orbits.append(orb)
    unseen.difference_update(orb)
assert len(orbits) == (P - 1) // D == 9
assert not unseen

# Each nonzero shift orbit can be represented by its least element.
reps = [orb[0] for orb in orbits]


def sequence(bits):
    # Global negation preserves every PAF. Normalize x[0]=+1.
    a = [0] * P
    a[0] = 1
    for bit, orb in zip(bits, orbits):
        v = 1 if bit else -1
        for j in orb:
            a[j] = v
    assert all(v in (-1, 1) for v in a)
    # Symmetry follows abstractly from -1 in K; assert it directly too.
    assert all(a[j] == a[(-j) % P] for j in range(P))
    return a


def paf_at(a, s):
    return sum(a[j] * a[(j + s) % P] for j in range(P))


signatures = []
rowsums = []
for bits in product((0, 1), repeat=len(orbits)):
    a = sequence(bits)
    rowsums.append(sum(a))
    sig = tuple(paf_at(a, s) for s in reps)
    # PAF must be constant on K-orbits of shifts. Verify all 522 shifts.
    for orb, val in zip(orbits, sig):
        assert all(paf_at(a, s) == val for s in orb)
    signatures.append(sig)

assert len(signatures) == 2 ** 9 == 512
row_sum_values = sorted(set(rowsums))
expected_rows = [-521, -405, -289, -173, -57, 59, 175, 291, 407, 523]
assert row_sum_values == expected_rows
min_abs_row_sum = min(abs(r) for r in row_sum_values)
assert min_abs_row_sum == 57
rowsum_lower_bound = 4 * min_abs_row_sum**2
assert rowsum_lower_bound == 12996 > 4 * P

# Exact four-signature check. If s_i are the 9-coordinate nonzero-shift PAF
# signatures, Williamson requires s_1+s_2+s_3+s_4 = 0.
pairs = {}
for i in range(len(signatures)):
    si = signatures[i]
    for j in range(i, len(signatures)):
        sj = signatures[j]
        key = tuple(a + b for a, b in zip(si, sj))
        pairs.setdefault(key, (i, j))

pair_total = len(signatures) * (len(signatures) + 1) // 2
# In fact every unordered pair has a distinct signature in this family.
assert len(pairs) == pair_total == 131328
complement_hits = []
for key, ij in pairs.items():
    neg = tuple(-x for x in key)
    if neg in pairs:
        complement_hits.append((ij, pairs[neg]))
        break
assert not complement_hits

print(f"p={P}")
print(f"primitive_root={G}")
print(f"subgroup_generator={HGEN}")
print(f"subgroup_order={D}")
print(f"minus_one_in_subgroup={P-1 in K}")
print(f"nonzero_orbit_count={len(orbits)}")
print("nonzero_orbit_sizes=" + ",".join(map(str, sorted({len(o) for o in orbits}))))
print(f"normalized_sequence_types={len(signatures)}")
print("row_sum_values=" + ",".join(map(str, row_sum_values)))
print(f"min_abs_row_sum={min_abs_row_sum}")
print(f"williamson_required_rowsum_square_sum={4*P}")
print(f"h58_family_rowsum_square_lower_bound={rowsum_lower_bound}")
print(f"unordered_pair_total={pair_total}")
print(f"distinct_pair_signature_count={len(pairs)}")
print("complementary_pair_signature_hits=0")
print("EXACT_RESTRICTED_CERTIFICATE_PASS")
print("PROVED_RESTRICTED: no order-523 Williamson quadruple invariant under the order-58 multiplicative subgroup of F_523^*.")
print("SCOPE: restricted Williamson family only; no claim about unrestricted Williamson(523) or H(2092).")
