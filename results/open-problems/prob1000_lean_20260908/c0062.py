import numpy as np, math, sys
from functools import lru_cache
def partitions(n, maxp=None):
    if maxp is None: maxp=n
    if n==0: yield (); return
    for k in range(min(n,maxp),0,-1):
        for rest in partitions(n-k,k): yield (k,)+rest
def logdim(lam, logfact):
    n=sum(lam)
    conj=[0]*(lam[0]+1)
    for p in lam:
        for j in range(p): conj[j]+=1
    s=0.0
    for i,p in enumerate(lam):
        for j in range(p):
            s+=math.log(p-j + conj[j]-i-1 +1 -1 +1) if False else math.log(p-(j+1)+conj[j]-(i+1)+1)
    return logfact[n]-s
def best_exhaustive(n, logfact):
    best=-1e18; arg=[]
    for lam in partitions(n):
        d=logdim(lam,logfact)
        if d>best+1e-12: best=d; arg=[lam]
        elif abs(d-best)<=1e-12: arg.append(lam)
    return best,arg
def conj(lam):
    if not lam: return ()
    c=[0]*lam[0]
    for p in lam:
        for j in range(p): c[j]+=1
    return tuple(c)
N=44
logfact=[0.0]*(N+2)
for k in range(1,N+2): logfact[k]=logfact[k-1]+math.log(k)
print("Exhaustive maximal-dimension shapes: is the maximiser unique up to conjugation?")
print(f"{'n':>4} {'#maximisers':>12} {'self-conj?':>11} {'unique up to conj?':>19}  shape")
for n in range(2,N+1):
    best,arg=best_exhaustive(n,logfact)
    cls=set()
    for lam in arg: cls.add(min(lam,conj(lam)))
    sc = any(lam==conj(lam) for lam in arg)
    ok = len(cls)==1
    if n>=36 or n%6==0 or not ok:
        print(f"{n:>4} {len(arg):>12} {str(sc):>11} {str(ok):>19}  {arg[0]}")
    if not ok: print("   *** NOT unique up to conjugation ***", arg)
