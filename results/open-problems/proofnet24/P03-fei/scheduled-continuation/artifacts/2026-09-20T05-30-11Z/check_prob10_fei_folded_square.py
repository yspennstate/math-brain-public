#!/usr/bin/env python3
"""
Finite self-check for the folded square-curvature mechanism in PROB10-01.

Checks:
  B_i(f) <= (1/2) J(D_i f) + kappa_3 j_i(f),
  F2(f) >= J(D_i f) + (F2(f^+)+F2(f^-))/2,
  H(f) <= (1/2) F2(f) + (kappa_3+2/ln 2) J(f),
for every Boolean truth table through dimension four.

Floating entropy evaluations are only a self-check; the report contains
all-dimensional proofs.  Influence quantities are dyadic in these tests.
"""
import json, math
from functools import lru_cache

KAPPA3 = 4.0 * (-(0.25)*math.log2(0.25) -(0.75)*math.log2(0.75))
C = 1.0/math.log(2.0)
TOL = 5e-11

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

@lru_cache(None)
def fwht(vals):
    a=[float(x) for x in vals]
    N=len(a); h=1
    while h<N:
        for s in range(0,N,2*h):
            for j in range(s,s+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return tuple(x/N for x in a)

@lru_cache(None)
def metrics(vals):
    p=tuple(x*x for x in fwht(vals))
    n=len(vals).bit_length()-1
    infl=tuple(sum(q for s,q in enumerate(p) if (s>>i)&1) for i in range(n))
    H=sum(-q*math.log2(q) for q in p if q>0.0)
    J=sum(min(a,1.0-a) for a in infl)
    return p,infl,H,J

@lru_cache(None)
def restrict(vals,i,b):
    n=len(vals).bit_length()-1
    out=[]
    for m in range(1<<(n-1)):
        lo=m&((1<<i)-1)
        hi=m>>i
        x=lo|(b<<i)|(hi<<(i+1))
        out.append(vals[x])
    return tuple(out)

@lru_cache(None)
def derivative(vals,i):
    a=restrict(vals,i,0)
    b=restrict(vals,i,1)
    return tuple(x*y for x,y in zip(a,b))

def B_i(vals,i):
    p=metrics(vals)[0]
    ans=0.0
    for s in range(len(p)):
        if ((s>>i)&1)==0:
            a,b=p[s],p[s|(1<<i)]
            q=a+b
            if q:
                ans += q*h2(b/q)
    return ans

@lru_cache(None)
def F2(vals):
    n=len(vals).bit_length()-1
    if n<2:
        return 0.0
    # Every unordered pair is counted in J(D_i) from both endpoints.
    return 0.5*sum(metrics(derivative(vals,i))[3] for i in range(n))

stats={
    "status":"PASS",
    "kappa3":KAPPA3,
    "one_over_ln2":C,
    "global_J_constant":KAPPA3+2*C,
    "coordinate_cases":0,
    "max_local_folded_derivative_violation":-1e100,
    "max_F2_supermartingale_violation":-1e100,
    "max_global_F2_entropy_violation":-1e100,
    "by_dimension":{}
}

for n in range(1,5):
    N=1<<n
    cases=0
    for mask in range(1<<N):
        vals=tuple(-1 if ((mask>>x)&1) else 1 for x in range(N))
        p,infl,H,Jroot=metrics(vals)
        global_violation=H-(0.5*F2(vals)+(KAPPA3+2*C)*Jroot)
        stats["max_global_F2_entropy_violation"]=max(
            stats["max_global_F2_entropy_violation"],global_violation)
        for i in range(n):
            j=min(infl[i],1.0-infl[i])
            D=derivative(vals,i)
            JD=metrics(D)[3] if len(D)>1 else 0.0
            local=B_i(vals,i)-(0.5*JD+KAPPA3*j)
            stats["max_local_folded_derivative_violation"]=max(
                stats["max_local_folded_derivative_violation"],local)
            a,b=restrict(vals,i,0),restrict(vals,i,1)
            tel=JD+0.5*(F2(a)+F2(b))-F2(vals)
            stats["max_F2_supermartingale_violation"]=max(
                stats["max_F2_supermartingale_violation"],tel)
            cases+=1
    stats["by_dimension"][str(n)]=cases
    stats["coordinate_cases"]+=cases

# Exact symbolic family ratios used as adversarial scope checks.
one_point=[]
for n in range(3,15):
    # F2/J = n-1 for a one-point defect.
    one_point.append({"n":n,"F2_over_J_exact":n-1})

addressing=[]
for s in range(2,15):
    # f(a,y)=y_a, m=2^s. F2=s(s-1)/4+2s, J=s/2+1.
    F2v=s*(s-1)/4+2*s
    Jv=s/2+1
    addressing.append({"s":s,"F2_over_J":F2v/Jv})

cubic_star=[]
for r in range(1,15):
    # Three folded square pairs of mass 1/2 per cubic monomial.
    F2v=1.5*r
    Jv=r/2+(1-2**(-r))/2
    cubic_star.append({"r":r,"F2_over_J":F2v/Jv})

for key in ("max_local_folded_derivative_violation",
            "max_F2_supermartingale_violation",
            "max_global_F2_entropy_violation"):
    if stats[key] > TOL:
        stats["status"]="FAIL"

stats["one_point_obstruction"]=one_point
stats["addressing_obstruction"]=addressing
stats["cubic_star_calibration"]=cubic_star
stats["limitations"]="Finite self-check only; no independent audit, no Lean verification, and no claim that F2 <= K J universally (one-point/addressing formulas refute that scalar closure)."

print(json.dumps(stats,indent=2,sort_keys=True))
