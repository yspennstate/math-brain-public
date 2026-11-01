#!/usr/bin/env python3
from fractions import Fraction
import itertools
import networkx as nx
import sympy as sp

print("R04 I0027 adversarial closure audit")
print("SELF-CHECK: exact finite/symbolic checks; published Alev theorem remains an external input")

# ------------------------------------------------------------
# A. C4 exact one-edge deletion checks on Graph Atlas through n<=6.
# ------------------------------------------------------------
def laplacian(G):
    nodes=list(G.nodes())
    idx={v:i for i,v in enumerate(nodes)}
    L=sp.zeros(len(nodes),len(nodes))
    for u in nodes:
        L[idx[u],idx[u]]=G.degree(u)
    for u,v in G.edges():
        i,j=idx[u],idx[v]
        L[i,j]-=1; L[j,i]-=1
    return nodes,idx,L

def resistances(G):
    nodes,idx,L=laplacian(G)
    n=len(nodes)
    if n==1: return {(nodes[0],nodes[0]):sp.Rational(0)}
    inv=L[:n-1,:n-1].inv()
    ans={}
    for ia,u in enumerate(nodes):
        for ib,v in enumerate(nodes):
            if ia==ib: val=0
            elif ia==n-1: val=inv[ib,ib]
            elif ib==n-1: val=inv[ia,ia]
            else: val=inv[ia,ia]+inv[ib,ib]-2*inv[ia,ib]
            ans[(u,v)]=sp.cancel(val)
    return ans

def kemeny(G):
    R=resistances(G); m=G.number_of_edges(); nodes=list(G.nodes())
    s=sp.Rational(0)
    for a,u in enumerate(nodes):
        for v in nodes[a+1:]:
            s += G.degree(u)*G.degree(v)*R[(u,v)]
    return sp.cancel(s/(2*m))

atlas=nx.graph_atlas_g()
checked=0
for G in atlas:
    n=G.number_of_nodes()
    if not (2<=n<=6 and nx.is_connected(G)): continue
    KG=kemeny(G); mG=G.number_of_edges()
    for e in list(G.edges()):
        H=G.copy(); H.remove_edge(*e)
        if not nx.is_connected(H): continue
        KH=kemeny(H); mH=H.number_of_edges(); q=1
        rhs=sp.Rational(mH,mG)*KH + sp.Rational((n-1)*(2*q*mH+q*q),mG)
        assert KG <= rhs
        checked+=1
print("C4_single_deletion_exact_cases",checked,"PASS")

# ------------------------------------------------------------
# B. C6 exact bridge-block identity on all connected atlas n<=7.
# ------------------------------------------------------------
def bridge_identity_rhs(G):
    m=G.number_of_edges()
    bridges=list(nx.bridges(G))
    H=G.copy(); H.remove_edges_from(bridges)
    comps=list(nx.connected_components(H))
    ci={v:i for i,C in enumerate(comps) for v in C}
    mi=[]
    for C in comps:
        mi.append(G.subgraph(C).number_of_edges())
    Q=nx.Graph(); Q.add_nodes_from(range(len(comps)))
    for u,v in bridges: Q.add_edge(ci[u],ci[v])
    w=[x+1 for x in mi]; W=sum(w)
    assert W==m+1
    Ed=sp.Rational(0)
    for i in range(len(comps)):
        for j in range(len(comps)):
            Ed += sp.Rational(w[i]*w[j],W*W)*nx.shortest_path_length(Q,i,j)
    return sp.cancel(sp.Rational(W*W,m)*Ed - sp.Rational((2*m+1)*len(bridges),2*m))

def bridge_contrib(G):
    m=G.number_of_edges(); s=sp.Rational(0)
    for u,v in nx.bridges(G):
        H=G.copy(); H.remove_edge(u,v)
        C=next(iter(nx.connected_components(H)))
        vol=sum(G.degree(x) for x in C)
        s += vol*(2*m-vol)
    return sp.cancel(s/(2*m))

checked2=0
for G in atlas:
    n=G.number_of_nodes()
    if not (2<=n<=7 and nx.is_connected(G)): continue
    assert bridge_contrib(G)==bridge_identity_rhs(G)
    checked2+=1
print("C6_bridge_identity_all_atlas_connected_n_le_7",checked2,"PASS")

