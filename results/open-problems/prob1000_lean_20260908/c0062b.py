import math, random
def partitions(n, maxp=None):
    if maxp is None: maxp=n
    if n==0: yield (); return
    for k in range(min(n,maxp),0,-1):
        for rest in partitions(n-k,k): yield (k,)+rest
def logdim(lam, logfact):
    n=sum(lam); conj=[0]*(lam[0])
    for p in lam:
        for j in range(p): conj[j]+=1
    s=0.0
    for i,p in enumerate(lam):
        for j in range(p): s+=math.log(p-(j+1)+conj[j]-(i+1)+1)
    return logfact[n]-s
def conjug(lam):
    if not lam: return ()
    c=[0]*lam[0]
    for p in lam:
        for j in range(p): c[j]+=1
    return tuple(c)
def neighbours(lam):
    L=list(lam); out=set()
    for i in range(len(L)):
        for j in range(len(L)+1):
            if i==j: continue
            M=L[:]; M[i]-=1
            if M[i]<0: continue
            if j<len(M): M[j]+=1
            else: M=M+[1]
            M=[x for x in M if x>0]
            if M!=sorted(M,reverse=True): continue
            if sum(M)!=sum(lam): continue
            out.add(tuple(M))
    return out
def climb(n, logfact, start, iters=100000):
    cur=start; curv=logdim(cur,logfact)
    for _ in range(iters):
        best=None;bv=curv
        for m in neighbours(cur):
            v=logdim(m,logfact)
            if v>bv+1e-12: bv=v; best=m
        if best is None: return cur,curv
        cur,curv=best,bv
    return cur,curv
N=44
logfact=[0.0]*(N+2)
for k in range(1,N+2): logfact[k]=logfact[k-1]+math.log(k)
random.seed(3)
print("Does single-box hill-climbing reach the GLOBAL maximiser?  (exhaustive ground truth, n<=44)")
print(f"{'n':>4} {'exhaustive best':>17} {'climb best':>12} {'match?':>8} {'random starts tried':>20}")
fails=0
for n in range(4,N+1):
    best=-1e18
    for lam in partitions(n):
        v=logdim(lam,logfact)
        if v>best: best=v
    ok=True; tries=8
    for _ in range(tries):
        # random start: a random partition of n
        parts=[]; rem=n
        while rem>0:
            k=random.randint(1,rem); parts.append(k); rem-=k
        parts.sort(reverse=True)
        # repair to a partition (already is)
        _,v=climb(n,logfact,tuple(parts))
        if v<best-1e-9: ok=False
    if not ok: fails+=1
    if n>=38 or n%8==0 or not ok:
        print(f"{n:>4} {best:>17.6f} {v:>12.6f} {str(ok):>8} {tries:>20}")
print(f"\n  n values where hill-climbing FAILED to reach the global max from all {8} random starts: {fails}")
