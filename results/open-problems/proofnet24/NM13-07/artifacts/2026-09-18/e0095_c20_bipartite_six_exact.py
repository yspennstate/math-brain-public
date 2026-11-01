#!/usr/bin/env python3
"""
Exact self-check for NM13-07 / E0095 / C20 bipartite equality constructions.

This does NOT re-prove Koledin--Stanic's exhaustive classification of all
bipartite cubic reflexive graphs. It independently checks the six order-20
LCF representatives J10--J15 listed in their Table 3: each is a source-valid
C20 + perfect-matching graph, is bipartite, and has exact second adjacency
eigenvalue 2.
"""
import sympy as sp
from collections import deque

x = sp.symbols("x")

SPECS = {
    "J10": ("repeat", [5,-5,9,-9], 5),
    "J11": ("mirror", [5,-9,-7,7,-7,-5,5,-9,5,7]),
    "J12": ("mirror", [-5,9,-9,5,-5,7,-9,7,-5,9]),
    "J13": ("mirror", [5,9,-9,5,-9,-5,-9,5,-5,9]),
    "J14": ("mirror", [5,9,-5,9,-9,-5,5,9,5,9]),
    "J15": ("mirror", [-9,5,-7,7,-7,7,-5,7,-9,7]),
}

EXPECTED = {
    "J10": (x-3)*(x-2)**4*(x-1)**5*(x+1)**5*(x+2)**4*(x+3),
    "J11": (x-3)*(x-2)**4*(x-1)**5*(x+1)**5*(x+2)**4*(x+3),
    "J12": x**2*(x-3)*(x-2)**3*(x-1)**3*(x+1)**3*(x+2)**3*(x+3)*(x**2-3)**2,
    "J13": (x-3)*(x-2)**2*(x-1)*(x+1)*(x+2)**2*(x+3)*(x**3-3*x-1)**2*(x**3-3*x+1)**2,
    "J14": x**2*(x-3)*(x-2)**3*(x-1)**3*(x+1)**3*(x+2)**3*(x+3)*(x**2-3)**2,
    "J15": (x-3)*(x-2)**2*(x-1)*(x+1)*(x+2)**2*(x+3)*(x**3-3*x-1)**2*(x**3-3*x+1)**2,
}

def expand(spec):
    if spec[0] == "repeat":
        _, base, times = spec
        return base * times
    _, half = spec
    return half + [-a for a in reversed(half)]

def matching_from_lcf(seq):
    n = len(seq)
    edges = set()
    for i, d in enumerate(seq):
        j = (i + d) % n
        edges.add(tuple(sorted((i, j))))
    return edges

def adjacency(seq):
    n = len(seq)
    A = sp.zeros(n)
    for i in range(n):
        A[i, (i-1) % n] = 1
        A[i, (i+1) % n] = 1
    M = matching_from_lcf(seq)
    for a, b in M:
        A[a,b] = A[b,a] = 1
    return A, M

def bipartite(A):
    n = A.rows
    col = [-1]*n
    for s in range(n):
        if col[s] != -1:
            continue
        col[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in range(n):
                if A[u,v] == 0:
                    continue
                if col[v] == -1:
                    col[v] = 1-col[u]
                    q.append(v)
                elif col[v] == col[u]:
                    return False
    return True

# The only non-linear factors which can occur above 2 in EXPECTED are
# x^2-3 and x^3-3x±1. They have no root >2:
# sqrt(3)<2; and each cubic has positive value at 2 and derivative
# 3x^2-3 >0 for x>=2.
assert 3 < 4
for c in (-1, 1):
    f = x**3 - 3*x + c
    assert sp.expand(f.subs(x,2)) > 0
    assert sp.diff(f,x) == 3*x**2 - 3

for name, spec in SPECS.items():
    seq = expand(spec)
    assert len(seq) == 20
    A, M = adjacency(seq)

    # Source-valid C20 plus a new perfect matching.
    assert len(M) == 10
    degM = [0]*20
    for a,b in M:
        degM[a] += 1
        degM[b] += 1
        assert (a-b) % 20 not in (1,19)
    assert degM == [1]*20

    # Cubic and bipartite.
    assert all(sum(int(A[i,j]) for j in range(20)) == 3 for i in range(20))
    assert bipartite(A)

    # Exact characteristic polynomial and therefore exact lambda_2=2.
    p = sp.expand(A.charpoly(x).as_expr())
    e = sp.expand(EXPECTED[name])
    assert p == e
    assert sp.rem(sp.Poly(p,x), sp.Poly((x-3)*(x-2),x)).is_zero

    print(f"{name}: VALID_C20_MATCHING BIPARTITE lambda2=2")
    print("  charpoly =", sp.factor(p))

print("ALL_EXACT_CHECKS_PASS")
