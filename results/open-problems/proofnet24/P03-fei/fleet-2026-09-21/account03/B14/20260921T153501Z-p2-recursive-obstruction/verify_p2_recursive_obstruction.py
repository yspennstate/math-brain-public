#!/usr/bin/env python3
from __future__ import annotations
from collections import Counter
from fractions import Fraction
import hashlib, itertools, json
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
# Certified in the account02/B14 recursive-selector predecessor; this script does not re-audit it.
RHO5_LOWER = Fraction(7096060618744925556394954995917, 10**30)

def fwht(a):
    out=np.array(a,dtype=np.int64,copy=True); h=1
    while h<len(out):
        v=out.reshape(-1,2*h); L=v[:,:h].copy(); R=v[:,h:].copy()
        v[:,:h]=L+R; v[:,h:]=L-R; h*=2
    return out

def reconstruct():
    base=int("".join(SLICES[0]),16)
    masks=[int("".join(row),16)^base for row in SLICES[1:]]
    if any(m & base for m in masks) or any(m.bit_count()!=2 for m in masks): raise AssertionError("bad source slices")
    seen=base; hosts=[]
    for m in masks:
        if seen&m: raise AssertionError("host overlap")
        seen |= m; hosts.append([x for x in range(512) if (m>>x)&1])
    core=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int8)
    tab=np.tile(core,(1<<len(hosts),1))
    for j,cells in enumerate(hosts):
        active=(np.arange(1<<len(hosts))&(1<<j))!=0
        tab[np.ix_(active,np.array(cells,dtype=int))]=-1
    tab=tab.ravel()
    dig=hashlib.sha256(",".join(map(str,tab)).encode()).hexdigest()
    if dig != EXPECTED_SHA: raise AssertionError((dig,EXPECTED_SHA))
    return tab

def influence(W,n,i):
    N=1<<n; bit=1<<i
    return Fraction(sum(int(W[s])**2 for s in range(N) if s&bit),N*N)

def child_modulation(W,n,i,j):
    """d_ij = Inf_j(G_i^+) - Inf_j(G_i^-), exact."""
    N=1<<n; bi=1<<i; bj=1<<j
    z=sum(int(W[T])*int(W[T|bi]) for T in range(N) if not (T&bi) and (T&bj))
    return Fraction(4*z,N*N)

def ln2_interval(terms=80):
    # ln 2 = 2 atanh(1/3); positive-series lower plus geometric tail upper.
    z=Fraction(1,3); z2=z*z; zp=z; s=Fraction(0)
    for k in range(terms):
        s += zp/Fraction(2*k+1); zp *= z2
    lo=2*s; hi=lo + 2*zp/(Fraction(2*terms+1)*(1-z2))
    return lo,hi

def dec_floor(x,d=18):
    sc=10**d; y=x*sc; q=y.numerator//y.denominator
    s=str(abs(q)).rjust(d+1,"0"); return ("-" if q<0 else "")+s[:-d]+"."+s[-d:]

def dec_ceil(x,d=18):
    sc=10**d; y=x*sc; q=-((-y.numerator)//y.denominator)
    s=str(abs(q)).rjust(d+1,"0"); return ("-" if q<0 else "")+s[:-d]+"."+s[-d:]

def main():
    tab=reconstruct(); n=18; W=fwht(tab)
    inf=[influence(W,n,i) for i in range(n)]
    drows=[]; D=[]
    for i in range(n):
        row=[child_modulation(W,n,i,j) for j in range(n) if j!=i]
        drows.append(row); D.append(sum(x*x for x in row))
    core=Fraction(57,256); aux=Fraction(1,256)
    assert inf[:9]==[core]*9 and inf[9:]==[aux]*9
    assert D[:9]==[Fraction(485,2048)]*9
    assert D[9:]==[Fraction(1,2048)]*9
    A2=sum(x*x for x in inf); assert A2==Fraction(14625,32768)
    type_data={"C":(core,core,Fraction(485,2048)), "A":(aux,aux,Fraction(1,2048))}
    def state(path):
        a,s,d=type_data[path[-1]]; p=a; q=s; DD=d; A2r=A2
        for lab in reversed(path[:-1]):
            a,s,d=type_data[lab]
            # Exact theorem proved in the accompanying report.
            DD=a*a*DD + q*q*A2r*d
            p=a*p; q=s*q; A2r=A2*A2r
        factor=Fraction(1)-p/Fraction(3)+DD/(12*p)
        return p,q,DD,factor
    levels=[]
    for r in range(1,9):
        rows=[]
        for tup in itertools.product("CA",repeat=r):
            path="".join(tup); p,q,DD,f=state(path); rows.append((f,path,p,DD))
        fmax,pmax,_,_=max(rows,key=lambda x:x[0]); fmin,pmin,_,_=min(rows,key=lambda x:x[0])
        levels.append({"depth":r,"max_factor_path":pmax,"max_factor_exact":str(fmax),"min_factor_path":pmin,"min_factor_exact":str(fmin)})
    lnlo,lnhi=ln2_interval(); c_lo=Fraction(2,1)/lnhi; c_hi=Fraction(2,1)/lnlo
    f5=Fraction(levels[4]["max_factor_exact"]); p2_upper=c_hi*f5
    residual_lower=RHO5_LOWER-p2_upper
    return {
      "status":"PASS",
      "scope":"exact child-modulation recursion for P2 on recovered Numaro fixed-seed composition; peer-certified rho0(F5) lower bound is an explicit dependency; not full FEI",
      "seed_sha256":EXPECTED_SHA,
      "seed_A2_exact":str(A2),
      "seed_D_class_exact":{"C":str(D[0]),"A":str(D[9])},
      "seed_D_C_pattern":{str(k):v for k,v in Counter(drows[0]).items()},
      "seed_D_A_pattern":{str(k):v for k,v in Counter(drows[9]).items()},
      "identity":"D_{outer i}(G o H)=a_i^2 D(H)+q(H)^2 A2(H) D_i(G)",
      "levels":levels,
      "cstar_lower":dec_floor(c_lo,24),
      "cstar_upper":dec_ceil(c_hi,24),
      "F5_peer_rho0_lower":dec_floor(RHO5_LOWER,30),
      "F5_max_P2_drop_ratio_path":levels[4]["max_factor_path"],
      "F5_max_P2_drop_ratio_upper":dec_ceil(p2_upper,24),
      "F5_every_coordinate_residual_ratio_lower":dec_floor(residual_lower,24),
    }

if __name__=="__main__": print(json.dumps(main(),indent=2,sort_keys=True))
