#!/usr/bin/env python3
from fractions import Fraction
from collections import Counter
from math import log2

n = 4
N = 1 << n


def parity(x):
    return x.bit_count() & 1


def affine_mask(a, c):
    m = 0
    for x in range(N):
        m |= (c ^ parity(a & x)) << x
    return m


M = {affine_mask(a, c) for a in range(N) for c in (0, 1)}
assert len(M) == 32

D = []
for A in range(1 << N):
    if all(parity(A & m) == 0 for m in M):
        D.append(A)
Dset = set(D)
assert len(D) == 2048
wd = Counter(A.bit_count() for A in D)
assert wd == Counter({0: 1, 4: 140, 6: 448, 8: 870, 10: 448, 12: 140, 16: 1})

# Quadratic gate g(x)=x_1 x_2; its derivative under a physical translation is affine.
g = 0
for x in range(N):
    if ((x >> 0) & 1) and ((x >> 1) & 1):
        g |= 1 << x
assert g not in M

separated = [A for A in D if parity(A & g)]
sep_shell = Counter(A.bit_count() for A in separated)
assert sep_shell == Counter({4: 64, 6: 256, 8: 384, 10: 256, 12: 64})

# Two exact Boolean phases, represented by their -1 truth-table sets.
# A: codimension-three two-point subcube {0,4}.
# B: the four Hamming-weight-one points.
bA = (1 << 0) | (1 << 4)
bB = sum(1 << x for x in (1, 2, 4, 8))


def relation_set(b):
    return {A for A in separated if parity(A & b)}


RA, RB = relation_set(bA), relation_set(bB)


def shell_counts(R):
    return Counter(A.bit_count() for A in R)


target_C = Counter({4: 32, 6: 128, 8: 192, 10: 128, 12: 32})
assert shell_counts(RA) == target_C
assert shell_counts(RB) == target_C

overlap = {}
for k in (4, 6, 8, 10, 12):
    a = {A for A in RA if A.bit_count() == k}
    b = {A for A in RB if A.bit_count() == k}
    overlap[k] = (len(a & b), len(a - b), len(b - a), len(a ^ b))
assert overlap == {
    4: (16, 16, 16, 32),
    6: (64, 64, 64, 128),
    8: (96, 96, 96, 192),
    10: (64, 64, 64, 128),
    12: (16, 16, 16, 32),
}


def translate_mask(A, i):
    out = 0
    for x in range(N):
        if (A >> x) & 1:
            out |= 1 << (x ^ (1 << i))
    return out


# D and the quadratic-gate separation predicate are invariant under physical translations.
for i in range(n):
    assert all(translate_mask(A, i) in Dset for A in D)
    assert all(parity(translate_mask(A, i) & g) == parity(A & g) for A in D)


def boundary_counts(R):
    R = set(R)
    # Each undirected translation edge is seen twice in the ordered sum.
    return tuple(
        sum((A in R) != (translate_mask(A, i) in R) for A in D) // 2
        for i in range(n)
    )


bdA = boundary_counts(RA)
bdB = boundary_counts(RB)
assert bdA == (256, 256, 0, 512)
assert bdB == (256, 256, 256, 256)


def values(b):
    return [-1 if (b >> x) & 1 else 1 for x in range(N)]


def influence_profile(b):
    f = values(b)
    return tuple(
        Fraction(sum(f[x] != f[x ^ (1 << i)] for x in range(N)), N)
        for i in range(n)
    )


jA = influence_profile(bA)
jB = influence_profile(bB)
assert jA == (Fraction(1, 4), Fraction(1, 4), Fraction(0), Fraction(1, 4))
assert jB == (Fraction(1, 2),) * 4
JA = sum(jA, Fraction())
JB = sum(jB, Fraction())
assert JA == Fraction(3, 4)
assert JB == Fraction(2)


def walsh(b):
    f = values(b)
    ans = []
    for S in range(1 << n):
        num = sum(f[x] * (-1 if parity(S & x) else 1) for x in range(N))
        ans.append(Fraction(num, N))
    return ans


wA, wB = walsh(bA), walsh(bB)
mA = Counter(c * c for c in wA if c)
mB = Counter(c * c for c in wB if c)
assert mA == Counter({Fraction(1, 16): 7, Fraction(9, 16): 1})
assert mB == Counter({Fraction(1, 16): 8, Fraction(1, 4): 2})
IA = sum(Fraction(S.bit_count()) * wA[S] ** 2 for S in range(1 << n))
IB = sum(Fraction(S.bit_count()) * wB[S] ** 2 for S in range(1 << n))
assert IA == JA == Fraction(3, 4)
assert IB == JB == Fraction(2)

HA = 4.0 - (9.0 / 8.0) * log2(3.0)
HB = 3.0

print("EXACT_PASS")
print("D_weight_distribution", dict(sorted(wd.items())))
print("separated_shells", dict(sorted(sep_shell.items())))
print("frustrated_shell_counts_A", dict(sorted(shell_counts(RA).items())))
print("frustrated_shell_counts_B", dict(sorted(shell_counts(RB).items())))
print("shell_overlap_intersection_Aonly_Bonly_symdiff", overlap)
print("translation_boundary_A", bdA)
print("translation_boundary_B", bdB)
print("influence_A", tuple(str(x) for x in jA), "J_A", JA)
print("influence_B", tuple(str(x) for x in jB), "J_B", JB)
print("spectrum_A_masses", {str(k): v for k, v in mA.items()}, "H_A", repr(HA), "I_A", IA)
print("spectrum_B_masses", {str(k): v for k, v in mB.items()}, "H_B", repr(HB), "I_B", IB)
print(
    "common_scalar_gate_packet",
    "G(theta)=64*sin(theta)^4*cos(theta)^4*(cos(theta)^2-sin(theta)^2)^4"
    "=64*sin(theta)^4*cos(theta)^4*cos(2*theta)^4",
)
