from fractions import Fraction
import itertools
import networkx as nx
import sympy as sp

print("R04 I0027 exact checker")
print("SELF-CHECK: finite arithmetic only; literature/theorem inputs audited separately")

def kemeny_exact(G):
    G = nx.convert_node_labels_to_integers(G, ordering="sorted")
    n = G.number_of_nodes()
    m = G.number_of_edges()
    if n == 1:
        return Fraction(0,1)
    L = sp.zeros(n,n)
    deg = [G.degree(i) for i in range(n)]
    for i in range(n):
        L[i,i] = deg[i]
    for i,j in G.edges():
        L[i,j] -= 1
        L[j,i] -= 1
    R = L[:n-1,:n-1].inv()
    rstar = sp.Rational(0)
    for i in range(n):
        for j in range(i+1,n):
            if j == n-1:
                rij = R[i,i]
            elif i == n-1:
                rij = R[j,j]
            else:
                rij = R[i,i] + R[j,j] - 2*R[i,j]
            rstar += deg[i]*deg[j]*rij
    K = sp.cancel(rstar/(2*m))
    return Fraction(int(sp.numer(K)), int(sp.denom(K)))

# 1. Exhaustive Graph Atlas scan through n=7.
atlas = nx.graph_atlas_g()
rows = []
for n in range(2,8):
    gs = [g for g in atlas if g.number_of_nodes()==n and nx.is_connected(g)]
    vals = [(kemeny_exact(g), g) for g in gs]
    mx = max(v for v,g in vals)
    maxgs = [g for v,g in vals if v==mx]
    codes = [nx.to_graph6_bytes(nx.convert_node_labels_to_integers(g), header=False).decode().strip()
             for g in maxgs]
    edge_lists = [sorted(tuple(sorted(e)) for e in g.edges()) for g in maxgs]
    rows.append((n,len(gs),mx,codes,edge_lists))
    assert len(maxgs)==1

expected = {
    2: Fraction(1,2),
    3: Fraction(3,2),
    4: Fraction(19,6),
    5: Fraction(11,2),
    6: Fraction(17,2),
    7: Fraction(293,24),
}
for n,count,mx,codes,edges in rows:
    assert mx == expected[n]
    print("atlas", n, "connected", count, "maxK", f"{mx.numerator}/{mx.denominator}",
          "graph6", codes[0], "edges", edges[0])

for n,count,mx,codes,edges in rows[:-1]:
    g = nx.from_graph6_bytes(codes[0].encode())
    assert nx.is_isomorphic(g, nx.path_graph(n))

g7 = nx.from_graph6_bytes(rows[-1][3][0].encode())
triangles = sum(nx.triangles(g7).values())//3
assert triangles == 2
assert sorted(dict(g7.degree()).values()) == [2,2,2,2,2,3,3]
assert nx.number_connected_components(g7) == 1
print("atlas_n7_structure two_triangles_with_one_intermediate_path_vertex PASS")

# 2. Exact algebra for fixed clique-tree asymptotic optimization.
x,y = sp.symbols('x y', nonnegative=True)
s,t = sp.symbols('s t', nonnegative=True)
ratio = t**2/(s**2-2*t)
dr = sp.factor(sp.diff(ratio,t))
assert sp.simplify(dr - 2*t*(s**2-t)/(s**2-2*t)**2) == 0
u = sp.symbols('u', real=True)
f = (1-u)*u**2/sp.Integer(8)
assert sp.factor(sp.diff(f,u)) == -u*(3*u-2)/8
assert sp.simplify(f.subs(u,sp.Rational(2,3)) - sp.Rational(1,54)) == 0
print("clique_tree_optimization_symbolic max_coefficient 1/54 PASS")

# 3. Independent R05 n=11 finite arithmetic audit.
p=11
Fstar=set(range(1,p))
minus1=p-1

def mulsubgroup(generator):
    H={1}
    x=1
    while True:
        x=(x*generator)%p
        if x in H: break
        H.add(x)
    return frozenset(H)

subs=set()
for a in Fstar:
    subs.add(mulsubgroup(a))
sub_orders=sorted({len(H) for H in subs})
contain_minus=sorted({len(H) for H in subs if minus1 in H})
assert sub_orders == [1,2,5,10]
assert contain_minus == [2,10]

pairs=[{a,(-a)%p} for a in range(1,(p+1)//2)]
invsets=[]
for mask in range(1,1<<len(pairs)):
    S=set()
    for i,P in enumerate(pairs):
        if (mask>>i)&1: S |= P
    invsets.append(frozenset(S))
assert len(invsets)==31

arc_candidates=[]
for S in invsets:
    for H in subs:
        if minus1 not in H: continue
        if any(frozenset((h*s)%p for h in H)==S for s in S):
            arc_candidates.append(S)
            break
degrees=sorted(set(len(S) for S in arc_candidates))
assert degrees == [2,10]
assert sum(len(S)==2 for S in arc_candidates)==5
assert sum(len(S)==10 for S in arc_candidates)==1
print("R05_n11_independent_affine_certificate subgroup_orders", sub_orders,
      "orders_containing_minus_one", contain_minus,
      "candidate_degrees", degrees, "PASS")

print("RESULT PASS")
