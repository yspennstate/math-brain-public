#!/usr/bin/env python3
import math, random
import numpy as np

TOL=2e-10

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p)-(1.0-p)*math.log2(1.0-p)

# Synthetic symmetric potential. The addressing identities checked below
# are algebraic and hold for every symmetric Gamma.
def Gamma(p):
    return p*(1.0-p)*(2.3+0.7*(1.0-2.0*p)**2)

def coeffs(vals, ps):
    n=len(ps); N=1<<n
    out=np.zeros(N)
    for S in range(N):
        z=0.0
        for x in range(N):
            fac=1.0
            for i,p in enumerate(ps):
                b=(x>>i)&1
                if (S>>i)&1:
                    fac *= math.sqrt(p*(1-p))*(1.0 if b==0 else -1.0)
                else:
                    fac *= p if b else 1-p
            z += vals[x]*fac
        out[S]=z
    return out

def stats(vals, ps):
    c=coeffs(vals,ps); w=c*c; n=len(ps)
    H=-sum(z*math.log2(z) for z in w if z>1e-300)
    pout=(1-c[0])/2
    Its=[sum(w[S] for S in range(1<<n) if (S>>i)&1) for i in range(n)]
    rhs=0.0
    for Ii,p in zip(Its,ps):
        V=4*p*(1-p)
        rhs += Ii*(Gamma(p)+h2(V))/V
    D=rhs-H-Gamma(pout)
    I=sum(Its)
    W=I/4-pout*(1-pout)
    return H,pout,Its,D,W

def addr_vals(k):
    m=1<<k; n=k+m; vals=[]
    for x in range(1<<n):
        a=sum(((x>>i)&1)<<i for i in range(k))
        y=(x>>(k+a))&1
        vals.append(-1.0 if y else 1.0)
    return vals

def addr_formula(ps,q):
    Vq=4*q*(1-q)
    Vs=[4*p*(1-p) for p in ps]
    H=h2(Vq)+2*Vq*sum(h2(p) for p in ps)
    D=Vq/2*sum(Gamma(p)+h2(V)-4*h2(p) for p,V in zip(ps,Vs))
    W=Vq/8*sum(Vs)
    return H,D,W

def eq_vals(d):
    vals=[]
    for x in range(1<<d):
        all0=(x==0); all1=(x==(1<<d)-1)
        vals.append(-1.0 if (all0 or all1) else 1.0)
    return vals

def and_vals(d):
    vals=[1.0]*(1<<d); vals[0]=-1.0
    return vals

rng=random.Random(170922)
maxH=maxD=maxW=0.0
cases=0
for k in (1,2):
    vals=addr_vals(k)
    for _ in range(12):
        ps=[rng.uniform(0.04,0.96) for _ in range(k)]
        q=rng.uniform(0.04,0.96)
        H,pout,Its,D,W=stats(vals, ps+[q]*(1<<k))
        H0,D0,W0=addr_formula(ps,q)
        maxH=max(maxH,abs(H-H0)); maxD=max(maxD,abs(D-D0)); maxW=max(maxW,abs(W-W0))
        assert abs(pout-q)<TOL
        cases += 1

ps=[0.19,0.47,0.83]; q=0.37
H,pout,Its,D,W=stats(addr_vals(3), ps+[q]*8)
H0,D0,W0=addr_formula(ps,q)
maxH=max(maxH,abs(H-H0)); maxD=max(maxD,abs(D-D0)); maxW=max(maxW,abs(W-W0))
assert abs(pout-q)<TOL
cases += 1

eq_cases=0; min_Idiff=1e99; max_Hdiff=0.0; max_pdiff=0.0
for d in range(3,9):
    E=stats(eq_vals(d), [0.5]*d)
    A=stats(and_vals(d-1), [0.5]*(d-1))
    max_Hdiff=max(max_Hdiff,abs(E[0]-A[0]))
    max_pdiff=max(max_pdiff,abs(E[1]-A[1]))
    Idiff=sum(E[2])-sum(A[2])
    min_Idiff=min(min_Idiff,Idiff)
    assert Idiff >= -TOL
    eq_cases += 1

ok=max(maxH,maxD,maxW,max_Hdiff,max_pdiff)<TOL and min_Idiff>=-TOL
print("PASS" if ok else "FAIL")
print(f"addressing_direct_cases={cases}")
print(f"max_abs_addressing_H_error={maxH:.3e}")
print(f"max_abs_addressing_D_error={maxD:.3e}")
print(f"max_abs_addressing_W_error={maxW:.3e}")
print(f"uniform_EQ_cases={eq_cases}")
print(f"max_abs_EQ_AND_H_error={max_Hdiff:.3e}")
print(f"max_abs_EQ_AND_pout_error={max_pdiff:.3e}")
print(f"min_EQ_minus_AND_influence={min_Idiff:.12g}")
