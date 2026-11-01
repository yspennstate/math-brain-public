#!/usr/bin/env python3
from fractions import Fraction as F
from functools import lru_cache
import itertools, json, math, hashlib
import numpy as np
import numba

TOP='fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00'
BOT='fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'
SLICES=[
 (TOP,BOT),
 (TOP,'fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000'),
 (TOP,'fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000'),
 ('fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00','fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP,'fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP,'fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000'),
 ('fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00',BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00',BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00',BOT),
 ('fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00',BOT),
]
N=512
DEN=N*N
TERMS=36
SCALE=1<<30

def fwht(a):
    a=np.asarray(a,dtype=np.int64).copy()
    h=1
    while h<len(a):
        for st in range(0,len(a),2*h):
            x=a[st:st+h].copy(); y=a[st+h:st+2*h].copy()
            a[st:st+h]=x+y; a[st+h:st+2*h]=x-y
        h*=2
    return a

def p2(k): return F(1<<k) if k>=0 else F(1,1<<(-k))

def log_unit(x):
    assert F(1)<=x<=F(2)
    if x==1:return F(0),F(0)
    z=(x-1)/(x+1); z2=z*z; p=z; s=F(0)
    for j in range(TERMS):
        s += p/F(2*j+1); p*=z2
    return 2*s, 2*s+2*p/(F(2*TERMS+1)*(1-z2))

@lru_cache(None)
def log2q(x):
    x=F(x)
    if x<1:
        lo,hi=log2q(1/x); return -hi,-lo
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x<p2(e): e-=1
    m=x/p2(e)
    a,b=log_unit(m); c,d=log_unit(F(2))
    return F(e)+a/d, F(e)+b/c

