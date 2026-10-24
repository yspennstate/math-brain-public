#!/usr/bin/env python3
from fractions import Fraction
import itertools
import math
import networkx as nx
import sympy as sp

print("R04 I0027 sparse-compression / bridge-variational checker")
print("SELF-CHECK: exact finite arithmetic only; theorem proofs are in the immutable report")

def kemeny_exact(G):
    G=nx.convert_node_labels_to_integers(G, ordering="sorted")
    n=G.number_of_nodes(); m=G.number_of_edges()
    assert nx.is_connected(G) and n>=2
    deg=[G.degree(i) for i in range(n)]
    L=sp.zeros(n,n)
    for i in range(n): L[i,i]=deg[i]
    for u,v in G.edges():
        L[u,v]-=1; L[v,u]-=1
    R=L[:n-1,:n-1].inv()
    total=sp.Rational(0)
    for i in range(n):
        for j in range(i+1,n):
            if j==n-1: rij=R[i,i]
            elif i==n-1: rij=R[j,j]
            else: rij=R[i,i]+R[j,j]-2*R[i,j]
            total += deg[i]*deg[j]*rij
    K=sp.cancel(total/(2*m))
    return Fraction(int(sp.numer(K)),int(sp.denom(K)))

# C4 sparse-deletion stability, one-edge deletions through n=6.
atlas=nx.graph_atlas_g(); checks=0
for G0 in atlas:
    n=G0.number_of_nodes()
    if not (2<=n<=6 and nx.is_connected(G0)): continue
    G=nx.convert_node_labels_to_integers(G0,ordering="sorted")
    KG=kemeny_exact(G); mG=G.number_of_edges()
    for e in list(G.edges()):
        H=G.copy(); H.remove_edge(*e)
        if not nx.is_connected(H): continue
        KH=kemeny_exact(H); mH=H.number_of_edges(); q=mG-mH
        rhs=Fraction(mH,mG)*KH + Fraction((n-1)*(2*q*mH+q*q),mG)
        assert KG <= rhs
        checks += 1
print("C4_sparse_deletion_one_edge_atlas_checks",checks,"PASS")

# C4 all connected spanning subgraphs of atlas graphs through n=5 when <=10 edges.
checks_multi=0
for G0 in atlas:
    n=G0.number_of_nodes()
    if not (2<=n<=5 and nx.is_connected(G0)): continue
    G=nx.convert_node_labels_to_integers(G0,ordering="sorted")
    edges=list(G.edges()); KG=kemeny_exact(G); mG=len(edges)
    if len(edges)>10: continue
    for mask in range(1,1<<len(edges)):
        H=nx.Graph(); H.add_nodes_from(G.nodes())
        H.add_edges_from([edges[i] for i in range(len(edges)) if (mask>>i)&1])
        if not nx.is_connected(H): continue
        mH=H.number_of_edges()
        if mH==mG: continue
        KH=kemeny_exact(H); q=mG-mH
        rhs=Fraction(mH,mG)*KH + Fraction((n-1)*(2*q*mH+q*q),mG)
        assert KG <= rhs
        checks_multi += 1
print("C4_sparse_deletion_multiedge_atlas_checks",checks_multi,"PASS")

# C5 chain-compression combinatorics.
def descendants(T,root):
    parent={root:None}; order=[root]
    for u in order:
        for v in T.neighbors(u):
            if v==parent[u]: continue
            parent[v]=u; order.append(v)
    children={u:[] for u in T}
    for v,p in parent.items():
        if p is not None: children[p].append(v)
    sub={}
    for u in reversed(order):
        S={u}
        for v in children[u]: S |= sub[v]
        sub[u]=S
    return parent,sub

rng_seed=202609162012
import random
rng=random.Random(rng_seed); chain_checks=0
for n in range(6,16):
    for trial in range(20):
        seq=[rng.randrange(n) for _ in range(n-2)]
        T=nx.from_prufer_sequence(seq); root=0
        parent,sub=descendants(T,root)
        deep=max(range(n),key=lambda v:nx.shortest_path_length(T,root,v))
        path=nx.shortest_path(T,root,deep); selected=path[1::2]
        if not selected: continue
        A=[sub[v] for v in selected]
        assert all(A[j+1] < A[j] for j in range(len(A)-1))
        layers=[set(T.nodes())-A[0]]
        for j in range(len(A)-1): layers.append(A[j]-A[j+1])
        layers.append(A[-1]); which={}
        for j,C in enumerate(layers):
            for v in C:
                assert v not in which; which[v]=j
        assert len(which)==n
        selected_edges={(min(parent[v],v),max(parent[v],v)) for v in selected}
        cross_T={(min(u,v),max(u,v)) for u,v in T.edges() if which[u]!=which[v]}
        assert cross_T==selected_edges
        G=T.copy()
        for u in range(n):
            for v in range(u+1,n):
                if not G.has_edge(u,v) and rng.random()<0.18: G.add_edge(u,v)
        cross={(u,v) for u,v in G.edges() if which[u]!=which[v]}
        sum_cut=0
        for Aj in A:
            sum_cut += sum(1 for u,v in G.edges() if ((u in Aj)!=(v in Aj)))
        assert len(cross)<=sum_cut
        H=G.copy()
        for u,v in list(H.edges()):
            if which[u]!=which[v] and (min(u,v),max(u,v)) not in selected_edges:
                H.remove_edge(u,v)
        assert nx.is_connected(H)
        cross_H={(min(u,v),max(u,v)) for u,v in H.edges() if which[u]!=which[v]}
        assert cross_H==selected_edges
        for e in selected_edges:
            H2=H.copy(); H2.remove_edge(*e); assert not nx.is_connected(H2)
        chain_checks+=1
