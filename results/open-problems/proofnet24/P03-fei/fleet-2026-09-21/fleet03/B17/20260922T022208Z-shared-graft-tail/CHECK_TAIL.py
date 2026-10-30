from __future__ import annotations
from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction as F
from functools import lru_cache

TERMS = 80
ALPHA = F(9, 256)
BETA = F(133, 128)
B = F(257, 256)

# Exact nine-host source representation inherited from the source-validated
# shared-graft construction. The checker reconstructs its 9-bit core Walsh data.
TOP='fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00'
BOT='fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'
SLICES=[
 (TOP,BOT),
 (TOP,'fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000'),
 (TOP,'fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000'),
 ('fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00',
  'fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP,'fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP,'fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000'),
 ('fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00',BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00',BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00',BOT),
 ('fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00',BOT),
]

def fwht(a):
    x=list(a); h=1
    while h<len(x):
        for i in range(0,len(x),2*h):
            for j in range(i,i+h):
                u=x[j]; v=x[j+h]
                x[j]=u+v; x[j+h]=u-v
        h*=2
    return x

def source_core():
    base=int(''.join(SLICES[0]),16)
    masks=[int(''.join(row),16)^base for row in SLICES[1:]]
    assert all(m.bit_count()==2 for m in masks)
    hosts=[[x for x in range(512) if (m>>x)&1] for m in masks]
    a=[-1 if (base>>x)&1 else 1 for x in range(512)]
    for host in hosts:
        for x in host:
            a[x]=0
    A=fwht(a)
    Q=[0]*512
    for lo,hi in hosts:
        q=[0]*512; q[lo]=1; q[hi]=-1
        w=fwht(q)
        Q=[x+y for x,y in zip(Q,w)]
    return Counter(zip(A,Q))

@lru_cache(maxsize=None)
def log_unit_interval(x):
    x=F(x)
    assert F(1)<=x<=F(2)
    if x==1:
        return F(0),F(0)
    z=(x-1)/(x+1); z2=z*z; power=z; s=F(0)
    for k in range(TERMS):
        s += power/(2*k+1)
        power *= z2
    lo=2*s
    rem=2*power/((2*TERMS+1)*(1-z2))
    return lo,lo+rem

@lru_cache(maxsize=None)
def log2_interval(x):
    x=F(x)
    if x<1:
        lo,hi=log2_interval(1/x)
        return -hi,-lo
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x<F(2)**e:
        e-=1
    m=x/F(2)**e
    a,b=log_unit_interval(m)
    c,d=log_unit_interval(F(2))
    return F(e)+a/d,F(e)+b/c

def phi_point_interval(x):
    x=F(x)
    if not x:
        return F(0),F(0)
    lo,hi=log2_interval(1/x)
    return x*lo,x*hi

def hcore_interval(hist,blo,bhi):
    # Every squared core mass below is <1/20<1/e, where phi(x)=-x log2 x
    # is increasing. Endpoint coefficient bounds therefore give rigorous
    # entropy bounds without an optimizer.
    out_lo=F(0); out_hi=F(0); max_x=F(0)
    for (a,q),mult in hist.items():
        vals=(F(a)+blo*q,F(a)+bhi*q)
        low=min(vals); high=max(vals)
        maxabs=max(abs(low),abs(high))
        minabs=F(0) if low<=0<=high else min(abs(low),abs(high))
        xlo=(minabs/F(512))**2
        xhi=(maxabs/F(512))**2
        max_x=max(max_x,xhi)
        assert xhi<F(1,20)
        plo,_=phi_point_interval(xlo)
        _,phi=phi_point_interval(xhi)
        out_lo += mult*plo
        out_hi += mult*phi
    return out_lo,out_hi,max_x

def cmap(c):
    return F(57,256)+c**4/F(256)

def dec(x,digits=60):
    getcontext().prec=digits+20
    return format(Decimal(x.numerator)/Decimal(x.denominator),f'.{digits}f')

