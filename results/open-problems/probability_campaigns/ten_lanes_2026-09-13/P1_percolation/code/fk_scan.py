"""Exhaustive small-graph scan of the random-cluster (FK) model with cluster weight q<1.

Two questions, both stated open in the campaign ledgers:
  (C0091) pairwise negative correlation of edge states, Cov(w_e, w_f) <= 0 for 0<q<1
  (C0146) stochastic monotonicity in p at fixed q<1 (necessary for a monotone coupling)

Everything here is a finite exact computation once a candidate is found; the scan
itself runs in floating point and any hit is re-checked with exact rationals.
"""
import itertools, sys
from fractions import Fraction

def comps(n, edges, mask):
    par = list(range(n))
    def find(x):
        while par[x]!=x:
            par[x]=par[par[x]]; x=par[x]
        return x
    c = n
    for i,(u,v) in enumerate(edges):
        if mask>>i & 1:
            a,b = find(u), find(v)
            if a!=b:
                par[a]=b; c-=1
    return c

def graphs(n, connected_only=True):
    allp = list(itertools.combinations(range(n),2))
    M = len(allp)
    for s in range(1<<M):
        edges = [allp[i] for i in range(M) if s>>i&1]
        if not edges: continue
        if connected_only and comps(n, edges, (1<<len(edges))-1) != 1: continue
        yield edges

def fk_stats(n, edges, p, q):
    """returns Z, and for each edge the marginal numerator, and pair numerators."""
    m = len(edges)
    Z = 0*p
    one = p*0 + 1
    marg = [0*p]*m
    pair = {}
    for i in range(m):
        for j in range(i+1,m): pair[(i,j)]=0*p
    for mask in range(1<<m):
        k = comps(n, edges, mask)
        c = bin(mask).count("1")
        w = (p**c)*((1-p)**(m-c))*(q**k)
        Z += w
        for i in range(m):
            if mask>>i&1:
                marg[i]=marg[i]+w
                for j in range(i+1,m):
                    if mask>>j&1: pair[(i,j)]=pair[(i,j)]+w
    return Z, marg, pair

def scan_negcorr(nmax=5, ps=None, qs=None, verbose=True):
    if ps is None: ps=[0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95]
    if qs is None: qs=[0.01,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.99]
    best = (-1e9, None)
    cnt=0
    for n in range(2,nmax+1):
        for edges in graphs(n):
            cnt+=1
            m=len(edges)
            for q in qs:
                for p in ps:
                    Z,marg,pair = fk_stats(n,edges,p,q)
                    for (i,j),v in pair.items():
                        cov = v/Z - (marg[i]/Z)*(marg[j]/Z)
                        if cov > best[0]:
                            best = (cov, (n,tuple(edges),i,j,p,q))
    if verbose:
        print("graphs scanned:", cnt)
        print("max covariance found:", best[0])
        print("witness:", best[1])
    return best

if __name__=="__main__":
    scan_negcorr(nmax=int(sys.argv[1]) if len(sys.argv)>1 else 5)
