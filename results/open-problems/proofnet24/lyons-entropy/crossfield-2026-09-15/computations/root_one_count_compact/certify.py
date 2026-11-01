"""Outward fixed-point integer intervals for the remaining one-count square.

Every interval endpoint is an integer divided by SCALE. No binary floating
point or external transcendental implementation enters a sign certificate.
"""
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from functools import lru_cache
import json
import time
from pathlib import Path

SCALE = 10**24

def ceildiv(a, b):
    return -((-a)//b)

@dataclass(frozen=True)
class I:
    lo: int
    hi: int

    @staticmethod
    def rational(x):
        x = Fraction(x)
        return I(x.numerator*SCALE//x.denominator,
                 ceildiv(x.numerator*SCALE, x.denominator))

    def __add__(self, other):
        other = as_i(other)
        return I(self.lo+other.lo, self.hi+other.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + (-as_i(other))
    def __rsub__(self, other):
        return as_i(other) + (-self)
    def __mul__(self, other):
        other = as_i(other)
        p = [self.lo*other.lo, self.lo*other.hi,
             self.hi*other.lo, self.hi*other.hi]
        return I(min(p)//SCALE, ceildiv(max(p),SCALE))
    __rmul__ = __mul__
    def reciprocal(self):
        assert self.lo > 0 or self.hi < 0
        return I(SCALE*SCALE//self.hi, ceildiv(SCALE*SCALE,self.lo))
    def __truediv__(self, other):
        other = as_i(other)
        assert other.lo > 0 or other.hi < 0
        quotients = [Fraction(a*SCALE,b) for a in (self.lo,self.hi)
                     for b in (other.lo,other.hi)]
        low,high=min(quotients),max(quotients)
        return I(low.numerator//low.denominator,
                 ceildiv(high.numerator,high.denominator))
    def __rtruediv__(self, other):
        return as_i(other)/self
    def square(self):
        vals = [self.lo*self.lo, self.hi*self.hi]
        low = 0 if self.lo <= 0 <= self.hi else min(vals)
        return I(low//SCALE, ceildiv(max(vals),SCALE))
    def sqrt(self):
        assert self.lo >= 0
        low = isqrt(self.lo*SCALE)
        high = isqrt(self.hi*SCALE)
        if high*high < self.hi*SCALE:
            high += 1
        return I(low,high)

def as_i(x):
    return x if isinstance(x,I) else I.rational(x)

@lru_cache(maxsize=None)
def exp_point(n):
    # Used only for nonnegative arguments. Reduce to x<=1/2.
    assert n >= 0
    halves = 0
    while n > SCALE*(2**halves)//2:
        halves += 1
    x = I(n//(2**halves),ceildiv(n,2**halves))
    term = as_i(1)
    total = term
    for k in range(1,33):
        term = term*x/k
        total = total+term
    next_term = term*x/33
    # Subsequent term ratios are at most x/34.
    tail = next_term/(1-x/34)
    total = I(total.lo,total.hi+tail.hi)
    for _ in range(halves):
        total = total.square()
    return total

def exp_interval(x):
    assert x.lo >= 0
    return I(exp_point(x.lo).lo,exp_point(x.hi).hi)

def log_unit(x):
    # 1<=x<=2. Positive atanh series and its geometric tail.
    assert x.lo >= SCALE and x.hi <= 2*SCALE
    z=(x-1)/(x+1)
    zz=z.square()
    term=z
    total=as_i(0)
    for k in range(40):
        total=total+2*term/(2*k+1)
        term=term*zz
    tail=2*term/(81*(1-zz))
    return I(total.lo,total.hi+tail.hi)

LOG2=log_unit(as_i(2))

@lru_cache(maxsize=None)
def log_point(n):
    assert n>0
    # Exact rational normalization n/SCALE = 2^k * numerator/denominator.
    num,den,k=n,SCALE,0
    while num>=2*den:
        den*=2
        k+=1
    while num<den:
        num*=2
        k-=1
    x=I(num*SCALE//den,ceildiv(num*SCALE,den))
    # Rounding can hit the endpoints, but cannot escape [1,2].
    return log_unit(x)+k*LOG2

def log_interval(x):
    assert x.lo>0
    return I(log_point(x.lo).lo,log_point(x.hi).hi)

def hyperbolic(x):
    e=exp_interval(2*x)
    low,high=I(e.lo,e.lo),I(e.hi,e.hi)
    # tanh increases and sech squared decreases on the nonnegative axis.
    r=I(((low-1)/(low+1)).lo,((high-1)/(high+1)).hi)
    a=I((4*high/(high+1).square()).lo,
        (4*low/(low+1).square()).hi)
    return r,a

def matrix_box(rl,rh,sl,sh):
    R=I(I.rational(rl).lo,I.rational(rh).hi)
    S=I(I.rational(sl).lo,I.rational(sh).hi)
    r,a=hyperbolic(R)
    s,b=hyperbolic(S)
    rr,ss=r.square(),s.square()
    c=a+b-a*b
    if min(a.lo,b.lo,c.lo)<=0:
        return None
    k=log_interval(c/(a*b))/2
    rs=r*s
    if (1-rs).lo<=0:
        return None
    P=log_interval((1+rs)/(1-rs))/2
    t11=R+s*P
    t12=S-s*k
    # Keep the large-R cancellation inside a logarithm.
    h=log_interval(1+r)-log_interval(1+a*ss/b)/2
    t21=(1-r)*R+r*h
    t22=S+r*P
    rootab=(a*b).sqrt()
    m11=2+2*a*ss/c-a*(t11.square()+t12.square())
    m22=2+2*b*rr/c-b*(t21.square()+t22.square())
    m12=rootab*(2/c-2*k-t11*t21-t12*t22)
    det=m11*m22-m12.square()
    return m11,m22,m12,det

def encode_box(box):
    return [str(x) for x in box]

def run(max_boxes=200000):
    started=time.monotonic()
    todo=[(Fraction(2,3),Fraction(14),Fraction(1,5),Fraction(5))]
    accepted=[]
    skipped=0
    examined=0
    while todo:
        box=todo.pop()
        rl,rh,sl,sh=box
        # Only the ordered compact region S<=R<=2S+4 is needed.
        if rh<sl or rl>2*sh+4:
            skipped+=1
            continue
        examined+=1
        result=matrix_box(*box)
        if result is not None and result[0].lo>0 and result[3].lo>0:
            accepted.append({'box':encode_box(box),
                             'm11_lower':str(result[0].lo),
                             'det_lower':str(result[3].lo)})
        else:
            if max(rh-rl,sh-sl)<Fraction(1,10**15):
                raise ArithmeticError('Unresolved microscopic box: '+str(encode_box(box)))
            if examined>=max_boxes:
                out={'status':'INCOMPLETE','examined':examined,
                     'accepted':len(accepted),'pending':len(todo)+1,
                     'box':encode_box(box),'seconds':time.monotonic()-started}
                print(json.dumps(out),flush=True)
                return out
            if rh-rl>=sh-sl:
                mid=(rl+rh)/2
                todo.extend([(rl,mid,sl,sh),(mid,rh,sl,sh)])
            else:
                mid=(sl+sh)/2
                todo.extend([(rl,rh,sl,mid),(rl,rh,mid,sh)])
        if examined%10000==0:
            print(json.dumps({'progress':examined,'accepted':len(accepted),
                              'pending':len(todo),'seconds':time.monotonic()-started}),flush=True)
    out={'status':'PASS','scale':str(SCALE),'initial_box':['2/3','14','1/5','5'],
         'domain':'S<=R<=2*S+4','examined':examined,'accepted':len(accepted),
         'skipped':skipped,'seconds':time.monotonic()-started,
         'leaves':accepted}
    path=Path(__file__).with_name('certificate.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='leaves'}),flush=True)
    return out

if __name__=='__main__':
    run()
