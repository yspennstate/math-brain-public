#!/usr/bin/env python3
"""Exact source-admissibility/spectral certificate for NM13-07 / E0095 / C20.

Verifies a Hamiltonian C20-plus-perfect-matching cubic graph whose second
adjacency eigenvalue is strictly below 2. Proof-critical comparisons use exact
integer/rational arithmetic and Sturm root counts via SymPy.
"""
from fractions import Fraction
from collections import deque
import sympy as sp

N = 20
MATCHING = [(0,6),(1,15),(2,9),(3,18),(4,13),(5,10),(7,14),(8,17),(11,16),(12,19)]
THRESH = sp.Rational(193,100)
x = sp.symbols('x')

# Build graph exactly.
adj = [set() for _ in range(N)]
cycle_edges = set()
for i in range(N):
    j = (i+1) % N
    e = tuple(sorted((i,j)))
    cycle_edges.add(e)
    adj[i].add(j); adj[j].add(i)

seen = set()
for a,b in MATCHING:
    assert a != b
    e = tuple(sorted((a,b)))
    assert e not in cycle_edges, f"matching edge is cycle edge: {e}"
    assert a not in seen and b not in seen, f"matching repeats vertex: {e}"
    seen.add(a); seen.add(b)
    adj[a].add(b); adj[b].add(a)
assert seen == set(range(N))
assert all(len(adj[v]) == 3 for v in range(N))

# Connectedness and explicit Hamiltonian cycle 0,1,...,19,0 are immediate,
# but check connectedness combinatorially.
q=deque([0]); reached={0}
while q:
    v=q.popleft()
    for w in adj[v]:
        if w not in reached:
            reached.add(w); q.append(w)
assert len(reached)==N

# Bipartiteness check: the witness must genuinely cross the prior bipartite boundary.
color={0:0}; q=deque([0]); bip=True
while q:
    v=q.popleft()
    for w in adj[v]:
        if w not in color:
            color[w]=1-color[v]; q.append(w)
        elif color[w]==color[v]:
            bip=False
assert not bip

# Exact girth by BFS from each root.
def girth_of_graph():
    best = 10**9
    for s in range(N):
        dist=[-1]*N; parent=[-1]*N; dist[s]=0; q=deque([s])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if dist[w] < 0:
                    dist[w]=dist[v]+1; parent[w]=v; q.append(w)
                elif parent[v] != w:
                    best=min(best, dist[v]+dist[w]+1)
    return best
GIRTH=girth_of_graph()
assert GIRTH == 6

# Exact adjacency matrix and characteristic polynomial.
A=sp.zeros(N,N)
for v in range(N):
    for w in adj[v]:
        A[v,w]=1
charpoly=sp.Poly(A.charpoly(x).as_expr(),x,domain=sp.ZZ)
fac=sp.factor(charpoly.as_expr())
expected=(x-3)*(x**2-x-1)**2*(x**3-4*x+1)*(x**4-5*x**2+5)*(x**3+2*x**2-4*x-7)*(x**5+3*x**4-3*x**3-11*x**2-3*x+1)
assert sp.expand(fac-expected)==0

# Let p be the factor containing the candidate lambda_2. Certify exactly that
# it has one real root alpha in (1.93,2), while every other nontrivial factor
# has no real root in [1.93,3). Since 3 is the Perron eigenvalue of this
# connected cubic graph, alpha is exactly lambda_2 and alpha<2.
p=sp.Poly(x**3+2*x**2-4*x-7,x,domain=sp.ZZ)
assert p.eval(THRESH) < 0
assert p.eval(2) > 0
assert sp.polys.polytools.count_roots(p, THRESH, sp.Rational(2,1)) == 1

other_factors=[
    sp.Poly(x**2-x-1,x),
    sp.Poly(x**3-4*x+1,x),
    sp.Poly(x**4-5*x**2+5,x),
    sp.Poly(x**5+3*x**4-3*x**3-11*x**2-3*x+1,x),
]
for f in other_factors:
    assert sp.polys.polytools.count_roots(f, THRESH, sp.Rational(3,1)) == 0, f

# Also certify that p has exactly one root in (1.93,2) and no root >=2.
assert sp.polys.polytools.count_roots(p, sp.Rational(2,1), sp.Rational(3,1)) == 0

# A narrower exact bracket helps make the numerical value reproducible.
lo=sp.Rational(19354,10000)
hi=sp.Rational(19355,10000)
assert p.eval(lo) < 0 and p.eval(hi) > 0
assert sp.polys.polytools.count_roots(p,lo,hi)==1

# Report a high precision decimal for readability only, not proof.
alpha=[r for r in sp.nroots(p.as_expr(), n=40, maxsteps=200) if abs(sp.im(r)) < sp.Rational(1,10)**30 and float(sp.re(r))>1][0]
alpha=float(sp.re(alpha))
gap=1-alpha/3

print('E0095 C20 nonbipartite exact certificate')
print('matching=' + repr(MATCHING))
print('hamiltonian_cycle=' + repr(list(range(N)) + [0]))
print('degrees=' + repr([len(adj[v]) for v in range(N)]))
print('bipartite=' + repr(bip))
print('girth=' + repr(GIRTH))
print('charpoly_factorization=' + str(fac))
print('lambda2_factor=x^3 + 2*x^2 - 4*x - 7')
print('exact_bracket_lambda2=(19354/10000,19355/10000)')
print('lambda2_decimal=%.15f' % alpha)
print('gap_decimal=%.15f' % gap)
print('lambda2_lt_2=True')
print('gap_gt_1_over_3=True')
print('ALL_EXACT_CHECKS_PASS')
