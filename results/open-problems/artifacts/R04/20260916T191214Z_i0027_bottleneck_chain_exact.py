#!/usr/bin/env python3
from fractions import Fraction
import networkx as nx
import sympy as sp
import numpy as np

print('R04 I0027 bottleneck-chain / broom counterexample / R05 scoped audit')
print('SELF-CHECK: exact finite arithmetic and symbolic constants only')

# A. Broom-star counterexample to K <= |E| diam / 2.
p = sp.symbols('p', integer=True, positive=True)
n = 3*p + 4
m = 3*p + 3
d = sp.Integer(4)
S_leaf = 3*p*(2*n-3)
S_arm = 3*(2*(p+1)-1)*(2*(n-(p+1))-1)
K = sp.factor((S_leaf + S_arm)/(2*(n-1)))
assert sp.simplify(K - (14*p+5)/2) == 0
ratio = sp.factor(K/(m*d/2))
assert sp.simplify(ratio - (14*p+5)/(12*(p+1))) == 0
assert sp.limit(ratio,p,sp.oo) == sp.Rational(7,6)
assert K.subs(p,4) == sp.Rational(61,2)
assert (m*d/2).subs(p,4) == 30
print('broom_family_K', K)
print('broom_family_ratio_to_md_over_2', ratio, 'limit', sp.Rational(7,6))
print('broom_p4 n=16 m=15 d=4 K=61/2 > 30: PASS')

def broom(pv):
    G=nx.Graph(); root=0; nxt=1
    for _ in range(3):
        arm=nxt; nxt+=1; G.add_edge(root,arm)
        for _ in range(pv):
            leaf=nxt; nxt+=1; G.add_edge(arm,leaf)
    return G

G=broom(4)
assert G.number_of_nodes()==16 and G.number_of_edges()==15
assert nx.diameter(G)==4 and nx.is_tree(G)
num=Fraction(0,1)
for u in G:
    for v in G:
        if u<v:
            num += Fraction(G.degree(u)*G.degree(v)*nx.shortest_path_length(G,u,v),1)
K_direct = num/Fraction(2*G.number_of_edges(),1)
assert K_direct == Fraction(61,2)
assert 2*K_direct > G.number_of_edges()*nx.diameter(G)
print('broom_p4_direct_degree_resistance K', K_direct, 'counterexample PASS')

# B. Structural bottleneck theorem constants at kappa=1/54.
kap=sp.Rational(1,54)
high=sp.factor(4*kap**2)
boundary=sp.factor(1/(4*kap**2))
chain=sp.factor(4*kap**3)
assert high==sp.Rational(1,729)
assert boundary==729
assert chain==sp.Rational(1,39366)
print('C3_at_kappa_1_54 high_fraction', high, 'boundary_cap', boundary,
      'chain_fraction', chain, 'PASS')

# C. Independent scoped audit of R05 order-12 Conder graph 2.
adj={
1:[2,5,9,12],2:[1,6,10,12],3:[5,7,10,11],4:[8,9,11,12],
5:[1,3,9,10],6:[2,7,8,10],7:[3,6,8,11],8:[4,6,7,12],
9:[1,4,5,11],10:[2,3,5,6],11:[3,4,7,9],12:[1,2,4,8]
}
H=nx.Graph(); H.add_nodes_from(range(1,13))
for u,vs in adj.items():
    for v in vs: H.add_edge(u,v)
assert nx.is_connected(H) and set(dict(H.degree()).values())=={4}
gm=nx.algorithms.isomorphism.GraphMatcher(H,H)
autos=list(gm.isomorphisms_iter())
ref=(1,2)
orbit={(a[ref[0]],a[ref[1]]) for a in autos}
arcs={(u,v) for u,v in H.edges()} | {(v,u) for u,v in H.edges()}
assert orbit==arcs
print('R05_graph2 automorphisms',len(autos),'ordered_edge_orbit',len(orbit),'arc_transitive PASS')

A=np.zeros((12,12),dtype=object)
for u,v in H.edges(): A[u-1,v-1]=A[v-1,u-1]=1
M=np.eye(12,dtype=object)
for r in range(0,16):
    assert len({M[i,i] for i in range(12)})==1
    assert len({M[u-1,v-1] for u,v in H.edges()})==1
    AM=A@M
    assert AM[0,0] == 4*M[0,1]
    M=AM
print('R05_graph2 walk_constancy_and_identity_through_15 PASS')

dist=nx.single_source_shortest_path_length(H,1)
def triple(v):
    dv=dist[v]
    return tuple(sum(dist[w]==level for w in H.neighbors(v))
                 for level in (dv-1,dv,dv+1))
assert dist[3]==2 and dist[4]==2
assert triple(3)==(1,2,1) and triple(4)==(2,2,0)
print('R05_graph2 non_distance_regular_witness', triple(3), triple(4), 'PASS')
print('RESULT PASS')