def main():
    hist=source_core()
    assert sum(hist.values())==512 and len(hist)==19

    # Exact F1 singleton and three applications give c4.
    c1=F(14593,65536)
    c2=cmap(c1); c3=cmap(c2); c4=cmap(c3)

    # Rational trapping interval for every c_t from t=4 onward.
    cL=F(22266585228323679,10**17)
    cU=F(22266585228323683,10**17)
    assert cL<c4<cU
    assert cmap(cL)>cL
    assert cmap(cU)<cU

    # K(b)=H_core(b)+alpha[-phi(b^2)+16(1-b^2)] for b=c_t^4.
    blo=cL**4; bhi=cU**4
    hLo,hHi,max_x=hcore_interval(hist,blo,bhi)
    phiBloLo,_=phi_point_interval(blo**2)
    _,phiBhiHi=phi_point_interval(bhi**2)
    KLo=hLo+ALPHA*(-phiBhiHi+16*(1-bhi**2))
    KHi=hHi+ALPHA*(-phiBloLo+16*(1-blo**2))

    # Certified F4 interval from fleet03/B18's exact source-bound checker.
    R4Lo=F('6.5218509485644448965490881329959858569477358114202360')
    R4Hi=F('6.5218509485644448965496895824490791318643557898359043')

    # Exact influence recurrence through F4.
    I=F(68013,32768)
    for _ in range(3):
        I=F(261,128)+ALPHA*(I**4-1)
    I4=I
    assert F(449,50)<I4<F(9)

    # The recurrence is
    # R_{t+1}-R_t = [K(c_t^4)-BETA R_t]/D_t,
    # D_t=ALPHA I_t^4+B = I_{t+1}-1.
    threshold=KLo/BETA
    NLo=KLo-BETA*R4Hi
    NHi=KHi-BETA*R4Lo
    assert NLo>0 and threshold>R4Hi

    # D4>229, and D_{t+1}=ALPHA(D_t+1)^4+B >= ALPHA D_t^4.
    # Consequently D_{t+1}/D_t > 400000 for every t>=4.
    D4=ALPHA*I4**4+B
    assert D4>229
    assert ALPHA*F(229)**3>400000

    # Conditional on the already-proved positive increments, N_t<=NHi.
    # The geometric reciprocal-D bound then keeps all later R_t below
    # threshold; induction closes and proves every later increment positive.
    reciprocal_sum_upper=F(1,229)/(1-F(1,400000))
    tail_upper=NHi*reciprocal_sum_upper
    reserve=threshold-R4Hi-tail_upper
    assert reserve>0

    # One explicit new finite gate F5 gives a stronger FEI lower bound.
    # D4 < ALPHA*9^4+B and its numerator is >=NLo.
    D4_upper=ALPHA*F(9)**4+B
    first_increment_lower=NLo/D4_upper
    Rinf_lower=R4Lo+first_increment_lower
    Rinf_upper=R4Hi+tail_upper
    assert Rinf_lower>F('6.5218509495')
    assert Rinf_upper>Rinf_lower

    lift_C0=4*(Rinf_lower-F('6.4548'))
    lift_readonce=4*(Rinf_lower-F('6.4573'))

    print('PASS')
    print('core_pair_types='+str(len(hist)))
    print('core_mass_max_upper='+dec(max_x,50))
    print('c4='+dec(c4,50))
    print('c_trap=['+dec(cL,50)+','+dec(cU,50)+']')
    print('K_lower='+dec(KLo,60))
    print('K_upper='+dec(KHi,60))
    print('threshold_K_over_beta='+dec(threshold,60))
    print('R4_lower='+dec(R4Lo,60))
    print('R4_upper='+dec(R4Hi,60))
    print('numerator_lower='+dec(NLo,60))
    print('numerator_upper='+dec(NHi,60))
    print('I4='+dec(I4,60))
    print('D4='+dec(D4,60))
    print('reciprocal_D_tail_upper='+dec(reciprocal_sum_upper,60))
    print('future_ratio_gain_upper='+dec(tail_upper,60))
    print('threshold_reserve='+dec(reserve,60))
    print('F5_increment_lower='+dec(first_increment_lower,60))
    print('shared_graft_limit_lower='+dec(Rinf_lower,60))
    print('shared_graft_limit_upper='+dec(Rinf_upper,60))
    print('limit_interval_width='+dec(Rinf_upper-Rinf_lower,60))
    print('scalar_lift_floor_over_C0='+dec(lift_C0,60))
    print('scalar_lift_floor_over_readonce_6.4573='+dec(lift_readonce,60))
    print('all_future_shared_graft_increments=PROVED_POSITIVE')
    print('full_FEI_status=OPEN')

if __name__=='__main__':
    main()
