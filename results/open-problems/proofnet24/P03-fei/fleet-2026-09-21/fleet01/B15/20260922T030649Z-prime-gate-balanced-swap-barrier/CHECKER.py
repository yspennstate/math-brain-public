"""B15 exact-source certificate: the explicit composition-prime 10-input FEI
gate is a strict local maximizer of balanced excess ratio R=H/(I-1) under
every balance-preserving two-point truth-table swap.

This is a finite local statement only; it does not prove FEI.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import hashlib, math
import numpy as np

EXPECTED_PARENT_SHA="f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
EXPECTED_WITNESS_SHA="3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4"
TOP="fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT="fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES=[
(TOP,BOT),
(TOP,"fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
(TOP,"fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00","fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
(TOP,"fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
(TOP,"fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00",BOT),
("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00",BOT),
("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00",BOT),
("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00",BOT)]
FIXED={9:0,10:0,11:0,12:1,13:1,14:0,15:1,16:1}
FREE=[0,1,2,3,4,5,6,7,8,17]
TERMS=40
PAD=1e-9

def parent():
    base=int("".join(SLICES[0]),16)
    masks=[int("".join(row),16)^base for row in SLICES[1:]]
    seen=base; hosts=[]
    for mask in masks:
        assert mask.bit_count()==2 and not(seen&mask)
        seen|=mask
        hosts.append([x for x in range(512) if (mask>>x)&1])
    core=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int8)
    T=np.tile(core,(512,1))
    for j,cells in enumerate(hosts):
        ys=np.where((np.arange(512)&(1<<j))!=0)[0]
        T[np.ix_(ys,np.array(cells,dtype=int))]=-1
    a=T.ravel()
    sha=hashlib.sha256(",".join(map(str,a.tolist())).encode()).hexdigest()
    assert sha==EXPECTED_PARENT_SHA and int(a.sum())==0
    return a

def witness_from_parent(P):
    out=np.empty(1<<len(FREE),dtype=np.int8)
    base=sum(v<<i for i,v in FIXED.items())
    for z in range(len(out)):
        idx=base
        for j,i in enumerate(FREE):
            idx|=((z>>j)&1)<<i
        out[z]=P[idx]
    sha=hashlib.sha256(",".join(map(str,out.tolist())).encode()).hexdigest()
    assert sha==EXPECTED_WITNESS_SHA and int(out.sum())==0
    return out

def hadamard(n):
    H=np.array([[1]],dtype=np.int8)
    for _ in range(n):
        H=np.block([[H,H],[H,-H]])
    return H

def log_unit_interval(x,terms=TERMS):
    assert F(1)<=x<=F(2)
    if x==1:return F(0),F(0)
    z=(x-1)/(x+1); z2=z*z; power=z; s=F(0)
    for k in range(terms):
        s+=power/(2*k+1); power*=z2
    lo=2*s
    rem=2*power/((2*terms+1)*(1-z2))
    return lo,lo+rem

@lru_cache(maxsize=None)
def log2_interval(x):
    x=F(x)
    if x<1:
        lo,hi=log2_interval(1/x); return -hi,-lo
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x<F(2)**e:e-=1
    m=x/F(2)**e
    a,b=log_unit_interval(m); c,d=log_unit_interval(F(2))
    return F(e)+a/d,F(e)+b/c

def phi_tables(N):
    lo=np.zeros(N//2+1); hi=np.zeros(N//2+1)
    for a in range(2,N+1,2):
        p=F(a*a,N*N)
        ll,uu=log2_interval(1/p)
        xl=float(p*ll); xu=float(p*uu)
        lo[a//2]=np.nextafter(xl,-np.inf)
        hi[a//2]=np.nextafter(xu,np.inf)
    return lo,hi

def entropy_bounds(W,plo,phi):
    idx=np.abs(W).astype(np.int64)//2
    # 1024 nonnegative terms, all <= 1/(e ln 2). IEEE round-to-nearest
    # accumulation error is <1e-11; PAD=1e-9 is deliberately much larger.
    return math.fsum(plo[idx].tolist())-PAD, math.fsum(phi[idx].tolist())+PAD

def main():
    f=witness_from_parent(parent())
    N=len(f); n=N.bit_length()-1
    H=hadamard(n); W=(H.astype(np.int16)@f.astype(np.int16)).astype(np.int16)
    deg=np.array([s.bit_count() for s in range(N)],dtype=np.int64)
    plo,phi=phi_tables(N)
    h0lo,h0hi=entropy_bounds(W,plo,phi)
    I0num=int((W.astype(np.int64)**2)@deg)
    assert I0num==F(257,128)*N*N
    R0lo=h0lo*N*N/(I0num-N*N)
    R0hi=h0hi*N*N/(I0num-N*N)

    plus=np.flatnonzero(f==1); minus=np.flatnonzero(f==-1)
    assert len(plus)==len(minus)==N//2
    H16=H.astype(np.int16)
    maxRub=-1.0; arg=None; maxH=None; maxInum=None
    count=0
    for x in plus:
        X=np.full(len(minus),int(x),dtype=np.int64)
        Y=minus.astype(np.int64)
        Ws=W[None,:]+2*(H16[:,Y].T-H16[:,X].T)
        idx=np.abs(Ws).astype(np.int32)//2
        Hubs=phi[idx].sum(axis=1)+PAD
        Inums=(Ws.astype(np.int64)**2)@deg
        Rubs=Hubs*(N*N)/(Inums-N*N)
        loc=float(Rubs.max())
        if loc>maxRub+1e-12:
            maxRub=loc
            jj=np.flatnonzero(np.abs(Rubs-loc)<1e-12)
            count=len(jj); j=int(jj[0])
            arg=(int(x),int(Y[j])); maxH=float(Hubs[j]); maxInum=int(Inums[j])
        elif abs(loc-maxRub)<1e-12:
            count+=int(np.sum(np.abs(Rubs-maxRub)<1e-12))
    gap=R0lo-maxRub
    assert gap>0.0204

    x,y=arg
    Wq=W.astype(np.int64)+2*(H[:,y].astype(np.int64)-H[:,x].astype(np.int64))
    def ent_float(A):
        p=(A.astype(float)/N)**2
        z=p[p>0]
        return float(-(z*np.log2(z)).sum())
    H0=ent_float(W); Hq=ent_float(Wq)
    p=(W.astype(float)/N)**2; q=(Wq.astype(float)/N)**2; m=(p+q)/2
    z=m[m>0]; Hm=float(-(z*np.log2(z)).sum())
    JS=Hm-(H0+Hq)/2
    Iq=maxInum/(N*N)
    Rq=Hq/(Iq-1)

    print("PASS")
    print("source_witness_sha256",EXPECTED_WITNESS_SHA)
    print("balanced_swaps_checked",len(plus)*len(minus))
    print("source_R_lower",format(R0lo,".15f"))
    print("source_R_upper",format(R0hi,".15f"))
    print("max_neighbor_R_upper",format(maxRub,".15f"))
    print("certified_gap_lower",format(gap,".15f"))
    print("closest_neighbor_example",arg)
    print("closest_neighbor_tie_count",count)
    print("closest_neighbor_I",format(Iq,".12f"))
    print("closest_neighbor_H",format(Hq,".15f"))
    print("closest_neighbor_R",format(Rq,".15f"))
    print("delta_H",format(Hq-H0,".15f"))
    print("delta_I",format(Iq-float(F(257,128)),".12f"))
    print("midpoint_entropy",format(Hm,".15f"))
    print("JS_negative_credit",format(JS,".15f"))
    print("twice_JS_credit",format(2*JS,".15f"))
    print("identity_deltaH_minus_[2(Hm-H0)-2JS]",
          format((Hq-H0)-(2*(Hm-H0)-2*JS),".3e"))
    print("full_FEI_status OPEN_NOT_PROVED")
if __name__=="__main__":main()
