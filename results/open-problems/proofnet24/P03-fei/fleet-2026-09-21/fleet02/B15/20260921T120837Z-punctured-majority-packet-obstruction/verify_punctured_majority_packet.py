#!/usr/bin/env python3
from math import comb, log2
from fractions import Fraction
import json

def kraw_fixedS(n,t,k):
    s=0
    for j in range(max(0,k-(n-t)), min(t,k)+1):
        s += (-1)**j * comb(t,j)*comb(n-t,k-j)
    return s

def spectrum_levels(n):
    assert n>=6 and n%4==2
    m=n//2
    vals=[-1 if k<m else 1 for k in range(n+1)]
    vals[n]=-1
    W=[]
    for t in range(n+1):
        W.append(sum(vals[k]*kraw_fixedS(n,t,k) for k in range(n+1)))
    return W

rows=[]
for n in range(6,51,4):
    m=n//2
    C=comb(n,m)
    W=spectrum_levels(n)
    target=C-2
    equal_levels=[t for t,w in enumerate(W) if abs(w)==target]
    assert equal_levels == [0,1], (n,equal_levels,W)
    assert W[0]==target and W[1]==-target
    I_spec=sum(Fraction(comb(n,t)*t*W[t]*W[t], 4**n) for t in range(n+1))
    I_edge=Fraction(m*C+n, 2**(n-1))
    assert I_spec==I_edge, (n,I_spec,I_edge)
    assert all((2*k-(n-1))%2 for k in range(n+1))
    a2=Fraction(target*target,4**n)
    p=Fraction((n+1)*target*target,4**n)
    I_packet=Fraction(n*target*target,4**n)
    assert I_packet == a2*n
    rows.append({
        "n":n,
        "central_binomial":C,
        "target_walsh_abs":target,
        "equal_magnitude_levels":equal_levels,
        "packet_mass":str(p),
        "packet_influence_standard":str(I_packet),
        "total_influence":str(I_spec),
        "positive_normalizer_over_packet_influence":((n+1)/n)*log2(n+1),
        "D_packet_over_packet_influence":((n+1)/n)*(n-log2(target))
    })

print(json.dumps({"all_ok": True, "rows": rows}, indent=2, sort_keys=True))
