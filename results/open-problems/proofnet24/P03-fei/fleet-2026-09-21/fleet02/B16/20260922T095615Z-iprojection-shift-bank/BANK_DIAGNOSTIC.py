from itertools import combinations
from hashlib import sha256
import math
import numpy as np

CQ=6.558445589
CDAG=6.521851214
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
EXPECTED='f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839'

def fwht(v):
    a=np.asarray(v,dtype=float).copy(); h=1
    while h<len(a):
        b=a.reshape(-1,2*h); x=b[:,:h].copy(); y=b[:,h:].copy()
        b[:,:h]=x+y; b[:,h:]=x-y; h*=2
    return a

def solve_c(r):
    if float(sum(r))<=1+1e-13: return 1.0
    def g(c): return 1-c-float(np.prod(1-c*r))
    lo=1e-14; hi=1.0
    for _ in range(100):
        mid=(lo+hi)/2
        if g(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def root_bank(d):
    d=np.asarray(d,float)
    if d.max(initial=0)==0: return 0.0
    lo=0.; hi=float(d.max())
    for _ in range(100):
        u=(lo+hi)/2
        F=float(np.square(np.maximum(d-u,0)).sum()-4*u)
        if F>0: lo=u
        else: hi=u
    return (lo+hi)/2

def bank_for_truth(tab,C):
    N=len(tab); n=N.bit_length()-1
    A=fwht(tab)/N; P=A*A
    r=np.array([P[((np.arange(N)>>i)&1)==1].sum() for i in range(n)])
    mu=float(r.sum())
    if mu<=1+1e-12: return 0.0,0.0,0.0
    c=solve_c(r); t=c*r; idx=np.arange(N); qu=np.ones(N)
    for i,ti in enumerate(t): qu *= np.where(((idx>>i)&1)!=0,ti,1-ti)
    Q=qu/c; Q[0]=0
    Hmax=-float(np.sum(Q[Q>0]*np.log2(Q[Q>0])))
    b=np.where(A<0,-1.0,1.0)*np.sqrt(Q)
    Hb=fwht(b); Cb=fwht(Hb*Hb)/N
    u=root_bank(np.abs(Cb[1:]))
    return -2*math.log2(1-u/2), Hmax-C*(mu-1), u

minimum=1e100; count=0
for neg in combinations(range(16),8):
    ns=set(neg); tab=np.array([-1 if x in ns else 1 for x in range(16)],dtype=float)
    KLhalf,need,u=bank_for_truth(tab,CDAG)
    A=fwht(tab)/16; P=A*A
    mu=sum(sum(P[s] for s in range(16) if (s>>i)&1) for i in range(4))
    if mu>1+1e-12: minimum=min(minimum,KLhalf-need)
    count+=1

N=1<<18; base=int(''.join(SLICES[0]),16)
masks=[int(''.join(r),16)^base for r in SLICES[1:]]; seen=base; hosts=[]
for m in masks:
    assert not (seen&m) and m.bit_count()==2; seen|=m
    hosts.append([x for x in range(512) if (m>>x)&1])
core=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)
tab=np.tile(core,(1<<9,1))
for j,cells in enumerate(hosts):
    active=(np.arange(1<<9)&(1<<j))!=0
    tab[np.ix_(active,np.array(cells,dtype=int))]=-1
tab=tab.ravel()
assert sha256(','.join(map(str,tab)).encode()).hexdigest()==EXPECTED
KLhalf,need,u=bank_for_truth(tab,CQ)

print('PASS_DIAGNOSTIC')
print('balanced_n4_count',count)
print('balanced_n4_min_noncharacter_margin_at_Cdag',format(minimum,'.17g'))
print('numaro_bank_u_star',format(u,'.17g'))
print('numaro_bank_KLhalf',format(KLhalf,'.17g'))
print('numaro_balanced_target_need_at_CQ',format(need,'.17g'))
print('numaro_bank_shortfall',format(need-KLhalf,'.17g'))
print('NOTE float diagnostic only; theorem proof and source clearance use exact report/checker.')
