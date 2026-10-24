"""Automorphisms (g(sigma x) = g(x)) and dual isomorphisms (g(pi x) = -g(-x)) of g among coordinate permutations.
Core coordinates 0..8, auxiliaries 9..17; a permutation must map core to core and aux to aux (influences differ).
Candidates are pruned by the signed core graph (sign of ghat({i,j})) and the core-aux zero matching, then checked
on the whole truth table."""
import itertools
import numpy as np
from gate import load_table, biased_spectrum, N

t = load_table().astype(np.int8)
c = biased_spectrum(t.astype(float), [0.5] * N)
W = np.rint(c * (1 << N)).astype(np.int64)
S = np.zeros((18, 18), dtype=np.int64)
for i in range(18):
    for j in range(18):
        if i != j:
            S[i, j] = W[(1 << i) | (1 << j)]
match = {}
for i in range(9):
    zs = [j for j in range(9, 18) if S[i, j] == 0]
    assert len(zs) == 1
    match[i] = zs[0]
idx = np.arange(1 << N, dtype=np.int64)


def permute_table(perm):
    # (g o perm)(x): new coordinate i reads old coordinate perm[i]; build index map
    y = np.zeros_like(idx)
    for i in range(N):
        y |= ((idx >> perm[i]) & 1) << i
    return y


def full_perm(pc):
    perm = list(pc) + [None] * 9
    for i in range(9):
        perm[match[i]] = match[pc[i]]
    return perm


autos, duals = [], []
comp = idx ^ ((1 << N) - 1)
for pc in itertools.permutations(range(9)):
    ok_a = all(S[pc[i], pc[j]] == S[i, j] for i in range(9) for j in range(i + 1, 9))
    ok_d = all(S[pc[i], pc[j]] == -S[i, j] for i in range(9) for j in range(i + 1, 9))
    if not (ok_a or ok_d):
        continue
    perm = full_perm(pc)
    y = permute_table(perm)
    if ok_a and np.array_equal(t[y], t):
        autos.append(perm)
    if ok_d and np.array_equal(t[y], -t[comp]):
        duals.append(perm)
print("automorphisms of g:", len(autos))
for p in autos:
    print("  ", p)
print("dual isomorphisms g(pi x) = -g(-x):", len(duals))
for p in duals[:6]:
    print("  ", p)
orb_core = {p[0] for p in autos}; orb_aux = {p[9] for p in autos}
print("orbit of core 0 under automorphisms:", sorted(orb_core), "; orbit of aux 9:", sorted(orb_aux))
