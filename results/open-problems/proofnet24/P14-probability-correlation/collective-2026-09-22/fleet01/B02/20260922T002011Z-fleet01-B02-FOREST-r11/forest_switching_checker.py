#!/usr/bin/env python3
"""Exact finite regression for FOREST-SWITCH-CORE-v2.

For every labelled simple graph on 2..5 vertices with at least two edges
and every marked present edge pair e,f:
  (1) verify the canonical marked-1-separation colour-swap involution and
      the induced signed core identity;
  (2) for every instance admitting a cut delta(S)={e,f,g}, verify that
      deleting g maps every A00 forest injectively into Q, and therefore
      (R,B)->(B,R-g) maps A00 x A11 injectively to H x Q.

This is finite regression evidence only, not a proof of the all-graphs theorem.
"""
from itertools import combinations

def is_forest(n, edges, mask):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            a,b=find(u),find(v)
            if a==b:
                return False
            p[a]=b
    return True

def connected(n, edges, mask, u, v):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for i,(a,b) in enumerate(edges):
        if (mask>>i)&1:
            ra,rb=find(a),find(b)
            if ra!=rb:
                p[ra]=rb
    return find(u)==find(v)

def selected(edges, mask):
    return [edges[i] for i in range(len(edges)) if (mask>>i)&1]

def add_edges_forest(n, edges, mask, extra):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for u,v in selected(edges,mask)+list(extra):
        a,b=find(u),find(v)
        if a==b:
            return False
        p[a]=b
    return True

def state(n, K, h, e, f):
    return (int(not connected(n,K,h,*e)), int(not connected(n,K,h,*f)))

def q_event(n,K,h,e,f):
    return state(n,K,h,e,f)==(1,1) and not add_edges_forest(n,K,h,[e,f])

def forests(n,K):
    return [m for m in range(1<<len(K)) if is_forest(n,K,m)]

def canonical_marked_one_sep(K, u, e, f):
    # Edge partition s disjoint_union t = u. Marked endpoints are included
    # as isolated vertices on their assigned side when necessary.
    for s in range(1<<len(K)):
        if s & ~u:
            continue
        t=u^s
        vs=set(e)
        vt=set(f)
        for i,(a,b) in enumerate(K):
            if (s>>i)&1:
                vs.update((a,b))
            if (t>>i)&1:
                vt.update((a,b))
        if len(vs & vt)<=1:
            return s
    return None

def swap_side(r,b,s):
    return ((r & ~s)|(b & s), (b & ~s)|(r & s))

def canonical_marked_three_cut(n,G,ei,fi):
    e,f=G[ei],G[fi]
    # S and V\S define the same cut; require vertex 0 in S for uniqueness.
    for sm in range(1,1<<n):
        if not (sm&1) or sm==(1<<n)-1:
            continue
        def crosses(ed):
            a,b=ed
            return ((sm>>a)&1)!=((sm>>b)&1)
        if not crosses(e) or not crosses(f):
            continue
        cut=[j for j,ed in enumerate(G) if crosses(ed)]
        if len(cut)==3 and ei in cut and fi in cut:
            gj=next(j for j in cut if j not in (ei,fi))
            Kidx=[j for j in range(len(G)) if j not in (ei,fi)]
            return sm,Kidx.index(gj)
    return None

stats={
    "graphs":0,
    "edge_pair_instances":0,
    "signed_identity_checks":0,
    "marked_1sep_domain_pairs":0,
    "marked_1sep_target_pairs":0,
    "three_edge_cut_instances":0,
    "three_edge_cut_A00_forests":0,
    "three_edge_cut_domain_pairs":0,
}

for n in range(2,6):
    allE=list(combinations(range(n),2))
    for gm in range(1<<len(allE)):
        G=[allE[i] for i in range(len(allE)) if (gm>>i)&1]
        if len(G)<2:
            continue
        stats["graphs"]+=1
        for ei,fi in combinations(range(len(G)),2):
            e,f=G[ei],G[fi]
            K=[ed for j,ed in enumerate(G) if j not in (ei,fi)]
            cls={(i,j):[] for i in (0,1) for j in (0,1)}
            Q=[]
            for h in forests(n,K):
                st=state(n,K,h,e,f)
                cls[st].append(h)
                if q_event(n,K,h,e,f):
                    Q.append(h)
            stats["edge_pair_instances"]+=1

            dsep=tsep=0
            for r in cls[(0,0)]:
                for b in cls[(1,1)]:
                    s=canonical_marked_one_sep(K,r|b,e,f)
                    if s is None:
                        continue
                    r2,b2=swap_side(r,b,s)
                    assert is_forest(n,K,r2) and is_forest(n,K,b2)
                    assert state(n,K,r2,e,f)==(1,0)
                    assert state(n,K,b2,e,f)==(0,1)
                    assert canonical_marked_one_sep(K,r2|b2,e,f)==s
                    assert swap_side(r2,b2,s)==(r,b)
                    dsep+=1
            for r in cls[(1,0)]:
                for b in cls[(0,1)]:
                    s=canonical_marked_one_sep(K,r|b,e,f)
                    if s is None:
                        continue
                    r2,b2=swap_side(r,b,s)
                    assert state(n,K,r2,e,f)==(0,0)
                    assert state(n,K,b2,e,f)==(1,1)
                    tsep+=1
            assert dsep==tsep
            n00,n10,n01,n11=(len(cls[x]) for x in ((0,0),(1,0),(0,1),(1,1)))
            dcore=n00*n11-dsep
            tcore=n10*n01-tsep
            assert n00*n11-n10*n01==dcore-tcore
            stats["marked_1sep_domain_pairs"]+=dsep
            stats["marked_1sep_target_pairs"]+=tsep
            stats["signed_identity_checks"]+=1

            cut=canonical_marked_three_cut(n,G,ei,fi)
            if cut is not None:
                stats["three_edge_cut_instances"]+=1
                _,gi=cut
                bit=1<<gi
                for r in cls[(0,0)]:
                    # Any R-path joining either marked pair must cross the
                    # unique remaining cut edge g.
                    assert r&bit
                    h=r&~bit
                    assert q_event(n,K,h,e,f)
                    assert (h|bit)==r
                    stats["three_edge_cut_A00_forests"]+=1
                stats["three_edge_cut_domain_pairs"]+=n00*n11

print("FOREST_SWITCHING_REGRESSION_PASS")
for key in sorted(stats):
    print(f"{key}={stats[key]}")
