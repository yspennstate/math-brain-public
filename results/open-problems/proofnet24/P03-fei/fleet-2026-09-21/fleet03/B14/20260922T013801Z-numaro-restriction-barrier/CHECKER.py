#!/usr/bin/env python3
from fractions import Fraction
from collections import Counter
from functools import lru_cache
from itertools import combinations
import hashlib, json
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
CAP = Fraction(64559,10000)
R6_TARGET_HIST = Counter({16:32,64:4,256:4,576:4})
R6_TARGET_I = Fraction(13,8)

def reconstruct():
    base = int("".join(SLICES[0]),16)
    masks = [int("".join(row),16)^base for row in SLICES[1:]]
    assert all((m & base)==0 and m.bit_count()==2 for m in masks)
    core=[-1 if (base>>x)&1 else 1 for x in range(512)]
    hosts=[[x for x in range(512) if (m>>x)&1] for m in masks]
    table=[]
    for y in range(512):
        row=core.copy()
        for j,cells in enumerate(hosts):
            if (y>>j)&1:
                for x in cells: row[x]=-1
        table.extend(row)
    digest=hashlib.sha256(",".join(map(str,table)).encode()).hexdigest()
    assert digest==EXPECTED_SHA and sum(table)==0
    return np.asarray(table,dtype=np.int8)

def g10_for_yfix(table,yfix):
    out=np.empty(1024,dtype=np.int8)
    base_y=sum(((yfix>>j)&1)<<(9+j) for j in range(8))
    for z in range(1024):
        idx=(z & 511) | base_y | (((z>>9)&1)<<17)
        out[z]=table[idx]
    return out

def restriction_map(free):
    k=len(free)
    comp=[i for i in range(10) if i not in free]
    z=np.arange(1<<k,dtype=np.int64)
    fv=np.zeros(1<<k,dtype=np.int64)
    for t,i in enumerate(free): fv |= ((z>>t)&1)<<i
    b=np.arange(1<<len(comp),dtype=np.int64)
    bv=np.zeros(1<<len(comp),dtype=np.int64)
    for t,i in enumerate(comp): bv |= ((b>>t)&1)<<i
    return bv[:,None]+fv[None,:]

def fwht_batch(A):
    A=A.astype(np.int64,copy=True); n=A.shape[1]; h=1
    while h<n:
        B=A.reshape(A.shape[0],-1,2*h)
        x=B[:,:,:h].copy(); y=B[:,:,h:].copy()
        B[:,:,:h]=x+y; B[:,:,h:]=x-y
        A=B.reshape(A.shape[0],n); h*=2
    return A

def essential_mask(R,k):
    ans=np.ones(R.shape[0],dtype=bool)
    for j in range(k):
        z0=np.asarray([z for z in range(1<<k) if ((z>>j)&1)==0],dtype=np.int64)
        ans &= np.any(R[:,z0] != R[:,z0+(1<<j)],axis=1)
    return ans

def ln_interval(q,N=24):
    q=Fraction(q); z=(q-1)/(q+1); s=Fraction()
    for n in range(N): s += 2*z**(2*n+1)/(2*n+1)
    if not z: return s,s
    rem=2*z**(2*N+1)/((2*N+1)*(1-z*z))
    return s,s+rem

LN2_LO,LN2_HI=ln_interval(Fraction(2),24)

@lru_cache(None)
def log2_int_interval(x):
    k=x.bit_length()-1; y=Fraction(x,1<<k); lo,hi=ln_interval(y,24)
    return Fraction(k)+lo/LN2_HI, Fraction(k)+hi/LN2_LO

def entropy_interval(rowW):
    N=len(rowW); k=N.bit_length()-1
    hist=Counter(int(w*w) for w in rowW if w)
    hlo=Fraction(); hhi=Fraction()
    for x,c in hist.items():
        llo,lhi=log2_int_interval(x); mass=Fraction(c*x,N*N)
        hlo += mass*(2*k-lhi); hhi += mass*(2*k-llo)
    return hlo,hhi,hist

