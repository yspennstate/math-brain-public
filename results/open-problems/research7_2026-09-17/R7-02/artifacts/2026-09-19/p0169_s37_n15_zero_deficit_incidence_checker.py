from math import comb
from collections import Counter

def ceildiv(a,b): return -((-a)//b)

def enumerate_profiles(N,target16,target_mu16=None):
    C=[comb(N,k) for k in range(N+1)]
    c=[[0]*(N+1) for _ in range(6)]
    for j in range(6):
        for k in range(j,N+1): c[j][k]=comb(N-j,k-j)
    out=[]; prefixes=0
    for u0 in (0,1):
        for b1 in range(C[1]+1):
            u1=b1-c[0][1]*u0
            for b2 in range(C[2]+1):
                u2=b2-c[0][2]*u0-c[1][2]*u1
                for b3 in range(C[3]+1):
                    prefixes+=1
                    u3=b3-c[0][3]*u0-c[1][3]*u1-c[2][3]*u2
                    R=target16+16*u1+16*u2+12*u3
                    lo=-10**30; hi=10**30; ok=True
                    for k in range(N+1):
                        base=u0*c[0][k]+u1*c[1][k]+u2*c[2][k]+u3*c[3][k]
                        A=5*base-c[5][k]*R
                        B=5*c[4][k]-8*c[5][k]
                        M=5*C[k]
                        if B==0:
                            if not (0<=A<=M): ok=False; break
                        elif B>0:
                            lo=max(lo,ceildiv(-A,B)); hi=min(hi,(M-A)//B)
                        else:
                            bb=-B; lo=max(lo,ceildiv(A-M,bb)); hi=min(hi,A//bb)
                        if lo>hi: ok=False; break
                    if not ok: continue
                    residue=(-2*R)%5
                    start=lo+((residue-lo)%5)
                    for u4 in range(start,hi+1,5):
                        u5=(-R-8*u4)//5
                        mu16=32*u0+16*u1+8*u2+4*u3+2*u4+u5-16
                        if target_mu16 is not None and mu16!=target_mu16: continue
                        u=(u0,u1,u2,u3,u4,u5)
                        b=tuple(sum(u[j]*c[j][k] for j in range(6)) for k in range(N+1))
                        if all(0<=b[k]<=C[k] for k in range(N+1)): out.append((u,b,mu16))
    return prefixes,out

def combine(bp,bm):
    n=len(bp)-1
    return tuple((bp[k] if k<=n else 0)+(bm[k-1] if k>=1 else 0) for k in range(n+2))

p15,parents=enumerate_profiles(15,37)
print('N15_L37_profiles',len(parents),'mu',dict(Counter(x[2] for x in parents)))
child_cache={m:enumerate_profiles(14,35,m)[1] for m in (-5,-3,-1,1,3,5)}
print('N14_L35_child_counts',{m:len(v) for m,v in child_cache.items()})
compatible=[]
for p in parents:
    u,b,pmu=p; pairs=[]
    for a in child_cache.get(pmu+2,[]):
        for m in child_cache.get(pmu-2,[]):
            if combine(a[1],m[1])==b: pairs.append((a[1],m[1]))
    compatible.append(pairs)
print('parents_with_zero_pair',sum(bool(x) for x in compatible))
C14=[comb(14,k) for k in range(15)]
def comps(total,m,prefix=()):
    if m==1:
        yield prefix+(total,)
    else:
        for x in range(total+1): yield from comps(total-x,m-1,prefix+(x,))

survivors=[]
for pidx,p in enumerate(parents):
    pairs=compatible[pidx]
    if not pairs: continue
    u,b,pmu=p
    plus=[]; seen=set()
    for pp,mm in pairs:
        if pp not in seen: seen.add(pp); plus.append(pp)
    found=None
    for z in range(8,15):
        r=15-z
        for cnt in comps(z,len(plus)):
            ok=True
            for k in range(16):
                sumz=sum(cnt[q]*(plus[q][k] if k<=14 else 0) for q in range(len(plus)))
                target=(15-k)*b[k]
                lo=max(0,b[k]-(C14[k-1] if 1<=k<=15 else 0))
                hi=min(b[k],C14[k] if k<=14 else 0)
                if not (sumz+r*lo <= target <= sumz+r*hi): ok=False; break
            if ok: found=(z,cnt); break
        if found: break
    if found: survivors.append((pidx,p,found,len(plus)))
print('weak_incidence_survivors',len(survivors))
for pidx,p,found,m in survivors:
    print('SURV',pidx,'mu16',p[2],'u',p[0],'z',found[0],'types',m)
assert len(parents)==92
assert sum(bool(x) for x in compatible)==52
assert len(survivors)==16
print('ASSERTIONS_PASS')
