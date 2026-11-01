#!/usr/bin/env python3
"""Exact finite certificate excluding the order-32 multiplier-invariant cyclic
bordered Goethals--Seidel (BGS) family at order 2060.

Target difference family over Z_514:
    (514; 256,257,257,257; 512).
If it existed, the bordered Goethals--Seidel construction would give H(2060).
Restriction certified here: every block is invariant under multiplication by
H32=<393> <= (Z/514Z)^*.  This class strictly contains the H64-invariant class
excluded in the neighboring P15 track because 393 = 81^2 and <393> < <81>.

The search is exact. Candidate signatures use Python-integer bitsets and exact
population counts. The final meet-in-the-middle certificate uses a fixed
additive map Z^17 -> Z/(2^64): if exact signature vectors were equal, their
hashes would necessarily be equal. Therefore an EMPTY hash intersection is a
one-sided exact certificate of nonexistence; hash collisions could create false
positives but can never create a false negative.

Requirements: Python 3, numpy, numba. No floating point, randomness, solver,
or timeout inference is used.
"""
from itertools import combinations
from collections import Counter
import math
import numpy as np
from numba import njit

V = 514
TARGET = 512
GEN_H64 = 81
GEN = pow(GEN_H64, 2, V)  # 393, order 32
MASKV = (1 << V) - 1
MASK64 = (1 << 64) - 1


def multiplicative_subgroup(g):
    H = []
    x = 1
    while x not in H:
        H.append(x)
        x = (x * g) % V
    assert x == 1
    return H


H = multiplicative_subgroup(GEN)
assert len(H) == 32
assert all(math.gcd(h, V) == 1 for h in H)
H64 = multiplicative_subgroup(GEN_H64)
assert len(H64) == 64
assert set(H).issubset(H64)

# Multiplicative H-orbits on Z_514.
unseen = set(range(V))
orbits = []
while unseen:
    a = min(unseen)
    O = tuple(sorted({(a * h) % V for h in H}))
    orbits.append(O)
    unseen.difference_update(O)
profile = Counter(map(len, orbits))
assert profile == Counter({32: 16, 1: 2})
fixed = sorted(O[0] for O in orbits if len(O) == 1)
assert fixed == [0, 257]
large = [O for O in orbits if len(O) == 32]
assert len(large) == 16

# For nonzero shifts, there are 16 H-orbits of length 32 plus {257}.
shift_orbits = large + [(257,)]
shift_reps = [min(O) for O in shift_orbits]
assert len(shift_reps) == 17
assert sum(len(O) for O in shift_orbits) == V - 1


def bits_of(O):
    b = 0
    for x in O:
        b |= 1 << x
    return b


large_bits = [bits_of(O) for O in large]


def rotl_v(b, t):
    if t == 0:
        return b
    return ((b << t) & MASKV) | (b >> (V - t))


def nu_bits(b, t):
    # |{x in X : x+t in X}|; replacing t by -t gives the same count.
    return (b & rotl_v(b, t)).bit_count()


def signature(b):
    return tuple(nu_bits(b, t) for t in shift_reps)


# Size 256: exactly eight 32-orbits and no fixed point.
# Size 257: exactly eight 32-orbits and exactly one of {0,257}.
combos = list(combinations(range(16), 8))
assert len(combos) == math.comb(16, 8) == 12870
A = np.empty((len(combos), 17), dtype=np.int16)
B = np.empty((2 * len(combos), 17), dtype=np.int16)

for ci, I in enumerate(combos):
    b = 0
    for i in I:
        b |= large_bits[i]
    assert b.bit_count() == 256
    A[ci, :] = signature(b)
    for fp, f in enumerate(fixed):
        bb = b | (1 << f)
        assert bb.bit_count() == 257
        B[2 * ci + fp, :] = signature(bb)

