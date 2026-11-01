#!/usr/bin/env python3
"""Exact positive certificates for two (5,8) TFIK22 survivors.

Generate the full Delta-Y / Y-Delta family of K_{3,3,1,1} up to graph
isomorphism and verify that survivor classes 1 and 4 from
`tfik22_profile_5_8_exact_reduction_20260919.py` lie in it.

The family generation is purely combinatorial.  Isomorphism tests use NetworkX's
exact graph-isomorphism algorithm; no floating point arithmetic is involved.
"""
import itertools
from collections import deque, Counter
import networkx as nx

C1=((0,1),(0,4),(0,5),(0,10),(1,2),(1,6),(1,12),(2,3),(2,7),(2,11),(3,8),(3,10),(3,12),(4,9),(4,11),(4,12),(5,8),(5,11),(6,8),(6,9),(7,9),(7,10))
C4=((0,1),(0,4),(0,7),(0,9),(1,2),(1,10),(1,11),(2,3),(2,8),(2,12),(3,4),(3,9),(3,10),(4,11),(4,12),(5,6),(5,8),(5,11),(6,7),(6,10),(7,12),(8,9))

def graph(edges,n):
    G=nx.Graph(); G.add_nodes_from(range(n)); G.add_edges_from(edges); return G

def base_k3311():
    parts=((0,1,2),(3,4,5),(6,),(7,))
    G=nx.Graph(); G.add_nodes_from(range(8))
    for i in range(len(parts)):
        for j in range(i+1,len(parts)):
            G.add_edges_from((u,v) for u in parts[i] for v in parts[j])
    assert G.number_of_edges()==22
    return G

def sig(G): return (G.number_of_nodes(),tuple(sorted(dict(G.degree()).values())))

def dy(G):
    for a,b,c in itertools.combinations(G.nodes(),3):
        tri=((a,b),(a,c),(b,c))
        if all(G.has_edge(*e) for e in tri):
            H=G.copy(); H.remove_edges_from(tri)
            w=max(H.nodes())+1
            H.add_node(w); H.add_edges_from(((w,a),(w,b),(w,c)))
            yield nx.convert_node_labels_to_integers(H),("DY",(a,b,c))

def yd(G):
    for v in list(G.nodes()):
        if G.degree(v)!=3: continue
        N=tuple(sorted(G.neighbors(v)))
        if any(G.has_edge(a,b) for a,b in itertools.combinations(N,2)): continue
        H=G.copy(); H.remove_node(v); H.add_edges_from(itertools.combinations(N,2))
        yield nx.convert_node_labels_to_integers(H),("YD",v,N)

def iso_index(fam,G):
    s=sig(G)
    for i,H in enumerate(fam):
        if sig(H)==s and nx.is_isomorphic(G,H): return i
    return None

def main():
    fam=[base_k3311()]; parent=[None]; q=deque([0])
    while q:
        i=q.popleft(); G=fam[i]
        for H,mv in itertools.chain(dy(G),yd(G)):
            if iso_index(fam,H) is None:
                fam.append(H); parent.append((i,mv)); q.append(len(fam)-1)
    print("K3311_FAMILY_SIZE",len(fam))
    print("ORDER_DISTRIBUTION",tuple(sorted(Counter(G.number_of_nodes() for G in fam).items())))
    assert len(fam)==58
    for name,E in (("CLASS1",C1),("CLASS4",C4)):
        T=graph(E,13)
        idx=iso_index(fam,T)
        print(name,"FAMILY_INDEX",idx)
        assert idx is not None
        seq=[]; cur=idx
        while parent[cur] is not None:
            p,mv=parent[cur]; seq.append((p,cur,mv)); cur=p
        seq.reverse()
        print(name,"MOVE_SEQUENCE",tuple(seq))
    print("ALL_EXACT_TFIK22_58_POSITIVE_FAMILY_CHECKS_PASS")
if __name__=="__main__": main()
