#!/usr/bin/env python3
"""Exact self-check for NM13-07 / E0095, C20 + perfect matching, girth >= 6.

The finite claim is exact. Floating eigenvectors are used only to *find* integer
Rayleigh witnesses; every accepted witness is checked with integer arithmetic.
Boundary cases are checked by exact characteristic polynomials over Z[x].
"""
from collections import deque, Counter
from fractions import Fraction
import numpy as np
import sympy as sp

N = 20
X = sp.symbols('x')
# alpha is the unique root in (1.9354,1.9355) of p.
P = X**3 + 2*X**2 - 4*X - 7
LO = sp.Rational(9677, 5000)   # 1.9354
HI = sp.Rational(3871, 2000)   # 1.9355
Q  = sp.Rational(97, 50)       # 1.94, exact separator used for Rayleigh certificates

CP0 = sp.Poly((X-3)*(X**2-X-1)**2*(X**3-4*X+1)*(X**4-5*X**2+5)*P*(X**5+3*X**4-3*X**3-11*X**2-3*X+1), X)
CP1 = sp.Poly((X-3)*(X**2-X-1)**4*(X**2+3*X+1)*(X**3-4*X+1)*P**2, X)

WITNESS = tuple(sorted([(0,6),(1,15),(2,9),(3,18),(4,13),(5,10),(7,14),(8,17),(11,16),(12,19)]))

# Root-order certificate for alpha and the two boundary characteristic polynomials.
assert sp.count_roots(P, LO, HI) == 1
assert sp.count_roots(P, HI, sp.Integer(3)) == 0
assert HI < Q < 2
for cp in (CP0, CP1):
    assert cp.degree() == 20

# To certify the eigenvalue ordering, isolate alpha via its irreducible cubic
# and check every *other* irreducible factor separately.  This avoids any
# ambiguity in repeated-root counting for the full characteristic polynomial.
other_factors = [
    X**2-X-1,
    X**3-4*X+1,
    X**4-5*X**2+5,
    X**5+3*X**4-3*X**3-11*X**2-3*X+1,
    X**2+3*X+1,
]
for f in other_factors:
    assert sp.count_roots(f, LO, sp.Integer(3)) == 0

base_adj = [set() for _ in range(N)]
for i in range(N):
    base_adj[i].add((i-1) % N)
    base_adj[i].add((i+1) % N)
adj = [set(s) for s in base_adj]
mate = [-1]*N

count = 0
rayleigh_count = 0
boundary_count = 0
boundary_cp = Counter()
min_exact_margin_num = None
max_scale = 0
witness_seen = False

def short_distance(u, v):
    """Return a distance <=4 if one exists in current partial graph, else 5."""
    seen = 1 << u
    frontier = [u]
    for d in range(4):
        nxt = []
        for a in frontier:
            for b in adj[a]:
                if b == v:
                    return d+1
                if not ((seen >> b) & 1):
                    seen |= 1 << b
                    nxt.append(b)
        frontier = nxt
    return 5

def edges_from_mate(m):
    E = {(i,(i+1)%N) if i < (i+1)%N else ((i+1)%N,i) for i in range(N)}
    # Above set misses normalization for edge (19,0), repair robustly.
    E = {tuple(sorted(e)) for e in E}
    for i,j in enumerate(m):
        if i < j:
            E.add((i,j))
    return sorted(E)

def adjacency_matrix(m):
    A = np.zeros((N,N), dtype=float)
    for u,v in edges_from_mate(m):
        A[u,v]=A[v,u]=1.0
    return A

