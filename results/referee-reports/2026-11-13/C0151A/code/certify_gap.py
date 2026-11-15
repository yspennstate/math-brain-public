"""Rational interval certificate for a degree-1000 gap.

No floating point arithmetic in assertions. Logs use the atanh power series
with a proved geometric tail; square roots use integer square roots.
"""
from fractions import Fraction as F
from math import isqrt
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
import json

class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = self.lo if hi is None else F(hi)
        assert self.lo <= self.hi
    @staticmethod
    def cast(x): return x if isinstance(x, I) else I(x)
    def __add__(self, other):
        b=self.cast(other); return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self, other): return self+-self.cast(other)
    def __rsub__(self, other): return self.cast(other)+-self
    def __mul__(self, other):
        b=self.cast(other); p=[x*y for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self, other):
        b=self.cast(other); assert b.lo*b.hi>0
        return self*I(1/b.hi,1/b.lo)
    def sqrt(self):
        assert self.lo>=0
        scale=10**35
        def floor(x): return F(isqrt(x.numerator*scale*scale//x.denominator),scale)
        return I(floor(self.lo),floor(self.hi)+F(1,scale))
    def strings(self):
        def dec(x, rounding):
            with localcontext() as ctx:
                ctx.prec=24;ctx.rounding=rounding
                return str(Decimal(x.numerator)/Decimal(x.denominator))
        return [dec(self.lo,ROUND_FLOOR),dec(self.hi,ROUND_CEILING)]

def log_between_one_two(x):
    assert 1<=x<=2
    z=(x-1)/(x+1); z2=z*z; term=z; total=F(0); n=65
    for j in range(n):
        total+=2*term/(2*j+1); term*=z2
    return I(total,total+2*term/((2*n+1)*(1-z2)))

LOG2=log_between_one_two(F(2))
def logq(x):
    x=F(x); assert x>0
    k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    return log_between_one_two(x)+k*LOG2

def log(x):
    x=I.cast(x)
    return I(logq(x.lo).lo, logq(x.hi).hi)

def h(x):
    x=I.cast(x)
    if x.lo==x.hi==0:return I(0)
    return -x*log(x)

def phi(d,a):
    a=I.cast(a)
    return h(a)+F(d,2)*h(1-2*a)-(d-1)*h(1-a)

def pair_rate(d,a,b):
    a,b=I.cast(a),I.cast(b)
    t=F(1,2)-a
    c=(t*t+(a-b)*(a-b)).sqrt()-t
    return F(d,2)*(2*h(b)+2*h(c)+4*h(a-b-c)+h(1-4*a+2*b+2*c))-(d-1)*(h(b)+2*h(a-b)+h(1-2*a+b))

def main():
    d=1000; a=F('0.0106');b=F('0.005')
    # Theorem 1.3: alpha* >= alpha_FM - epsilon_d.
    # Unique positive root alpha_FM > .0109, because phi(.0109)>0.
    ph=phi(d,F('0.0109')); assert ph.lo>0
    # e > sum_{k=0}^9 1/k! > 2.71828, using its positive series.
    fact=1; esum=F(1)
    for k in range(1,10):fact*=k;esum+=F(1,fact)
    assert esum>F('2.71828')
    eps=4*(2*logq(d)).sqrt()/(I(d)*I(d).sqrt()*I(esum))
    assert eps.hi<F('0.000174')
    lower=I('0.0109')-eps
    assert lower.lo>F('0.0107')
    assert a*a<b<a
    rate=pair_rate(d,a,b)
    assert rate.hi<F('-0.0005')
    # Thinning rules out every FIID density >= a, not just density a.
    out=dict(d=d,FIID_forbidden_at_or_above=str(a),beta=str(b),
             phi_at_0_0109=ph.strings(),epsilon_upper_interval=eps.strings(),
             alpha_star_lower_interval=lower.strings(),pair_rate=rate.strings(),
             conclusion='sup_FIID <= 0.0106 < 0.0107 < alpha_star',
             method='exact Fraction intervals, 65-term log series, 35-place sqrt bounds')
    dest=Path(__file__).resolve().parents[1]/'data'/'gap_certificate.json'
    dest.parent.mkdir(exist_ok=True);dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
