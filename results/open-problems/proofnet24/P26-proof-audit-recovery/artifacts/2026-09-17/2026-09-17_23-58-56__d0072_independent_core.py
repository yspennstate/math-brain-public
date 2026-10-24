#!/usr/bin/env python3
"""Independent exact finite-core audit for P20/D0072 canonical K3 witness.

Checks only finite S3/A5 assertions. It does not machine-prove the free-product
normal-form facts or the Leemann--de la Salle GRR theorem.
"""
from itertools import permutations


def compose(p, q):
    # p after q
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2


def subgroup_generated(gens, identity):
    H = {identity}
    changed = True
    while changed:
        changed = False
        old = list(H)
        for a in old:
            for b in gens:
                for c in (compose(a, b), compose(b, a)):
                    if c not in H:
                        H.add(c)
                        changed = True
    return H


def commutator(a, b):
    return compose(compose(compose(a, b), inverse(a)), inverse(b))


def commutator_subgroup(G, identity):
    comms = {commutator(a, b) for a in G for b in G}
    return subgroup_generated(comms, identity)


def left_coset(H, g):
    return frozenset(compose(h, g) for h in H)


S3 = list(permutations(range(3)))
e3 = tuple(range(3))
tau = (1, 0, 2)
H = subgroup_generated([tau], e3)
assert len(S3) == 6
assert len(H) == 2

conjugates = {
    frozenset(compose(compose(g, h), inverse(g)) for h in H)
    for g in S3
}
assert len(conjugates) == 3  # H is not normal.

cosets = []
for g in S3:
    C = left_coset(H, g)
    if C not in cosets:
        cosets.append(C)
assert len(cosets) == 3
assert all(len(C) == 2 for C in cosets)

Sstar = [g for g in S3 if g != e3]
adj = [[False] * 3 for _ in range(3)]
for i, C in enumerate(cosets):
    for g in C:
        for s in Sstar:
            h = compose(g, s)
            for j, D in enumerate(cosets):
                if i != j and h in D:
                    adj[i][j] = True
expected = [[False, True, True], [True, False, True], [True, True, False]]
assert adj == expected

S3prime = commutator_subgroup(S3, e3)
assert len(S3prime) == 3
assert len(S3) // len(S3prime) == 2

A5 = [p for p in permutations(range(5)) if parity(p) == 0]
e5 = tuple(range(5))
assert len(A5) == 60
A5prime = commutator_subgroup(A5, e5)
assert len(A5prime) == 60

print("P26-D0072-INDEPENDENT-FINITE-CORE: PASS")
print("S3_order=6")
print("H_order=2")
print("H_index=3")
print("H_conjugate_count=3")
print("quotient_adjacency=K3")
print("S3_commutator_order=3")
print("S3_abelianization_order=2")
print("A5_order=60")
print("A5_commutator_order=60")
print("A5_abelianization_order=1")
print("Therefore canonical free-product abelianization input is C2, so no C3 quotient.")
print("END P26-D0072-INDEPENDENT-FINITE-CORE")
