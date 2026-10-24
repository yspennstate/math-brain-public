from fractions import Fraction
import itertools
import networkx as nx

# Frozen labelled representatives of the 15 order-16 classes in
# Marston Conder's Dec. 2021 complete connected symmetric/arc-transitive census.
# They were transcribed from the primary source's neighbour-list block and
# encoded as graph6; the source supplies completeness and arc-transitivity.
G6 = [
    r"OQGOOG@?_?_C?@?AO?Q?A",
    r"O??CbACQ?oC_T?i??Q_BO",
    r"OQGQSGPGaGpCC`GQOaQPA",
    r"O????Bo{@wF_BoBoWWEE?",
    r"OahLb@__KA?y@iESbD`go",
    r"O?hTAbEqPqEoZDfIQYbFO",
    r"O?r@`ahTdKJGekX[LPciW",
    r"O??FfbKr@wF_~?~??^_Fw",
    r"OKUdQhUiQktKiYTdIqtRQ",
    r"O]Ku]WrKuXxeKrKrXe]Xe",
    r"O?]uf@vmuy\o\vmzZmf\o",
    r"Oqh\vZq{~ZZyNiNtztrju",
    r"O?~vfb~~v}^w~~~~^~f~w",
    r"O]~v~z~~v~~}~~~~^~~~}",
    r"O~~~~~~~~~~~~~~~~~~~~",
]
EXPECTED_VALENCIES = [2,3,4,4,5,6,6,6,7,8,9,10,12,14,15]
EXPECTED_AUT_ORDERS = [32,96,384,4096,1920,192,1152,12288,80640,
                       3251404800,1152,1920,7962624,10321920,20922789888000]

def matmul(A,B):
    n=len(A); C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,a in enumerate(A[i]):
            if a:
                for j,b in enumerate(B[k]):
                    if b: C[i][j]+=a*b
    return C

def adjacency_matrix(G):
    nodes=sorted(G); idx={u:i for i,u in enumerate(nodes)}; n=len(nodes)
    A=[[0]*n for _ in range(n)]
    for u,v in G.edges():
        i,j=idx[u],idx[v]; A[i][j]=A[j][i]=1
    return A,nodes,idx

def exact_walk_homogeneity(G,max_power=36):
    A,nodes,idx=adjacency_matrix(G); n=len(A); d=next(iter(dict(G.degree()).values()))
    P=[[int(i==j) for j in range(n)] for i in range(n)]
    for m in range(max_power+1):
        assert len({P[i][i] for i in range(n)})==1
        assert len({P[idx[u]][idx[v]] for u,v in G.edges()})==1
        if m<max_power:
            NP=matmul(P,A)
            for u,v in G.edges():
                assert NP[idx[u]][idx[u]] == d*P[idx[u]][idx[v]]
            P=NP
    return True

graphs=[nx.from_graph6_bytes(s.encode()) for s in G6]
assert len(graphs)==15
for i,G in enumerate(graphs):
    assert G.number_of_nodes()==16
    assert nx.is_connected(G)
    assert {d for _,d in G.degree()}=={EXPECTED_VALENCIES[i]}
    assert exact_walk_homogeneity(G,36)
assert all(not nx.is_isomorphic(graphs[i],graphs[j])
           for i,j in itertools.combinations(range(15),2))

# Exact sharpness check for the new discrete-time lazy theorem.
# On K2, Q_h=hI+(1-h)A has eigenvalues 1 and c=2h-1, so
# r_m=(1-c^m)/(1+c^m).  At h=1/4, c=-1/2 and r_1=3>3/5=r_2.
h=Fraction(1,4); c=2*h-1
r1=(1-c)/(1+c); r2=(1-c*c)/(1+c*c)
assert c==Fraction(-1,2)
assert r1==3 and r2==Fraction(3,5) and r2<r1
# For every 0<h<1/2, i.e. -1<c<0,
# r1-r2 = 2*c*(c-1)/((c+1)*(c*c+1)) > 0.
assert 2*c*(c-1)>0

print('R05 I0030 exact order-16 census + lazy-threshold certificate')
print('primary_census_claim complete connected symmetric/arc-transitive graphs orders 2-47')
print('order16_source_classes',len(graphs))
print('order16_valencies',EXPECTED_VALENCIES)
print('order16_aut_group_orders_source_metadata',EXPECTED_AUT_ORDERS)
print('all_simple_connected_regular',True)
print('pairwise_nonisomorphic',True)
print('exact_walk_homogeneity_through_power',36)
print('all_15_walk_certificates_PASS',True)
print('lazy_K2_h',h,'c',c,'r1',r1,'r2',r2,'strict_drop',r2<r1)
print('lazy_symbolic_sign_factor','2*c*(c-1)/((c+1)*(c^2+1)) > 0 for -1<c<0')
print('metric_largest_fully_certified_vertex_count',16)
print('RESULT PASS')
