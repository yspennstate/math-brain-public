# Exhaustive check on small boxes of
#  (a) the all-waves identity: multiset {W_k(eta): eta in R_K, k<=N(eta)} == multiset {0-component of a 2-forest of K}
#  (b) LLS (arXiv 2605.19419) Lemma 2.14: nu_K(W_1 in A) = G_K(0,0) nu^(0)_K(T in A) for A = sets containing a nbr of 0,
#      which (given (a)) requires that no later wave contains a neighbour of 0.
#  (c) Dhar's formula as a sanity check of the toppling code.
import itertools, sys
from fractions import Fraction
from collections import Counter
import numpy as np

def make_box(dims):
    sites = list(itertools.product(*[range(n) for n in dims]))
    idx = {s:i for i,s in enumerate(sites)}
    d = len(dims); deg = 2*d
    nbrs = []  # list of neighbour indices inside K (others are sink)
    for s in sites:
        lst=[]
        for a in range(d):
            for e in (-1,1):
                t=list(s); t[a]+=e; t=tuple(t)
                if t in idx: lst.append(idx[t])
        nbrs.append(lst)
    o = idx[tuple(n//2 for n in dims)]
    return sites, idx, nbrs, deg, o

def is_recurrent(eta, nbrs, deg, sink_burnt=()):
    # burning test: burnt set starts as the sink (outside K) plus sink_burnt (extra sink vertices inside K)
    n=len(eta); burnt=[False]*n
    for s in sink_burnt: burnt[s]=True
    changed=True
    while changed:
        changed=False
        for x in range(n):
            if burnt[x]: continue
            unb = sum(1 for y in nbrs[x] if not burnt[y])
            if eta[x] >= unb:
                burnt[x]=True; changed=True
    return all(burnt)

def waves(eta, nbrs, deg, o):
    """Avalanche at o decomposed into waves. Returns list of wave sets (each includes o) and toppling counts."""
    h=list(eta); h[o]+=1
    n=len(h); topp=[0]*n; W=[]
    while h[o]>=deg:
        # one wave: topple o once, then everything except o
        wave={o}; h[o]-=deg; topp[o]+=1
        for y in nbrs[o]: h[y]+=1
        stack=[y for y in nbrs[o] if h[y]>=deg]
        while stack:
            x=stack.pop()
            if x==o or h[x]<deg: continue
            # in a wave a vertex topples at most once; assert it
            assert x not in wave, "vertex toppled twice within a wave"
            wave.add(x); h[x]-=deg; topp[x]+=1
            for y in nbrs[x]:
                h[y]+=1
                if y!=o and h[y]>=deg: stack.append(y)
        W.append(frozenset(wave))
    return W, topp

def two_forests(nbrs, o, n):
    """All 2-component spanning forests of K wired: roots o and the sink. Return list of 0-components (frozensets incl. o)."""
    others=[x for x in range(n) if x!=o]
    # each x picks a parent: a neighbour in K, or the sink (-1); count sink-edges multiplicity = deg - len(nbrs[x])
    choices=[]
    for x in others:
        ch=list(nbrs[x]) + [-1]*(2*len(nbrs[0])//len(nbrs[0]) and 0)  # placeholder
        choices.append(ch)
    deg=None
    return None

def two_forest_components(nbrs, deg, o, n):
    others=[x for x in range(n) if x!=o]
    opts=[]
    for x in others:
        ch=[(y,1) for y in nbrs[x]]
        ms = deg-len(nbrs[x])
        if ms>0: ch.append((-1,ms))   # multiedges to the sink
        opts.append(ch)
    comps=Counter(); total=0
    for par in itertools.product(*[range(len(c)) for c in opts]):
        parent={}; mult=1
        for x,pi in zip(others,par):
            y,m=opts[others.index(x)][pi]; parent[x]=y; mult*=m
        # check forest: every chain ends at o or sink (-1), no cycles
        root={}
        ok=True
        for x in others:
            path=[]; cur=x
            while cur in parent and cur not in root:
                path.append(cur); cur=parent[cur]
                if cur in path: ok=False; break
            if not ok: break
            r = root[cur] if cur in root else cur
            for p in path: root[p]=r
        if not ok: continue
        comp=frozenset([o]+[x for x in others if root[x]==o])
        comps[comp]+=mult; total+=mult
    return comps,total

def green(nbrs, deg, n):
    L=np.zeros((n,n))
    for x in range(n):
        L[x,x]=deg
        for y in nbrs[x]: L[x,y]-=1
    return np.linalg.inv(L)

def run(dims):
    sites, idx, nbrs, deg, o = make_box(dims)
    n=len(sites)
    R=[eta for eta in itertools.product(range(deg), repeat=n) if is_recurrent(eta,nbrs,deg)]
    G=green(nbrs,deg,n)
    print(f"dims={dims} |K|={n} |R_K|={len(R)} det Delta={round(np.linalg.det(np.linalg.inv(G)))} G_K(o,o)={G[o,o]:.6f}")
    allw=Counter(); firstw=Counter(); laterw_nbr=0; first_nbr=0
    topsum=np.zeros(n); nfirst=0
    N0=set(nbrs[o])
    for eta in R:
        W,topp=waves(eta,nbrs,deg,o)
        topsum+=topp
        for k,w in enumerate(W):
            allw[w]+=1
            if k==0:
                firstw[w]+=1
                if w & N0: first_nbr+=1
            elif w & N0: laterw_nbr+=1
    # Dhar check
    dhar_ok = np.allclose(topsum/len(R), G[o,:])
    print("  Dhar's formula E n(o,x)=G_K(o,x) for all x:", dhar_ok)
    comps,total=two_forest_components(nbrs,deg,o,n)
    print(f"  #2-forests={total}, |R_K|*G_K(o,o)={len(R)*G[o,o]:.3f}, total waves={sum(allw.values())}")
    print("  all-waves multiset == 2-forest 0-component multiset:", allw==comps)
    nb2f=sum(m for c,m in comps.items() if c & N0)
    print(f"  #{{eta: W_1 contains a nbr of o}} = {first_nbr};  #{{2-forests: T_o contains a nbr of o}} = {nb2f}  (LLS Lemma 2.14 claims equality)")
    print(f"  # of LATER waves (k>=2) containing a nbr of o = {laterw_nbr}  (= the discrepancy {nb2f-first_nbr})")
    # per-set comparison for first waves
    bad=sum(1 for c in set(comps)|set(firstw) if (c & N0) and comps[c]!=firstw[c])
    print(f"  number of wave-sets A (containing a nbr) with #first waves != #2-forests: {bad}")
    return

if __name__=="__main__":
    for dims in [(3,),(5,),(7,),(9,),(3,3)]:
        run(dims)
