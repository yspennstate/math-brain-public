#!/usr/bin/env python3
"""Self-check for B16 active entropy-baseline radial multiplier theorem.

Engineering/self-check only.  The proof is in REPORT.md.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import permutations
from math import comb, log2
import json

def Hc(c: int) -> float:
    eps = 2.0 ** (1-c)
    p0 = (1-eps)**2
    p1 = eps**2
    return -p0*log2(p0) - (2**c-1)*p1*log2(p1)

def kraw(m: int, k: int, l: int) -> int:
    return sum((-1)**j * comb(l,j)*comb(m-l,k-j)
               for j in range(max(0,k-(m-l)), min(k,l)+1))

def W(n: int, k: int) -> float:
    return sum(comb(c-1,k)*Hc(c) for c in range(k+1,n+1))/(n*comb(n-1,k))

def G_direct(n: int, l: int) -> float:
    m=n-1
    return sum(W(n,k)*(comb(m,k)-kraw(m,k,l)) for k in range(1,m+1))

def G_closed(n: int, l: int) -> float:
    m=n-1
    out=0.0
    for c in range(2,n+1):
        ratio=(comb(m-l,c-1)/comb(m,c-1)) if m-l >= c-1 else 0.0
        out += 2**(c-1)*Hc(c)*(1-ratio)
    return out/n

def coeff_direct(n: int, l: int, c: int) -> Fraction:
    m=n-1
    return sum((Fraction(comb(c-1,k), n*comb(m,k)) *
                (comb(m,k)-kraw(m,k,l))) for k in range(1,c))

def coeff_closed(n: int, l: int, c: int) -> Fraction:
    m=n-1
    ratio=(Fraction(comb(m-l,c-1),comb(m,c-1))
           if m-l >= c-1 else Fraction(0))
    return Fraction(2**(c-1),n)*(1-ratio)

def fwht(a):
    a=[float(x) for x in a]
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def spectral_baseline(f,n):
    N=1<<n
    out=0.0
    for i in range(n):
        ei=1<<i
        tau=[f[x]*f[x^ei] for x in range(N)]
        hat=[x/N for x in fwht(tau)]
        for S,a in enumerate(hat):
            if S:
                out += 0.5*a*a*G_closed(n,S.bit_count())
    return out

def direct_baseline(f,n):
    N=1<<n
    total=0.0
    count=0
    for order in permutations(range(n)):
        rank={i:r+1 for r,i in enumerate(order)}
        for anchor in range(N):
            cur=0.0
            for v in range(1,N):
                if v.bit_count()<2:
                    continue
                pivot=min((i for i in range(n) if (v>>i)&1), key=rank.__getitem__)
                e=1<<pivot
                if f[anchor]*f[anchor^e]*f[anchor^v]*f[anchor^v^e] == -1:
                    cur += Hc(n-rank[pivot]+1)
            total += cur
            count += 1
    return total/count

def influences(f,n):
    N=1<<n
    return [sum(f[x]!=f[x^(1<<i)] for x in range(N))/N for i in range(n)]

def run():
    formal=0
    for n in range(2,13):
        for l in range(1,n):
            prev=None
            for c in range(2,n+1):
                assert coeff_direct(n,l,c)==coeff_closed(n,l,c)
                formal += 1
            g=G_closed(n,l)
            assert abs(g-G_direct(n,l))<1e-9
            if prev is not None:
                assert g>prev
            prev=g

    n=3
    N=1<<n
    max_err=0.0
    min_ratio=None
    checked=0
    for mask in range(1<<N):
        f=[-1 if (mask>>x)&1 else 1 for x in range(N)]
        direct=direct_baseline(f,n)
        spec=spectral_baseline(f,n)
        max_err=max(max_err,abs(direct-spec))
        J=sum(min(p,1-p) for p in influences(f,n))
        if J:
            ratio=direct/J
            min_ratio=ratio if min_ratio is None else min(min_ratio,ratio)
            assert direct + 1e-10 >= G_closed(n,1)*J
        checked += 1

    matching={}
    for n in range(2,7):
        N=1<<n
        f=[-1 if ((x&1) and (x&2)) else 1 for x in range(N)]
        B=spectral_baseline(f,n)
        J=sum(min(p,1-p) for p in influences(f,n))
        err=abs(B/J-G_closed(n,1))
        assert err<1e-10
        matching[str(n)]={"B_over_J":B/J,"G1":G_closed(n,1),"error":err}

    complete={}
    for n in (2,4,6):
        N=1<<n
        f=[]
        for x in range(N):
            bits=[(x>>i)&1 for i in range(n)]
            q=0
            for i in range(n):
                for j in range(i+1,n):
                    q ^= bits[i]&bits[j]
            f.append(-1 if q else 1)
        B=spectral_baseline(f,n)
        J=sum(min(p,1-p) for p in influences(f,n))
        err=abs(B/J-G_closed(n,n-1))
        assert err<1e-10
        complete[str(n)]={"B_over_J":B/J,"Gmax":G_closed(n,n-1),"error":err}

    return {
        "status":"PASS",
        "scope":"self_check_not_independent_FEI_verification",
        "formal_entropy_coefficient_identities":formal,
        "all_boolean_functions_n3":checked,
        "max_direct_vs_spectral_error_n3":max_err,
        "minimum_B_over_J_n3":min_ratio,
        "G3_1":G_closed(3,1),
        "matching_quadratic_sharpness":matching,
        "complete_quadratic_endpoint":complete,
        "selected_multipliers":{
            str(n):{"G1":G_closed(n,1),"Gmax":G_closed(n,n-1)}
            for n in (4,6,10,20,40)
        },
    }

if __name__=="__main__":
    print(json.dumps(run(),sort_keys=True,indent=2))
