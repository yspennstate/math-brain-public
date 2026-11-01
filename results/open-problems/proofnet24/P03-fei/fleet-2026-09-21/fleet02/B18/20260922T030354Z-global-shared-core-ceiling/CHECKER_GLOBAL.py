from fractions import Fraction as F
from functools import lru_cache
from decimal import Decimal, getcontext
import math

TERMS = 80
N = 512
ALPHA = F(9,256)
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
    z=(x-1)/(x+1); z2=z*z; power=z; s=F(0)
    for k in range(terms):
        s += power/(2*k+1); power *= z2
    lo=2*s
    rem=2*power/((2*terms+1)*(1-z2))
    return lo,lo+rem

LN2_LO,LN2_HI=log_unit_interval(F(2))
INV_LN2=(1/LN2_HI,1/LN2_LO)

@lru_cache(maxsize=None)
def log2_interval(x):
    x=F(x); assert x>0
    if x<1:
        lo,hi=log2_interval(1/x); return -hi,-lo
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x < F(2)**e: e -= 1
    m=x/F(2)**e
    a,b=log_unit_interval(m)
    return F(e)+a/LN2_HI, F(e)+b/LN2_LO

def add(I,J): return I[0]+J[0],I[1]+J[1]
def scale(c,I):
    c=F(c)
    return (c*I[0],c*I[1]) if c>=0 else (c*I[1],c*I[0])

def psi_interval(x):
    x=F(x)
    if x==0: return F(0),F(0)
    return scale(-x,add(log2_interval(x*x/F(N*N)),INV_LN2))

def class_derivative_interval(a,q,m,b):
    a,q,b=F(a),F(q),F(b)
    return scale(F(2*m)*q/F(N*N),psi_interval(a+b*q))

def hcore_derivative_interval(b):
    ans=(F(0),F(0))
    for a,q,m in CLASSES:
        if q: ans=add(ans,class_derivative_interval(a,q,m,b))
    return ans

def correction_derivative_interval(b):
    b=F(b)
    if b==0: return F(0),F(0)
    bracket=add(add(log2_interval(b*b),INV_LN2),(F(-16),F(-16)))
    return scale(2*ALPHA*b,bracket)

def dec(x,digits=36):
    getcontext().prec=digits+20
    return format(Decimal(x.numerator)/Decimal(x.denominator),f'.{digits}f')

def main():
    assert sum(m for _,_,m in CLASSES)==512
    assert sum(F(m*q*q,N*N) for _,q,m in CLASSES)==ALPHA

    max_abs_neg=max(abs(F(a)+b*F(q)) for a,q,m in CLASSES if q for b in (F(-1),F(0)))
    assert max_abs_neg==114
    e_partial=sum(F(1,math.factorial(k)) for k in range(7))
    e_upper=e_partial+F(1,4410)
    assert e_upper < F(68,25)
    assert F(N*N,114*114) > F(68,25)**3

    max_abs_pos=max(abs(F(a)+b*F(q)) for a,q,m in CLASSES if q and (a,q,m)!=SPECIAL for b in (F(1,4),F(1)))
    assert max_abs_pos==44
    assert F(N*N,44*44) > 27
    assert F(N*N,1)/(F(229,2)**2) < 20
    e_lower=F(163,60)
    assert e_lower**3 > 20

    print('PASS')
    print('class_count=19')
    print('multiplicity_sum=512')
    print('sum_q2_over_512sq='+str(ALPHA))
    print('negative_side_max_abs_x='+str(max_abs_neg))
    print('positive_side_nonspecial_max_abs_x='+str(max_abs_pos))

    neg_segments=[
        (F(-1),F(-3,4)),(F(-3,4),F(-1,2)),(F(-1,2),F(-1,4)),
        (F(-1,4),F(-1,8)),(F(-1,8),F(-1,16)),(F(-1,16),F(-1,32)),
        (F(-1,32),F(-1,64)),(F(-1,64),F(-1,128))]
    for j,(lo,hi) in enumerate(neg_segments,1):
        total=add(hcore_derivative_interval(lo),correction_derivative_interval(hi))
        assert total[0] > 0
        print(f'negative_segment_{j}=[{lo},{hi}]')
        print('  K_prime_lower='+dec(total[0]))
    hnear=hcore_derivative_interval(F(-1,128))
    assert hnear[0]>0
    print('negative_segment_9=[-1/128,0]')
    print('  Hcore_prime_lower='+dec(hnear[0]))
    print('  correction_prime_lower=0')
    print('  K_prime_lower='+dec(hnear[0]))

    pos_segments=[(F(1,4),F(1,2)),(F(1,2),F(3,4)),(F(3,4),F(1))]
    for j,(lo,hi) in enumerate(pos_segments,1):
        h=(F(0),F(0))
        for a,q,m in CLASSES:
            if not q: continue
            b=lo if (a,q,m)==SPECIAL else hi
            h=add(h,class_derivative_interval(a,q,m,b))
        c=correction_derivative_interval(lo)
        total=add(h,c)
        assert total[1]<0
        print(f'positive_segment_{j}=[{lo},{hi}]')
        print('  Hcore_prime_upper='+dec(h[1]))
        print('  correction_prime_upper='+dec(c[1]))
        print('  K_prime_upper='+dec(total[1]))
    print('GLOBAL_CONCLUSION=K_increases_on_[-1,0]_and_decreases_on_[1/4,1]')

if __name__=='__main__': main()
