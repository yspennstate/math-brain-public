#!/usr/bin/env python3
from collections import Counter
import sympy as sp
import networkx as nx

def oriented_edges(G):
    return [(u,v) for u,v in G.edges()] + [(v,u) for u,v in G.edges()]

def reversal_augmented_arc_matrix(G):
    arcs = oriented_edges(G)
    idx = {a:i for i,a in enumerate(arcs)}
    A = sp.zeros(len(arcs))
    for i,(u,v) in enumerate(arcs):
        neigh = set()
        for w in G.neighbors(v):
            if w != u:
                neigh.add((v,w))
        for w in G.neighbors(u):
            if w != v:
                neigh.add((w,u))
        neigh.add((v,u))
        for b in neigh:
            A[i,idx[b]] = 1
    return arcs,A

def line_graph_matrix(G, und_edges):
    A = sp.zeros(len(und_edges))
    sets = [set(e) for e in und_edges]
    for i in range(len(und_edges)):
        for j in range(len(und_edges)):
            if i != j and sets[i] & sets[j]:
                A[i,j] = 1
    return A

def exact_test(G,name):
    nodes = list(G.nodes())
    d = G.degree[nodes[0]]
    assert all(G.degree[u] == d for u in nodes)
    q = d-1
    DB = 2*q+1

    arcs,A = reversal_augmented_arc_matrix(G)
    N = len(arcs)
    idx = {a:i for i,a in enumerate(arcs)}
    assert A == A.T
    assert all(A[i,i] == 0 for i in range(N))
    assert all(sum(A[i,j] for j in range(N)) == DB for i in range(N))
    Q = A/sp.Integer(DB)

    J = sp.zeros(N)
    for i,(u,v) in enumerate(arcs):
        J[i,idx[(v,u)]] = 1
    assert J*Q == Q*J

    und_edges = list(dict.fromkeys(tuple(sorted(e)) for e in G.edges()))
    eidx = {e:i for i,e in enumerate(und_edges)}
    R = sp.zeros(N,len(und_edges))
    for i,(u,v) in enumerate(arcs):
        R[i,eidx[tuple(sorted((u,v)))]] = 1
    AL = line_graph_matrix(G,und_edges)
    QL = AL/sp.Integer(2*q)
    alpha = sp.Rational(2*q,DB)
    beta = sp.Rational(1,DB)
    Qlazy = beta*sp.eye(len(und_edges)) + alpha*QL
    assert Q*R == R*Qlazy

    vidx = {u:i for i,u in enumerate(nodes)}
    Div = sp.zeros(len(nodes),N)
    Grad = sp.zeros(N,len(nodes))
    for j,(u,v) in enumerate(arcs):
        Div[vidx[u],j] = 1
        Grad[j,vidx[v]] = 1
        Grad[j,vidx[u]] = -1
    Odd = (sp.eye(N)-J)/2
    assert (DB*Q*Odd) == (sp.eye(N)+Grad*Div)*Odd

    AG = sp.zeros(len(nodes))
    for u,v in G.edges():
        AG[vidx[u],vidx[v]] = 1
        AG[vidx[v],vidx[u]] = 1
    P = AG/sp.Integer(d)
    assert Div*Grad == d*(P-sp.eye(len(nodes)))

    spec = Counter()
    for val,mult in Q.eigenvals().items():
        spec[sp.simplify(val)] += mult

    pe = []
    for val,mult in P.eigenvals().items():
        pe.extend([sp.N(val,40)]*mult)
    pe.sort(reverse=True)
    gamma = sp.nsimplify(1-pe[1])

    qe = []
    for val,mult in spec.items():
        qe.extend([sp.N(val,40)]*mult)
    qe.sort(reverse=True)
    actual_gap = sp.nsimplify(1-qe[1])
    gap_bound = sp.Min(sp.Rational(d,DB)*gamma,sp.Rational(2*q,DB))
    assert sp.N(actual_gap-gap_bound,40) >= -sp.Float("1e-30")

    print(f"{name}: d={d}, q={q}, |arcs|={N}, degree={DB}")
    print(f"{name}: spectrum={dict(sorted(spec.items(), key=lambda z: float(z[0]), reverse=True))}")
    print(f"{name}: base_gap={gamma}, theorem_gap_bound={gap_bound}, actual_gap={actual_gap}")
    print(f"{name}: lazy-line lumping, reversal commutation, odd Hodge identity, Dgrad identity PASS")

exact_test(nx.complete_graph(4),"K4")
exact_test(nx.complete_bipartite_graph(3,3),"K3,3")

# Degree-six explicit constants.
d=6
q=d-1
DB=2*q+1
center = sp.Rational(DB,d-2)
odd_rate = sp.Rational(2*q,DB)
assert center == sp.Rational(11,4)
assert odd_rate == sp.Rational(10,11)
assert sp.simplify(center*odd_rate) == sp.Rational(5,2)
ram_gap = sp.simplify(sp.Rational(d,DB)*(1-2*sp.sqrt(q)/d))
assert ram_gap == sp.Rational(6,11)-2*sp.sqrt(5)/11
assert 2*q > q
print(f"d=6: center_coeff={center}, odd_rate={odd_rate}, odd_exponent_coeff={center*odd_rate}")
print(f"d=6: Ramanujan output gap lower bound={ram_gap}; output branching {2*q} > projected branching {q}")

# Root-stabilizer orbit sanity check on Q_3.
# Stabilizer orbits are Hamming layers with sizes 1,3,3,1.
m=[1,3,3,1]
cplus=[3,2,1,0]
cminus=[0,1,2,3]
for i in range(3):
    assert m[i]*cplus[i] == m[i+1]*cminus[i+1]
    ratio = sp.Rational(m[i+1],m[i])
    assert sp.Rational(1,3) <= ratio <= 3
gamma_cube = sp.Rational(2,3)
# The h=0 sublevel is weights 0 and 3, stationary mass 1/4;
# its closed neighborhood is all 8 vertices.
pS = sp.Rational(2,8)
pN = sp.Rational(8,8)
assert pN >= (1+gamma_cube/2)*pS
print("Q3 stabilizer orbits: sizes=[1,3,3,1], edge-balance PASS, adjacent size ratios in [1/3,3]")
print(f"Q3 vertex-expansion sanity: pi(S)={pS}, pi(N[S])={pN}, required>={(1+gamma_cube/2)*pS}")

print("ALL_EXACT_CHECKS_PASS")
