#!/usr/bin/env python3
"""Exact n=10 certificate for R05 / Aldous-Fill Open Problem 7.30 frozen edge MNHD statement.

Input class completeness comes from Conder--Verret (Algebraic Combinatorics 2019),
worked example order 10: exactly 8 connected vertex-transitive edge-transitive graphs,
and no half-arc-transitive graph of order 10. The script constructs those 8 graphs
explicitly and checks, using exact graph isomorphism / integer walk counts, that they
are pairwise nonisomorphic, connected, regular and arc-transitive, and verifies the
coefficient identity behind the frozen heat-ratio theorem.

No floating point arithmetic is used for the finite certificate.
"""
from itertools import combinations
import networkx as nx
from networkx.algorithms.isomorphism import categorical_node_match

N=10

def cycle10():
    return nx.cycle_graph(N)

def petersen():
    return nx.petersen_graph()

def petersen_comp():
    return nx.complement(petersen())

def circulant_10_23():
    G=nx.Graph(); G.add_nodes_from(range(N))
    for x in range(N):
        for s in (2,3,-2,-3):
            G.add_edge(x,(x+s)%N)
    return G

def k10():
    return nx.complete_graph(N)

def k10_minus_5k2():
    G=k10()
    for i in range(5): G.remove_edge(2*i,2*i+1)
    return G

def k55():
    return nx.complete_bipartite_graph(5,5)

def crown_5():
    G=k55()
    for i in range(5): G.remove_edge(i,5+i)
    return G

GRAPHS={
    'C10': cycle10(),
    'Petersen': petersen(),
    'PetersenComplement': petersen_comp(),
    'C10_{2,3}': circulant_10_23(),
    'K10': k10(),
    'K10_minus_5K2': k10_minus_5k2(),
    'K5,5': k55(),
    'K5,5_minus_5K2': crown_5(),
}

def relabel_with_marks(G,a,b):
    H=G.copy()
    nx.set_node_attributes(H,0,'mark')
    H.nodes[a]['mark']=1
    H.nodes[b]['mark']=2
    return H

def arc_transitive_exact(G):
    arcs=[(u,v) for u,v in G.edges() for (u,v) in ((u,v),(v,u))]
    s,t=arcs[0]
    Gs=relabel_with_marks(G,s,t)
    nm=categorical_node_match('mark',0)
    for u,v in arcs:
        Gt=relabel_with_marks(G,u,v)
        if not nx.is_isomorphic(Gs,Gt,node_match=nm):
            return False,(u,v)
    return True,None

def matmul(A,B):
    n=len(A); m=len(B); p=len(B[0])
    C=[[0]*p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            aik=A[i][k]
            if aik:
                for j in range(p):
                    C[i][j]+=aik*B[k][j]
    return C

def adjacency_int(G):
    return [[1 if G.has_edge(i,j) else 0 for j in range(N)] for i in range(N)]

def walk_identity(G,max_m=24):
    d=G.degree(0)
    A=adjacency_int(G)
    I=[[int(i==j) for j in range(N)] for i in range(N)]
    P=I
    # For every m >= 0: (A^{m+1})_{xx} = d (A^m)_{xy} on every oriented edge.
    for m in range(max_m+1):
        AP=matmul(A,P)
        diag={P[i][i] for i in range(N)}
        edge={P[u][v] for u,v in G.edges()} | {P[v][u] for u,v in G.edges()}
        assert len(diag)==1, (m,'diag',diag)
        assert len(edge)==1, (m,'edge',edge)
        for u,v in G.edges():
            assert AP[u][u] == d*P[u][v], (m,u,v,AP[u][u],d*P[u][v])
            assert AP[v][v] == d*P[v][u], (m,v,u,AP[v][v],d*P[v][u])
        P=AP
    return True

def main():
    assert len(GRAPHS)==8
    names=list(GRAPHS)
    # Pairwise nonisomorphic: exact VF2 decision.
    for a,b in combinations(names,2):
        assert not nx.is_isomorphic(GRAPHS[a],GRAPHS[b]), (a,b)

    print('source_class_size_order_10',8)
    print('source_completeness_basis','Conder-Verret-2019-worked-example-order-10')
    print('name degree edges diameter graph6 arc_orbit_cert walk_identity_m_le_24')
    degrees=[]
    for name in names:
        G=GRAPHS[name]
        assert G.number_of_nodes()==N
        assert nx.number_of_selfloops(G)==0
        assert nx.is_connected(G)
        ds={d for _,d in G.degree()}
        assert len(ds)==1
        d=next(iter(ds)); degrees.append(d)
        ok,bad=arc_transitive_exact(G)
        assert ok,(name,bad)
        assert walk_identity(G,24)
        g6=nx.to_graph6_bytes(G,header=False).decode().strip()
        print(name,d,G.number_of_edges(),nx.diameter(G),g6,'PASS','PASS')

    # Exact source theorem coefficient consequences at t=0.
    # r'_{xy}(0)=1/d, so among the order-10 source class K10 is the unique
    # least initial slope and C10 is the unique greatest initial slope.
    mind=max(degrees); maxd=min(degrees)
    assert names[degrees.index(mind)]=='K10'
    assert names[degrees.index(maxd)]=='C10'
    print('initial_slope_min','K10','1/9')
    print('initial_slope_max','C10','1/2')
    print('metric_largest_fully_certified_vertex_count',10)
    print('RESULT PASS')

if __name__=='__main__': main()
