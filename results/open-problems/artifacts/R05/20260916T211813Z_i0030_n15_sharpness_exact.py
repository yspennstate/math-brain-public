#!/usr/bin/env python3
"""
R05 / I0030 exact run-11 certificate.

Finite cores:
(1) Complete order-15 class: hard-coded from Marston Conder's December 2021
    complete connected symmetric (arc-transitive) graph census, order 15.
    We independently verify graph structure, pairwise nonisomorphism,
    and exact edge-walk identities; arc-transitivity/completeness are taken
    from Conder's primary census.
(2) Exact sharpness obstruction outside the source class:
    a connected simple unweighted 4-regular graph on 9 vertices for which an
    adjacent normalized heat ratio has negative derivative at t = 12 log 2.
    The sign is certified by rational arithmetic using the integral spectrum.
No floating-point arithmetic is used in any claimed finite certificate.
"""
from fractions import Fraction
import networkx as nx

# ---------- helpers ----------
def graph_from_adj(adj):
    G=nx.Graph()
    n=len(adj)
    G.add_nodes_from(range(1,n+1))
    for u,nb in adj.items():
        for v in nb:
            G.add_edge(u,v)
    return G

def directed_arc_transitive_exact(G):
    arcs=[(u,v) for u,v in G.edges() for (u,v) in [(u,v),(v,u)]]
    ref=arcs[0]
    def marked(u,v):
        H=G.copy()
        nx.set_node_attributes(H,0,"mark")
        H.nodes[u]["mark"]=1
        H.nodes[v]["mark"]=2
        return H
    R=marked(*ref)
    nm=nx.algorithms.isomorphism.categorical_node_match("mark",0)
    for a in arcs:
        if not nx.is_isomorphic(R, marked(*a), node_match=nm):
            return False
    return True

def matmul_int(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][r]*B[r][j] for r in range(k)) for j in range(m)] for i in range(n)]

def int_walk_checks(G,mmax):
    nodes=sorted(G.nodes()); ix={v:i for i,v in enumerate(nodes)}
    n=len(nodes); d=G.degree(nodes[0])
    A=[[0]*n for _ in range(n)]
    for u,v in G.edges():
        i,j=ix[u],ix[v]; A[i][j]=A[j][i]=1
    P=[[int(i==j) for j in range(n)] for i in range(n)]
    powers=[P]
    for _ in range(mmax+1):
        powers.append(matmul_int(powers[-1],A))
    for m in range(mmax+1):
        diag={powers[m][i][i] for i in range(n)}
        edgevals={powers[m][ix[u]][ix[v]] for u,v in G.edges()}
        if len(diag)!=1 or len(edgevals)!=1:
            return False
        # A^{m+1}_{xx}=sum_{y~x} A^m_{xy}=d * common edge value
        lhs=powers[m+1][0][0]
        rhs=d*next(iter(edgevals))
        if lhs!=rhs:
            return False
    return True

