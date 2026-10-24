"""Rigorous scalar certificate for B14's nine-core block selector.

This checker uses the exact source-bound nine-core data already validated in the
shared-graft FEI construction.  It proves an upper bound for the elementary
block-price envelope U(b) on 0 <= b <= 1/4.  It does not prove FEI.
"""
from fractions import Fraction as F
from collections import Counter

TOP='fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00'
BOT='fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'
SLICES=[
(TOP,BOT),(TOP,'fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000'),
(TOP,'fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000'),
('fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00','fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'),
(TOP,'fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000'),
(TOP,'fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000'),
('fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00',BOT),
('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00',BOT),
('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00',BOT),
('fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00',BOT)]

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

base=int(''.join(SLICES[0]),16)
masks=[int(''.join(r),16)^base for r in SLICES[1:]]
assert len(masks)==9 and all(m.bit_count()==2 for m in masks)
hosts=[[x for x in range(512) if (m>>x)&1] for m in masks]
a=[-1 if (base>>x)&1 else 1 for x in range(512)]
for h in hosts:
    for x in h:
        a[x]=0
A=fwht(a)
qsum=[0]*512
for lo,hi in hosts:
    q=[0]*512; q[lo]=1; q[hi]=-1
    w=fwht(q)
    qsum=[u+v for u,v in zip(qsum,w)]
assert A[1]==114 and qsum[1]==2
pairs=Counter(zip(A,qsum))
assert len(pairs)==19

# Exact rational atanh enclosure for every logarithm.
NTERMS=28

def p2(k):
    return F(1<<k,1) if k>=0 else F(1,1<<(-k))

def norm2(x):
    k=x.numerator.bit_length()-x.denominator.bit_length()
    while x<p2(k): k-=1
    while x>=p2(k+1): k+=1
    return k,x/p2(k)

def lnunit(y):
    if y==1:
        return F(0),F(0)
    z=(y-1)/(y+1); z2=z*z; t=z; s=F(0)
    for j in range(NTERMS):
        if j:
            t*=z2
        s+=t/F(2*j+1)
    lo=2*s
    rem=2*z**(2*NTERMS+1)/(F(2*NTERMS+1)*(1-z2))
    return lo,lo+rem

LN2L,LN2U=lnunit(F(2))

def log2b(x):
    k,y=norm2(x); lo,hi=lnunit(y)
    return F(k)+lo/LN2U,F(k)+hi/LN2L

def phib(p):
    if p==0:
        return F(0),F(0)
    lo,hi=log2b(1/p)
    return p*lo,p*hi

alpha=F(9,256)
B=F(257,256)

def hcore_upper(l,u):
    out=F(0)
    for (ai,qi),mult in pairs.items():
        if ai==0 and qi==0:
            continue
        pmax=max((F(ai)+l*qi)**2,(F(ai)+u*qi)**2)/F(512*512)
        # p <= 1/16 < 1/e, so phi(p)=-p log_2 p is increasing here.
        assert pmax<F(1,16)
        out+=mult*phib(pmax)[1]
    return out

def cell_upper(l,u):
    # On [0,1/4], h_2 and 1+b-b^2 are increasing, while phi(b^2)
    # is increasing.  The choices below therefore give a rigorous numerator
    # upper bound and denominator lower bound on the whole cell.
    nup=(hcore_upper(l,u)+alpha*(
        phib(u)[1]+phib(1-u)[1]
        +2*u/LN2L
        -phib(l*l)[0]
        +16*(1-l*l)))
    dlo=B+alpha*(1+l-l*l)
    return nup/dlo

M=64
bmax=F(1,4)
target=F(816,125)  # 6.528
mx=F(0); arg=-1
for k in range(M):
    l=bmax*k/M; u=bmax*(k+1)/M
    value=cell_upper(l,u)
    if value>mx:
        mx,arg=value,k

assert mx<target
print('PASS')
print('cells',M,'worst_cell',arg)
print('max_upper_float',float(mx))
print('target',float(target))
print('strict_gap_float',float(target-mx))
print('full_FEI','OPEN_NOT_PROVED')
