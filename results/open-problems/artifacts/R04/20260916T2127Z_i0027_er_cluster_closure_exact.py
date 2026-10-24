#!/usr/bin/env python3
import itertools
from fractions import Fraction
import sympy as sp
import networkx as nx

print("R04 I0027 effective-resistance clustering closure checker")
print("SELF-CHECK: exact finite/symbolic core only; Alev-Anari-Lau-Oveis Gharan Theorem 3 and published barbell lower bound are external inputs")

# --------------------------------------------------------------------
# 1. Scaling bookkeeping for delta_n=n^(1/10).
# Alev: q = O(m/delta), eps = O(delta^3*n/m).
# In the dense regime m=Theta(n^2):
# C4 errors are O(n^3/delta)+O(n^3/delta^2);
# cluster internal-resistance error is O(delta^3*n^2).
# --------------------------------------------------------------------
a = sp.Rational(1,10)
assert 3-a < 3
assert 3-2*a < 3
assert 2+3*a < 3
print("scaling_exponents",
      "C4_linear", 3-a,
      "C4_quadratic", 3-2*a,
      "cluster_internal", 2+3*a,
      "all_strictly_below_3 PASS")

# --------------------------------------------------------------------
# 2. C6 probability-vector inequality:
# (1-Q2)/S^2 <= 1/4 where S=sum sqrt(p_i), Q2=sum p_i^2.
# The analytic proof is Q2*S^2 >=1 by Holder, then <=Q2(1-Q2)<=1/4.
# Exhaustive exact sanity check on square-rational distributions p_i=a_i^2/sum a_j^2.
# --------------------------------------------------------------------
tested=0
for k in range(1,6):
    for vec in itertools.product(range(1,6), repeat=k):
        den=sum(x*x for x in vec)
        ps=[Fraction(x*x,den) for x in vec]
        Q2=sum(p*p for p in ps)
        # For these square-rational p, S^2 is rational:
        Snum=sum(vec)
        S2=Fraction(Snum*Snum, den)
        assert Q2*S2 >= 1
        lhs=(1-Q2)/S2
        assert lhs <= Fraction(1,4)
        tested += 1
print("C6_probability_inequality_exact_cases",tested,"PASS")

# --------------------------------------------------------------------
# 3. Exact finite graph verification of the cluster-tree resistance split.
# Build H from complete induced clusters joined by one bridge per quotient-tree edge.
# Verify:
# R_H(u,v) = quotient bridge distance + sum of within-cluster terminal resistances,
# hence R_H(u,v)-d_Q(cluster(u),cluster(v)) <= (#visited clusters)*eps.
# Also verify K(H) <= K_br(H)+m*n*eps.
# --------------------------------------------------------------------
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

def all_resistances(G):
    nodes,idx,L=laplacian(G)
    n=len(nodes)
    # grounded inverse
    R=L[:n-1,:n-1].inv()
    ans={}
    for ia,u in enumerate(nodes):
        for ib,v in enumerate(nodes):
            if ia==ib:
                ans[(u,v)]=sp.Rational(0)
            elif ia==n-1:
                ans[(u,v)]=sp.cancel(R[ib,ib])
            elif ib==n-1:
                ans[(u,v)]=sp.cancel(R[ia,ia])
            else:
                ans[(u,v)]=sp.cancel(R[ia,ia]+R[ib,ib]-2*R[ia,ib])
    return ans

def exact_kemeny(G,R=None):
    if R is None: R=all_resistances(G)
    m=G.number_of_edges()
    s=sp.Rational(0)
    ns=list(G.nodes())
    for i,u in enumerate(ns):
        for v in ns[i+1:]:
            s += G.degree(u)*G.degree(v)*R[(u,v)]
    return sp.cancel(s/(2*m))

def bridge_contribution(G,R=None):
    # exact K_br = 1/(2m) sum over bridges vol(A)vol(Ac)
    m=G.number_of_edges()
    out=sp.Rational(0)
    for u,v in nx.bridges(G):
        G2=G.copy(); G2.remove_edge(u,v)
        comps=list(nx.connected_components(G2))
        assert len(comps)==2
        A=comps[0]
        vol=sum(G.degree(x) for x in A)
        out += vol*(2*m-vol)
    return sp.Rational(out,2*m)

def make_cluster_tree(sizes, qedges):
    G=nx.Graph()
    clusters=[]
    nxt=0
    for s in sizes:
        C=list(range(nxt,nxt+s)); nxt+=s
        clusters.append(C)
        for u,v in itertools.combinations(C,2):
            G.add_edge(u,v)
    # deterministic distinct attachment vertices where possible
    used=[0]*len(sizes)
    for i,j in qedges:
        ui=clusters[i][used[i] % len(clusters[i])]; used[i]+=1
        vj=clusters[j][used[j] % len(clusters[j])]; used[j]+=1
        G.add_edge(ui,vj)
    return G,clusters

examples=[
    ([3,2,4],[(0,1),(1,2)]),
    ([2,3,2,3],[(0,1),(1,2),(1,3)]),
    ([4,2,2,3,2],[(0,1),(1,2),(2,3),(2,4)]),
]
for sizes,qedges in examples:
    H,clusters=make_cluster_tree(sizes,qedges)
    assert nx.is_tree(nx.Graph(qedges))
    RH=all_resistances(H)
    qG=nx.Graph(); qG.add_nodes_from(range(len(sizes))); qG.add_edges_from(qedges)
    cluster_of={}
    for i,C in enumerate(clusters):
        for u in C: cluster_of[u]=i
    eps=sp.Rational(0)
    for C in clusters:
        Gi=H.subgraph(C).copy()
        Ri=all_resistances(Gi)
        eps=max(eps,max(Ri.values()))
    for u,v in itertools.combinations(H.nodes(),2):
        r=nx.shortest_path_length(qG,cluster_of[u],cluster_of[v])
        # lower bound by the r unit bridges, upper bound using at most r+1 cluster traversals
        assert RH[(u,v)] >= r
        assert RH[(u,v)] - r <= (r+1)*eps
        assert RH[(u,v)] - r <= H.number_of_nodes()*eps
    K=exact_kemeny(H,RH)
    Kbr=bridge_contribution(H)
    m=H.number_of_edges(); n=H.number_of_nodes()
    assert K <= Kbr + m*n*eps
    print("cluster_tree_example",sizes,qedges,
          "n",n,"m",m,"eps",eps,"K",K,"Kbr",Kbr,
          "split_bound PASS")

# --------------------------------------------------------------------
# 4. Exact sparse-surgery algebra sanity:
# If q/m ->0 and m=Theta(n^2), C4 correction / n^3 ->0.
# Symbolic substitution q=m/delta, m=A n^2 checks powers.
# --------------------------------------------------------------------
n,delta,A,C=sp.symbols('n delta A C', positive=True)
m=A*n**2
q=C*m/delta
err=sp.expand(2*q*n + q**2*n/m)
err_norm=sp.simplify(err/n**3)
assert sp.simplify(err_norm - (2*A*C/delta + A*C**2/delta**2))==0
print("C4_normalized_error",err_norm,"PASS")

# --------------------------------------------------------------------
# 5. Fixed optimization:
# s^2(1-s)/8 <= 1/54, equality s=2/3.
# --------------------------------------------------------------------
s=sp.symbols('s', real=True)
f=s**2*(1-s)/8
assert sp.factor(sp.diff(f,s)) == -s*(3*s-2)/8
assert sp.simplify(f.subs(s,sp.Rational(2,3))-sp.Rational(1,54))==0
print("C6_optimization max 1/54 at s=2/3 PASS")

print("RESULT PASS")
