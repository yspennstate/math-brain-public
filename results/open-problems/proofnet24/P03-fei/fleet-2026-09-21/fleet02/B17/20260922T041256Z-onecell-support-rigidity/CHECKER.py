#!/usr/bin/env python3
from fractions import Fraction as F
from functools import lru_cache
import json

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
C=F(1623,250) # 6.492

def fwht(a):
    a=list(map(int,a)); h=1
    while h<len(a):
        for st in range(0,len(a),2*h):
            for j in range(st,st+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def p2(k):
    return F(1<<k) if k>=0 else F(1,1<<(-k))

def log_unit(x):
    assert F(1)<=x<=F(2)
    if x==1:return F(0),F(0)
    z=(x-1)/(x+1); z2=z*z; p=z; s=F(0)
    for j in range(TERMS):
        s += p/F(2*j+1); p*=z2
    return 2*s, 2*s+2*p/(F(2*TERMS+1)*(1-z2))

@lru_cache(None)
def log2i(x):
    x=F(x)
    if x<1:
        lo,hi=log2i(1/x); return -hi,-lo
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x<p2(e): e-=1
    m=x/p2(e)
    a,b=log_unit(m); c,d=log_unit(F(2))
    return F(e)+a/d, F(e)+b/c

@lru_cache(None)
def phi_upper_abs(z):
    z=abs(int(z))
    if z==0:return F(0)
    p=F(z*z,DEN)
    _,hi=log2i(F(DEN,z*z))
    return p*hi

def chi_point(x):
    return [1 if ((s & x).bit_count()&1)==0 else -1 for s in range(N)]

base=int(TOP+BOT,16)
masks=[int(''.join(row),16)^base for row in SLICES[1:]]
pairs=[[x for x in range(N) if (m>>x)&1] for m in masks]
assert all(len(p)==2 for p in pairs)
T=[x for p in pairs for x in p]
truth=[-1 if (base>>x)&1 else 1 for x in range(N)]
assert sum(truth)==18
assert all(truth[x]==1 for x in T)
positive=[x for x,v in enumerate(truth) if v==1]
assert len(positive)==265

a=truth[:]
for x in T:a[x]=0
A0=fwht(a)
chis={x:chi_point(x) for x in set(T+positive)}
sizes=[s.bit_count() for s in range(N)]

def empty_stats_upper(A):
    Hu=sum(phi_upper_abs(z) for z in A)
    I=sum(F(sizes[s]*A[s]*A[s],DEN) for s in range(N))
    return Hu,I

H0u,I0=empty_stats_upper(A0)
Iorig=I0+F(45,256)
assert Iorig==F(261,128)

# For every one-cell exchange, grant the host bank its optimistic minimum
# influence 45/256.  Any actual 9-pair regrouping has the same host entropy
# 9/16 and no smaller influence.
best_margin=None
best_pair=None
checked=0
for old in T:
    co=chis[old]
    for new in positive:
        if new in T: continue
        cn=chis[new]
        A=[A0[s]+co[s]-cn[s] for s in range(N)]
        Hu,Ie=empty_stats_upper(A)
        Htot_u=Hu+F(9,16)
        Ioptim=Ie+F(45,256)
        assert Ioptim>1
        margin=C*(Ioptim-1)-Htot_u
        checked+=1
        if best_margin is None or margin<best_margin:
            best_margin=margin; best_pair=(old,new,Ioptim,Htot_u)

assert checked==18*(265-18)==4446
assert best_margin>0

def dec(x,places=40):
    from decimal import Decimal,getcontext
    getcontext().prec=places+12
    return str(Decimal(x.numerator)/Decimal(x.denominator))

out={
 "status":"PASS",
 "scope":"all 4446 one-cell mutations of the exact 18-row exceptional support; arbitrary 9-pair host regrouping bounded optimistically by 9 adjacent pairs",
 "constant_upper":"1623/250 = 6.492",
 "mutations_checked":checked,
 "best_case_old_cell":best_pair[0],
 "best_case_new_cell":best_pair[1],
 "best_rigorous_margin_C_times_Iminus1_minus_H_lower_bound":dec(best_margin),
 "best_case_optimistic_I":str(best_pair[2]),
 "best_case_entropy_upper":dec(best_pair[3]),
 "original_I":str(Iorig),
 "finite_scope_only":True,
 "full_FEI":"OPEN_NOT_PROVED"
}
print(json.dumps(out,indent=2))
