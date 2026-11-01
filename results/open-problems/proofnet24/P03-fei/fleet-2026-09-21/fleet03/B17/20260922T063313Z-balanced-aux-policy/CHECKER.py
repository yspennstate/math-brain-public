#!/usr/bin/env python3
"""Exact certificate for the balanced auxiliary-restriction lattice of the 18-input FEI seed.

Integer Walsh arithmetic is exact in int64 at these dimensions.  Every logarithm
is enclosed by a Fraction atanh series with a positive remainder.
"""
from fractions import Fraction
from functools import lru_cache
from decimal import Decimal, getcontext
import hashlib, itertools, json
import numpy as np

CORE_HEX=(
"fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
"fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
)
HOSTS=[[78,79],[113,121],[228,484],[170,186],[149,151],
       [338,466],[284,316],[291,295],[393,457]]
EXPECTED_SHA="f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
C0=Fraction(64548,10000)
CDAG=Fraction(6521851214,10**9)
ADAG=Fraction(268204856,10**9)

base=int(CORE_HEX,16)
core=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)


def full_source_hash():
    vals=[]
    for y in range(512):
        row=core.copy()
        for j,cells in enumerate(HOSTS):
            if (y>>j)&1:
                row[cells]=-1
        vals.extend(map(int,row))
    return hashlib.sha256(",".join(map(str,vals)).encode()).hexdigest()


def edge_boundary(row):
    b=0
    for x in range(512):
        for i in range(9):
            y=x^(1<<i)
            if x<y and row[x]!=row[y]: b+=1
    return b


def check_host_geometry():
    assert int(core.sum())==18
    assert edge_boundary(core)==513
    cells=[(j,x) for j,hs in enumerate(HOSTS) for x in hs]
    adj=[]
    for u,(j,x) in enumerate(cells):
        for k,y in cells[u+1:]:
            if (x^y).bit_count()==1: adj.append((j,x,k,y))
    assert len(adj)==9 and all(j==k for j,x,k,y in adj)
    for j,(x,y) in enumerate(HOSTS):
        assert (x^y).bit_count()==1
        plus=minus=0
        for z in (x,y):
            for bit in range(9):
                w=z^(1<<bit)
                if w in (x,y): continue
                if core[w]==1: plus+=1
                else: minus+=1
        assert (plus,minus)==(8,8)
    # Every subset of complete host-pair flips preserves the core boundary.
    for mask in range(512):
        row=core.copy()
        for j,cellsj in enumerate(HOSTS):
            if (mask>>j)&1: row[cellsj]=-1
        assert edge_boundary(row)==513


def make_gate(free,ones):
    free=tuple(free); ones=set(ones)
    fixed=core.copy()
    for j in ones: fixed[HOSTS[j]]=-1
    rows=[]
    for y in range(1<<len(free)):
        row=fixed.copy()
        for k,j in enumerate(free):
            if (y>>k)&1: row[HOSTS[j]]=-1
        rows.append(row)
    return np.concatenate(rows)


def fwht(a):
    a=np.array(a,dtype=np.int64,copy=True)
    h=1
    while h<a.size:
        m=a.reshape(-1,2*h)
        x=m[:,:h].copy(); y=m[:,h:].copy()
        m[:,:h]=x+y; m[:,h:]=x-y
        a=m.reshape(-1); h*=2
    return a


def ln_interval(q,N=22):
    assert Fraction(1)<=q<=Fraction(2)
    z=(q-1)/(q+1)
    s=Fraction(0)
    for n in range(N): s += 2*z**(2*n+1)/(2*n+1)
    if not z: return s,s
    rem=2*z**(2*N+1)/((2*N+1)*(1-z*z))
    return s,s+rem

LN2_LO,LN2_HI=ln_interval(Fraction(2))

@lru_cache(None)
def log2_int_interval(x):
    if x==1: return Fraction(0),Fraction(0)
    k=x.bit_length()-1
    y=Fraction(x,1<<k)
    lo,hi=ln_interval(y)
    return Fraction(k)+lo/LN2_HI, Fraction(k)+hi/LN2_LO


