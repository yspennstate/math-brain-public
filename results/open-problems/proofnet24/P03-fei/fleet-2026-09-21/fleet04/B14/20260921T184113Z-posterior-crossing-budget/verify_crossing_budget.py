#!/usr/bin/env python3
"""Finite regression check for the posterior-crossing budget.

This is not a proof of FEI.  The analytic theorem is in REPORT.md.
The script enumerates Boolean functions through n=4 modulo global sign,
centers each spectrum by its coordinatewise median character, retains
functions whose H/J ratio is maximal over all physical descendants, and
checks the all-block budget plus the two-coordinate face identity.
"""
from __future__ import annotations
import itertools, json, math
import numpy as np

TOL = 1e-8

def fwht(a):
    a=np.array(a,dtype=float); h=1; n=len(a)
    while h<n:
        for i in range(0,n,2*h):
            x=a[i:i+h].copy(); y=a[i+h:i+2*h].copy()
            a[i:i+h]=x+y; a[i+h:i+2*h]=x-y
        h*=2
    return a/n

def entropy(vals):
    mu=fwht(vals)**2
    nz=mu>1e-15
    return float(-(mu[nz]*np.log2(mu[nz])).sum())

def influences(vals,n):
    vals=np.asarray(vals); N=1<<n
    idx=np.arange(N)
    return np.array([np.mean(vals != vals[idx^(1<<i)]) for i in range(n)])

def restrict_vals(vals,n,fixed):
    rem=[i for i in range(n) if i not in fixed]; out=[]
    for y in range(1<<len(rem)):
        x=0
        for i,b in fixed.items():
            if b: x|=1<<i
        for r,i in enumerate(rem):
            if (y>>r)&1: x|=1<<i
        out.append(vals[x])
    return np.array(out),rem

def HJ(vals,n):
    H=entropy(vals)
    p=influences(vals,n) if n else np.array([])
    J=float(np.minimum(p,1-p).sum())
    return H,J,p

def center(vals,n):
    _,_,p=HJ(vals,n)
    A=[i for i,x in enumerate(p) if x>0.5+1e-12]
    out=np.array(vals).copy()
    for x in range(1<<n):
        if sum((x>>i)&1 for i in A)&1: out[x]*=-1
    return out

def critical(vals,n):
    vals=center(vals,n); H,J,p=HJ(vals,n)
    if J<=TOL or H<=TOL: return None
    R=H/J
    for r in range(1,n+1):
        for C in itertools.combinations(range(n),r):
            for bits in itertools.product([0,1],repeat=r):
                rv,rem=restrict_vals(vals,n,dict(zip(C,bits)))
                Hr,Jr,_=HJ(rv,len(rem))
                if Jr>TOL and Hr/Jr>R+TOL: return None
    return vals,H,J,p,R

def h2(p):
    if p<=0 or p>=1: return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

def jfun(p):
    p=min(max(float(p),0.0),0.5)
    return 1-h2(0.5+math.sqrt(p*(1-p)))

def Psi(p): return h2(float(p))+jfun(p)

def crossing(vals,n,A):
    A=tuple(sorted(A)); B=[j for j in range(n) if j not in A]; total=0.0
    for j in B:
        a=0.0
        for bits in itertools.product([0,1],repeat=len(A)):
            rv,rem=restrict_vals(vals,n,dict(zip(A,bits)))
            pj=influences(rv,len(rem))[rem.index(j)]
            a+=max(2*pj-1,0)
        total+=a/(2**len(A))
    return total

def mixed_face(vals,n,j,k):
    N=1<<n; idx=np.arange(N)
    eta=(vals != vals[idx^(1<<j)])
    return float(np.mean(eta != eta[idx^(1<<k)]))

summary={}
for n in range(1,5):
    N=1<<n; kept=0
    max_budget_violation=-1e100; max_pair_identity_error=0.0
    max_pair_budget_violation=-1e100
    for mask in range(1<<(N-1)):  # quotient by global output sign
        vals=np.ones(N,dtype=int)
        for x in range(1,N):
            if (mask>>(x-1))&1: vals[x]=-1
        data=critical(vals,n)
        if data is None: continue
        kept+=1
        vals,H,J,p,R=data
        delta=np.array([Psi(x)-R*x for x in p])
        D=float(delta.sum())
        for r in range(1,n+1):
            for A in itertools.combinations(range(n),r):
                v=R*crossing(vals,n,A)-sum(delta[i] for i in A)
                max_budget_violation=max(max_budget_violation,float(v))
        for j in range(n):
            for k in range(j+1,n):
                A=[i for i in range(n) if i not in (j,k)]
                C=crossing(vals,n,A)
                c=mixed_face(vals,n,j,k)
                max_pair_identity_error=max(max_pair_identity_error,abs(C-(p[j]+p[k]-c)))
                v=(Psi(p[j])+Psi(p[k])-D)-R*c
                max_pair_budget_violation=max(max_pair_budget_violation,float(v))
    if kept==0:
        max_budget_violation=max_pair_budget_violation=None
    summary[str(n)]={
        "sign_normalized_critical_cores":kept,
        "max_all_block_budget_violation":max_budget_violation,
        "max_pair_identity_error":max_pair_identity_error,
        "max_pair_budget_violation":max_pair_budget_violation,
    }
print(json.dumps({"status":"PASS","scope":"all Boolean functions n<=4 modulo global sign; analytic theorem not inferred from finite check","summary":summary},indent=2,sort_keys=True))