# ---------- Conder order-15 census ----------
ADJS=[]
ADJS.append({
1:[2,15],2:[1,3],3:[2,4],4:[3,5],5:[4,6],6:[5,7],7:[6,8],8:[7,9],
9:[8,10],10:[9,11],11:[10,12],12:[11,13],13:[12,14],14:[13,15],15:[1,14]})
ADJS.append({
1:[2,5,12,15],2:[1,3,6,13],3:[2,4,7,14],4:[3,5,8,15],5:[1,4,6,9],
6:[2,5,7,10],7:[3,6,8,11],8:[4,7,9,12],9:[5,8,10,13],10:[6,9,11,14],
11:[7,10,12,15],12:[1,8,11,13],13:[2,9,12,14],14:[3,10,13,15],15:[1,4,11,14]})
ADJS.append({
1:[2,5,11,12],2:[1,7,10,12],3:[4,8,12,15],4:[3,5,8,14],5:[1,4,11,14],
6:[7,9,14,15],7:[2,6,10,14],8:[3,4,10,13],9:[6,11,13,15],10:[2,7,8,13],
11:[1,5,9,13],12:[1,2,3,15],13:[8,9,10,11],14:[4,5,6,7],15:[3,6,9,12]})
ADJS.append({
1:[3,4,6,8,10,13],2:[4,6,9,11,13,15],3:[1,5,7,9,11,13],
4:[1,2,7,9,10,12],5:[3,6,9,10,12,15],6:[1,2,5,8,11,12],
7:[3,4,8,11,12,15],8:[1,6,7,9,14,15],9:[2,3,4,5,8,14],
10:[1,4,5,11,14,15],11:[2,3,6,7,10,14],12:[4,5,6,7,13,14],
13:[1,2,3,12,14,15],14:[8,9,10,11,12,13],15:[2,5,7,8,10,13]})
ADJS.append({
1:[2,5,7,10,12,15],2:[1,3,6,8,11,13],3:[2,4,7,9,12,14],
4:[3,5,8,10,13,15],5:[1,4,6,9,11,14],6:[2,5,7,10,12,15],
7:[1,3,6,8,11,13],8:[2,4,7,9,12,14],9:[3,5,8,10,13,15],
10:[1,4,6,9,11,14],11:[2,5,7,10,12,15],12:[1,3,6,8,11,13],
13:[2,4,7,9,12,14],14:[3,5,8,10,13,15],15:[1,4,6,9,11,14]})
ADJS.append({
1:[2,3,5,8,9,12,14,15],2:[1,3,4,6,9,10,13,15],3:[1,2,4,5,7,10,11,14],
4:[2,3,5,6,8,11,12,15],5:[1,3,4,6,7,9,12,13],6:[2,4,5,7,8,10,13,14],
7:[3,5,6,8,9,11,14,15],8:[1,4,6,7,9,10,12,15],9:[1,2,5,7,8,10,11,13],
10:[2,3,6,8,9,11,12,14],11:[3,4,7,9,10,12,13,15],12:[1,4,5,8,10,11,13,14],
13:[2,5,6,9,11,12,14,15],14:[1,3,6,7,10,12,13,15],15:[1,2,4,7,8,11,13,14]})
ADJS.append({
1:[2,5,7,9,11,12,14,15],2:[1,3,5,7,8,10,12,14],3:[2,4,6,8,10,12,14,15],
4:[3,5,6,8,11,13,14,15],5:[1,2,4,7,8,11,13,14],6:[3,4,7,9,10,13,14,15],
7:[1,2,5,6,9,10,13,14],8:[2,3,4,5,10,11,12,13],9:[1,6,7,10,11,12,13,15],
10:[2,3,6,7,8,9,12,13],11:[1,4,5,8,9,12,13,15],12:[1,2,3,8,9,10,11,15],
13:[4,5,6,7,8,9,10,11],14:[1,2,3,4,5,6,7,15],15:[1,3,4,6,9,11,12,14]})
ADJS.append({
1:[2,3,5,6,8,9,11,12,14,15],2:[1,3,4,6,7,9,10,12,13,15],
3:[1,2,4,5,7,8,10,11,13,14],4:[2,3,5,6,8,9,11,12,14,15],
5:[1,3,4,6,7,9,10,12,13,15],6:[1,2,4,5,7,8,10,11,13,14],
7:[2,3,5,6,8,9,11,12,14,15],8:[1,3,4,6,7,9,10,12,13,15],
9:[1,2,4,5,7,8,10,11,13,14],10:[2,3,5,6,8,9,11,12,14,15],
11:[1,3,4,6,7,9,10,12,13,15],12:[1,2,4,5,7,8,10,11,13,14],
13:[2,3,5,6,8,9,11,12,14,15],14:[1,3,4,6,7,9,10,12,13,15],
15:[1,2,4,5,7,8,10,11,13,14]})
ADJS.append({
1:[2,3,4,5,7,9,10,11,12,13,14,15],2:[1,3,5,6,7,8,10,11,12,13,14,15],
3:[1,2,4,5,6,8,9,10,12,13,14,15],4:[1,3,5,6,7,8,10,11,12,13,14,15],
5:[1,2,3,4,6,7,8,9,11,12,13,14],6:[2,3,4,5,7,9,10,11,12,13,14,15],
7:[1,2,4,5,6,8,9,10,12,13,14,15],8:[2,3,4,5,7,9,10,11,12,13,14,15],
9:[1,3,5,6,7,8,10,11,12,13,14,15],10:[1,2,3,4,6,7,8,9,11,12,13,14],
11:[1,2,4,5,6,8,9,10,12,13,14,15],12:[1,2,3,4,5,6,7,8,9,10,11,15],
13:[1,2,3,4,5,6,7,8,9,10,11,15],14:[1,2,3,4,5,6,7,8,9,10,11,15],
15:[1,2,3,4,6,7,8,9,11,12,13,14]})
ADJS.append({i:[j for j in range(1,16) if j!=i] for i in range(1,16)})

