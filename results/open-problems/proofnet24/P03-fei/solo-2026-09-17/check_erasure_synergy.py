#!/usr/bin/env python3
"""Exact self-checks for ERASURE_SYNERGY_AND_DUALITY_2026-09-18.md."""
from fractions import Fraction as F
from pathlib import Path
import json
import math

from certify_nand80 import wht


def bent(t, r):
    return 1-2*(sum(((t >> j) & 1)*((t >> (j+1)) & 1)
                    for j in range(0, r, 2)) % 2)


def entropy_power_law(p):
    out=F(0)
    for x in p:
        if not x: continue
        if x.numerator!=1 or x.denominator & (x.denominator-1):
            return None
        out += x*(x.denominator.bit_length()-1)
    return out


def metrics(values):
    N=len(values); n=N.bit_length()-1
    coeff=[F(x,N) for x in wht(values)]
    p=[x*x for x in coeff]
    H=entropy_power_law(p)
    influences=[]; erasures=[]
    for i in range(n):
        influences.append(sum((p[S] for S in range(N) if S & (1<<i)),F(0)))
        B=F(0); exact_uniform=True
        for S in range(N):
            if S & (1<<i): continue
            r,s=p[S],p[S|(1<<i)]
            # Every law used here is uniform on a linear subspace or on the
            # full cube, so conditional entropy is exactly 0 or pair mass.
            if r and s:
                if r==s: B += r+s
                else: exact_uniform=False
        if not exact_uniform: B=None
        erasures.append(B)
    aggregate=None if any(x is None for x in erasures) else sum(erasures,F(0))
    return coeff,p,H,sum(influences,F(0)),aggregate,influences,erasures


def synergy(m):
    assert m>=3 and m%2==1
    r=m-1; N=1<<m
    g0=[];g1=[]
    for y in range(N):
        ym=(y>>(m-1))&1
        t=sum(((((y>>j)&1)^ym)<<j) for j in range(r))
        v=bent(t,r)
        g0.append(v);g1.append(v*(1-2*ym))
    c0,p0,H0,I0,B0,_,_=metrics(g0)
    c1,p1,H1,I1,B1,_,_=metrics(g1)
    assert H0==H1==m-1 and I0==I1==F(m,2) and B0==B1==0
    even={S for S in range(N) if S.bit_count()%2==0}
    odd=set(range(N))-even
    assert {S for S,x in enumerate(c0) if x}==even
    assert {S for S,x in enumerate(c1) if x}==odd
    assert all(p0[S]==F(1,1<<(m-1)) for S in even)
    assert all(p1[S]==F(1,1<<(m-1)) for S in odd)
    selector_difference=F(sum(a!=b for a,b in zip(g0,g1)),N)
    assert selector_difference==F(1,2)
    full=g0+g1
    c,p,H,I,B,infs,ers=metrics(full)
    assert H==B==m+1 and I==F(m+1,2)
    assert all(x==F(1,1<<(m+1)) for x in p)
    assert infs[-1]==F(1,2) and ers[-1]==1
    return {'m':m,'selector_function_dimension':m+1,
            'restriction':{'H':str(H0),'B':str(B0),'I':str(I0),
                           'support_size':len(even)},
            'full':{'H':str(H),'B':str(B),'I':str(I)},
            'selector_influence':str(selector_difference),
            'mixture_erasure_gain':str(m),
            'all_signed_coefficients_checked':len(c)}


def pair_lift(values):
    n=(len(values)).bit_length()-1
    out=[]
    for x in range(1<<(2*n)):
        y=0
        for j in range(n):
            # Product of signs corresponds to XOR of {0,1} exponents.
            y |= ((((x>>(2*j))&1)^((x>>(2*j+1))&1))<<j)
        out.append(values[y])
    return out


def parity_lift(values):
    n=(len(values)).bit_length()-1
    out=[]
    for index in range(1<<(n+1)):
        x=index&((1<<n)-1); z=(index>>n)&1
        out.append(values[x ^ (((1<<n)-1) if z else 0)])
    return out


