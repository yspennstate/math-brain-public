from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from decimal import Decimal, getcontext
import hashlib
import numpy as np

TERMS=80
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

def fwht(a):
    x=np.array(a,dtype=np.int64,copy=True)
    h=1
    while h<len(x):
        y=x.reshape(-1,2*h)
        u=y[:,:h].copy();v=y[:,h:].copy()
        y[:,:h]=u+v;y[:,h:]=u-v
        h*=2
    return x

def core_and_hosts():
    base=int(''.join(SLICES[0]),16)
    masks=[int(''.join(row),16)^base for row in SLICES[1:]]
    assert all(m.bit_count()==2 for m in masks)
    hosts=[[x for x in range(512) if (m>>x)&1] for m in masks]
    return base,hosts

def source_table(base,hosts):
    core=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)
    T=np.tile(core,(512,1))
    for j,cells in enumerate(hosts):
        mask=(np.arange(512)&(1<<j))!=0
        T[np.ix_(mask,np.array(cells,dtype=int))]=-1
    return T.ravel()

def log_unit_interval(x,terms=TERMS):
    assert F(1)<=x<=F(2)
    if x==1:return F(0),F(0)
    z=(x-1)/(x+1);z2=z*z;power=z;s=F(0)
    for k in range(terms):
        s+=power/(2*k+1);power*=z2
    lo=2*s
    rem=2*power/((2*terms+1)*(1-z2))
    return lo,lo+rem

@lru_cache(maxsize=None)
def log2_interval(x):
    x=F(x)
    if x<1:
        lo,hi=log2_interval(1/x);return -hi,-lo
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x<F(2)**e:e-=1
    m=x/F(2)**e
    a,b=log_unit_interval(m);c,d=log_unit_interval(F(2))
    return F(e)+a/d,F(e)+b/c

def entropy_hist(hist,norm):
    lo=F(0);hi=F(0)
    for s,m in hist.items():
        if not s:continue
        a,b=log2_interval(F(norm,s));w=F(s*m,norm)
        lo+=w*a;hi+=w*b
    return lo,hi

def phi_interval(x):
    x=F(x)
    if not x:return F(0),F(0)
    a,b=log2_interval(1/x)
    return x*a,x*b

def core_data(base,hosts):
    a=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)
    for h in hosts:a[h]=0
    A=fwht(a)
    Q=[]
    for lo,hi in hosts:
        q=np.zeros(512,dtype=np.int64);q[lo]=1;q[hi]=-1
        Q.append(fwht(q))
    return A,np.sum(np.array(Q),axis=0)

def hcore_interval(A,Qsum,b):
    b=F(b);num=b.numerator;den=b.denominator
    nums=[int(ai)*den+num*int(qi) for ai,qi in zip(A,Qsum)]
    norm=(512*den)**2
    hist=Counter(v*v for v in nums if v)
    return entropy_hist(hist,norm)

def dec(x,digits=40):
    getcontext().prec=digits+15
    return format(Decimal(x.numerator)/Decimal(x.denominator),f'.{digits}f')

def main():
    base,hosts=core_and_hosts();table=source_table(base,hosts)
    digest=hashlib.sha256(','.join(map(str,table)).encode()).hexdigest()
    assert digest==EXPECTED_SHA and table.sum()==0
    W=fwht(table);norm=len(table)**2
    assert sum(int(v)*int(v) for v in W)==norm
    Hglo,Hghi=entropy_hist(Counter(int(v)*int(v) for v in W if v),norm)
    Is=F(sum(i.bit_count()*int(v)*int(v) for i,v in enumerate(W)),norm)
    assert Is==F(261,128)
    A,Qsum=core_data(base,hosts)
    alpha=F(9,256);b0=F(1,256)
    hc0lo,hc0hi=hcore_interval(A,Qsum,b0);p0lo,p0hi=phi_interval(b0*b0)
    H1lo=hc0lo+alpha*(Hglo-p0hi+16*(1-b0*b0))
    H1hi=hc0hi+alpha*(Hghi-p0lo+16*(1-b0*b0))
    I1=Is+alpha*(Is-1)
    assert I1==F(68013,32768)
    c1=F(int(A[1]),512)+b0*F(int(Qsum[1]),512)
    assert c1==F(14593,65536)
    R1lo=H1lo/(I1-1);R1hi=H1hi/(I1-1)

    # A = fourth balanced self-composition power of F1.
    IA=I1**4
    factor=(IA-1)/(I1-1)
    HAlo=H1lo*factor;HAhi=H1hi*factor
    bA=c1**4

    # F2: place a fresh copy of A on each of the nine source host edges,
    # identifying A's chosen leaf with the corresponding host pivot.
    hcalo,hcahi=hcore_interval(A,Qsum,bA);palo,pahi=phi_interval(bA*bA)
    H2lo=hcalo+alpha*(HAlo-pahi+16*(1-bA*bA))
    H2hi=hcahi+alpha*(HAhi-palo+16*(1-bA*bA))
    I2=Is+alpha*(IA-1)
    R2lo=H2lo/(I2-1);R2hi=H2hi/(I2-1)
    gain=R2lo-R1hi
    assert gain>F(67,100000000)  # > 6.7e-7, exact-rational sign decision
    assert R2lo>F('6.5218507')

    print('PASS')
    print('source_sha256='+digest)
    print('I1='+str(I1))
    print('core_singleton_c1='+str(c1))
    print('self_comp_depth=4')
    print('IA='+str(IA))
    print('shared_leaf_bA='+str(bA))
    print('I2='+str(I2))
    print('R1_lower='+dec(R1lo,45))
    print('R1_upper='+dec(R1hi,45))
    print('R2_lower='+dec(R2lo,45))
    print('R2_upper='+dec(R2hi,45))
    print('certified_gain_lower='+dec(gain,50))
    print('full_FEI_status=OPEN')

if __name__=='__main__':main()