graphs=[graph_from_adj(a) for a in ADJS]
expected_val=[2,4,4,6,6,8,8,10,12,14]
for i,G in enumerate(graphs):
    assert nx.is_connected(G)
    assert all(G.degree(v)==expected_val[i] for v in G)
    assert all(u not in G[u] for u in G)
    # adjacency source consistency
    assert all(set(G.neighbors(u))==set(ADJS[i][u]) for u in G)
for i in range(10):
    for j in range(i+1,10):
        assert not nx.is_isomorphic(graphs[i],graphs[j])
for i,G in enumerate(graphs):
    # Conder's primary census is the completeness/arc-transitivity source.
    # Here we independently exact-check the algebraic edge-homogeneity
    # consequence needed by the frozen theorem.
    assert int_walk_checks(G,36), i

# ---------- exact unweighted regular counterexample outside source class ----------
# graph6 HUpdIwy, zero-based edge list:
bad_edges=[
(0,2),(0,3),(0,4),(0,6),
(1,3),(1,4),(1,5),(1,7),
(2,5),(2,6),(2,8),
(3,7),(3,8),
(4,7),(4,8),
(5,6),(5,7),
(6,8)]
Gb=nx.Graph(); Gb.add_nodes_from(range(9)); Gb.add_edges_from(bad_edges)
assert nx.is_connected(Gb)
assert all(Gb.degree(v)==4 for v in Gb)

# Exact rational matrix helpers
def zmat(n):
    return [[Fraction(0) for _ in range(n)] for __ in range(n)]
def eye(n):
    M=zmat(n)
    for i in range(n): M[i][i]=Fraction(1)
    return M
def madd(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]
def mscale(c,A):
    return [[c*x for x in row] for row in A]
def mmul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum((A[i][r]*B[r][j] for r in range(k)),Fraction(0)) for j in range(m)] for i in range(n)]
def mpow(A,k):
    R=eye(len(A)); X=A
    while k:
        if k&1: R=mmul(R,X)
        X=mmul(X,X); k//=2
    return R
def iszero(A):
    return all(x==0 for row in A for x in row)

Ab=zmat(9)
for u,v in bad_edges: Ab[u][v]=Ab[v][u]=Fraction(1)
roots=[-3,-2,-1,0,1,2,4]
# m(A)=prod(A-rI)=0 certifies spectrum lies in these distinct integer roots.
M=eye(9)
for r in roots:
    M=mmul(M,madd(Ab,mscale(Fraction(-r),eye(9))))
assert iszero(M)

# Interpolating polynomial for 8^x on the spectral roots:
coeff=[Fraction(184320,184320), Fraction(1598352,184320),
       Fraction(746956,184320), Fraction(-1275960,184320),
       Fraction(-300125,184320), Fraction(403368,184320),
       Fraction(117649,184320)]
def peval_scalar(k):
    s=Fraction(0)
    for c in reversed(coeff): s=s*k+c
    return s
for r in roots:
    assert peval_scalar(Fraction(r)) == Fraction(8) ** r

