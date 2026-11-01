import math, itertools
def partitions(n, maxp=None):
    if maxp is None: maxp=n
    if n==0: yield (); return
    for k in range(min(n,maxp),0,-1):
        for rest in partitions(n-k,k): yield (k,)+rest
def logdim(lam,lf):
    conj=[0]*lam[0]
    for p in lam:
        for j in range(p): conj[j]+=1
    s=0.0
    for i,p in enumerate(lam):
        for j in range(p): s+=math.log(p-(j+1)+conj[j]-(i+1)+1)
    return lf[sum(lam)]-s
def conjug(lam):
    c=[0]*lam[0]
    for p in lam:
        for j in range(p): c[j]+=1
    return tuple(c)
def nbrs1(lam):
    L=list(lam); out=set()
    for i in range(len(L)):
        for j in range(len(L)+1):
            if i==j: continue
            M=L[:]; M[i]-=1
            if M[i]<0: continue
            if j<len(M): M[j]+=1
            else: M=M+[1]
            M=[x for x in M if x>0]
            if M==sorted(M,reverse=True) and sum(M)==sum(lam): out.add(tuple(M))
    return out
def nbrs2(lam):
    out=set(nbrs1(lam))
    for m in list(out): out|=nbrs1(m)
    out.discard(tuple(lam)); return out
n=38
lf=[0.0]*(n+2)
for k in range(1,n+2): lf[k]=lf[k-1]+math.log(k)
vals={lam:logdim(lam,lf) for lam in partitions(n)}
gbest=max(vals.values())
locmax1=[l for l,v in vals.items() if all(vals[m]<=v+1e-12 for m in nbrs1(l))]
print(f"n=38: global max log-dim = {gbest:.6f}")
print(f"  number of LOCAL maxima under single-box moves: {len(locmax1)}")
for l in sorted(locmax1,key=lambda l:-vals[l]):
    tag = "GLOBAL" if vals[l]>gbest-1e-9 else "trap"
    print(f"    {tag:>7}  logdim={vals[l]:.6f}  gap={gbest-vals[l]:+.6f}  {l}")
locmax2=[l for l in locmax1 if all(vals[m]<=vals[l]+1e-12 for m in nbrs2(l))]
print(f"\n  local maxima that SURVIVE two-box moves: {len(locmax2)}")
for l in locmax2:
    print(f"    logdim={vals[l]:.6f} {'GLOBAL' if vals[l]>gbest-1e-9 else 'STILL A TRAP'}  {l}")
# scan all n<=44 for single-box traps
print("\n  Smallest n with a strict single-box local maximum, scanning n=4..44:")
for N in range(4,45):
    lf2=[0.0]*(N+2)
    for k in range(1,N+2): lf2[k]=lf2[k-1]+math.log(k)
    V={lam:logdim(lam,lf2) for lam in partitions(N)}
    g=max(V.values())
    traps=[l for l,v in V.items() if v<g-1e-9 and all(V[m]<=v+1e-12 for m in nbrs1(l))]
    if traps:
        print(f"    n={N}: {len(traps)} trap(s), best trap gap {min(g-V[t] for t in traps):.6f}, e.g. {min(traps,key=lambda t:g-V[t])}")
