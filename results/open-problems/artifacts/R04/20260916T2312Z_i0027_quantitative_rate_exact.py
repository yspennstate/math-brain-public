#!/usr/bin/env python3
import sympy as sp
import networkx as nx
from fractions import Fraction

print("R04 I0027 quantitative-rate / bridge identity / R05 C13 audit checker")
print("SELF-CHECK: exact symbolic/integer arithmetic only; published decomposition/lower-bound inputs are external.")

# 1. Optimize the three n-exponents from delta=n^a, plus the quantitative bridge error.
a=sp.symbols('a', real=True)
e_surgery1=3-a
e_surgery2=3-2*a
e_cluster=2+3*a
e_bridge=sp.Rational(5,2)
astar=sp.solve(sp.Eq(e_surgery1,e_cluster),a)[0]
assert astar==sp.Rational(1,4)
vals=[sp.simplify(x.subs(a,astar)) if hasattr(x,'subs') else x
      for x in [e_surgery1,e_surgery2,e_cluster,e_bridge]]
assert vals==[sp.Rational(11,4),sp.Rational(5,2),sp.Rational(11,4),sp.Rational(5,2)]
print("delta_exponent_optimizer a=1/4 exponents", vals, "max=11/4 PASS")

# 2. Quantitative C6 cutoff eta=n^{-b}: small-mass error n^{-b}; path/capacity error n^{b-1}.
# Balance b=1/2.
b=sp.symbols('b', real=True)
assert sp.solve(sp.Eq(-b,b-1),b)[0]==sp.Rational(1,2)
print("bridge_cutoff_optimizer b=1/2 coefficient_error=n^-1/2 -> K_error=n^(5/2) PASS")

# 3. Scalar optimization and Hölder equality profile.
s=sp.symbols('s', real=True)
f=s**2*(1-s)/8
assert sp.factor(sp.diff(f,s)) == -s*(3*s-2)/8
assert sp.simplify(f.subs(s,sp.Rational(2,3))-sp.Rational(1,54))==0
print("bridge_scalar_profile max=1/54 at s=2/3 PASS")

# Exhaust exact square-rational distributions to verify (1-Q2)/S^2 <=1/4
# and equality only at exactly two equal positive coordinates in this test class.
eq_patterns=set()
tested=0
for k in range(1,6):
    for vec in __import__('itertools').product(range(1,6), repeat=k):
        den=sum(x*x for x in vec)
        Q2=Fraction(sum(x**4 for x in vec), den*den)
        S2=Fraction(sum(vec)**2, den)
        assert Q2*S2 >= 1
        lhs=(1-Q2)/S2
        assert lhs <= Fraction(1,4)
        if lhs==Fraction(1,4):
            # equality must be k=2 and equal positive coordinates
            assert k==2 and vec[0]==vec[1]
            eq_patterns.add((k,vec[0],vec[1]))
        tested+=1
print("holder_profile_exact_cases",tested,"equality_patterns",len(eq_patterns),"PASS")

# 4. Exact bridge-block identity on every connected Graph Atlas graph through n=7.
def bridge_identity(G):
    G=nx.convert_node_labels_to_integers(G, ordering="sorted")
    m=G.number_of_edges()
    bridges=list(nx.bridges(G))
    H=G.copy()
    H.remove_edges_from(bridges)
    comps=list(nx.connected_components(H))
    idx={}
    mi=[]
    for i,C in enumerate(comps):
        for v in C: idx[v]=i
        mi.append(H.subgraph(C).number_of_edges())
    Q=nx.Graph()
    Q.add_nodes_from(range(len(comps)))
    for u,v in bridges:
        Q.add_edge(idx[u],idx[v])
    assert nx.is_tree(Q)
    W=m+1
    weights=[x+1 for x in mi]
    assert sum(weights)==W
    # exact Kbr direct
    direct=Fraction(0,1)
    for u,v in bridges:
        G2=G.copy(); G2.remove_edge(u,v)
        parts=list(nx.connected_components(G2))
        assert len(parts)==2
        vol=sum(G.degree(x) for x in parts[0])
        direct += Fraction(vol*(2*m-vol),2*m)
    # iid weighted distance
    ed=Fraction(0,1)
    for i in range(len(comps)):
        for j in range(len(comps)):
            ed += Fraction(weights[i]*weights[j],W*W)*nx.shortest_path_length(Q,i,j)
    rhs=Fraction(W*W,m)*ed - Fraction((2*m+1)*Q.number_of_edges(),2*m)
    return direct,rhs

atlas=nx.graph_atlas_g()
count=0
for G in atlas:
    if 2<=G.number_of_nodes()<=7 and nx.is_connected(G):
        d,r=bridge_identity(G)
        assert d==r
        count+=1
assert count==995
print("bridge_identity_graph_atlas_connected_through_7",count,"PASS")

# 5. Independent exact audit of R05 C13.
edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,4),(3,5),(4,6),(4,7),(5,6),(5,7),(6,7)]
G=nx.Graph(); G.add_nodes_from(range(8)); G.add_edges_from(edges)
assert nx.is_connected(G)
assert set(dict(G.degree()).values())=={3}
A=sp.zeros(8,8)
for u,v in edges:
    A[u,v]=A[v,u]=1
z=sp.symbols('z')
char=sp.factor(A.charpoly(z).as_expr(),extension=sp.sqrt(5))
target=sp.expand((z-3)*(z-1)*(z+1)**4*(z**2-5))
assert sp.expand(char-target)==0
rvals=[sp.Integer(3),sp.sqrt(5),sp.Integer(1),sp.Integer(-1),-sp.sqrt(5)]
I=sp.eye(8)
projectors={}
for r in rvals:
    E=sp.eye(8)
    for q in rvals:
        if q!=r:
            E=E*(A-q*I)/(r-q)
    projectors[r]=sp.simplify(E)

x,y=2,0
expected={
    sp.Integer(3):(sp.Rational(1,8),sp.Rational(1,8),sp.Integer(1)),
    sp.sqrt(5):(sp.Rational(1,8)-sp.sqrt(5)/40, sp.sqrt(5)/20,(1+sp.sqrt(5))/2),
    sp.Integer(1):(sp.Rational(1,4),sp.Integer(0),sp.Integer(0)),
    sp.Integer(-1):(sp.Rational(3,8),-sp.Rational(1,8),-sp.Rational(1,3)),
    -sp.sqrt(5):(sp.Rational(1,8)+sp.sqrt(5)/40,-sp.sqrt(5)/20,(1-sp.sqrt(5))/2)
}
for r,(ea,eb,ep) in expected.items():
    aa=sp.simplify(projectors[r][x,x]); bb=sp.simplify(projectors[r][x,y]); pp=sp.simplify(bb/aa)
    assert sp.simplify(aa-ea)==0 and sp.simplify(bb-eb)==0 and sp.simplify(pp-ep)==0
coef=sp.simplify(2-sp.Rational(14,15)*sp.sqrt(5))
assert coef.evalf()<0
# not edge-transitive: common-neighbor count differs between two edges.
cn={e:len(set(G.neighbors(e[0])) & set(G.neighbors(e[1]))) for e in G.edges()}
assert len(set(cn.values()))>1
print("R05_C13_exact_projectors_charpoly_eventual_negative_derivative_non_edge_transitive PASS")

print("RESULT PASS")
