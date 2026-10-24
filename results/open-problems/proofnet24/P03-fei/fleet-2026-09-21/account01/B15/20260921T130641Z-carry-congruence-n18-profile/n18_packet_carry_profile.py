#!/usr/bin/env python3
"""Exact n=18 FEI magnitude-packet profiler and carry-congruence checker.

Reconstructs Numaro's published balanced 18-variable seed from the ten factual
512-bit slices already recovered in the private FEI continuation.  The seed is
accepted only after matching the published truth-table SHA-256.  Integer Walsh
transforms are exact; logarithms are descriptive only.  No FEI proof is claimed.
"""
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import log2
import numpy as np

EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
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

def fwht(v):
    a=np.asarray(v,dtype=np.int64).copy()
    h=1
    while h<len(a):
        b=a.reshape(-1,2*h)
        x=b[:,:h].copy(); y=b[:,h:].copy()
        b[:,:h]=x+y; b[:,h:]=x-y
        h*=2
    return a

def v2(z):
    z=abs(int(z))
    if not z: raise ValueError("v2(0)")
    return (z & -z).bit_length()-1

def reconstruct():
    base=int("".join(SLICES[0]),16)
    masks=[int("".join(row),16)^base for row in SLICES[1:]]
    seen=base; hosts=[]
    for m in masks:
        assert not (seen&m) and m.bit_count()==2
        seen|=m
        hosts.append([x for x in range(512) if (m>>x)&1])
    core=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)
    tab=np.tile(core,(1<<len(hosts),1))
    for j,cells in enumerate(hosts):
        active=(np.arange(1<<len(hosts))&(1<<j))!=0
        tab[np.ix_(active,np.array(cells,dtype=int))]=-1
    tab=tab.ravel()
    got=sha256(",".join(map(str,tab)).encode()).hexdigest()
    assert got==EXPECTED_SHA
    return tab,hosts

def moment_depth(entries,n,limit=8):
    """Largest r<=limit certified by the exact signed upper-incidence congruences."""
    depth=0
    for r in range(1,limit+1):
        ok=True
        for t in range(r):
            mod=1<<(r-t)
            for T in combinations(range(n),t):
                mask=sum(1<<i for i in T)
                A=sum(c for s,c in entries if (s&mask)==mask)
                if A%mod:
                    ok=False; break
            if not ok: break
        if not ok: return depth
        depth=r
    return depth

def main():
    table,hosts=reconstruct()
    n=18; N=1<<n
    assert len(table)==N and int(table.sum())==0
    W=fwht(table)
    assert int(np.dot(W,W))==N*N
    I=sum(Fraction(int(w)*int(w),N*N)*s.bit_count() for s,w in enumerate(W))
    assert I==Fraction(261,128)

    groups=defaultdict(list)
    for s,w in enumerate(W):
        if w: groups[abs(int(w))].append((s,1 if w>0 else -1))

    rows=[]; R=Fraction(0); Nnorm=Fraction(0); D=0.0
    bands=defaultdict(lambda:[Fraction(0),Fraction(0),0,0,0.0])
    for mag,entries in sorted(groups.items()):
        spec=np.zeros(N,dtype=np.int64)
        for s,c in entries: spec[s]=c
        V=fwht(spec)
        nz=V[V!=0]
        r=min(v2(x) for x in nz)
        rc=moment_depth(entries,n,limit=r+1)
        assert rc==r
        m=len(entries)
        assert m >= (1<<r)
        p=Fraction(m*mag*mag,N*N)
        b=Fraction(mag*(1<<r),N)
        R += p*r
        Nnorm += p/(b*b)
        d=float(p)*log2(1/float(b))
        D += d
        band=bands[r]
        band[0]+=p; band[1]+=p/(b*b); band[2]+=m; band[3]+=1; band[4]+=d
        rows.append({
            "walsh_magnitude":mag, "multiplicity":m, "valuation":r,
            "mass":str(p), "mesh_b":str(b),
            "physical_support":int(np.count_nonzero(V)),
            "min_nonzero_abs_V":int(np.min(np.abs(nz))),
            "max_nonzero_abs_V":int(np.max(np.abs(nz))),
            "moment_congruence_depth":rc,
            "multiplicity_bound_2^r":1<<r,
        })
    assert sum(Fraction(r["multiplicity"]*r["walsh_magnitude"]**2,N*N) for r in rows)==1

    H=sum(float(Fraction(int(w)*int(w),N*N))*log2(1/float(Fraction(int(w)*int(w),N*N)))
          for w in W if w)
    assert abs(H-(2*float(R)+2*D))<1e-12
    out={
      "source_table_sha256":EXPECTED_SHA,
      "auxiliary_hosts":hosts,
      "I_exact":str(I),
      "nonzero_fourier_coefficients":int(np.count_nonzero(W)),
      "packet_count":len(groups),
      "R_exact":str(R),
      "R_float":float(R),
      "D_float_descriptive":D,
      "H_float_descriptive":H,
      "N_exact":str(Nnorm),
      "packet_KL_float_descriptive":log2(float(Nnorm))-2*D,
      "amplification_H_over_I_minus_1_float":H/(float(I)-1),
      "normalized_R":2*float(R)/(float(I)-1),
      "normalized_D":2*D/(float(I)-1),
      "valuation_bands": {
        str(r): {"mass":str(v[0]),"N":str(v[1]),"coefficient_count":v[2],
                 "packet_count":v[3],"D_float_descriptive":v[4]}
        for r,v in sorted(bands.items())
      },
      "packets":rows,
      "checks":[
        "published truth-table SHA-256 matched",
        "balance and Parseval matched",
        "I=261/128 exactly",
        "H=2R+2D to binary64 display precision",
        "carry moment-congruence depth equals direct pointwise valuation for every packet",
        "multiplicity m >= 2^r for every packet"
      ]
    }
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    import json
    main()
