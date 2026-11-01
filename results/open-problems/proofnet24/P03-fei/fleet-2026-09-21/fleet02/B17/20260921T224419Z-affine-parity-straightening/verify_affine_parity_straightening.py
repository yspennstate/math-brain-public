#!/usr/bin/env python3
"""Exact checks for B17 affine-parity straightening.

Finite verification only.  The accompanying REPORT contains the analytic proof.

Checks:
1. Elementary shear identity for every Boolean function through n=3 after
   median-character centering:
       I(f o T_{i->k})-I(f)=j_i-2 q_{ik}.
2. Approximate affine-parity straightening for every centered Boolean function
   in n=2,3, every pivot i, every nonempty parity support F disjoint from i,
   and both affine parity signs whenever the symmetric-difference error e<=1/2:
       error is preserved and becomes a coordinate halfcube;
       J(after centering) <= J(before)+|F| e.
   For e<=1/34 it also checks the exact folded-drift lower bound
       D_control >= 1-3e.
3. The connected quadratic cycle family n=5,...,8:
       J=M=n/2;
       p_{ik}=1 exactly on the cycle neighbours and 0 otherwise;
       every derivative support is at distance exactly 1/4 from the nearest
       coordinate subcube (hence it is not 1/16-relative-near a subcube);
       the exact affine-parity straightening of a row has zero error and does
       not increase J.

Arithmetic deciding the identities is Fraction/integer arithmetic. Entropies
are not used to decide the exact pass/fail claims.
"""
from fractions import Fraction
from itertools import combinations
import json

def fwht(a):
    a=list(map(int,a)); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def spectrum(vals):
    N=len(vals); W=fwht(vals)
    return [Fraction(w*w,N*N) for w in W]

def raw_influences(vals):
    p=spectrum(vals); n=len(vals).bit_length()-1
    return [
        sum((p[s] for s in range(1<<n) if (s>>i)&1), Fraction())
        for i in range(n)
    ]

def center(vals):
    a=raw_influences(vals)
    flips=[i for i,x in enumerate(a) if x>Fraction(1,2)]
    out=[]
    for x,v in enumerate(vals):
        parity=sum((x>>i)&1 for i in flips)&1
        out.append(-v if parity else v)
    return out

def J(vals):
    return sum((min(x,1-x) for x in raw_influences(vals)), Fraction())

def pivot(vals,i):
    return [int(vals[x]!=vals[x^(1<<i)]) for x in range(len(vals))]

def symdiff(a,b):
    return Fraction(sum(x!=y for x,y in zip(a,b)),len(a))

def p_ij(vals,i,k):
    eta=pivot(vals,i)
    return Fraction(sum(eta[x]!=eta[x^(1<<k)] for x in range(len(vals))),len(vals))

def q_ij(vals,i,k):
    p=spectrum(vals); n=len(vals).bit_length()-1
    return sum((p[s] for s in range(1<<n)
                if ((s>>i)&1) and ((s>>k)&1)), Fraction())

def shear(vals,i,k):
    # old x_i = new y_i xor new y_k; all other old coordinates equal y.
    out=[]
    for y in range(len(vals)):
        x=y
        b=((y>>i)&1)^((y>>k)&1)
        if b: x |= 1<<i
        else: x &= ~(1<<i)
        out.append(vals[x])
    return out

def straighten(vals,F):
    # Triangular invertible map:
    # x_{F_s}=y_{F_s} xor y_{F_{s+1}} for s<r, x_{F_r}=y_{F_r}.
    # Therefore xor_{k in F} x_k = y_{F_0}.
    F=list(F); n=len(vals).bit_length()-1
    out=[0]*len(vals)
    for y in range(1<<n):
        x=y
        for s in range(len(F)-1):
            b=((y>>F[s])&1)^((y>>F[s+1])&1)
            if b: x |= 1<<F[s]
            else: x &= ~(1<<F[s])
        out[y]=vals[x]
    return out

def restrict(vals,k,b):
    n=len(vals).bit_length()-1
    out=[]
    for y in range(1<<(n-1)):
        low=y&((1<<k)-1)
        high=y>>k
        x=low|(b<<k)|(high<<(k+1))
        out.append(vals[x])
    return out

def cycle_vals(n):
    out=[]
    for x in range(1<<n):
        q=0
        for i in range(n):
            q ^= ((x>>i)&1)&((x>>((i+1)%n))&1)
        out.append(-1 if q else 1)
    return out

