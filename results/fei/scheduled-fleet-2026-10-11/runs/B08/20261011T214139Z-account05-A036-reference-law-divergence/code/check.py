"""Exact rational validation. Run from the run directory: python -X utf8 code/check.py."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json, time, hashlib

START = time.perf_counter()
N = 16
def ln_unit(x):
    assert 1 <= x < 2
    t=(x-1)/(x+1)
    s=sum((2*t**(2*j+1)/F(2*j+1) for j in range(N)), F(0))
    err=2*t**(2*N+1)/(F(2*N+1)*(1-t*t))
    return s,s+err
LN2=ln_unit(F(2)-F(1,2**80))
# Use x=2 directly with the same valid t=1/3 series, rather than a limit.
t=F(1,3)
s=sum((2*t**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
LN2=(s,s+2*t**(2*N+1)/(F(2*N+1)*(1-t*t)))
def log2(x):
    assert x>0
    k=0
    while x<1: x*=2; k-=1
    while x>=2: x/=2; k+=1
    lo,hi=ln_unit(x)
    return F(k)+lo/LN2[1],F(k)+hi/LN2[0]
def ent_atom(x):
    if x==0:return F(0),F(0)
    lo,hi=log2(x)
    return -x*hi,-x*lo
def isum(xs):
    xs=list(xs)
    return sum((x[0] for x in xs),F(0)),sum((x[1] for x in xs),F(0))
def encode(iv):
    grid=10**18
    lo=(iv[0]*grid).__floor__()
    hi=(iv[1]*grid).__ceil__()
    return {'lower':str(F(lo,grid)),'upper':str(F(hi,grid)), 'rounding':'outward to denominator 10^18'}
def calc(m):
    d=F(1,2**(m-1)); a=4*d*(1-d)
    v=[F(1)]+[a**k*(1-F(4,2**k)*(1-d)**(m-k))**2 for k in range(1,m+1)]
    Z=sum((comb(m,k)*v[k] for k in range(m+1)),F(0))
    li=isum((tuple(comb(m,k)*z for z in ent_atom(v[k])) for k in range(m+1)))
    T=(li[0]/Z,li[1]/Z)
    pp=F(1,2**m)
    H=isum([ent_atom((1-2*pp)**2),tuple((2**m-1)*z for z in ent_atom(4*pp*pp))])
    h=isum([ent_atom(d),ent_atom(1-d)])
    B=(m*h[0],m*h[1]); K=(B[0]-H[1],B[1]-H[0]); I=m*d
    assert H[1]<=4*I
    assert T[1]/4-K[0]<=8*I
    assert B[1]-T[0]/4<=8*I
    assert T[1]/4-B[0]<=4*I
    assert Z>=1 and all(0<=v[k]<=a**k for k in range(1,m+1))
    # Independent direct Walsh / autocorrelation representation.
    if m<=7:
        size=2**m
        truth=[-1]+[1]*(size-1)
        aa=[F(sum(truth[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(size)),size) for s in range(size)]
        P=[x*x for x in aa]
        assert sum(P)==1
        assert all(sum(P[s] for s in range(size) if s>>i&1)==d for i in range(m))
        for u in range(size):
            k=u.bit_count()
            # Each differing bit contributes sqrt(d(1-d)); remaining bits contribute rational mass.
            c=F(0)
            for ss in range(size):
                rr=ss^u
                sign=(1 if aa[ss]>0 else -1)*(1 if aa[rr]>0 else -1)
                j=(ss & (size-1-u)).bit_count()
                c+=sign*d**j*(1-d)**(m-k-j)
            vv=c*c*(d*(1-d))**k
            assert vv==v[k]
    return {'m':m,'I':str(I),'Z':str(Z),'v_by_level':[str(x) for x in v], 'H':encode(H),'B':encode(B),'K':encode(K),'T':encode(T)}

rows=[calc(m) for m in range(2,17)]
# Finite rational constants used in the all-m proof.
d=F(1,64);a=4*d*(1-d)
assert (1+a)**6<F(3,2)
assert (1+a)**7<F(8,5)
assert F(8*8-3,128)*7<F(7,2)
assert 8*4*F(1,128)<=F(1,4)
assert 8*7*4*F(1,128)<=F(7,4)
# Monotonicity: m(m-1)2^(1-m) ratio (m+1)/(2(m-1)) <=1 for m>=3.
assert F(9,14)<1
# Rational lower estimates for e ln2 used in scalar bounds.
assert LN2[0]>F(2,3)
assert sum((F(1) / __import__('math').factorial(k) for k in range(5)),F(0))>F(8,3)
# Exact tensor autocorrelation construction and normalizer identity.
v2=[F(x) for x in rows[0]['v_by_level']]
v3=[F(x) for x in rows[1]['v_by_level']]
w=[v2[s.bit_count()]*v3[t.bit_count()] for s in range(4) for t in range(8)]
assert sum(w)==F(rows[0]['Z'])*F(rows[1]['Z'])
assert F(rows[1]['Z'])==F(319,256)
out={'helper_version':'A036-point-defect-collision-v1','arithmetic':'exact Fraction; rational ln series with geometric remainder','ln_terms':N,'cases':rows,'direct_Walsh_dimensions':[2,3,4,5,6,7], 'tensor_Z_verified':True,'all_assertions_passed':True,'runtime_seconds_diagnostic':time.perf_counter()-START}
path=Path('out/verification.json');path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'cases':len(rows),'all_assertions_passed':True,'output':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'runtime_seconds_diagnostic':out['runtime_seconds_diagnostic']}))
