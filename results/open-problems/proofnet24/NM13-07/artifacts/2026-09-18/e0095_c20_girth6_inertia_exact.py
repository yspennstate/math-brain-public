#!/usr/bin/env python3
"""Exact self-check for NM13-07 / E0095, C20 + perfect matching, girth >= 6.

The finite claim is exact. Every spectral comparison is exact: rational congruence/inertia at q=97/50
certifies the nonboundary cases, and boundary cases are checked by exact
characteristic polynomials over Z[x].
"""
from collections import Counter
from fractions import Fraction
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
# and check every *other* irreducible factor separately. This avoids any
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
above_q_count = 0
boundary_count = 0
boundary_cp = Counter()
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
    E = {tuple(sorted(e)) for e in E}
    for i,j in enumerate(m):
        if i < j:
            E.add((i,j))
    return sorted(E)

def exact_inertia_above_q(m):
    """Exact inertia of B=50*A-97*I; #positive = # adjacency eigenvalues > 97/50."""
    B = [[Fraction(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        B[i][i] = Fraction(-97)
    for u,v in edges_from_mate(m):
        B[u][v] = B[v][u] = Fraction(50)

    pos = neg = zero = 0
    k = 0

    def swap_index(i, j):
        if i == j:
            return
        B[i], B[j] = B[j], B[i]
        for r in range(N):
            B[r][i], B[r][j] = B[r][j], B[r][i]

    while k < N:
        pivot_index = next((i for i in range(k, N) if B[i][i] != 0), None)
        if pivot_index is not None:
            swap_index(k, pivot_index)
            pivot = B[k][k]
            if pivot > 0:
                pos += 1
            else:
                neg += 1
            # Symmetric Schur complement, an exact congruence step.
            for i in range(k+1, N):
                bik = B[i][k]
                if bik == 0:
                    continue
                for j in range(i, N):
                    bjk = B[j][k]
                    if bjk != 0:
                        B[i][j] = B[j][i] = B[i][j] - bik*bjk/pivot
            k += 1
            continue

        # If all remaining diagonal entries vanish, use a nonzero 2x2 block
        # [[0,a],[a,0]], whose inertia is (1,1).
        pair = None
        for i in range(k, N):
            for j in range(i+1, N):
                if B[i][j] != 0:
                    pair = (i,j)
                    break
            if pair is not None:
                break
        if pair is None:
            zero += N-k
            break
        i,j = pair
        swap_index(k, i)
        swap_index(k+1, j)
        a = B[k][k+1]
        assert B[k][k] == 0 and B[k+1][k+1] == 0 and a != 0
        pos += 1
        neg += 1
        for r in range(k+2, N):
            br, cr = B[r][k], B[r][k+1]
            for t in range(r, N):
                bt, ct = B[t][k], B[t][k+1]
                B[r][t] = B[t][r] = B[r][t] - (br*ct + cr*bt)/a
        k += 2

    assert pos + neg + zero == N
    return pos, neg, zero

def exact_charpoly(m):
    M = [[0]*N for _ in range(N)]
    for u,v in edges_from_mate(m):
        M[u][v]=M[v][u]=1
    return sp.Poly(sp.Matrix(M).charpoly(X).as_expr(), X)

def verify_full(m):
    global count, above_q_count, boundary_count, witness_seen
    count += 1
    E = edges_from_mate(m)
    assert len(E) == 30
    deg = [0]*N
    for u,v in E:
        deg[u]+=1; deg[v]+=1
    assert deg == [3]*N
    mm = tuple(sorted((i,m[i]) for i in range(N) if i < m[i]))
    if mm == WITNESS:
        witness_seen = True

    pos, neg, zero = exact_inertia_above_q(m)
    # q=97/50 cannot be an eigenvalue of an integer matrix: any rational root
    # of its monic integer characteristic polynomial is an integer.
    assert zero == 0
    assert pos >= 1  # Perron eigenvalue 3 is above q.
    if pos >= 2:
        above_q_count += 1
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

assert count == 8966
assert boundary_count == 275
assert above_q_count + boundary_count == count
assert boundary_cp == Counter({'CP0': 210, 'CP1': 65})
assert witness_seen
wm = [-1]*N
for u,v in WITNESS:
    wm[u]=v; wm[v]=u
assert exact_charpoly(tuple(wm)) == CP0

print('E0095 C20 GIRTH>=6 EXACT SELF-CHECK')
print('alpha_polynomial:', sp.factor(P))
print('alpha_interval: 9677/5000 < alpha < 3871/2000')
print('inertia_separator_q: 97/50')
print('enumerated_source_matchings:', count)
print('exact_inertia_lambda2_gt_q:', above_q_count)
print('boundary_exact_charpoly:', boundary_count)
print('boundary_charpoly_classes:', dict(boundary_cp))
print('incumbent_witness_seen:', witness_seen)
print('CONCLUSION: every C20+perfect-matching graph of girth >= 6 has lambda2 >= alpha; equality occurs in the CP0/CP1 boundary classes, and the incumbent attains alpha.')
print('ALL_EXACT_CHECKS_PASS')
