#!/usr/bin/env python3
"""Sanity checks for B17 self-XOR/Hellinger FEI bridge.

Analytic theorems are proved in REPORT.md.  This script checks only finite
implementations:
  * exact physical-translation dictionary for all Boolean functions n<=3;
  * exact vanishing of singleton Hellinger affinities for odd majorities n=3,5,7;
  * exact one-point-defect formulas for n=3..12;
  * numerical (not theorem-establishing) H(P) <= B(P) on all Boolean functions n<=3.

Walsh transforms and algebraic identities use integers/Fraction.  Transcendental
entropy values are displayed with ordinary floating point and are not used to
certify any universal theorem.
"""
from fractions import Fraction
from math import log2
import json

def fwht_int(vals):
    a=list(map(int,vals)); h=1; N=len(a)
    while h<N:
        for i in range(0,N,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def spectrum(vals):
    N=len(vals); W=fwht_int(vals)
    p=[Fraction(w*w,N*N) for w in W]
    absamp=[Fraction(abs(w),N) for w in W]
    return W,p,absamp

def xor_convolution(p):
    N=len(p)
    return [sum(p[s]*p[s^d] for s in range(N)) for d in range(N)]

def affinities(absamp):
    N=len(absamp)
    return [sum(absamp[s]*absamp[s^d] for s in range(N)) for d in range(N)]

def entropy(prob):
    return -sum(float(x)*log2(float(x)) for x in prob if x)

def bridge(vals):
    W,p,a=spectrum(vals)
    c=xor_convolution(p); A=affinities(a)
    B=entropy(c)+sum(float(c[d])*log2(float(A[d])) for d in range(len(c)) if c[d])
    return entropy(p),B,p,c,A

def influence_marginals(p,n):
    return [sum(p[s] for s in range(len(p)) if (s>>i)&1) for i in range(n)]

def physical_delta(vals,x):
    N=len(vals)
    return Fraction(sum(vals[y]!=vals[y^x] for y in range(N)),N)

def majority_vals(n):
    assert n%2==1
    return [1 if x.bit_count()<=n//2 else -1 for x in range(1<<n)]

# 1. Exact translation dictionary and numerical bridge check, exhaustive n<=3.
dictionary_checks=0
bridge_checks=0
min_bridge_gap=10.0
for n in range(1,4):
    N=1<<n
    # quotient global sign by fixing value at 0 = +1
    for mask in range(1<<(N-1)):
        vals=[1]*N
        for x in range(1,N):
            if (mask>>(x-1))&1:
                vals[x]=-1
        H,B,p,c,A=bridge(vals)
        if B+1e-11 < H:
            raise AssertionError(("bridge",n,mask,H,B))
        min_bridge_gap=min(min_bridge_gap,B-H)
        bridge_checks+=1
        for x in range(N):
            lhs=sum(c[d] for d in range(N) if ((d & x).bit_count()&1))
            delta=physical_delta(vals,x)
            rhs=2*delta*(1-delta)
            if lhs!=rhs:
                raise AssertionError(("dictionary",n,mask,x,lhs,rhs))
            dictionary_checks+=1

# 2. Odd majority has only odd Fourier levels, hence singleton A_ei = 0.
majority_checks=[]
for n in (3,5,7):
    vals=majority_vals(n)
    W,p,a=spectrum(vals); A=affinities(a)
    even_nonzero=sum(1 for s,w in enumerate(W) if w and s.bit_count()%2==0)
    singleton=[A[1<<i] for i in range(n)]
    assert even_nonzero==0
    assert all(x==0 for x in singleton)
    H,B,_,_,_=bridge(vals)
    majority_checks.append({
        "n":n,
        "entropy":H,
        "bridge":B,
        "singleton_affinities":["0" for _ in singleton]
    })

# 3. One-point defect exact formulas.
# Direct Walsh/convolution replay is done only through n=7; n=8..12 use the
# analytically derived closed forms to avoid quadratic Fraction work.
one_point=[]
for n in range(3,13):
    N=1<<n
    alpha=Fraction(2,N)
    I=Fraction(2*n,N)
    rho=2*alpha*(1-alpha)
    cstar=Fraction(8*(N-2),N**3)
    R=Fraction(N-1)*cstar
    Astar=Fraction(8*(N-2),N**2)
    p0=Fraction((N-2)**2,N**2)
    pu=Fraction(4,N**2)
    h2=lambda z: 0.0 if z in (0,1) else -float(z)*log2(float(z))-(1-float(z))*log2(1-float(z))
    rp=1-p0
    H_formula=h2(rp)+float(rp)*log2(N-1)
    B_formula=h2(R)+float(R)*log2(float((N-1)*Astar))
    M_formula=n*h2(rho)+float(R)*log2(float(Astar))
    if n<=7:
        vals=[1]*N; vals[0]=-1
        H,B,p,c,A=bridge(vals)
        assert p[0]==p0
        assert all(p[s]==pu for s in range(1,N))
        assert all(c[d]==cstar for d in range(1,N))
        assert all(A[d]==Astar for d in range(1,N))
        infs=influence_marginals(p,n)
        assert all(q==alpha for q in infs)
        if abs(H-H_formula)>1e-10 or abs(B-B_formula)>1e-10:
            raise AssertionError(("closed_form",n,H,H_formula,B,B_formula))
    one_point.append({
        "n":n,
        "H_over_I":H_formula/float(I),
        "B_joint_over_I":B_formula/float(I),
        "B_marginalized_over_I":M_formula/float(I),
        "R_nonzero_difference":str(R),
        "A_nonzero_shift":str(Astar)
    })

out={
    "status":"PASS",
    "scope":"exact algebraic checks as documented; transcendental entropy comparisons are finite numerical sanity checks only",
    "dictionary_exact_checks":dictionary_checks,
    "bridge_numerical_checks":bridge_checks,
    "min_finite_B_minus_H":min_bridge_gap,
    "majority_singleton_obstruction":majority_checks,
    "one_point_defect":one_point,
    "full_FEI_status":"OPEN / NOT PROVED"
}
print(json.dumps(out,indent=2,sort_keys=True))
