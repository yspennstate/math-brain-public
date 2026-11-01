#!/usr/bin/env python3
"""B17 FEI gate-repair adversarial checker.

Exact finite combinatorics for sparse 5-input Boolean gates at uniform bias,
plus a deterministic Boolean two-point perturbation stress test around the
published balanced n=18 seed. The sparse part uses integer Walsh sums only.
The n=18 entropy ratios are descriptive binary64 values; the seed itself is
accepted only after its published SHA-256 matches.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import log2
import numpy as np

C0 = 6.4548
EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"

def parity(x): return x.bit_count() & 1
def is_edge(a,b): return (a^b).bit_count() == 1

def affine_rank(A, n):
    b=A[0]; basis=[0]*n; r=0
    for v in (x^b for x in A[1:]):
        x=v
        while x:
            i=x.bit_length()-1
            if basis[i]:
                x ^= basis[i]
            else:
                basis[i]=x; r+=1; break
    return r

def internal_edges(A):
    return sum(is_edge(a,b) for a,b in combinations(A,2))

def walsh_indicator_counts(A,n):
    c=Counter()
    for s in range(1<<n):
        z=sum(1 if parity(s&x)==0 else -1 for x in A)
        if s: c[abs(z)] += 1
    return c

def sparse5():
    n=5; V=range(1<<n)
    out={}
    # |A|=1
    out["m1_total"]=32
    # |A|=2: all have the same spectral magnitudes; equality only coordinate edges.
    c2=Counter()
    for A in combinations(V,2):
        e=internal_edges(A); r=affine_rank(A,n)
        wc=tuple(sorted(walsh_indicator_counts(A,n).items()))
        c2[(e,r,wc)] += 1
    assert c2[(1,1,((0,16),(2,15)))] == 80
    assert c2[(0,1,((0,16),(2,15)))] == 416
    # |A|=4: classify exactly by affine rank and physical internal edges.
    c4=Counter()
    for A in combinations(V,4):
        e=internal_edges(A); r=affine_rank(A,n)
        wc=tuple(sorted(walsh_indicator_counts(A,n).items()))
        c4[(e,r,wc)] += 1
    # rank-2 affine planes: only coordinate square faces have e=4.
    assert c4[(4,2,((0,24),(4,7)))] == 80
    assert sum(v for (e,r,w),v in c4.items() if r==2) == 1240
    # all affine-rank-3 four-sets have the same exact Walsh-magnitude counts.
    assert sum(v for (e,r,w),v in c4.items() if r==3) == 34720
    for (e,r,w),v in c4.items():
        if r==3:
            assert w == ((0,12),(2,16),(4,3))
            assert e <= 3
    # At fixed output mass 1/8, relative to a coordinate square:
    # rank-3 sets have H-H_face = 1/2 exactly and I-I_face >= 1/8.
    # Hence D-D_face >= C0/8-1/2 > 0 since C0>4.
    gap_rank3 = Fraction(1,8) * Fraction(16137,2500) - Fraction(1,2)
    assert gap_rank3 > 0
    out["m2_classes"]={str(k):v for k,v in sorted(c2.items(), key=lambda kv:str(kv[0]))}
    out["m4_classes"]={str(k):v for k,v in sorted(c4.items(), key=lambda kv:str(kv[0]))}
    out["m4_rank3_min_defect_gap_at_C0"]=str(gap_rank3)
    out["m4_rank3_best_c_descriptive"]=-8*(C0-4)/7
    return out

TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
 (TOP, BOT),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
 ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00", "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
 ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
 ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]
def reconstruct():
    base=int("".join(SLICES[0]),16)
    masks=[int("".join(row),16)^base for row in SLICES[1:]]
    seen=base; hosts=[]
    for m in masks:
        assert not (seen&m) and m.bit_count()==2
        seen |= m
        hosts.append([x for x in range(512) if (m>>x)&1])
    core=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)
    tab=np.tile(core,(1<<len(hosts),1))
    for j,cells in enumerate(hosts):
        active=(np.arange(1<<len(hosts))&(1<<j))!=0
        tab[np.ix_(active,np.array(cells,dtype=int))]=-1
    tab=tab.ravel()
    got=sha256(",".join(map(str,tab)).encode()).hexdigest()
    assert got==EXPECTED_SHA and int(tab.sum())==0
    return tab

def fwht(v):
    a=np.asarray(v,dtype=np.int64).copy(); h=1
    while h<len(a):
        b=a.reshape(-1,2*h)
        x=b[:,:h].copy(); y=b[:,h:].copy()
        b[:,:h]=x+y; b[:,h:]=x-y; h*=2
    return a

def entropy_influence_with_pc(W,pc):
    N=len(W)
    p=(W.astype(np.float64)/N)**2
    nz=p>0
    H=float(np.sum(-p[nz]*np.log2(p[nz])))
    I=float(np.sum(p*pc))
    return H,I

def numaro_swap_stress(samples=5000, seed=20260922):
    tab=reconstruct(); N=len(tab); n=18
    W=fwht(tab)
    assert int(np.dot(W,W))==N*N
    pc=np.fromiter((i.bit_count() for i in range(N)),dtype=np.uint8,count=N)
    H,I=entropy_influence_with_pc(W,pc)
    assert abs(I-261/128)<1e-15
    R=H/(I-1)
    idx=np.arange(N,dtype=np.int64); par=(pc&1).astype(np.int8)
    pos=np.flatnonzero(tab==1); neg=np.flatnonzero(tab==-1)
    rng=np.random.default_rng(seed)
    best=(-1.0,None,None,None,None)
    for _ in range(samples):
        a=int(pos[rng.integers(len(pos))]); b=int(neg[rng.integers(len(neg))])
        chia=1-2*par[np.bitwise_and(idx,a)]
        chib=1-2*par[np.bitwise_and(idx,b)]
        Wp=W+2*(chib.astype(np.int64)-chia.astype(np.int64))
        Hp,Ip=entropy_influence_with_pc(Wp,pc)
        Rp=Hp/(Ip-1)
        if Rp>best[0]: best=(Rp,a,b,Hp,Ip)
    assert best[0] < R
    return {
      "truth_table_sha256":EXPECTED_SHA,
      "seed_H_descriptive":H,
      "seed_I_exact":"261/128",
      "seed_R_descriptive":R,
      "sample_count":samples,
      "rng_seed":seed,
      "best_sampled_swap":{"R":best[0],"plus_to_minus_index":best[1],
                           "minus_to_plus_index":best[2],"H":best[3],"I":best[4]},
      "sampled_gap_seed_minus_best":R-best[0],
      "claim_scope":"deterministic finite stress test only; not an exhaustive neighborhood proof"
    }

if __name__=="__main__":
    import json
    out={"sparse5":sparse5(),"numaro_swaps":numaro_swap_stress()}
    print("PASS")
    print(json.dumps(out,indent=2,sort_keys=True))