# ------------------------------------------------------------
# C. Robust Alev-parameter window delta=n^a.
# C4 errors: n^3/delta and n^3/delta^2; cluster internal: delta^3*n^2.
# All are < n^3 exactly when a>0 and a<1/3.
# ------------------------------------------------------------
a=sp.symbols('a', real=True)
powers=[3-a,3-2*a,2+3*a]
assert sp.expand(3-(3-a)) == a
assert sp.expand(3-(3-2*a)) == 2*a
assert sp.expand(3-(2+3*a)) == 1-3*a
for q in [sp.Rational(1,100), sp.Rational(1,10), sp.Rational(1,4), sp.Rational(1,3)-sp.Rational(1,1000)]:
    assert all(sp.N(pow.subs(a,q)) < 3 for pow in powers)
print("C9_parameter_window delta=n^a: proof conditions a>0 and a<1/3 PASS")

# ------------------------------------------------------------
# D. C6 probability inequality and equality family.
# Q2*S^2 >=1. For uniform k-support p_i=1/k, equality holds and
# (1-Q2)/S^2=(k-1)/k^2, maximized over integer k>=1 at k=2 =1/4.
# ------------------------------------------------------------
for k in range(1,50):
    val=sp.Rational(k-1,k*k)
    assert val <= sp.Rational(1,4)
    if val==sp.Rational(1,4): assert k==2
print("C6_uniform_support_equality k=2 unique integer maximizer PASS")

eq=[]; tested=0
for k in range(1,6):
    for vec in itertools.product(range(1,5), repeat=k):
        den=sum(x*x for x in vec)
        ps=[sp.Rational(x*x,den) for x in vec]
        Q2=sum(x*x for x in ps)
        S2=sp.Rational(sum(vec)**2,den)
        lhs=(1-Q2)/S2
        assert lhs <= sp.Rational(1,4)
        if lhs==sp.Rational(1,4): eq.append(tuple(vec))
        tested+=1
assert all(len(v)==2 and v[0]==v[1] for v in eq)
print("C6_square_rational_equality_cases",len(eq),"of",tested,"all two_equal PASS")

# ------------------------------------------------------------
# E. Independent audit of R05 C7 exact 9-vertex counterexample.
# ------------------------------------------------------------
edges=[(0,2),(0,3),(0,4),(0,6),(1,3),(1,4),(1,5),(1,7),
       (2,5),(2,6),(2,8),(3,7),(3,8),(4,7),(4,8),(5,6),(5,7),(6,8)]
A=sp.zeros(9,9)
Gbad=nx.Graph(); Gbad.add_nodes_from(range(9)); Gbad.add_edges_from(edges)
for u,v in edges: A[u,v]=A[v,u]=1
assert nx.is_connected(Gbad)
assert all(sum(int(A[i,j]) for j in range(9))==4 for i in range(9))
common_counts={len(set(Gbad.neighbors(u)) & set(Gbad.neighbors(v))) for u,v in Gbad.edges()}
assert common_counts == {0,1,3}
print("R05_C7_outside_source connected_4_regular edge_common_neighbor_counts", sorted(common_counts), "NOT_EDGE_TRANSITIVE PASS")

x=sp.symbols('x'); roots=[-3,-2,-1,0,1,2,4]
M=sp.eye(9)
for r in roots: M=M*(A-r*sp.eye(9))
assert M==sp.zeros(9,9)
p=(117649*x**6+403368*x**5-300125*x**4-1275960*x**3+746956*x**2+1598352*x+184320)/sp.Integer(184320)
for r in roots: assert sp.simplify(p.subs(x,r)-8**r)==0
coeff=sp.Poly(sp.factor(sp.together(p)),x)
B=sp.zeros(9,9)
for (deg,),coef in coeff.terms(): B += coef*(A**deg)
Gen=A/sp.Integer(4)-sp.eye(9); Bp=sp.simplify(B*Gen)
num=sp.factor(Bp[0,2]*B[0,0]-B[0,2]*Bp[0,0]); den=sp.factor(B[0,0]**2)
der=sp.factor(num/den)
claimed=-sp.Rational(86682499335,448720082124196)
assert der==claimed and der<0
print("R05_C7_derivative_exact",der,"PASS")

print("RESULT PASS")
