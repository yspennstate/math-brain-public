"""Brute force: N = Z_e Z_f - Z Z_ef for random-cluster weight lam^|A| q^k(A) on a graph, as {(i,j): coeff} in lam^i u^j, u=1-q."""
import itertools, sys
from collections import defaultdict
from math import comb
def comps(n, edges):
    p=list(range(n))
    def f(x):
        while p[x]!=x: p[x]=p[p[x]]; x=p[x]
        return x
    k=n
    for a,b in edges:
        ra,rb=f(a),f(b)
        if ra!=rb: p[ra]=rb; k-=1
    return k
def Zs(n, E, e, f):
    # returns dict sets: Z, Ze, Zf, Zef as {(edges, k): count}
    out=[defaultdict(int) for _ in range(4)]
    m=len(E)
    for mask in range(1<<m):
        A=[E[i] for i in range(m) if mask>>i&1]
        k=comps(n,A); s=len(A)
        ie=e in A; jf=f in A
        out[0][(s,k)]+=1
        if ie: out[1][(s,k)]+=1
        if jf: out[2][(s,k)]+=1
        if ie and jf: out[3][(s,k)]+=1
    return out
def to_u(d):
    # q^k = (1-u)^k
    r=defaultdict(int)
    for (s,k),c in d.items():
        for j in range(k+1): r[(s,j)]+=c*comb(k,j)*(-1)**j
    return r
def mul(a,b):
    r=defaultdict(int)
    for (i,j),c in a.items():
        for (k,l),d in b.items(): r[(i+k,j+l)]+=c*d
    return r
def N_of(n,E,e,f):
    Z,Ze,Zf,Zef=[to_u(x) for x in Zs(n,E,e,f)]
    a=mul(Ze,Zf); b=mul(Z,Zef)
    r={k:a.get(k,0)-b.get(k,0) for k in set(a)|set(b)}
    return {k:v for k,v in r.items() if v}
if __name__=='__main__':
    n=int(sys.argv[1]); kind=sys.argv[2]
    E=list(itertools.combinations(range(n),2))
    e=(0,1); f=(0,2) if kind=='adj' else (2,3)
    N=N_of(n,E,e,f)
    print(sorted(N.items()))