def entropy_interval(W,n):
    sq=W*W
    vals,counts=np.unique(sq[sq>0],return_counts=True)
    lo=Fraction(0); hi=Fraction(0); den=1<<(2*n)
    for xx,cc in zip(vals,counts):
        x=int(xx); c=int(cc)
        llo,lhi=log2_int_interval(x)
        mass=Fraction(c*x,den)
        lo += mass*(2*n-lhi)
        hi += mass*(2*n-llo)
    return lo,hi


def dec(x,digits=50):
    getcontext().prec=digits
    return str(Decimal(x.numerator)/Decimal(x.denominator))


def main():
    assert full_source_hash()==EXPECTED_SHA
    check_host_geometry()

    R={}; counts={}; max_width=Fraction(0)
    allj=set(range(9))
    for r in (1,3,5,7,9):
        m=(9-r)//2; count=0
        for free in itertools.combinations(range(9),r):
            rest=sorted(allj-set(free))
            for ones in itertools.combinations(rest,m):
                g=make_gate(free,ones)
                n=9+r
                assert int(g.sum())==0
                W=fwht(g)
                assert int((W*W).sum())==(1<<n)**2
                hlo,hhi=entropy_interval(W,n)
                I=Fraction(513+r,256)
                rlo=hlo/(I-1); rhi=hhi/(I-1)
                key=(frozenset(free),frozenset(ones))
                R[key]=(rlo,rhi)
                max_width=max(max_width,rhi-rlo)
                count+=1
        counts[r]=count
    assert counts=={1:630,3:1680,5:756,7:72,9:1}
    assert len(R)==3139

    transition_count=0; min_gain=None; min_edge=None
    for (free,ones),(rlo,rhi) in R.items():
        zeros=allj-set(free)-set(ones)
        for j in ones:
            for k in zeros:
                key2=(frozenset(set(free)|{j,k}),frozenset(set(ones)-{j}))
                lo2,hi2=R[key2]
                gain=lo2-rhi
                assert gain>0
                transition_count+=1
                if min_gain is None or gain<min_gain:
                    min_gain=gain; min_edge=(sorted(free),sorted(ones),j,k)
    assert transition_count==28296

    source_key=(frozenset(range(9)),frozenset())
    source_lo,source_hi=R[source_key]
    for key,(lo,hi) in R.items():
        if key!=source_key: assert hi<source_lo
    assert source_hi<CDAG

    c_hi=4*(source_hi-C0)
    assert c_hi<ADAG

    by_r={}
    for r in (1,3,5,7,9):
        vals=[v for k,v in R.items() if len(k[0])==r]
        by_r[str(r)]={
            "count":counts[r],
            "min_lower":dec(min(v[0] for v in vals),35),
            "max_upper":dec(max(v[1] for v in vals),35),
        }

    out={
      "status":"PASS",
      "source_sha256":EXPECTED_SHA,
      "balanced_restrictions":len(R),
      "balance_preserving_transitions":transition_count,
      "minimum_transition_gain_lower":dec(min_gain,45),
      "minimum_transition_edge":{"free":min_edge[0],"ones":min_edge[1],"released_one":min_edge[2],"released_zero":min_edge[3]},
      "widest_R_interval":dec(max_width,25),
      "by_free_auxiliary_count":by_r,
      "source_R_lower":dec(source_lo,55),
      "source_R_upper":dec(source_hi,55),
      "C_dagger":dec(CDAG,20),
      "C_dagger_minus_source_R_lower_bound":dec(CDAG-source_hi,40),
      "source_cG_at_C0_upper":dec(c_hi,40),
      "a_dagger":dec(ADAG,20),
      "a_dagger_minus_source_cG_lower_bound":dec(ADAG-c_hi,40),
      "unique_maximum_is_unrestricted_source":True,
      "full_FEI_proved":False
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__": main()