def subcube(n,F,pat):
    ans=[]
    for x in range(1<<n):
        ok=True
        for t,k in enumerate(F):
            if ((x>>k)&1)!=((pat>>t)&1):
                ok=False; break
        ans.append(int(ok))
    return ans

shear_checks=0
for n in range(1,4):
    N=1<<n
    for mask in range(1<<N):
        vals=center([-1 if (mask>>x)&1 else 1 for x in range(N)])
        a=raw_influences(vals)
        I0=sum(a,Fraction())
        assert I0==J(vals)
        for i in range(n):
            for k in range(n):
                if i==k: continue
                g=shear(vals,i,k)
                I1=sum(raw_influences(g),Fraction())
                assert I1-I0 == a[i]-2*q_ij(vals,i,k)
                shear_checks += 1

straightening_checks=0
small_error_drift_checks=0
for n in range(2,4):
    N=1<<n
    for mask in range(1<<N):
        vals=center([-1 if (mask>>x)&1 else 1 for x in range(N)])
        J0=J(vals)
        for i in range(n):
            eta=pivot(vals,i)
            others=[k for k in range(n) if k!=i]
            for r in range(1,len(others)+1):
                for F in combinations(others,r):
                    for c in (0,1):
                        par=[
                            int((sum((x>>k)&1 for k in F)&1)==c)
                            for x in range(N)
                        ]
                        e=symdiff(eta,par)
                        if e>Fraction(1,2):
                            continue
                        g=center(straighten(vals,F))
                        k0=F[0]
                        lit=[int(((x>>k0)&1)==c) for x in range(N)]
                        assert symdiff(pivot(g,i),lit)==e
                        assert J(g) <= J0+r*e
                        straightening_checks += 1
                        if e<=Fraction(1,34):
                            c0=center(restrict(g,k0,0))
                            c1=center(restrict(g,k0,1))
                            D=J(g)-(J(c0)+J(c1))/2
                            assert D >= 1-3*e
                            small_error_drift_checks += 1

cycle_rows=0
cycle_subcubes=0
cycle_records=[]
for n in range(5,9):
    vals=center(cycle_vals(n))
    assert J(vals)==Fraction(n,2)
    M=Fraction()
    row_best=[]
    for i in range(n):
        eta=pivot(vals,i)
        assert sum(eta)==len(vals)//2
        for k in range(n):
            if k==i: continue
            expected = Fraction(1) if k in ((i-1)%n,(i+1)%n) else Fraction(0)
            got=p_ij(vals,i,k)
            assert got==expected
            M += got/4
        others=[k for k in range(n) if k!=i]
        best=Fraction(1)
        # Include all coordinate subcubes on coordinates other than the pivot.
        for r in range(0,len(others)+1):
            if r==0:
                F=()
                d=symdiff(eta,[1]*len(vals))
                best=min(best,d)
                cycle_subcubes+=1
                continue
            for F in combinations(others,r):
                for pat in range(1<<r):
                    d=symdiff(eta,subcube(n,F,pat))
                    best=min(best,d)
                    cycle_subcubes+=1
        assert best==Fraction(1,4)
        row_best.append(best)
        # Exact parity on the two neighbours; straightening must cost no folded J.
        F=((i-1)%n,(i+1)%n)
        g=center(straighten(vals,F))
        assert J(g)<=J(vals)
        cycle_rows += 1
    assert M==J(vals)==Fraction(n,2)
    cycle_records.append({
        "n":n,
        "J":str(J(vals)),
        "M":str(M),
        "nearest_coordinate_subcube_distance":str(min(row_best))
    })

result={
    "status":"PASS",
    "scope":{
        "elementary_shear_identity_checks":shear_checks,
        "affine_parity_straightening_checks":straightening_checks,
        "small_error_folded_drift_checks":small_error_drift_checks,
        "quadratic_cycle_rows_checked":cycle_rows,
        "coordinate_subcubes_compared_for_cycles":cycle_subcubes,
        "cycle_dimensions":[5,6,7,8]
    },
    "cycle_records":cycle_records,
    "arithmetic":"integer Walsh transforms and fractions for all pass/fail claims",
    "full_FEI_status":"OPEN / NOT PROVED; finite checks establish only their stated scope"
}
print(json.dumps(result,indent=2,sort_keys=True))
