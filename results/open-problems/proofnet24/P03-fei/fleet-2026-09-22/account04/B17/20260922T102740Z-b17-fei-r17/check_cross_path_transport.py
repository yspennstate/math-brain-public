import math
from itertools import product

def fwht(vals):
    a=[float(x) for x in vals]
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    N=len(a)
    return [x/N for x in a]

def h2(x):
    if x<=0.0 or x>=1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def jfun(q):
    if q<=0.0: return 0.0
    return 1.0-h2(0.5+math.sqrt(q*(1-q)))

def kl(P,Q):
    s=0.0
    for p,q in zip(P,Q):
        if p>0:
            if q<=0: return float("inf")
            s += p*math.log2(p/q)
    return s

def bernkl(p,q):
    s=0.0
    if p>0: s+=p*math.log2(p/q)
    if p<1: s+=(1-p)*math.log2((1-p)/(1-q))
    return s

def iproj_nonempty(r):
    mu=sum(r)
    if mu<=1+1e-13:
        return None,None
    def F(c):
        z=1.0
        for ri in r:z*=1-c*ri
        return 1-z-c
    lo=1e-14; hi=1.0
    for _ in range(120):
        mid=(lo+hi)/2
        if F(mid)>0: lo=mid
        else: hi=mid
    c=(lo+hi)/2
    t=[c*ri for ri in r]
    N=1<<len(r)
    Q=[0.0]*N
    for S in range(1,N):
        z=1.0
        for i,ti in enumerate(t):
            z*=ti if ((S>>i)&1) else (1-ti)
        Q[S]=z/c
    return c,Q

def median_shift(P,n):
    marg=[sum(P[S] for S in range(1<<n) if (S>>i)&1) for i in range(n)]
    T=0
    for i,ri in enumerate(marg):
        if ri>0.5:
            T|=1<<i
    Pg=[0.0]*(1<<n)
    for S in range(1<<n):
        Pg[S]=P[S^T]
    return T,Pg

checks=0
worst=0.0
for n in (2,3,4):
    N=1<<n
    # global sign duplicates spectra, so fix truth-table value 0 to +1
    for tail in range(1<<(N-1)):
        vals=[1]+[1 if ((tail>>(x-1))&1)==0 else -1 for x in range(1,N)]
        hats=fwht(vals)
        P=[a*a for a in hats]
        T,Pg=median_shift(P,n)
        q=[sum(Pg[S] for S in range(N) if (S>>i)&1) for i in range(n)]
        J=sum(q)
        if J<1e-14:
            continue
        H=-sum(p*math.log2(p) for p in Pg if p>0)
        Ks=sum(h2(x) for x in q)-H
        if Ks<-2e-11:
            raise AssertionError(("Ks negative",n,tail,Ks))
        # exact Path-C surplus transport at rho=4
        Pc=sum(jfun(x) for x in q)
        lhs=H-Pc-4*J
        reserve=sum(h2(x)-jfun(x)-4*x for x in q)
        err=abs(lhs-(reserve-Ks))
        worst=max(worst,err)
        if err>2e-10:
            raise AssertionError(("surplus",n,tail,err))
        # Anchor-conditioned decomposition when nonempty branch has mu>1.
        v=1-Pg[0]
        c0=1.0
        for x in q: c0*=1-x
        c0=1-c0
        if v>1e-12 and c0>1e-12:
            Pplus=[0.0]*N
            for S in range(1,N): Pplus[S]=Pg[S]/v
            r=[x/v for x in q]
            mu=sum(r)
            if mu>1+1e-9:
                c,Qa=iproj_nonempty(r)
                Ka=kl(Pplus,Qa)
                R=[0.0]*N
                for S in range(N):
                    z=1.0
                    for i,x in enumerate(q):
                        z*=x if ((S>>i)&1) else (1-x)
                    R[S]=z
                Rp=[0.0]*N
                for S in range(1,N): Rp[S]=R[S]/c0
                Km=kl(Qa,Rp)
                rhs=bernkl(v,c0)+v*Ka+v*Km
                err=abs(Ks-rhs)
                worst=max(worst,err)
                if err>5e-9:
                    raise AssertionError(("anchor",n,tail,v,c0,Ks,rhs,err))
        # radial mismatch identity for balanced suspension
        z=0.07
        d=n+1
        A=(1+z)**d-1
        # Suspension law indexed by old S but corresponding set size 1+|S|
        Drad=sum(Pg[S]*math.log2(Pg[S]/(z**(1+S.bit_count())/A))
                  for S in range(N) if Pg[S]>0)
        Qs=[0.0]*N
        for S in range(N):
            w=1.0
            for i,x in enumerate(q):
                w*=x if ((S>>i)&1) else (1-x)
            Qs[S]=w
        Mrad=math.log2(A)-(1+J)*math.log2(z)-sum(h2(x) for x in q)
        err=abs(Drad-(Ks+Mrad))
        worst=max(worst,err)
        if err>5e-9:
            raise AssertionError(("radial",n,tail,err))
        checks+=1

# Mandatory recursive-majority preflight from the source-exact formulas.
for m in range(1,13):
    q=2.0**(-m)
    J=(1.5)**m
    H=4*(J-1)
    Ks=(3**m)*h2(q)-H
    lower=(m-4)*J+4
    if Ks+1e-10<lower:
        raise AssertionError(("RM3 KL growth",m,Ks,lower))
    Pc=(3**m)*jfun(q)
    surplus=H-Pc-4*J
    if abs(surplus-(-4-Pc))>1e-9:
        raise AssertionError(("RM3 surplus",m,surplus,-4-Pc))

print("CROSS_PATH_TRANSPORT_EXHAUSTIVE_PASS", checks)
print("MAX_ABS_IDENTITY_ERROR", format(worst,".3e"))
print("RM3_MULTISCALE_PREFLIGHT_PASS", 12)
print("ALL_CHECKS_PASS")
