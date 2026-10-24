from fractions import Fraction as F
from functools import lru_cache
from decimal import Decimal, getcontext

TERMS = 80
N = 512
ALPHA = F(9,256)

# Exact (A_s,Q_s) Walsh numerator classes and multiplicities from the
# source-bound nine-host core in account01/B18.
CLASSES = [
    (-18,-2,72),(2,2,72),(0,0,46),(-16,0,36),(16,0,36),
    (10,-6,36),(4,4,36),(-4,-4,36),(-2,-2,36),
    (44,-4,18),(-44,4,18),(-6,10,18),(38,6,12),
    (114,2,9),(8,8,9),(-8,-8,9),(4,-12,6),(-4,12,6),(2,18,1)
]
SPECIAL = (114,2,9)

def log_unit_interval(x, terms=TERMS):
    x=F(x)
    assert F(1) <= x <= F(2)
    if x == 1:
        return F(0),F(0)
    z=(x-1)/(x+1)
    z2=z*z
    power=z
    s=F(0)
    for k in range(terms):
        s += power/(2*k+1)
        power *= z2
    lo=2*s
    rem=2*power/((2*terms+1)*(1-z2))
    return lo,lo+rem

LN2_LO,LN2_HI=log_unit_interval(F(2))
INV_LN2=(1/LN2_HI,1/LN2_LO)

@lru_cache(maxsize=None)
def log2_interval(x):
    x=F(x)
    assert x>0
    if x<1:
        lo,hi=log2_interval(1/x)
        return -hi,-lo
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x < F(2)**e:
        e -= 1
    m=x/F(2)**e
    a,b=log_unit_interval(m)
    return F(e)+a/LN2_HI, F(e)+b/LN2_LO

def add(I,J):
    return I[0]+J[0], I[1]+J[1]

def scale(c,I):
    c=F(c)
    return (c*I[0],c*I[1]) if c>=0 else (c*I[1],c*I[0])

def psi_interval(x):
    x=F(x)
    if x==0:
        return F(0),F(0)
    lp=log2_interval(x*x/F(N*N))
    return scale(-x, add(lp,INV_LN2))

def class_derivative_interval(a,q,m,b):
    a,q,b=F(a),F(q),F(b)
    x=a+b*q
    return scale(F(2*m)*q/F(N*N), psi_interval(x))

def correction_derivative_interval(b):
    b=F(b)
    lb=log2_interval(b*b)
    bracket=add(add(lb,INV_LN2),(F(-16),F(-16)))
    return scale(2*ALPHA*b,bracket)

def dec(x,digits=30):
    getcontext().prec=digits+20
    return format(Decimal(x.numerator)/Decimal(x.denominator),f'.{digits}f')

def main():
    assert sum(m for _,_,m in CLASSES)==512
    assert sum(F(m*q*q,N*N) for _,q,m in CLASSES)==ALPHA

    # Analytic monotonicity reduction used by the theorem.
    max_abs=F(0)
    for a,q,m in CLASSES:
        if q==0 or (a,q,m)==SPECIAL:
            continue
        for b in (F(1,4),F(1)):
            max_abs=max(max_abs,abs(F(a)+b*F(q)))
    assert max_abs==44

    # Special class x=114+2b >= 229/2.  N^2/x^2<20, whereas
    # e > sum_{k=0}^5 1/k! = 163/60 and (163/60)^3>20.
    assert F(N*N,1) / (F(229,2)**2) < 20
    e_lower=F(163,60)
    assert e_lower**3 > 20

    segments=[(F(1,4),F(1,2)),(F(1,2),F(3,4)),(F(3,4),F(1))]
    print('PASS')
    print('class_count=19')
    print('multiplicity_sum=512')
    print('sum_q2_over_512sq='+str(ALPHA))
    print('nonspecial_max_abs_x='+str(max_abs))
    for j,(lo,hi) in enumerate(segments,1):
        h=(F(0),F(0))
        for a,q,m in CLASSES:
            if q==0:
                continue
            # Every nonspecial class derivative increases with b; the special
            # one decreases.  This endpoint choice is therefore a rigorous
            # classwise upper bound on the whole segment.
            b=lo if (a,q,m)==SPECIAL else hi
            h=add(h,class_derivative_interval(a,q,m,b))
        c=correction_derivative_interval(lo)  # correction derivative decreases
        total=add(h,c)
        assert total[1] < 0
        print(f'segment_{j}=[{lo},{hi}]')
        print('  Hcore_prime_upper='+dec(h[1],36))
        print('  correction_prime_upper='+dec(c[1],36))
        print('  K_prime_upper='+dec(total[1],36))
    print('GLOBAL_CONCLUSION=K_prime_strictly_negative_on_[1/4,1]')

if __name__=='__main__':
    main()
