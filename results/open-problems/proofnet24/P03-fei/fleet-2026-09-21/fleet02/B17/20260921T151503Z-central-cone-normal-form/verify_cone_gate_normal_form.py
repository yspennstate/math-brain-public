#!/usr/bin/env python3
"""
Exact self-check for B17 cone-phase / gate-leaf normal form.

Scope:
  * exhaustive balanced Boolean gates f on n<=3:
      G_f(x,y)=(-1)^{y(1-f(x))/2}
    has the exact predicted squared-Walsh multiset and exact influence identity;
  * exact rational influence recurrences and rigorous Decimal endpoint propagation
    for the committed 162-bit shared-graft seed at composition depths 2,7,20.

This verifies finite algebra/endpoint arithmetic only.  It does not prove full FEI.
"""
from fractions import Fraction
from decimal import Decimal, getcontext
from collections import Counter
import json, hashlib

def fwht(a):
    a=list(map(int,a)); h=1; N=len(a)
    while h<N:
        for i in range(0,N,2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]
                a[j],a[j+h]=u+v,u-v
        h*=2
    return a

def squared_walsh(vals):
    N=len(vals); W=fwht(vals)
    return [Fraction(w*w,N*N) for w in W]

def phys_influences(vals):
    N=len(vals); n=N.bit_length()-1
    return [Fraction(sum(vals[x]!=vals[x^(1<<i)] for x in range(N)),N)
            for i in range(n)]

def cone_lift(f):
    # Core bits occupy low positions; y is the new high bit.
    N=len(f)
    A=[0 if v==1 else 1 for v in f]
    return [f"bad"] if False else [
        (1 if (yb*A[x])%2==0 else -1)
        for yb in (0,1) for x in range(N)
    ]

balanced_checked=0
for n in range(1,4):
    N=1<<n
    for mask in range(1<<N):
        f=[-1 if (mask>>x)&1 else 1 for x in range(N)]
        if sum(f)!=0:
            continue
        p=squared_walsh(f)
        assert p[0]==0
        G=cone_lift(f)
        pg=squared_walsh(G)
        # Exact predicted law: two 1/4 atoms (empty core with/without y),
        # and two copies of every f spectral atom scaled by 1/4.
        pred=[Fraction(0)]*(2*N)
        pred[0]=Fraction(1,4)
        pred[N]=Fraction(1,4)
        for s in range(1,N):
            pred[s]=p[s]/4
            pred[N+s]=p[s]/4
        assert pg==pred
        inf_f=phys_influences(f)
        inf_g=phys_influences(G)
        assert inf_g[:-1] == [q/2 for q in inf_f]
        assert inf_g[-1] == Fraction(1,2)
        balanced_checked += 1


# Exact enumeration of all balanced quadratic ANF phases through n=5.
# A quadratic phase is represented by
#   P(x)=c + sum_i l_i x_i + sum_{i<j} q_ij x_i x_j  (mod 2).
# Standard quadratic-Walsh theory says a balanced quadratic phase has a flat
# nonzero squared spectrum.  Here we verify that finite claim directly and
# the analytic corollary H(cone)/I(cone) <= 12/5 exactly.
quadratic_checked=0
quadratic_by_n={}
quadratic_max_ratio=Fraction(0)
quadratic_max_witness=None
for n in range(1,6):
    N=1<<n
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    coeff_count=1+n+len(pairs)
    count_n=0
    max_n=Fraction(0)
    for coeff_mask in range(1<<coeff_count):
        c=coeff_mask&1
        lin=[(coeff_mask>>(1+i))&1 for i in range(n)]
        off=1+n
        quad=[(coeff_mask>>(off+k))&1 for k in range(len(pairs))]
        vals=[]
        for x in range(N):
            bit=c
            for i in range(n):
                bit ^= lin[i] & ((x>>i)&1)
            for k,(i,j) in enumerate(pairs):
                bit ^= quad[k] & ((x>>i)&1) & ((x>>j)&1)
            vals.append(-1 if bit else 1)
        if sum(vals)!=0:
            continue
        probs=squared_walsh(vals)
        nz=[q for q in probs if q]
        # Flat nonzero spectrum, with power-of-two support.
        assert len(set(nz))==1
        support=len(nz)
        assert support & (support-1) == 0
        Hf=support.bit_length()-1
        inf=sum(phys_influences(vals), Fraction(0))
        cone_ratio=Fraction(4+Hf,1) / (1+inf)
        assert cone_ratio <= Fraction(12,5)
        count_n += 1
        quadratic_checked += 1
        if cone_ratio>max_n:
            max_n=cone_ratio
        if cone_ratio>quadratic_max_ratio:
            quadratic_max_ratio=cone_ratio
            quadratic_max_witness={
                "n":n,
                "coeff_mask":coeff_mask,
                "H_f":Hf,
                "I_f":f"{inf.numerator}/{inf.denominator}",
                "cone_ratio":f"{cone_ratio.numerator}/{cone_ratio.denominator}",
            }
    quadratic_by_n[str(n)]={"balanced_quadratic_phases":count_n,
                            "max_cone_ratio":f"{max_n.numerator}/{max_n.denominator}"}

