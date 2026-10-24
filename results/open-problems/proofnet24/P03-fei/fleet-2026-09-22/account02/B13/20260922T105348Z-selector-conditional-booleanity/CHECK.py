#!/usr/bin/env python3
import itertools, math

LN2 = math.log(2.0)

def bits(x,n): return [(x>>i)&1 for i in range(n)]
def wt(xb, ps):
    z=1.0
    for b,p in zip(xb,ps): z*=p if b else (1-p)
    return z
def phi(b,p): return (b-p)/math.sqrt(p*(1-p))

def coeffs(vals, ps):
    n=len(ps); out=[0.0]*(1<<n)
    for x in range(1<<n):
        xb=bits(x,n); w=wt(xb,ps); ph=[phi(xb[i],ps[i]) for i in range(n)]
        for S in range(1<<n):
            z=1.0
            for i in range(n):
                if (S>>i)&1: z*=ph[i]
            out[S]+=w*vals[x]*z
    return out

def qform(z,U,ps):
    n=len(ps); kap=[(1-2*p)/math.sqrt(p*(1-p)) for p in ps]; ans=0.0
    for A in range(1<<n):
        for B in range(1<<n):
            c=1.0
            for i in range(n):
                a=(A>>i)&1; b=(B>>i)&1; u=(U>>i)&1
                if not u: d=1.0 if a==b else 0.0
                elif a==0 and b==0: d=0.0
                elif a!=b: d=1.0
                else: d=kap[i]
                c*=d
                if c==0.0: break
            ans += z[A]*z[B]*c
    return ans

def h2(x):
    if x<=1e-15 or x>=1-1e-15: return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)
def H(z):
    return sum(-a*a*math.log2(a*a) for a in z if a*a>1e-15)

def iproj(z):
    m=(len(z)).bit_length()-1
    v=sum(z[S]*z[S] for S in range(1,1<<m))
    if v<1e-14: return v,None,0.0
    P=[0.0]*(1<<m)
    for S in range(1,1<<m): P[S]=z[S]*z[S]/v
    r=[sum(P[S] for S in range(1,1<<m) if (S>>i)&1) for i in range(m)]
    mu=sum(r); Q=[0.0]*(1<<m)
    if abs(mu-1.0)<1e-10:
        for i,ri in enumerate(r): Q[1<<i]=ri
    else:
        def F(c):
            pr=1.0
            for ri in r: pr*=1-c*ri
            return 1-c-pr
        lo,hi=1e-12,1.0
        for _ in range(180):
            mid=(lo+hi)/2
            if F(mid)>0: lo=mid
            else: hi=mid
        c=(lo+hi)/2
        ts=[c*ri for ri in r]
        for S in range(1,1<<m):
            pr=1.0
            for i,ti in enumerate(ts): pr*=ti if (S>>i)&1 else (1-ti)
            Q[S]=pr/c
        zq=sum(Q); Q=[u/zq for u in Q]
    K=0.0
    for S in range(1,1<<m):
        if P[S]>1e-15: K+=P[S]*math.log2(P[S]/Q[S])
    return v,Q,K

def gap(z,ps,U,Q):
    if Q is None: return 0.0
    m=len(ps); v=sum(z[S]*z[S] for S in range(1,1<<m)); atoms=[S for S in range(1,1<<m) if Q[S]>1e-15]
    best=float("inf")
    for mask in range(1<<len(atoms)):
        b=[0.0]*(1<<m); b[0]=z[0]
        for k,S in enumerate(atoms):
            b[S]=(-1.0 if (mask>>k)&1 else 1.0)*math.sqrt(v*Q[S])
        best=min(best,abs(qform(b,U,ps)))
    return best

psr=[0.29,0.63]; selectors=[0.17,0.37,0.81]
max_transform=max_defect=max_entropy=max_credit_violation=0.0
identity_cases=credit_cases=0
for truth in itertools.product([-1,1],repeat=8):
    vals=list(truth)
    ch0=[vals[r<<1] for r in range(4)]
    ch1=[vals[(r<<1)|1] for r in range(4)]
    u=coeffs(ch0,psr); v=coeffs(ch1,psr)
    v0,Q0,K0=iproj(u); v1,Q1,K1=iproj(v)
    for t in selectors:
        q=1-t; a=coeffs(vals,[t]+psr)
        for S in range(4):
            max_transform=max(max_transform,abs(a[S<<1]-(q*u[S]+t*v[S])))
            max_transform=max(max_transform,abs(a[(S<<1)|1]-math.sqrt(t*q)*(v[S]-u[S])))
        HB=HJ=0.0
        for S in range(4):
            ms=q*u[S]*u[S]+t*v[S]*v[S]
            if ms>1e-15:
                theta=t*v[S]*v[S]/ms
                psi=t*q*(v[S]-u[S])**2/ms
                HB+=ms*h2(theta); HJ+=ms*h2(psi)
        rhs=h2(t)+q*H(u)+t*H(v)+HJ-HB
        max_entropy=max(max_entropy,abs(H(a)-rhs))
        for U in range(4):
            e0=qform(u,U,psr)-(1.0 if U==0 else 0.0)
            e1=qform(v,U,psr)-(1.0 if U==0 else 0.0)
            A=qform(a,U<<1,[t]+psr)-(1.0 if U==0 else 0.0)
            B=qform(a,(U<<1)|1,[t]+psr)
            max_defect=max(max_defect,abs(A-(q*e0+t*e1)),abs(B-math.sqrt(t*q)*(e1-e0)))
            max_defect=max(max_defect,abs(A*A+B*B-(q*e0*e0+t*e1*e1)))
        for U in (1,2,3):
            g0=gap(u,psr,U,Q0); g1=gap(v,psr,U,Q1)
            L=1.0
            for i,p in enumerate(psr):
                if (U>>i)&1: L*=math.sqrt(max(p,1-p)/min(p,1-p))
            lhs=q*v0*K0+t*v1*K1
            rhs=(q*g0*g0+t*g1*g1)/(4*L*L*LN2)
            max_credit_violation=max(max_credit_violation,rhs-lhs)
            credit_cases+=1
        identity_cases+=1

tol=2e-12
assert max_transform<tol and max_defect<tol and max_entropy<tol and max_credit_violation<tol
print("PASS")
print("identity_cases",identity_cases)
print("credit_cases",credit_cases)
print("max_transform_error",format(max_transform,".3e"))
print("max_defect_energy_error",format(max_defect,".3e"))
print("max_entropy_identity_error",format(max_entropy,".3e"))
print("max_credit_violation",format(max_credit_violation,".3e"))
