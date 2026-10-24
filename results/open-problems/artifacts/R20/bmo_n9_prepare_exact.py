#!/usr/bin/env python3
"""Prepare a complete exact connected 8-vertex representative set for the R20/BMO n=9 census.

This is the first stage of the finite checker. It starts from NetworkX graph_atlas_g(),
which contains every unlabeled graph through order 7. Every connected 8-vertex graph
has a non-cut vertex; deleting such a vertex leaves a connected 7-vertex graph. Hence
adding a new vertex with every nonempty old-vertex neighborhood to every unlabeled
7-vertex graph covers all connected order-8 graphs. We discard a candidate only after
an exact nx.is_isomorphic test. Degree sequence and WL hash are used only as
isomorphism-invariant pre-buckets, never as equality certificates.
"""
from __future__ import annotations
import argparse, collections, networkx as nx

def norm(G): return nx.convert_node_labels_to_integers(G, ordering='sorted')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('out'); args=ap.parse_args()
    atlas=nx.graph_atlas_g()
    base7=[norm(G) for G in atlas if G.number_of_nodes()==7]
    if len(base7)!=1044: raise SystemExit(f'bad atlas order7 count {len(base7)}')
    buckets={}; reps=[]; cand=0; iso_tests=0
    for B in base7:
        for mask in range(1,1<<7):
            G=B.copy(); G.add_node(7)
            for i in range(7):
                if mask>>i & 1: G.add_edge(7,i)
            if not nx.is_connected(G): continue
            cand += 1
            deg=tuple(sorted((d for _,d in G.degree()), reverse=True))
            wl=nx.weisfeiler_lehman_graph_hash(G,iterations=3,digest_size=8)
            L=buckets.setdefault((deg,wl),[])
            duplicate=False
            for R in L:
                iso_tests += 1
                if nx.is_isomorphic(G,R): duplicate=True; break
            if not duplicate:
                H=norm(G); L.append(H); reps.append(H)
    if len(reps)!=11117: raise SystemExit(f'bad connected n8 class count {len(reps)}')
    with open(args.out,'wb') as f:
        for G in reps: f.write(nx.to_graph6_bytes(G,header=False))
    byD=collections.Counter(max(dict(G.degree()).values()) for G in reps)
    print(f'atlas_unlabeled_order7={len(base7)}')
    print(f'n8_connected_augmentation_candidates={cand}')
    print(f'n8_exact_isomorphism_tests={iso_tests}')
    print(f'n8_connected_isomorphism_classes={len(reps)}')
    print('n8_counts_by_Delta='+repr(dict(sorted(byD.items()))))
    print(f'WROTE_N8_G6={args.out}')
if __name__=='__main__': main()
