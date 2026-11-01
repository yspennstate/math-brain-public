from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from decimal import Decimal, getcontext
import numpy as np
import mpmath as mp

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
R4_LO=F(Decimal('6.5218509485644448965490881329959858569477358114202361'))
R4_HI=F(Decimal('6.5218509485644448965496895824490791318643557898359042'))

def fwht(a):
    x=np.array(a,dtype=np.int64,copy=True)
    h=1
    while h<len(x):
        y=x.reshape(-1,2*h)
        u=y[:,:h].copy(); v=y[:,h:].copy()
        y[:,:h]=u+v; y[:,h:]=u-v
        h*=2
    return x

def core_and_hosts():
    base=int(''.join(SLICES[0]),16)
    masks=[int(''.join(row),16)^base for row in SLICES[1:]]
    assert all(m.bit_count()==2 for m in masks)
    return base, [[x for x in range(512) if (m>>x)&1] for m in masks]

def core_data(base,hosts):
    a=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)
    for h in hosts: a[h]=0
    A=fwht(a)
    Q=[]
    for lo,hi in hosts:
        q=np.zeros(512,dtype=np.int64); q[lo]=1; q[hi]=-1
        Q.append(fwht(q))
    return A,np.sum(np.array(Q),axis=0)

def dec(x,n=50):
    getcontext().prec=n+20
    return format(Decimal(x.numerator)/Decimal(x.denominator),f'.{n}f')

def main():
    # Endpoint Q enclosures independently recomputed this run by the inherited
    # exact-rational atanh-series method. This fast verifier checks the tail
    # deductions from those certified endpoint inputs.
    qmin_lo=F(Decimal('6.52185116719555246536276288334294304707982413002878'))
    qmax_hi=F(Decimal('6.52185116734786336372295569270409538753347541689836'))
    q4_lo=F(Decimal('6.52185116734782071493441014867858515967823376789247'))
    q4_hi=qmax_hi

    a=F(57,256); c=F(14593,65536)
    for _ in range(3): c=a+c**4/F(256)
    c4=c

    I=F(68013,32768)
    for _ in range(3): I=F(513,256)+F(9,256)*I**4
    I4=I
    I5=F(513,256)+F(9,256)*I4**4
    assert I4>8 and I5>200

    base,hosts=core_and_hosts()
    A,Qsum=core_data(base,hosts)
    pair_counts=Counter((int(x),int(y)) for x,y in zip(A,Qsum))
    assert sum(pair_counts.values())==512

    mp.iv.dps=50
    # Deliberately wider than the exact interval [a^4,c4^4].
    bI=mp.iv.mpf(['0.0024577605072408','0.0024581845086195'])
    assert float(a**4)>0.0024577605072408
    assert float(c4**4)<0.0024581845086195
    ln2=mp.iv.log(mp.iv.mpf(2)); kp=mp.iv.mpf(0)
    for (aa,qq),m in pair_counts.items():
        if qq==0: continue
        y=mp.iv.mpf(aa)+bI*qq; x=(y/512)**2
        phip=-mp.iv.log(x)/ln2-1/ln2
        kp += m*2*y*qq/(512**2)*phip
    alpha=mp.iv.mpf(9)/256
    phipb=-mp.iv.log(bI**2)/ln2-1/ln2
    kp += alpha*(-2*bI*phipb-32*bI)
    kp_lo=float(kp.a); kp_hi=float(kp.b)
    assert kp_lo>0

    S4=F(38,5265)
    tail_cap=(qmax_hi-R4_LO)*S4
    safety=qmin_lo-R4_HI
    assert tail_cap<safety

    lam4=F(133,128)/(I5-1)
    r5_lo=(1-lam4)*R4_LO+lam4*q4_lo
    r5_hi=(1-lam4)*R4_HI+lam4*q4_hi
    assert r5_lo>R4_HI

    S5=F(266,9)*F(1,200**4)/(1-F(1,200**4))
    rinf_hi=r5_hi+(qmax_hi-r5_lo)*S5

    print('PASS')
    print('pair_types='+str(len(pair_counts)))
    print('Kprime_interval=[%.18e,%.18e]'%(kp_lo,kp_hi))
    print('Qmin_lower='+dec(qmin_lo,48))
    print('Qmax_upper='+dec(qmax_hi,48))
    print('tail_weight_S4_upper='+dec(S4,30))
    print('tail_move_from_R4_upper='+dec(tail_cap,30))
    print('barrier_gap_lower='+dec(safety,30))
    print('R5_lower='+dec(r5_lo,48))
    print('R5_upper='+dec(r5_hi,48))
    print('R5_gain_over_R4_upper='+dec(r5_lo-R4_HI,48))
    print('Rinf_lower='+dec(r5_lo,48))
    print('Rinf_upper='+dec(rinf_hi,48))
    print('full_FEI_status=OPEN')

if __name__=='__main__': main()