B=zmat(9)
for k,c in enumerate(coeff):
    B=madd(B,mscale(c,mpow(Ab,k)))
# At t0=12 log 2 and degree d=4:
# exp(t0(A/4-I)) = exp(-t0) * exp(3 log 2 A)
#                  = exp(-t0) * 8^A
#                  = common positive scalar * B.
# The scalar cancels in q=H_xy/H_xx and in q'.
Gen=madd(mscale(Fraction(1,4),Ab),mscale(Fraction(-1),eye(9)))
Bp=mmul(B,Gen)
u,v=0,2
num=Bp[u][v]*B[u][u]-B[u][v]*Bp[u][u]
den=B[u][u]*B[u][u]
der=num/den
assert B[u][u]>0 and den>0 and num<0
assert B[u][u]==Fraction(10591507,23040)
assert B[u][v]==Fraction(21245903,46080)
assert Bp[u][u]==Fraction(-85033,30720)
assert Bp[u][v]==Fraction(-176027,61440)
assert num==Fraction(-1926277763,47185920)
assert der==Fraction(-86682499335,448720082124196)

# Show that the graph is outside the source symmetry class and even outside
# 1-walk-regularity: edge common-neighbor counts vary.
cn=sorted({len(set(Gb.neighbors(a)) & set(Gb.neighbors(b))) for a,b in Gb.edges()})
assert cn==[0,1,3]
assert len(cn)>1  # hence not edge-transitive, so not arc-transitive

# ---------- exact small deformation from the order-9 arc-transitive class ----------
# Prior retained n=9 certificate identifies graph6 H{dQXgj as the unique
# degree-4 arc-transitive isomorphism type on 9 vertices. We exhaust all
# 9! vertex relabelings and compute the exact smallest edge symmetric difference.
import itertools
Gat=nx.from_graph6_bytes(b"H{dQXgj")
assert Gat.number_of_nodes()==9 and Gat.number_of_edges()==18
assert all(Gat.degree(v)==4 for v in Gat)
Ebad={tuple(sorted(e)) for e in Gb.edges()}
Eat={tuple(sorted(e)) for e in Gat.edges()}
best_diff=10**9
best_perm=None
best_relab=None
for perm in itertools.permutations(range(9)):
    Er={tuple(sorted((perm[u],perm[v]))) for u,v in Eat}
    diff=len(Er ^ Ebad)
    if diff<best_diff:
        best_diff=diff
        best_perm=perm
        best_relab=Er
        if best_diff==0:
            break
assert best_diff==8
removed=sorted(best_relab-Ebad)
added=sorted(Ebad-best_relab)
assert len(removed)==4 and len(added)==4

print("R05 I0030 run-11 exact certificate")
print("order15_conder_complete_classes", len(graphs))
print("order15_valencies", expected_val)
print("order15_pairwise_nonisomorphic", True)
print("order15_arc_transitive_primary_census_source", True)
print("order15_edge_walk_homogeneity_exact_through_m", 36)
print("order15_walk_identity_exact_through_m", 36)
print("metric_largest_fully_certified_vertex_count", 15)
print("regular_counterexample_graph6", nx.to_graph6_bytes(Gb,header=False).strip().decode())
print("regular_counterexample_n_d", (9,4))
print("regular_counterexample_edge_common_neighbor_counts", cn)
print("regular_counterexample_time", "12*log(2)")
print("regular_counterexample_edge", (u,v))
print("regular_counterexample_B00", B[u][u])
print("regular_counterexample_B02", B[u][v])
print("regular_counterexample_Bp00", Bp[u][u])
print("regular_counterexample_Bp02", Bp[u][v])
print("regular_counterexample_derivative", der)
print("regular_counterexample_negative_derivative_exact", der<0)
print("deformation_from_n9_degree4_AT_graph6", "H{dQXgj")
print("deformation_min_edge_symmetric_difference_over_all_9factorial_relabelings", best_diff)
print("deformation_edge_replacements", len(removed))
print("deformation_removed_edges", removed)
print("deformation_added_edges", added)
print("RESULT PASS")