# Validate orbit-representative reduction on deterministic sample candidates by
# checking every shift inside every multiplicative orbit.
for row_index in (0, 1, 17, 1234, len(combos) - 1):
    I = combos[row_index]
    b = 0
    for i in I:
        b |= large_bits[i]
    for extra in (None, 0, 257):
        bb = b if extra is None else (b | (1 << extra))
        sig = signature(bb)
        for j, O in enumerate(shift_orbits):
            vals = {nu_bits(bb, t) for t in O}
            assert vals == {sig[j]}

# Duplicate candidates with the same exact 17-vector are irrelevant to the
# existence equation, so deduplicate signatures only (not approximations).
Au = np.unique(A.astype(np.int32), axis=0)
Bu = np.unique(B.astype(np.int32), axis=0)
assert Au.shape == (6470, 17)
assert Bu.shape == (6563, 17)

# Fixed additive certificate map to Z/(2^64). Exact equality of signature
# vectors implies equality of these residues. Hence disjoint hashed sets prove
# disjoint exact vector sets, regardless of possible hash collisions.
C0 = 0x9E3779B185EBCA87
C1 = 0xD1B54A32D192ED03
coeff = np.array([C0 ^ ((j * C1) & MASK64) for j in range(17)], dtype=np.uint64)


def hashes(M):
    return (M.astype(np.uint64) * coeff).sum(axis=1, dtype=np.uint64)


hA = hashes(Au)
hB = hashes(Bu)
target_vec = np.full(17, TARGET, dtype=np.int32)
hT = (target_vec.astype(np.uint64) * coeff).sum(dtype=np.uint64)

# Pair set P = {h(b2)+h(b3): b2,b3 in Bu}, repetitions allowed.
nB = len(hB)
pair_count = nB * (nB + 1) // 2
pair_hash = np.empty(pair_count, dtype=np.uint64)
pos = 0
for i in range(nB):
    vals = hB[i] + hB[i:]
    L = len(vals)
    pair_hash[pos:pos + L] = vals
    pos += L
assert pos == pair_count == 21539766
pair_hash.sort()

# Need set N = {h(T)-h(a)-h(b1): a in Au, b1 in Bu}.
need_hash = (np.uint64(hT) - hA[:, None] - hB[None, :]).ravel()
assert need_hash.size == len(Au) * len(Bu) == 42462610
need_hash.sort()


@njit
def first_common_sorted(x, y):
    i = 0
    j = 0
    while i < x.size and j < y.size:
        if x[i] == y[j]:
            return True, x[i], i, j
        if x[i] < y[j]:
            i += 1
        else:
            j += 1
    return False, np.uint64(0), i, j


# JIT warmup, then exact merge of the two sorted uint64 arrays.
first_common_sorted(np.array([1, 3], dtype=np.uint64),
                    np.array([2, 3], dtype=np.uint64))
has_common, common_value, ip, ineed = first_common_sorted(pair_hash, need_hash)
assert not has_common

# A solution A+B1+B2+B3=(512,...,512) would force
# h(B2)+h(B3)=h(T)-h(A)-h(B1), contradicting the empty intersection.
print('target_order=2060')
print('cyclic_length_v=', V)
print('multiplier_generator_h32=', GEN)
print('h32_order=', len(H))
print('h64_generator=', GEN_H64)
print('h32_subset_h64=', set(H).issubset(H64))
print('orbit_profile=', dict(sorted(profile.items())))
print('fixed_points=', fixed)
print('nonzero_shift_orbits=', len(shift_orbits))
print('A_candidate_count=', len(A))
print('B_candidate_count=', len(B))
print('A_unique_signatures=', len(Au))
print('B_unique_signatures=', len(Bu))
print('B_plus_B_hash_count=', len(pair_hash))
print('target_minus_A_plus_B_hash_count=', len(need_hash))
print('hash_modulus=2^64')
print('hash_intersection_empty=', not has_common)
print('PROVED: no H32-invariant cyclic BGS difference family (514;256,257,257,257;512)')
print('LOGIC: exact vector equality => additive-hash equality; empty hash intersection => no exact vector equality')
print('SCOPE: restricted-family nonexistence only; says nothing about unrestricted H(2060) existence')
print('ALL_EXACT_H32_CHECKS_PASSED')