def exact_rayleigh_witness(m):
    """Find c in Z^20, sum c=0, with R_A(c)>97/50; return exact margin."""
    A = adjacency_matrix(m)
    vals, vecs = np.linalg.eigh(A)
    # Numpy returns ascending eigenvalues; connected cubic Perron value is last.
    x = vecs[:, -2]
    E = edges_from_mate(m)
    for scale in (100, 300, 1000, 3000, 10000, 30000, 100000, 300000, 1000000):
        r = [int(round(scale*float(z))) for z in x]
        s = sum(r)
        c = [N*z - s for z in r]  # exact centering, so sum(c)=0
        den = sum(z*z for z in c)
        if den == 0:
            continue
        num = 2*sum(c[u]*c[v] for u,v in E)
        # R=num/den > 97/50 exactly iff 50*num - 97*den > 0.
        margin = 50*num - 97*den
        if margin > 0:
            assert sum(c) == 0
            return margin, scale
    return None

def exact_charpoly(m):
    M = [[0]*N for _ in range(N)]
    for u,v in edges_from_mate(m):
        M[u][v]=M[v][u]=1
    return sp.Poly(sp.Matrix(M).charpoly(X).as_expr(), X)

def verify_full(m):
    global count, rayleigh_count, boundary_count, min_exact_margin_num, max_scale, witness_seen
    count += 1
    # Exact graph sanity.
    E = edges_from_mate(m)
    assert len(E) == 30
    deg = [0]*N
    for u,v in E:
        deg[u]+=1; deg[v]+=1
    assert deg == [3]*N
    mm = tuple(sorted((i,m[i]) for i in range(N) if i < m[i]))
    if mm == WITNESS:
        witness_seen = True

    cert = exact_rayleigh_witness(m)
    if cert is not None:
        margin, scale = cert
        rayleigh_count += 1
        max_scale = max(max_scale, scale)
        min_exact_margin_num = margin if min_exact_margin_num is None else min(min_exact_margin_num, margin)
        return

    cp = exact_charpoly(m)
    if cp == CP0:
        boundary_cp['CP0'] += 1
    elif cp == CP1:
        boundary_cp['CP1'] += 1
    else:
        raise AssertionError('Uncertified boundary graph: charpoly differs from CP0 and CP1')
    boundary_count += 1

def rec():
    i = next((k for k in range(N) if mate[k] < 0), None)
    if i is None:
        verify_full(tuple(mate))
        return
    for j in range(i+1, N):
        if mate[j] >= 0 or j in adj[i]:
            continue
        # Adding i--j is legal for girth>=6 iff it does not close a cycle <=5.
        if short_distance(i,j) <= 4:
            continue
        mate[i]=j; mate[j]=i
        adj[i].add(j); adj[j].add(i)
        rec()
        adj[i].remove(j); adj[j].remove(i)
        mate[i]=mate[j]=-1

rec()

# These counts are part of the exact replay certificate.
assert count == 8966
assert boundary_count == 275
assert rayleigh_count + boundary_count == count
assert boundary_cp == Counter({'CP0': 210, 'CP1': 65})
assert witness_seen
wm = [-1]*N
for u,v in WITNESS:
    wm[u]=v; wm[v]=u
assert exact_charpoly(tuple(wm)) == CP0
assert min_exact_margin_num is not None and min_exact_margin_num > 0

print('E0095 C20 GIRTH>=6 EXACT SELF-CHECK')
print('alpha_polynomial:', sp.factor(P))
print('alpha_interval: 9677/5000 < alpha < 3871/2000')
print('rayleigh_separator_q: 97/50')
print('enumerated_source_matchings:', count)
print('exact_rayleigh_gt_q:', rayleigh_count)
print('boundary_exact_charpoly:', boundary_count)
print('boundary_charpoly_classes:', dict(boundary_cp))
print('minimum_integer_rayleigh_margin_50num_minus_97den:', min_exact_margin_num)
print('maximum_rounding_scale_used:', max_scale)
print('incumbent_witness_seen:', witness_seen)
print('CONCLUSION: every C20+perfect-matching graph of girth >= 6 has lambda2 >= alpha; equality occurs in the CP0/CP1 boundary classes, and the incumbent attains alpha.')
print('ALL_EXACT_CHECKS_PASS')
