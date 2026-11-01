#!/usr/bin/env python3
# Deterministic candidate-discovery heuristic for C28 / I0103.
# This script is NOT a proof: it uses floating eigenvalues only to rank candidates.
# Every reported mathematical finite claim is separately certified by
# 2026-09-16_p73_m14_exact_certificate.py.

import math, random
import numpy as np

p = 73
m = 14
restarts = 25
steps = 700
seed = 1073

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1)//2, p) == 1 else -1

def conference(p):
    C = np.zeros((p+1, p+1), dtype=int)
    for i in range(p):
        for j in range(p):
            if i != j:
                C[i,j] = legendre(i-j,p)
        C[i,p] = C[p,i] = 1
    return C

def cond(C,p,S):
    A = C[np.ix_(S,S)]
    e = np.linalg.eigvalsh(A)
    g = 1.0 + e/math.sqrt(p)
    return math.sqrt(g[-1]/g[0]), e

rng = random.Random(seed)
C = conference(p)
n = p+1
best = (-1.0, None, None)
for _ in range(restarts):
    S = set(rng.sample(range(n),m))
    c,e = cond(C,p,tuple(sorted(S)))
    best_local = (c,S.copy(),e)
    for step in range(steps):
        a = rng.choice(tuple(S))
        b = rng.choice(tuple(set(range(n))-S))
        S2 = S.copy(); S2.remove(a); S2.add(b)
        c2,e2 = cond(C,p,tuple(sorted(S2)))
        T = max(0.001, 0.1*(1-step/steps))
        if c2 > c or rng.random() < math.exp((c2-c)/T):
            S,c,e = S2,c2,e2
            if c > best_local[0]:
                best_local = (c,S.copy(),e)
    if best_local[0] > best[0]:
        best = (best_local[0], tuple(sorted(best_local[1])), best_local[2])

# Canonicalize under translations and multiplication by nonzero quadratic residues.
S = set(best[1])
QR = [a for a in range(1,p) if legendre(a,p)==1]
canonical = min(
    tuple(sorted((a*x+b)%p for x in S))
    for a in QR for b in range(p)
    if p not in S
)

print("C28_PALEY_ETF_DISCOVERY_HEURISTIC")
print(f"p={p} m={m} restarts={restarts} steps={steps} seed={seed}")
print("raw_subset=" + repr(best[1]))
print("raw_floating_condition=" + repr(best[0]))
print("canonical_subset=" + repr(canonical))
print("HEURISTIC_ONLY_USE_EXACT_CERTIFICATE_FOR_CLAIMS")
