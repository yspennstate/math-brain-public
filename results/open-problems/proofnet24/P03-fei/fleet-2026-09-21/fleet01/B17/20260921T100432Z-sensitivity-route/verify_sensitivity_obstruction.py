#!/usr/bin/env python3
"""Exact-formula check for the B17 one-point sensitivity-set obstruction.

For f_n:{0,1}^n->{-1,+1} with f_n(0^n)=-1 and f_n(x)=+1 otherwise:
Sens(0^n)=[n], Sens(e_i)={i}, otherwise Sens(x)=empty.
The script evaluates closed-form entropies and, for n<=8, checks the
sensitivity-set distribution by direct enumeration.
"""
import math, json

def phi(p):
    return 0.0 if p <= 0.0 else -p*math.log2(p)

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return phi(p)+phi(1.0-p)

def closed(n):
    N=2**n
    q=(n+1)/N
    I=n*2**(1-n)
    Hsens=h2(q)+q*math.log2(n+1)
    Hsize=h2(q)+q*h2(1/(n+1))
    p0=(1-2**(1-n))**2
    pnon=2**(2-2*n)
    Hfour=phi(p0)+(N-1)*phi(pnon)
    return {
        "n": n,
        "influence": I,
        "boundary_activation": q,
        "sensitivity_set_entropy": Hsens,
        "sensitivity_set_entropy_over_I": Hsens/I,
        "sensitivity_size_entropy": Hsize,
        "sensitivity_size_entropy_over_I": Hsize/I,
        "fourier_entropy": Hfour,
        "fourier_entropy_over_I": Hfour/I,
    }

def brute_sensitivity_distribution(n):
    N=2**n
    counts={}
    for x in range(N):
        fx=-1 if x==0 else 1
        mask=0
        for i in range(n):
            y=x^(1<<i)
            fy=-1 if y==0 else 1
            if fx != fy:
                mask |= 1<<i
        counts[mask]=counts.get(mask,0)+1
    return counts

rows=[]
for n in (2,3,4,5,8,12,16,24,32):
    r=closed(n)
    if n<=8:
        c=brute_sensitivity_distribution(n)
        expected={0:2**n-(n+1),(1<<n)-1:1}
        for i in range(n):
            expected[1<<i]=1
        expected={k:v for k,v in expected.items() if v}
        assert c==expected, (n,c,expected)
        r["brute_distribution_check"]="PASS"
    rows.append(r)

for n in (24,32):
    r=closed(n)
    assert abs(r["sensitivity_set_entropy_over_I"] - n/2) < 2.0
    assert abs(r["fourier_entropy_over_I"] - 4.0) < 0.1

out={
    "schema":"b17-fei-sensitivity-obstruction-v1",
    "family":"one-point defect",
    "formula":{
        "Pr_sens_empty":"1-(n+1)/2^n",
        "Pr_sens_full":"2^-n",
        "Pr_sens_singleton_i":"2^-n for each i",
        "I":"n*2^(1-n)",
        "H_sens":"h2((n+1)/2^n)+((n+1)/2^n)*log2(n+1)",
        "H_sens_over_I_asymptotic":"n/2 + O(1)",
        "H_fourier_over_I_limit":"4"
    },
    "rows":rows,
    "status":"PASS"
}
print(json.dumps(out,indent=2,sort_keys=True))
