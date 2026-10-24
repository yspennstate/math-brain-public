#!/usr/bin/env python3
"""Exact checks for the positive-XOR-coupling obstruction.

Scope:
  * exact Walsh spectra for one-point defects f_0 and f_v and their product;
  * all-dimensional symbolic Fréchet/Hall obstruction for n=3,...,12;
  * n=3, v=3 exact transportation witness showing the minimum TV defect is 1/8;
  * exact physical simultaneous-flip overlap R=0 when wt(v)>=2.

This checker does NOT prove FEI.  It checks the finite algebra and one sharp
8-point transportation witness used by the accompanying analytic proof.
Only Python's standard library and Fraction arithmetic are used.
"""
from fractions import Fraction
from collections import defaultdict
import json

def parity(x):
    return x.bit_count() & 1

def fwht(vals):
    a = list(map(int, vals))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def spectrum_sq(vals):
    W = fwht(vals)
    N = len(vals)
    return [Fraction(w*w, N*N) for w in W]

def one_point(N, u):
    return [-1 if x == u else 1 for x in range(N)]

def product(a,b):
    return [x*y for x,y in zip(a,b)]

def influence(vals):
    N=len(vals); n=N.bit_length()-1
    out=[]
    for i in range(n):
        c=0
        for x in range(N):
            if vals[x] != vals[x^(1<<i)]:
                c += 1
        out.append(Fraction(c,N))
    return out

def simultaneous_overlap(a,b):
    N=len(a); n=N.bit_length()-1
    s=Fraction(0)
    for i in range(n):
        c=0
        for x in range(N):
            if a[x] != a[x^(1<<i)] and b[x] != b[x^(1<<i)]:
                c+=1
        s += Fraction(c,N)
    return s

rows=[]
for n in range(3,13):
    N=1<<n
    v=3  # Hamming weight two
    f0=one_point(N,0)
    fv=one_point(N,v)
    h=product(f0,fv)
    p0=spectrum_sq(f0)
    pv=spectrum_sq(fv)
    r=spectrum_sq(h)
    assert p0 == pv
    w=Fraction((N-2)**2,N*N)
    eps=Fraction(4,N*N)
    assert p0[0] == w
    assert all(p0[s] == eps for s in range(1,N))
    H=[s for s in range(N) if parity(s&v)==0]
    assert len(H)==N//2
    assert r[0] == Fraction((N-4)**2,N*N)
    for s in range(1,N):
        target=Fraction(16,N*N) if s in H else Fraction(0)
        assert r[s] == target
    alpha=sum((p0[s] for s in H),Fraction(0))
    assert alpha == Fraction(N-2,N)
    forced=2*w-alpha
    target0=r[0]
    gap=forced-target0
    assert gap == Fraction(2*(N-4),N*N)
    assert gap>0
    assert simultaneous_overlap(f0,fv)==0
    inf0=influence(f0); infv=influence(fv); infh=influence(h)
    assert all(x==Fraction(2,N) for x in inf0)
    assert inf0==infv
    assert all(x==Fraction(4,N) for x in infh)
    rows.append({
        "n":n,
        "N":N,
        "parent_H_mass":str(alpha),
        "frechet_xor_zero_floor":str(forced),
        "child_xor_zero_target":str(target0),
        "tv_lower_bound":str(gap),
        "simultaneous_overlap":str(simultaneous_overlap(f0,fv)),
        "parent_total_influence":str(sum(inf0,Fraction(0))),
        "child_total_influence":str(sum(infh,Fraction(0))),
    })

# Exact n=3 transportation witness.  Rows/cols are frequencies 0,...,7.
# Entries are multiples of 1/16.
M=[
 [6,0,0,1,1,0,0,1],
 [0,0,0,0,0,0,1,0],
 [0,0,0,0,0,1,0,0],
 [1,0,0,0,0,0,0,0],
 [1,0,0,0,0,0,0,0],
 [0,1,0,0,0,0,0,0],
 [0,0,1,0,0,0,0,0],
 [1,0,0,0,0,0,0,0],
]
N=8; v=3
p=[Fraction(9,16)]+[Fraction(1,16)]*7
pi=[[Fraction(M[a][b],16) for b in range(N)] for a in range(N)]
assert [sum(row,Fraction(0)) for row in pi]==p
assert [sum((pi[a][b] for a in range(N)),Fraction(0)) for b in range(N)]==p
s=[Fraction(0) for _ in range(N)]
for a in range(N):
    for b in range(N):
        s[a^b]+=pi[a][b]
H=[q for q in range(N) if parity(q&v)==0]
r=[Fraction(0) for _ in range(N)]
r[0]=Fraction(1,4)
for q in H:
    if q: r[q]=Fraction(1,4)
tv=sum((abs(s[q]-r[q]) for q in range(N)),Fraction(0))/2
assert tv==Fraction(1,8)
# Analytic lower bound already proves every coupling has TV >=1/8.
# This witness proves the lower bound is sharp.
out={
 "status":"PASS",
 "claim_scope":"analytic formulas checked n=3..12; exact sharp n=3 transport witness",
 "family":"f_u=1-2*1_{x=u}, u=0 and v=3 (Hamming weight 2)",
 "all_dimensional_formula":"TV(any positive parent coupling XOR, child spectrum) >= 2(N-4)/N^2 for N=2^n,n>=3",
 "n3_exact_min_tv":"1/8",
 "n3_parent_spectrum":["9/16"]+["1/16"]*7,
 "n3_child_support":[0,3,4,7],
 "n3_xor_law_of_optimal_witness":[str(x) for x in s],
 "n3_transport_matrix_units_1_over_16":M,
 "rows":rows,
 "full_FEI_status":"OPEN / NOT PROVED",
 "finite_checks_only":True
}
print(json.dumps(out,indent=2))