print("C5_chain_compression_combinatorics_checks",chain_checks,"seed",rng_seed,"PASS")

# C6 Renyi/bridge inequality.
var_checks=0; eq_cases=[]
for k in range(1,7):
    for qvec in itertools.product(range(1,6),repeat=k):
        Q2=sum(x*x for x in qvec); Q4=sum(x**4 for x in qvec); S1=sum(qvec)
        lhs=4*(Q2*Q2-Q4); rhs=Q2*S1*S1
        assert lhs<=rhs
        if lhs==rhs: eq_cases.append(qvec)
        var_checks+=1
print("C6_Renyi_bridge_inequality_integer_checks",var_checks,"PASS")
assert all((len(q)==2 and q[0]==q[1]) for q in eq_cases)
print("C6_equality_pattern_two_equal_atoms PASS")
s=sp.symbols('s',real=True); f=s**2*(1-s)/8
assert sp.factor(sp.diff(f,s)) == -s*(3*s-2)/8
assert sp.simplify(f.subs(s,sp.Rational(2,3))-sp.Rational(1,54))==0
print("C6_vertex_budget_optimization max 1/54 at s=2/3 PASS")

# Exact bridge contribution identity on several bridge-block quotient paths.
bridge_checks=0
for sizes in [(3,1,4),(2,3,1,2),(4,2),(1,3,1,3,1)]:
    k=len(sizes); Q=nx.path_graph(k)
    mi=[z*(z-1)//2 for z in sizes]; b=k-1; M=sum(mi); m=M+b; W=m+1
    wi=[x+1 for x in mi]; assert sum(wi)==W
    raw=Fraction(0,1)
    for a,bv in Q.edges():
        Q2=Q.copy(); Q2.remove_edge(a,bv); S=list(nx.connected_components(Q2))[0]
        V=2*sum(mi[i] for i in S)+2*(len(S)-1)+1
        raw += Fraction(V*(2*m-V),2*m)
    Ed=Fraction(0,1); dist=dict(nx.all_pairs_shortest_path_length(Q))
    for i in range(k):
        for j in range(k): Ed += Fraction(wi[i]*wi[j]*dist[i][j],W*W)
    formula=Fraction(W*W,m)*Ed - Fraction((2*m+1)*(k-1),2*m)
    assert raw==formula
    bridge_checks+=1
print("C6_exact_bridge_identity_checks",bridge_checks,"PASS")

# Independent R05 n=13 finite core via prime-degree affine classification.
pmod=13; units=set(range(1,pmod)); minus1=pmod-1
def subgroup_generated(a):
    H={1}; x=1
    while True:
        x=(x*a)%pmod
        if x in H: break
        H.add(x)
    return frozenset(H)
subs={subgroup_generated(a) for a in units}
orders=sorted(len(H) for H in subs)
orders_with_minus=sorted(len(H) for H in subs if minus1 in H)
assert orders==[1,2,3,4,6,12]
assert orders_with_minus==[2,4,6,12]
def cayley_from_S(S):
    G=nx.Graph(); G.add_nodes_from(range(pmod))
    for x in range(pmod):
        for a in S: G.add_edge(x,(x+a)%pmod)
    return G
reps=[]
for d in orders_with_minus:
    Hs=next(H for H in subs if len(H)==d and minus1 in H)
    G=cayley_from_S(Hs)
    assert nx.is_connected(G); assert set(dict(G.degree()).values())=={d}
    reps.append(G)
assert all(not nx.is_isomorphic(reps[i],reps[j]) for i in range(len(reps)) for j in range(i))
print("R05_n13_prime_affine_audit degrees",orders_with_minus,
      "four_classes_conditional_on_Burnside_prime_degree_theorem PASS")

print("RESULT PASS")
