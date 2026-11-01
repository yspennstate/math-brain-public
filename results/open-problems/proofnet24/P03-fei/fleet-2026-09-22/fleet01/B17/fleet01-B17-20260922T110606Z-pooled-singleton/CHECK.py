#!/usr/bin/env python3
import itertools, math

C = 6.5584452830718245

def solve_linear(A,b):
    n=len(b)
    A=[list(map(float,row))+[float(bi)] for row,bi in zip(A,b)]
    for col in range(n):
        piv=max(range(col,n), key=lambda r: abs(A[r][col]))
        if abs(A[piv][col]) < 1e-13:
            raise ValueError("singular")
        A[col],A[piv]=A[piv],A[col]
        q=A[col][col]
        for j in range(col,n+1): A[col][j]/=q
        for r in range(n):
            if r==col: continue
            q=A[r][col]
            for j in range(col,n+1): A[r][j]-=q*A[col][j]
    return [A[i][n] for i in range(n)]

def solve_c(r):
    def f(c):
        z=1.0
        for x in r: z*=1-c*x
        return 1-c-z
    lo,hi=1e-14,1.0
    for _ in range(200):
        mid=(lo+hi)/2
        if f(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def omega(z):
    if z<=0: return 1.0
    return max(1.0,math.log(z)-1.0)

def two_flip(k,d):
    pts=list(itertools.product((-1,1), repeat=k))
    p0=(1,)*k
    p1=tuple(-1 if i<d else 1 for i in range(k))
    f={}
    for x in pts:
        val=x[0]
        if x==p0 or x==p1: val=-val
        f[x]=val
    a=[]
    for mask in range(1<<k):
        s=0.0
        for x,val in f.items():
            chi=1
            for i in range(k):
                if (mask>>i)&1: chi*=x[i]
            s+=val*chi
        a.append(s/(2**k))
    assert abs(a[0])<1e-15
    return a

def evaluate(k,d):
    a=two_flip(k,d)
    P=[a[m]*a[m] for m in range(1<<k)]
    r=[sum(P[m] for m in range(1,1<<k) if (m>>i)&1) for i in range(k)]
    c=solve_c(r)
    t=[c*x for x in r]
    Q=[0.0]*(1<<k)
    for m in range(1,1<<k):
        z=1.0
        for i in range(k):
            z*=t[i] if (m>>i)&1 else 1-t[i]
        Q[m]=z/c
    assert abs(sum(Q)-1)<1e-11
    assert max(abs(sum(Q[m] for m in range(1,1<<k) if (m>>i)&1)-r[i]) for i in range(k))<1e-10
    b=[0.0]*(1<<k)
    W=[1.0]*(1<<k)
    for m in range(1,1<<k):
        sg=1.0 if a[m]>=0 else -1.0
        b[m]=sg*math.sqrt(Q[m])
        W[m]=omega(P[m]/Q[m])
    cvec=[a[m]+b[m] for m in range(1<<k)]
    g=[]; Y=[]
    for i in range(k):
        sh=1<<i
        g.append(sum(b[m]*b[m^sh] for m in range(1<<k)))
        Y.append([cvec[m^sh]/math.sqrt(W[m]) for m in range(1,1<<k)])
    H=[[sum(Y[i][s]*Y[j][s] for s in range((1<<k)-1)) for j in range(k)] for i in range(k)]
    sol=solve_linear(H,g)
    weights=[2.0*(1.0 if g[i]>=0 else -1.0)*sol[i] for i in range(k)]
    assert min(weights) > 0
    pooled=sum(g[i]*sol[i] for i in range(k))/math.log(2)
    singles=[g[i]*g[i]/(H[i][i]*math.log(2)) for i in range(k)]
    Hp=-sum(p*math.log(p,2) for p in P if p>0)
    Hq=-sum(q*math.log(q,2) for q in Q if q>0)
    K=Hq-Hp
    I=sum(r)
    Binf=C*(I-1)-Hq
    R=C*(I-1)-Hp
    return dict(k=k,d=d,r=r,I=I,H=Hp,Hmax=Hq,K=K,Binf=Binf,R=R,
                pooled=pooled,best_single=max(singles),singles=singles,g=g,Gram=H,weights=weights)

z=evaluate(6,5)
assert z["Binf"] < 0
debt=-z["Binf"]
assert z["best_single"] < debt < z["pooled"] < z["K"]
assert z["R"] > 0
print("PASS")
for key in ("I","H","Hmax","K","Binf","R","best_single","pooled"):
    print(f"{key}={z[key]:.15f}")
print(f"debt={debt:.15f}")
print("r="+repr([round(x,15) for x in z["r"]]))
print("g="+repr([round(x,15) for x in z["g"]]))
print("weights="+repr([round(x,15) for x in z["weights"]]))
