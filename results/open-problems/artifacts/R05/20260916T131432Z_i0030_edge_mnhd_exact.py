#!/usr/bin/env python3
"""Exact finite certificate for R05 / Aldous-Fill Open Problem 7.30.

Frozen statement M_edge:
For every finite simple connected arc-transitive graph G, continuous-time
simple random walk with generator P-I (P=A/d), and every arc x~y,
    r_xy(t) = H_t(x,y)/H_t(x,x)
is nondecreasing for t>=0.

This checker does NOT use floating-point heat kernels. It exhausts the
Read-Wilson / NetworkX Graph Atlas through 7 vertices, identifies the full
arc-transitive class by exact graph automorphisms, and verifies the integer
walk-count identities underlying a'(t)=b(t)-a(t).
The monotonicity itself is proved analytically in the run report by spectral
log-convexity; the finite certificate audits the class and its symmetry
identities exactly.
"""
from __future__ import annotations
import hashlib
from collections import Counter, defaultdict
import networkx as nx
import networkx.generators.atlas as atlas_mod
from networkx.algorithms.isomorphism import GraphMatcher

MAX_N = 7
EXPECTED_ALL = {2:2, 3:4, 4:11, 5:34, 6:156, 7:1044}
EXPECTED_CONNECTED = {2:1, 3:2, 4:6, 5:21, 6:112, 7:853}
EXPECTED_ARC = {2:1, 3:1, 4:2, 5:2, 6:4, 7:2}
EXPECTED_CODES = {
    2:['A_'],
    3:['Bw'],
    4:['Cl','C~'],
    5:['Dhc','D~{'],
    6:['EhEG','ElUg','EznW','E~~w'],
    7:['FhCKG','F~~~w'],
}

def graph6(G: nx.Graph) -> str:
    return nx.to_graph6_bytes(G, header=False).decode('ascii').strip()

def is_arc_transitive_exact(G: nx.Graph):
    degs = [d for _,d in G.degree()]
    if len(set(degs)) != 1 or not G.edges:
        return False, 0
    x,y = next(iter(G.edges()))
    all_arcs = {(u,v) for u,v in G.edges() for (u,v) in ((u,v),(v,u))}
    orbit = set()
    aut_count = 0
    for phi in GraphMatcher(G,G).isomorphisms_iter():
        aut_count += 1
        orbit.add((phi[x],phi[y]))
    return orbit == all_arcs, aut_count

def matmul_int(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][r]*B[r][j] for r in range(k)) for j in range(m)] for i in range(n)]

def adjacency_int(G):
    n=G.number_of_nodes()
    return [[1 if G.has_edge(i,j) else 0 for j in range(n)] for i in range(n)]

def exact_walk_identities(G: nx.Graph):
    n=G.number_of_nodes(); d=next(iter(dict(G.degree()).values()))
    A=adjacency_int(G)
    M=[[int(i==j) for j in range(n)] for i in range(n)]
    arcs=[(u,v) for u,v in G.edges() for (u,v) in ((u,v),(v,u))]
    diags=[]; arcvals=[]
    for m in range(0,2*n+2):
        diag={M[i][i] for i in range(n)}
        aval={M[u][v] for u,v in arcs}
        assert len(diag)==1, (G.name,m,'diag')
        assert len(aval)==1, (G.name,m,'arc')
        diags.append(next(iter(diag)))
        arcvals.append(next(iter(aval)))
        M=matmul_int(M,A)
    for m in range(0,2*n+1):
        assert diags[m+1] == d*arcvals[m], (G.name,m,diags[m+1],d,arcvals[m])
    return d, diags[:n+2], arcvals[:n+1]

def main():
    raw=open(atlas_mod.ATLAS_FILE,'rb').read()
    print('networkx_version', nx.__version__)
    print('atlas_file_sha256', hashlib.sha256(raw).hexdigest())
    atlas=nx.graph_atlas_g()
    assert len(atlas)==1253
    all_counts=Counter(G.number_of_nodes() for G in atlas if 2<=G.number_of_nodes()<=MAX_N)
    print('all_graph_counts', dict(sorted(all_counts.items())))
    assert dict(sorted(all_counts.items()))==EXPECTED_ALL

    conn_counts=Counter()
    arc_records=defaultdict(list)
    for G in atlas:
        n=G.number_of_nodes()
        if not (2<=n<=MAX_N):
            continue
        if not nx.is_connected(G):
            continue
        conn_counts[n]+=1
        ok,aut_count=is_arc_transitive_exact(G)
        if not ok:
            continue
        d,diag,arc=exact_walk_identities(G)
        arc_records[n].append((G.name,graph6(G),d,aut_count,diag,arc))

    print('connected_counts', dict(sorted(conn_counts.items())))
    assert dict(sorted(conn_counts.items()))==EXPECTED_CONNECTED
    arc_counts={n:len(arc_records[n]) for n in range(2,MAX_N+1)}
    print('arc_transitive_counts', arc_counts)
    assert arc_counts==EXPECTED_ARC
    for n in range(2,MAX_N+1):
        codes=[r[1] for r in arc_records[n]]
        print(f'n={n} arc_graph6={codes}')
        assert codes==EXPECTED_CODES[n]
        for name,code,d,aut_count,diag,arc in arc_records[n]:
            print(f'  {name} g6={code} d={d} aut={aut_count} diag_m0..={diag} arc_m0..={arc}')

    total_conn=sum(conn_counts.values())
    total_arc=sum(len(v) for v in arc_records.values())
    print('total_connected_checked', total_conn)
    print('total_arc_transitive', total_arc)
    print('metric_largest_fully_certified_vertex_count', MAX_N)
    print('RESULT PASS')

if __name__=='__main__':
    main()