def exhaustive_lifts():
    records=[]
    for n in range(1,4):
        N=1<<n
        for label in range(1<<N):
            g=[1-2*((label>>x)&1) for x in range(N)]
            _,p,H,I,_,_,_=metrics(g)
            _,pl,Hl,Il,Bl,_,_=metrics(pair_lift(g))
            assert sorted(x for x in p if x)==sorted(x for x in pl if x)
            if H is not None: assert Hl==H
            assert Il==2*I
            assert all(not(pl[S] and pl[S^(1<<i)])
                       for S in range(len(pl)) for i in range(2*n))
            assert Bl==0
            lifted=pair_lift(g)
            recovered=[]
            # Set every even-numbered member in one-based notation, i.e. bit
            # 2j+1 in zero-based notation, to +1 (exponent zero).
            for odd_assignment in range(1<<n):
                x=sum(((odd_assignment>>j)&1)<<(2*j) for j in range(n))
                recovered.append(lifted[x])
            assert recovered==g
            records.append([n,label])
    return records


def exhaustive_parity_lifts():
    records=[]
    for n in range(1,5):
        N=1<<n
        for label in range(1<<N):
            g=[1-2*((label>>x)&1) for x in range(N)]
            _,p,H,I,_,_,_=metrics(g)
            lifted=parity_lift(g)
            _,pl,Hl,Il,Bl,_,_=metrics(lifted)
            assert sorted(x for x in p if x)==sorted(x for x in pl if x)
            if H is not None: assert Hl==H
            odd_mass=sum((p[S] for S in range(N) if S.bit_count()%2),F(0))
            assert Il==I+odd_mass and Il<=2*I and Bl==0
            assert all(not pl[S] for S in range(len(pl)) if S.bit_count()%2)
            assert lifted[:N]==g  # selector z=0, i.e. sign z=+1
            records.append([n,label])
    return records


def exploratory_d_over_i():
    # Complete enumeration, but logs are floating when probabilities are not
    # powers of two. This is explicitly not a proof of an optimum.
    out=[]
    for n in range(1,5):
        N=1<<n; best=(-1,None)
        for label in range(1<<N):
            f=[1-2*((label>>x)&1) for x in range(N)]
            w=wht(f); p=[(x/N)**2 for x in w]
            H=-sum(x*math.log2(x) for x in p if x)
            B=0.0; I=0.0
            for i in range(n):
                for S in range(N):
                    if S&(1<<i): I+=p[S]
                    else:
                        r,s=p[S],p[S|(1<<i)]; q=r+s
                        if r:B-=r*math.log2(r/q)
                        if s:B-=s*math.log2(s/q)
            ratio=(H-B)/I if I else 0.0
            if ratio>best[0]:best=(ratio,label)
        out.append({'n':n,'truth_tables':1<<N,'max_D_over_I_floating':best[0],
                    'witness_label':best[1]})
    return out


def main():
    synergies=[synergy(m) for m in [3,5,7]]
    lifts=exhaustive_lifts()
    parity_lifts=exhaustive_parity_lifts()
    result={'status':'PASS','arithmetic':'exact integer/rational except labeled exploratory block',
            'synergy_checks':synergies,
            'pair_lift_truth_tables_checked':len(lifts),
            'pair_lift_range':'every truth table in dimensions 1,2,3',
            'parity_lift_truth_tables_checked':len(parity_lifts),
            'parity_lift_range':'every truth table in dimensions 1,2,3,4',
            'exploratory_complete_enumeration':exploratory_d_over_i(),
            'scope':'The all-dimension theorems are proved in the note; these are self-checks, not independent audits.'}
    Path('erasure_synergy_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','synergy_dimensions':[x['m'] for x in synergies],
                      'pair_lift_truth_tables_checked':len(lifts),
                      'parity_lift_truth_tables_checked':len(parity_lifts),
                      'exploratory':result['exploratory_complete_enumeration']},indent=2))


if __name__=='__main__':main()
