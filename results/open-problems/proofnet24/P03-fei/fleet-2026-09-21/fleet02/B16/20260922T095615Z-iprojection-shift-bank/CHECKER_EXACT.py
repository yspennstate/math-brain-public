from fractions import Fraction as F
from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
import math
import numpy as np

EXPECTED_SHA='f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839'
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
N=1<<18
D=N*N
CQ=F(6558445589,10**9)

def reconstruct():
    base=int(''.join(SLICES[0]),16)
    masks=[int(''.join(r),16)^base for r in SLICES[1:]]
    seen=base
    hosts=[]
    for m in masks:
        assert not (seen&m) and m.bit_count()==2
        seen |= m
        hosts.append([x for x in range(512) if (m>>x)&1])
    core=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)
    tab=np.tile(core,(1<<9,1))
    for j,cells in enumerate(hosts):
        active=(np.arange(1<<9)&(1<<j))!=0
        tab[np.ix_(active,np.array(cells,dtype=int))]=-1
    tab=tab.ravel()
    assert sha256(','.join(map(str,tab)).encode()).hexdigest()==EXPECTED_SHA
    assert int(tab.sum())==0
    return tab

def fwht_int(v):
    a=np.asarray(v,dtype=np.int64).copy()
    h=1
    while h<len(a):
        b=a.reshape(-1,2*h)
        x=b[:,:h].copy()
        y=b[:,h:].copy()
        b[:,:h]=x+y
        b[:,h:]=x-y
        h*=2
    return a

def p2(e):
    return F(1<<e) if e>=0 else F(1,1<<(-e))

def flog2(x):
    e=x.numerator.bit_length()-x.denominator.bit_length()
    while p2(e)>x: e-=1
    while p2(e+1)<=x: e+=1
    return e

@lru_cache(None)
def lnred(x,M=50):
    assert F(1)<=x<=F(2)
    z=(x-1)/(x+1)
    zz=z*z
    term=z
    s=F(0)
    for k in range(M):
        s += term/F(2*k+1)
        term *= zz
    lo=2*s
    tail=F(0) if z==0 else 2*term/F(2*M+1)/(1-zz)
    return lo,lo+tail

@lru_cache(None)
def ln2iv(M=50):
    return lnred(F(2),M)

def log2iv(x,M=50):
    assert x>0
    e=flog2(x)
    y=x/p2(e)
    nlo,nhi=lnred(y,M)
    dlo,dhi=ln2iv(M)
    return F(e)+nlo/dhi,F(e)+nhi/dlo

def phiiv(x,M=50):
    if x==0: return F(0),F(0)
    lo,hi=log2iv(1/x,M)
    return x*lo,x*hi

def dec(x,d=18):
    return f"{float(x):.{d}g}"

tab=reconstruct()
W=fwht_int(tab)
assert sum(int(w)*int(w) for w in W)==D

cnt=Counter(int(w)*int(w) for w in W if w)
Hlo=F(0); Hhi=F(0)
for num,k in cnt.items():
    lo,hi=phiiv(F(num,D))
    Hlo += k*lo
    Hhi += k*hi

group_num=defaultdict(int)
l_num=defaultdict(int)
I_num=0
for s,w in enumerate(W):
    ww=int(w)*int(w)
    if ww==0: continue
    coremask=s & 511
    hostwt=(s>>9).bit_count()
    group_num[(coremask,hostwt)] += ww
    l_num[hostwt] += ww
    I_num += s.bit_count()*ww
assert sum(group_num.values())==D
I=F(I_num,D)
assert I==F(261,128)

HZlo=F(0); HZhi=F(0)
for num in group_num.values():
    lo,hi=phiiv(F(num,D))
    HZlo += lo
    HZhi += hi

Elo=F(0); Ehi=F(0)
for l,num in l_num.items():
    c=math.comb(9,l)
    if c==1: continue
    lo,hi=log2iv(F(c))
    wt=F(num,D)
    Elo += wt*lo
    Ehi += wt*hi

# Exact chain rule for Z=(all nine core labels, host Hamming weight):
# K_occ = Delta_Z + R_host, where
# R_host = H(Z)+E log2 binom(9,L)-H(P).
Rlo=HZlo+Elo-Hhi
Rhi=HZhi+Ehi-Hlo

# Balanced-center residual at the quartic-safe candidate:
# D_Q = C_Q (I-1)-H(P).
DQlo=CQ*(I-1)-Hhi
DQhi=CQ*(I-1)-Hlo

# Since Delta_Z - [Hmax-C_Q(I-1)] = D_Q-R_host,
# positive lower margin proves this source is admitted by the projected KL credit.
Mlo=DQlo-Rhi
Mhi=DQhi-Rlo

assert Hhi-Hlo < F(1,10**45)
assert Rhi-Rlo < F(1,10**45)
assert Mlo > F(5887256,10**9)

print("PASS")
print("truth_sha256",EXPECTED_SHA)
print("I",I)
print("H_interval",dec(Hlo),dec(Hhi))
print("host_label_loss_interval",dec(Rlo),dec(Rhi))
print("quartic_center_residual_interval",dec(DQlo),dec(DQhi))
print("projected_KL_margin_interval",dec(Mlo),dec(Mhi))
print("certified_margin_gt", "0.005887256")
print("groups_nonzero",len(group_num))
print("log_interval_width_lt","1e-45")
