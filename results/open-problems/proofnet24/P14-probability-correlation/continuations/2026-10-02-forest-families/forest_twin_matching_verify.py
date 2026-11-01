"""Independent exact integer enumeration checks of the heterogeneous formula."""
from itertools import combinations
from math import prod
import random


def enumerate_rayleigh(xs):
    edges=[(0,1,1),(2,3,1)]+[(i,4+j,x) for j,x in enumerate(xs) for i in range(4)]
    n=4+len(xs); counts=[0]*4
    for mask in range(1<<len(edges)):
        if mask.bit_count()>n-1:continue
        par=list(range(n)); w=1
        def root(v):
            while par[v]!=v:v=par[v]
            return v
        for k,(u,v,z) in enumerate(edges):
            if mask>>k&1:
                a,b=root(u),root(v)
                if a==b:break
                par[a]=b;w*=z
        else:counts[mask&3]+=w
    return counts[1]*counts[2]-counts[0]*counts[3]


def formula(xs):
    a=[1+4*x for x in xs]; out=0
    for i,j in combinations(range(len(xs)),2):
        out+=4*xs[i]**2*xs[j]**2*(1+xs[i]+xs[j])**2*prod(a[k]**2 for k in range(len(xs)) if k not in (i,j))
    for i,j,k in combinations(range(len(xs)),3):
        out+=8*xs[i]**2*xs[j]**2*xs[k]**2*(a[i]*a[j]+a[i]*a[k]+a[j]*a[k])*prod(a[l]**2 for l in range(len(xs)) if l not in (i,j,k))
    return out


if __name__=='__main__':
    rng=random.Random(261000549)
    tests=[[],[0],[3],[1,2],[0,4],[1,2,3],[0,2,4],[2,3,5,7]]
    tests +=[[rng.randrange(5) for _ in range(s)] for s in (2,2,3,3,3,4)]
    for xs in tests:
        exact=enumerate_rayleigh(xs); predicted=formula(xs)
        assert exact==predicted,(xs,exact,predicted)
        print(xs,exact,'verified')
    print(f'{len(tests)} independent exact weighted-enumeration checks passed.')