getcontext().prec=100
a=Fraction(68013,32768)
blo=Decimal("7.014850042680291613033104756310658624299893163")
bhi=Decimal("7.014850042680291613033104756310658624299893164")
old_hi=Decimal("6.521845710923046575658143972948578468366662293")

def D(fr):
    return Decimal(fr.numerator)/Decimal(fr.denominator)

levels=[]
for m in (2,7,20):
    am=a**m
    geom=(am-1)/(a-1)
    # Cone H = 2 + b*geom/2; cone I=(1+a^m)/2.
    Ilo=Fraction(1,2)*(1+am)
    Hlo=Decimal(2)+blo*D(geom)/Decimal(2)
    Hhi=Decimal(2)+bhi*D(geom)/Decimal(2)
    rlo=Hlo/D(Ilo); rhi=Hhi/D(Ilo)
    levels.append({
        "m":m,
        "core_dimension":162**m,
        "cone_dimension":162**m+1,
        "influence_exact":f"{Ilo.numerator}/{Ilo.denominator}",
        "entropy_lower":str(Hlo),
        "entropy_upper":str(Hhi),
        "ratio_lower":str(rlo),
        "ratio_upper":str(rhi),
        "exceeds_4":bool(rlo>Decimal(4)),
        "exceeds_readonce_6_4573":bool(rlo>Decimal("6.4573")),
        "exceeds_external_old_upper":bool(rlo>old_hi),
        "margin_over_external_old_upper":str(rlo-old_hi),
    })

out={
    "status":"PASS",
    "balanced_cone_lifts_exhaustively_checked":balanced_checked,
    "balanced_quadratic_gates_checked":quadratic_checked,
    "balanced_quadratic_by_n":quadratic_by_n,
    "balanced_quadratic_max_cone_ratio":f"{quadratic_max_ratio.numerator}/{quadratic_max_ratio.denominator}",
    "balanced_quadratic_max_witness":quadratic_max_witness,
    "finite_scope":"all balanced Boolean f for n<=3; all balanced quadratic ANF phases n<=5; shared-graft endpoint propagation at m=2,7,20",
    "exact_identities_checked":[
        "cone squared-Walsh law",
        "Inf_core(G)=Inf_core(f)/2",
        "Inf_y(G)=1/2",
        "balanced quadratic cone ratio <= 12/5 through n<=5",
    ],
    "shared_graft_source":{
        "I":"68013/32768",
        "H_lower":str(blo),
        "H_upper":str(bhi),
        "provenance":"committed SHARED_GRAFT_REPORT.md; this checker only propagates its certified endpoints"
    },
    "levels":levels,
    "full_FEI_status":"OPEN / NOT PROVED; finite checks only"
}
print(json.dumps(out,indent=2))
