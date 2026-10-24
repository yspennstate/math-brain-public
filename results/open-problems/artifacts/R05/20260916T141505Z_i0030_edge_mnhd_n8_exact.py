#!/usr/bin/env python3
from __future__ import annotations
from collections import Counter
import itertools, hashlib
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

N=8
EXPECTED_LABELED_REGULAR={0:1,1:105,2:3507,3:19355,4:19355,5:3507,6:105,7:1}
EXPECTED_CONNECTED_REGULAR={0:0,1:0,2:2520,3:19320,4:19355,5:3507,6:105,7:1}
EXPECTED_AT_LABELED={0:0,1:0,2:2520,3:840,4:35,5:0,6:105,7:1}
EXPECTED_AT_ISO={0:0,1:0,2:1,3:1,4:1,5:0,6:1,7:1}


def gen_d_regular(n:int,d:int):
    # Each labeled d-regular simple graph occurs exactly once: process the
    # smallest vertex whose incident higher-index choices are still unset,
    # choosing exactly its remaining degree among available higher vertices.
    adj=[set() for _ in range(n)]
    def rec(i):
        while i<n and len(adj[i])==d:
            i+=1
        if i==n:
            yield tuple(tuple(sorted(s)) for s in adj)
            return
        need=d-len(adj[i])
        candidates=[j for j in range(i+1,n) if len(adj[j])<d and j not in adj[i]]
        if need<0 or len(candidates)<need:
            return
        if need==0:
            yield from rec(i+1); return
        for chosen in itertools.combinations(candidates,need):
            for j in chosen:
                adj[i].add(j); adj[j].add(i)
            if all(len(adj[v])<=d for v in range(i+1,n)):
                yield from rec(i+1)
            for j in chosen:
                adj[i].remove(j); adj[j].remove(i)
    yield from rec(0)


def graph_from_adj(A):
    G=nx.Graph(); G.add_nodes_from(range(len(A)))
    for i in range(len(A)):
        for j in A[i]:
            if i<j: G.add_edge(i,j)
    return G


def complement_adj(A):
    n=len(A)
    return tuple(tuple(j for j in range(n) if j!=i and j not in A[i]) for i in range(n))


def matmul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][r]*B[r][j] for r in range(k)) for j in range(m)] for i in range(n)]


def adjacency_matrix(G):
    n=G.number_of_nodes()
    return [[1 if G.has_edge(i,j) else 0 for j in range(n)] for i in range(n)]


def one_walk_prefilter_exact(G):
    # Necessary for arc transitivity. Testing powers 0..n-1 is already enough
    # by Cayley-Hamilton, but only necessity is used here.
    n=G.number_of_nodes(); A=adjacency_matrix(G)
    M=[[int(i==j) for j in range(n)] for i in range(n)]
    arcs=[(u,v) for a,b in G.edges() for u,v in ((a,b),(b,a))]
    for _m in range(n):
        if len({M[i][i] for i in range(n)})!=1: return False
        if arcs and len({M[u][v] for u,v in arcs})!=1: return False
        M=matmul(M,A)
    return True


def is_arc_transitive_exact(G):
    if not nx.is_connected(G) or len({d for _,d in G.degree()})!=1 or G.number_of_edges()==0:
        return False,0
    x,y=next(iter(G.edges()))
    arcs={(u,v) for a,b in G.edges() for u,v in ((a,b),(b,a))}
    orbit=set(); aut=0
    for phi in GraphMatcher(G,G).isomorphisms_iter():
        aut+=1; orbit.add((phi[x],phi[y]))
    return orbit==arcs,aut


def exact_walk_identity(G):
    n=G.number_of_nodes(); d=next(iter(dict(G.degree()).values()))
    A=adjacency_matrix(G); M=[[int(i==j) for j in range(n)] for i in range(n)]
    arcs=[(u,v) for a,b in G.edges() for u,v in ((a,b),(b,a))]
    diag=[]; av=[]
    for m in range(2*n+2):
        ds={M[i][i] for i in range(n)}; es={M[u][v] for u,v in arcs}
        assert len(ds)==1 and len(es)==1
        diag.append(next(iter(ds))); av.append(next(iter(es)))
        M=matmul(M,A)
    for m in range(2*n+1):
        assert diag[m+1]==d*av[m]
    return diag,av


def g6(G):
    return nx.to_graph6_bytes(G,header=False).decode().strip()


def main():
    counts={}; conn={}; pre={}; atlabeled={}; atiso={}; reps={}
    for d in range(8):
        source_d=d if d<=3 else 7-d
        iterator=gen_d_regular(N,source_d)
        c=cc=cp=ca=0; r=[]
        for A0 in iterator:
            A=A0 if d<=3 else complement_adj(A0)
            c+=1
            G=graph_from_adj(A)
            if not nx.is_connected(G): continue
            cc+=1
            if not one_walk_prefilter_exact(G): continue
            cp+=1
            ok,aut=is_arc_transitive_exact(G)
            if not ok: continue
            ca+=1
            diag,av=exact_walk_identity(G)
            if not any(nx.is_isomorphic(G,H) for H,_,_,_ in r):
                r.append((G.copy(),aut,diag,av))
        counts[d]=c; conn[d]=cc; pre[d]=cp; atlabeled[d]=ca; atiso[d]=len(r); reps[d]=r
        print(f'd={d} labeled={c} connected={cc} one_walk_prefilter={cp} arc_labeled={ca} arc_iso={len(r)}')
        for G,aut,diag,av in r:
            print('  rep_g6',g6(G),'aut',aut,'diag',diag[:10],'arc',av[:9])
    print('labeled_regular_counts',counts)
    print('connected_regular_counts',conn)
    print('one_walk_prefilter_counts',pre)
    print('arc_transitive_labeled_counts',atlabeled)
    print('arc_transitive_iso_counts',atiso)
    assert counts==EXPECTED_LABELED_REGULAR, counts
    assert conn==EXPECTED_CONNECTED_REGULAR, conn
    assert atlabeled==EXPECTED_AT_LABELED, atlabeled
    assert atiso==EXPECTED_AT_ISO, atiso
    assert sum(conn.values())==44808
    assert sum(atlabeled.values())==3501
    assert sum(atiso.values())==5
    assert counts[1]==math_factorial(8)//(2**4*math_factorial(4))
    print('total_connected_labeled_regular_checked',sum(conn.values()))
    print('total_arc_transitive_labeled',sum(atlabeled.values()))
    print('unlabeled_arc_transitive_n8',sum(atiso.values()))
    print('metric_largest_fully_certified_vertex_count',8)
    print('RESULT PASS')

def math_factorial(n):
    z=1
    for k in range(2,n+1): z*=k
    return z

if __name__=='__main__': main()
