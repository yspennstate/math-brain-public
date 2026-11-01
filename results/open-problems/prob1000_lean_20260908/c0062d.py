import math
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
print("Does RADIUS-2 local search always reach the global maximum?  n = 4..44, exhaustive.")
print(f"{'n':>4} {'#radius-1 traps':>16} {'#radius-2 traps':>16}")
tot1=tot2=0
for N in range(4,45):
    lf=[0.0]*(N+2)
    for k in range(1,N+2): lf[k]=lf[k-1]+math.log(k)
    V={lam:logdim(lam,lf) for lam in partitions(N)}
    g=max(V.values())
    n1=[]
    for l,v in V.items():
        if v<g-1e-9 and all(V[m]<=v+1e-12 for m in nbrs1(l)): n1.append(l)
    n2=[]
    for l in n1:
        two=set()
        for m in nbrs1(l): two|=nbrs1(m)
        two.discard(l)
        if all(V[m]<=V[l]+1e-12 for m in two): n2.append(l)
    tot1+=len(n1); tot2+=len(n2)
    if n1: print(f"{N:>4} {len(n1):>16} {len(n2):>16}   traps: {n1}")
print(f"\n  totals over n=4..44:  radius-1 traps {tot1},  surviving radius-2 {tot2}")
