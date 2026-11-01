"""Exact integer outward interval arithmetic for the proposed saddle certificate.

Not itself a saddle certificate. Only rational integer operations and integer square
root are trusted primitives; atan/asin/pi use proved identities and remainder bounds.
"""
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from math import isqrt
from pathlib import Path

BITS=160
S=1<<BITS

def ceildiv(a,b):
    return -((-a)//b)

@dataclass(frozen=True,slots=True)
class I:
    lo:int
    hi:int
    def __post_init__(self):
        if type(self.lo) is not int or type(self.hi) is not int:
            raise TypeError("interval endpoints must be integers")
        if self.lo>self.hi: raise ValueError('reversed interval')
    @staticmethod
    def of(x):
        if isinstance(x,I): return x
        if isinstance(x,int): return I(x*S,x*S)
        if isinstance(x,str): x=Fraction(x)
        if isinstance(x,Fraction): return I(x.numerator*S//x.denominator,ceildiv(x.numerator*S,x.denominator))
        raise TypeError('Use an explicit exact integer, decimal string, or Fraction; floats are not exact constants')
    def __add__(self,other):
        b=I.of(other); return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,other): return self+-I.of(other)
    def __rsub__(self,other): return I.of(other)+-self
    def __mul__(self,other):
        b=I.of(other)
        p=[a*c for a in (self.lo,self.hi) for c in (b.lo,b.hi)]
        return I(min(p)//S,ceildiv(max(p),S))
    __rmul__=__mul__
    def __truediv__(self,other):
        b=I.of(other)
        if b.lo<=0<=b.hi: raise ZeroDivisionError('interval denominator contains zero')
        lower=[a*S//c for a in (self.lo,self.hi) for c in (b.lo,b.hi)]
        upper=[ceildiv(a*S,c) for a in (self.lo,self.hi) for c in (b.lo,b.hi)]
        return I(min(lower),max(upper))
    def __rtruediv__(self,other): return I.of(other)/self
    def square(self):
        if self.lo<=0<=self.hi: return I(0,ceildiv(max(self.lo*self.lo,self.hi*self.hi),S))
        a,b=self.lo*self.lo,self.hi*self.hi
        return I(min(a,b)//S,ceildiv(max(a,b),S))
    def sqrt(self):
        if self.lo<0: raise ValueError('sqrt has a negative lower endpoint')
        lower=isqrt(self.lo*S)
        target=self.hi*S
        upper=isqrt(target)
        if upper*upper<target: upper+=1
        return I(lower,upper)
    def maxabs(self): return max(abs(self.lo),abs(self.hi))
    def contains(self,x):
        x=Fraction(x)
        return self.lo*x.denominator<=x.numerator*S<=self.hi*x.denominator
    def positive(self): return self.lo>0
    def negative(self): return self.hi<0
    def mid_float(self):
        # Diagnostics/preconditioner choice only; never a certificate endpoint.
        return (self.lo+self.hi)/(2*S)
    def record(self):
        return {'lower_numerator':str(self.lo),'upper_numerator':str(self.hi),'denominator':str(S),
                'midpoint_diagnostic':self.mid_float()}
    def atan(self):
        low=_atan_point(self.lo)
        high=_atan_point(self.hi)
        return I(low.lo,high.hi)
    def asin(self):
        if self.lo<=-S or self.hi>=S: raise ValueError('asin requires a strict subinterval of (-1,1)')
        low=_asin_point(self.lo)
        high=_asin_point(self.hi)
        return I(low.lo,high.hi)

def _atan_small(x):
    if x.lo<0 or x.hi>S//5: raise ValueError('atan series domain')
    total=I.of(0)
    power=x
    x2=x.square()
    for n in range(600):
        term=power/(2*n+1)
        total=total+term if n%2==0 else total-term
        power=power*x2
        next_term=power/(2*n+3)
        if next_term.hi<=2:
            remainder=I(0,next_term.hi)
            # The sign of the alternating remainder is (-1)^(n+1), and its
            # magnitude is at most x^(2n+3)/(2n+3), by the geometric remainder.
            return total-remainder if n%2==0 else total+remainder
    raise ArithmeticError('atan series failed to reach its proved remainder bound')

def _atan_positive(x):
    if x.lo<0: raise ValueError('positive atan domain')
    factor=1
    for _ in range(256):
        if x.hi<=S//5: return factor*_atan_small(x)
        # tan(2 atan(t))=x for t=x/(1+sqrt(1+x^2)); principal angles stay positive.
        x=x/(1+(1+x.square()).sqrt())
        factor*=2
    raise ArithmeticError('atan half-angle reduction failed')

def _atan_point(raw):
    return -_atan_positive(I(-raw,-raw)) if raw<0 else _atan_positive(I(raw,raw))

def _asin_point(raw):
    if raw<0: return -_asin_point(-raw)
    if raw>=S: raise ValueError('asin endpoint outside domain')
    x=I(raw,raw)
    return _atan_positive(x/(1-x.square()).sqrt())

@lru_cache(maxsize=1)
def pi():
    # Machin: pi=16 atan(1/5)-4 atan(1/239). The rational tangent of the
    # quarter-angle expression is 1, and that expression lies in (0,pi/2).
    return 16*(I.of(1)/5).atan()-4*(I.of(1)/239).atan()

def self_test():
    checks=0
    for a in range(-24,25):
        for b in range(-12,13):
            if not b: continue
            exact=Fraction(a,b)
            q=a//b; c=ceildiv(a,b)
            assert Fraction(q)<=exact<=Fraction(c)
            checks+=1
    values=[Fraction(-7,3),Fraction(-2,11),Fraction(0),Fraction(1,3),Fraction(5,7)]
    for a in values:
        for b in values:
            x,y=I.of(a),I.of(b)
            assert (x+y).contains(a+b)
            assert (x-y).contains(a-b)
            assert (x*y).contains(a*b)
            if b: assert (x/y).contains(a/b)
            checks+=1
    root=I.of(2).sqrt()
    assert root.lo*root.lo<=2*S*S<=root.hi*root.hi
    assert I(-S,S).square()==I(0,S)
    p=pi()
    # A separate known decimal prefix is a sanity check, not the proof of pi's enclosure.
    low=I.of('3.1415926535897932384626433832795028841971')
    high=I.of('3.1415926535897932384626433832795028841972')
    assert low.lo<=p.lo<=p.hi<=high.hi
    a=(I.of(1)/2).asin()
    p6=p/6
    assert max(a.lo,p6.lo)<=min(a.hi,p6.hi)
    assert (a-p6).maxabs()<S//(10**40)
    assert (I.of('0.7').atan()+I.of('-0.7').atan()).contains(0)
    return {'passed':True,'bits':BITS,'exact_rational_cases':checks,'pi':p.record(),
            'asin_one_half':a.record(),'scope':'Interval primitive checks only; no saddle or eta interval certified',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    import os
    if os.name=='nt':
        import ctypes
        k=ctypes.WinDLL('kernel32')
        k.GetCurrentProcess.restype=ctypes.c_void_p
        k.SetPriorityClass.argtypes=[ctypes.c_void_p,ctypes.c_uint]
        k.SetPriorityClass(k.GetCurrentProcess(),0x4000)
    result=self_test()
    (Path(__file__).parent.parent/'logs/iv_exact_self_test.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2),flush=True)