def main():
    table=reconstruct()
    maps={k:[(free,restriction_map(free)) for free in combinations(range(10),k)] for k in range(6,11)}
    counts={k:{"restrictions":0,"balanced":0,"essential_balanced":0} for k in range(6,11)}
    ten_above=ten_below=0; six_equal=six_strict=six_inconclusive=0
    best10=None; best6=None
    l3lo,l3hi=log2_int_interval(3)
    r6lo=Fraction(46,5)-Fraction(9,5)*l3hi
    r6hi=Fraction(46,5)-Fraction(9,5)*l3lo

    for yfix in range(256):
        g10=g10_for_yfix(table,yfix)
        for k in range(6,11):
            for free,idx in maps[k]:
                R=g10[idx]; counts[k]["restrictions"] += R.shape[0]
                bal=(R.sum(axis=1)==0); counts[k]["balanced"] += int(bal.sum())
                if not bal.any(): continue
                RB=R[bal]; em=essential_mask(RB,k)
                counts[k]["essential_balanced"] += int(em.sum())
                if not em.any(): continue
                W=fwht_batch(RB[em])
                weights=np.asarray([s.bit_count() for s in range(1<<k)],dtype=np.int64)
                for rowW in W:
                    infl_num=sum(int(weights[s])*int(w)*int(w) for s,w in enumerate(rowW))
                    I=Fraction(infl_num,(1<<k)**2); assert I>1
                    hlo,hhi,hist=entropy_interval(rowW.tolist())
                    rlo=hlo/(I-1); rhi=hhi/(I-1)
                    if k==10:
                        if rlo>CAP: ten_above += 1
                        elif rhi<CAP: ten_below += 1
                        else: raise AssertionError("cap comparison inconclusive")
                        if best10 is None or rlo>best10[0]: best10=(rlo,rhi,yfix,I,hist)
                    if k==6:
                        assert rhi<CAP
                        if I==R6_TARGET_I and hist==R6_TARGET_HIST:
                            assert rlo<=r6hi and rhi>=r6lo; six_equal += 1
                        elif rhi<r6lo: six_strict += 1
                        else: six_inconclusive += 1
                        if best6 is None or rhi>best6[1]: best6=(rlo,rhi,yfix,I,hist)

    assert counts[10]=={"restrictions":256,"balanced":70,"essential_balanced":70}
    assert counts[9]=={"restrictions":5120,"balanced":0,"essential_balanced":0}
    assert counts[8]=={"restrictions":46080,"balanced":0,"essential_balanced":0}
    assert counts[7]=={"restrictions":245760,"balanced":8960,"essential_balanced":0}
    assert counts[6]=={"restrictions":860160,"balanced":37888,"essential_balanced":25088}
    assert ten_above==69 and ten_below==1
    assert six_equal==6656 and six_strict==18432 and six_inconclusive==0
    assert best10[2]==216 and best10[3]==Fraction(257,128)
    assert best6[3]==Fraction(13,8)

    out={
      "source_sha256":EXPECTED_SHA,
      "slice_definition":"fix y0..y7 arbitrarily; keep x0..x8,y8, then take ordinary coordinate restrictions",
      "counts":counts,
      "arity10_cap_6_4559":{"above":ten_above,"below":ten_below,
        "best_yfix":best10[2],"best_ratio_lower":format(float(best10[0]),".15f"),
        "best_ratio_upper":format(float(best10[1]),".15f")},
      "arity6":{"max_ratio_formula":"46/5-(9/5)log2(3)",
        "max_ratio_lower":format(float(r6lo),".15f"),
        "max_ratio_upper":format(float(r6hi),".15f"),
        "max_ties":six_equal,"strictly_below":six_strict,"inconclusive":six_inconclusive},
      "conclusion":"within this complete Numaro auxiliary-fixing slice, the read-once-cap obstruction occurs at arity 10 but no balanced essential ordinary-coordinate restriction of arity 6..9 exceeds 6.4559"
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__": main()