def ceilF(x): return -((-x.numerator)//x.denominator)
def floorF(x): return x.numerator//x.denominator

base=int(TOP+BOT,16)
masks=[int(''.join(row),16)^base for row in SLICES[1:]]
source_pairs=[[x for x in range(N) if (m>>x)&1] for m in masks]
assert all(len(p)==2 for p in source_pairs)
T=[x for p in source_pairs for x in p]
assert len(T)==18 and len(set(T))==18

truth=np.array([-1 if (base>>x)&1 else 1 for x in range(N)],dtype=np.int64)
P=[x for x,v in enumerate(truth) if v==1]
assert len(P)==265 and all(truth[x]==1 for x in T)

empty=truth.copy()
for x in T: empty[x]=0
A0=fwht(empty)

chi=np.empty((N,N),dtype=np.int8)
for x in range(N):
    for s in range(N):
        chi[x,s]=1 if ((s & x).bit_count()&1)==0 else -1

outsider=np.array([x for x in P if x not in set(T)],dtype=np.int64)
oldpairs=np.array(list(itertools.combinations(T,2)),dtype=np.int64)
newpairs=np.array(list(itertools.combinations(outsider,2)),dtype=np.int64)
assert oldpairs.shape[0]==153
assert newpairs.shape[0]==30381
assert oldpairs.shape[0]*newpairs.shape[0]==4648293

oldsum=chi[oldpairs[:,0]].astype(np.int64)+chi[oldpairs[:,1]].astype(np.int64)
newsum=chi[newpairs[:,0]].astype(np.int64)+chi[newpairs[:,1]].astype(np.int64)
sizes=np.array([s.bit_count() for s in range(N)],dtype=np.int64)

zmin=int(A0.min()-4); zmax=int(A0.max()+4)
phi_lo=np.zeros(zmax-zmin+1,dtype=np.int64)
phi_hi=np.zeros(zmax-zmin+1,dtype=np.int64)
for z in range(zmin,zmax+1):
    if z:
        p=F(z*z,DEN)
        lo,hi=log2q(F(DEN,z*z))
        phi_lo[z-zmin]=floorF(p*lo*SCALE)
        phi_hi[z-zmin]=ceilF(p*hi*SCALE)
assert int(np.max(phi_hi-phi_lo))<=1

HOST_H_NUM=9*SCALE//16
HOST_I_NUM=45*(DEN//256)

@numba.njit
def exhaustive(A0,sizes,oldsum,newsum,phi_hi,zmin):
    bestH=-1
    bestJ=1
    bo=-1
    bn=-1
    checked=0
    for oi in range(oldsum.shape[0]):
        for nj in range(newsum.shape[0]):
            Hnum=HOST_H_NUM
            Inum=HOST_I_NUM
            for s in range(A0.shape[0]):
                z=A0[s]+oldsum[oi,s]-newsum[nj,s]
                Hnum += phi_hi[z-zmin]
                Inum += sizes[s]*z*z
            J=Inum-DEN
            assert J>0
            checked+=1
            if bestH<0 or Hnum*bestJ > bestH*J:
                bestH=Hnum; bestJ=J; bo=oi; bn=nj
    return checked,bestH,bestJ,bo,bn

checked,bestH,bestJ,bo,bn=exhaustive(A0,sizes,oldsum,newsum,phi_hi,zmin)
assert checked==4648293
assert (int(oldpairs[bo,0]),int(oldpairs[bo,1]))==(78,79)
assert (int(newpairs[bn,0]),int(newpairs[bn,1]))==(30,31)

Z=A0+oldsum[bo]-newsum[bn]
Hlo=(int(phi_lo[Z-zmin].sum())+HOST_H_NUM)
Hhi=(int(phi_hi[Z-zmin].sum())+HOST_H_NUM)
assert Hhi==bestH
I_num=sum(int(sizes[s])*int(Z[s])**2 for s in range(N))+HOST_I_NUM
assert I_num-DEN==bestJ
assert F(I_num,DEN)==F(131,64)

C=F(162,25)
assert F(bestH,SCALE) < C*F(bestJ,DEN)

def fwht_list(v):
    a=list(map(int,v)); h=1
    while h<len(a):
        for st in range(0,len(a),2*h):
            for j in range(st,st+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

dust_checks=0
for r in range(1,4):
    R=1<<r
    for plus in itertools.combinations(range(R),R//2):
        plus=set(plus)
        vals=[1 if x in plus else -1 for x in range(R)]
        W=fwht_list(vals)
        for a in range(R):
            if vals[a]!=1: continue
            for b in range(R):
                if vals[b]!=-1: continue
                wx=a^b
                assert wx!=0
                for m in range(1,4):
                    n=r+m
                    active_base=[s for s in range(R) if ((s&wx).bit_count()&1)]
                    assert len(active_base)==R//2
                    active_total=1<<(n-1)
                    total_degree=n*(1<<(n-2))
                    L=sum(s.bit_count() for s in active_base)
                    Nd=active_total-len(active_base)
                    Dd=total_degree-L
                    assert Nd==(1<<(n-1))-(1<<(r-1))
                    assert Dd>=0
                    M=1<<n
                    gv=[]
                    u=a
                    v=b | (1<<r)
                    for z in range(M):
                        x=z & (R-1)
                        val=vals[x]
                        if z==u or z==v:
                            val=-val
                        gv.append(val)
                    WG=fwht_list(gv)
                    for s in range(M):
                        sx=s & (R-1)
                        sy=s >> r
                        base_num=(W[sx]*(1<<m)) if sy==0 else 0
                        chi_u=1 if ((sx&a).bit_count()&1)==0 else -1
                        parity=((sx&wx).bit_count() + (sy&1)) & 1
                        pred=base_num-4*chi_u if parity else base_num
                        assert WG[s]==pred
                    dust_checks+=1

ratio_upper=float(F(bestH,SCALE)/F(bestJ,DEN))
ratio_lower=float(F(Hlo,SCALE)/F(bestJ,DEN))
margin_648=float(C*F(bestJ,DEN)-F(bestH,SCALE))
out={
 "status":"PASS",
 "scope":"all exact symmetric-difference-4 support exchanges: remove any 2 of 18 source cells, add any 2 of 247 outside positive cells; every 9-pair host regrouping bounded by the optimistic 45/256 host influence",
 "supports_checked":checked,
 "old_pairs":len(oldpairs),
 "new_pairs":len(newpairs),
 "worst_upper_ratio_remove":[int(oldpairs[bo,0]),int(oldpairs[bo,1])],
 "worst_upper_ratio_add":[int(newpairs[bn,0]),int(newpairs[bn,1])],
 "worst_optimistic_I":"131/64",
 "worst_H_lower_dyadic":Hlo,
 "worst_H_upper_dyadic":Hhi,
 "dyadic_scale":SCALE,
 "worst_ratio_lower":ratio_lower,
 "worst_ratio_upper":ratio_upper,
 "rigorous_global_ratio_upper_lt_6_48":True,
 "rigorous_6_48_margin_lower":margin_648,
 "entropy_atom_rounding_width_units_max":int(np.max(phi_hi-phi_lo)),
 "sparse_two_point_formula_sanity_checks":dust_checks,
 "finite_scope_only":True,
 "full_FEI":"OPEN_NOT_PROVED"
}
print(json.dumps(out,indent=2,sort_keys=True))
