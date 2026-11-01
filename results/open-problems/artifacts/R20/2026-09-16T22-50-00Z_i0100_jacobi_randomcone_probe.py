#!/usr/bin/env python3
"""
R20 / I0100 research probe.

PART A is an EXACT INTEGER self-check of the all-prime Paley multiplicative
sequence autocorrelation identity used in the accompanying written proof.

PART B is DISCOVERY ONLY: floating LP experiments comparing
(i) random symmetric half-density Fourier row sets and
(ii) Haar/Gaussian projected simplices.
PART B is not an exact theta certificate and does not move R20's frozen metric.
"""
import math
import numpy as np
from scipy.optimize import linprog

SEED=20260917
rng=np.random.default_rng(SEED)

def primes_upto(n):
    ps=[]
    for p in range(2,n+1):
        ok=True
        for q in range(2,int(math.isqrt(p))+1):
            if p%q==0:
                ok=False; break
        if ok: ps.append(p)
    return ps

def primitive_root(p):
    phi=p-1
    fac=[]
    x=phi
    q=2
    while q*q<=x:
        if x%q==0:
            fac.append(q)
            while x%q==0:x//=q
        q+=1
    if x>1:fac.append(x)
    for g in range(2,p):
        if all(pow(g,phi//q,p)!=1 for q in fac):
            return g
    raise RuntimeError

def chi(a,p):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def exact_autocorr_check(p):
    L=p-1
    g=primitive_root(p)
    a=[chi(1-pow(g,j,p),p) for j in range(L)]
    assert a[0]==0
    assert sum(x*x for x in a)==p-2
    assert sum(a)==-1
    assert sum(((-1)**j)*a[j] for j in range(L))==-1
    for r in range(1,L):
        C=sum(a[j]*a[(j+r)%L] for j in range(L))
        expected=0 if r%2 else -2
        assert C==expected,(p,r,C,expected)
    n=L//2
    alpha=pow(g,2,p)
    for d in range(1,n):
        u=chi(1-pow(alpha,d,p),p)
        if u==1:
            assert a[(2*d)%L]==1 and a[(-2*d)%L]==1
    return True

checked=[]
for p in primes_upto(421):
    if p%4==1:
        exact_autocorr_check(p)
        checked.append(p)

print("PART_A_EXACT_INTEGER_SELF_CHECK=PASS")
print("checked_all_primes_p_eq_1_mod_4_up_to_421=",checked)

def random_symmetric_S(n,d):
    pairs=[]
    singles=[]
    for s in range(1,n):
        t=(-s)%n
        if s<t:pairs.append((s,t))
        elif s==t:singles.append(s)
    S=[]
    if d%2:
        assert singles
        S.append(singles[0])
    k=(d-len(S))//2
    ids=rng.choice(len(pairs),size=k,replace=False)
    for idx in ids:
        S.extend(pairs[int(idx)])
    return S

def theta_moment_lp(n,S):
    ms=np.arange(n,dtype=float)
    reps=sorted({min(s,(-s)%n) for s in S})
    A=[np.ones(n)]
    b=[1.0]
    for s in reps:
        A.append(np.cos(2*np.pi*s*ms/n)); b.append(0.0)
        if s not in (0,n//2):
            A.append(np.sin(2*np.pi*s*ms/n)); b.append(0.0)
    c=np.zeros(n); c[0]=-1.0
    res=linprog(c,A_eq=np.asarray(A),b_eq=np.asarray(b),
                bounds=[(0,None)]*n,method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    return 1.0/res.x[0]

def haar_simplex_theta(n):
    d=n//2-1
    G=rng.normal(size=(d,n))
    G-=G.mean(axis=1,keepdims=True)
    A=np.vstack([np.ones(n),G])
    b=np.r_[1.0,np.zeros(d)]
    c=np.zeros(n); c[0]=-1.0
    res=linprog(c,A_eq=A,b_eq=b,bounds=[(0,None)]*n,method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    return 1.0/res.x[0]

print("PART_B_DISCOVERY_ONLY=BEGIN")
print("seed=",SEED)
for n in [40,80,120,210,400]:
    d=n//2-1
    circ=[]
    haar=[]
    for _ in range(12):
        circ.append(theta_moment_lp(n,random_symmetric_S(n,d))/math.sqrt(n))
        haar.append(haar_simplex_theta(n)/math.sqrt(n))
    def stats(x):
        a=np.asarray(x)
        return (float(a.mean()),float(a.std()),
                float(np.quantile(a,.1)),float(np.median(a)),float(np.quantile(a,.9)))
    print("n=",n,
          "random_symmetric_fourier_theta_over_sqrtn mean,std,q10,median,q90=",stats(circ))
    print("n=",n,
          "haar_projected_simplex_theta_over_sqrtn mean,std,q10,median,q90=",stats(haar))
print("PART_B_DISCOVERY_ONLY=END")
print("NO_EXACT_PRIME_METRIC_MOVEMENT_CLAIMED")
