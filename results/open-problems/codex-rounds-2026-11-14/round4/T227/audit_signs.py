"""Second certificate: binomial-limit exponentials and signed extrema.

No imports from either verification script. All enclosures are rational.
The exponential bracket uses (1+x/n)^n <= exp(x) <= (1-x/n)^(-n),
with outward rounding after each squaring. This is independent of Taylor
series certification. Also checks the exact binomial tail by integer sums.
"""
import json
import math
import os
import resource
import time
from fractions import Fraction as Q

resource.setrlimit(resource.RLIMIT_CPU,(120,120))
started=time.monotonic()
assert os.environ['OMP_NUM_THREADS']=='1'
assert os.getpriority(os.PRIO_PROCESS,0)>=15
scale=10**25

def down(x): return Q((x*scale).__floor__(),scale)
def up(x): return Q((x*scale).__ceil__(),scale)

class I:
    def __init__(self,lo,hi=None):
        self.lo,self.hi=Q(lo),Q(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,y):
        if not isinstance(y,I): y=I(y)
        return I(down(self.lo+y.lo),up(self.hi+y.hi))
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,y): return self+-as_i(y)
    def __rsub__(self,y): return as_i(y)+-self
    def __mul__(self,y):
        y=as_i(y)
        xs=[a*b for a in (self.lo,self.hi) for b in (y.lo,y.hi)]
        return I(down(min(xs)),up(max(xs)))
    __rmul__=__mul__
    def __truediv__(self,y):
        y=Q(y)
        assert y>0
        return I(down(self.lo/y),up(self.hi/y))
    def square(self):
        lo=0 if self.lo<=0<=self.hi else min(self.lo**2,self.hi**2)
        return I(down(lo),up(max(self.lo**2,self.hi**2)))
    def absmax(self): return max(abs(self.lo),abs(self.hi))
    def pair(self): return [float(self.lo),float(self.hi)]

def as_i(x): return x if isinstance(x,I) else I(x)

def exp_binomial(x):
    n=2**30
    assert 0<=x<n
    lo=down(1+x/n)
    hi=up(1/(1-x/n))
    for _ in range(30):
        lo=down(lo*lo)
        hi=up(hi*hi)
    return lo,hi

def tanh_point(x):
    lo,hi=exp_binomial(2*x)
    return I(down((lo-1)/(lo+1)),up((hi-1)/(hi+1)))

def tanh_i(x):
    assert x.lo>=0
    return I(tanh_point(x.lo).lo,tanh_point(x.hi).hi)

# Direct signed extrema over all row/column sign proportions on E_m.
# A positive fraction p lies in [.725,.775]. For positive independent
# factor bounds X in [l,h], extrema of mean(S*U*X) are attained by
# putting X at opposite endpoints on positive and negative coordinates.
def signed_mean(x):
    return I(Q('.725')*Q('.999')*x.lo-Q('.275')*Q('1.001')*x.hi,
             Q('.775')*Q('1.001')*x.hi-Q('.225')*Q('.999')*x.lo)

a=I('7.99','8.01')
c=I('1.999','2.001')
u=tanh_i(c)
z=signed_mean(u)
v=tanh_i(z)
r=1-u.square()
q=1-v.square()
k=a*q
D=k*u
C=r*signed_mean(k)
F=a*v
h=I('.9','1.1')
a1=a-h*F*v
W1=I('-1.001','1.001')-h*F*D
c1=c-h*F*C
mk=v.square()+D.square()+C.square()
assert u.lo>Q('.96395') and u.hi<Q('.96410')
assert v.lo>Q('.407') and v.hi<Q('.487')
assert a1.lo>Q('5.8') and a1.hi<Q('6.9')
assert W1.lo>-29 and W1.hi<-16 and c1.lo>Q('.84')
assert mk.lo>34 and mk.hi<43 and (F.square()/2).hi<8
assert tanh_point(Q('.8')).lo>Q('.66')
assert 4/exp_binomial(Q('19.8'))[0]<Q('2e-8')
assert exp_binomial(Q(25))[0]>40_000_000_000

# Sum the literal Euclidean gradients in small square widths, keeping B
# as the coordinate. A cyclic negative block makes column counts match
# row counts. This is a second check of the metric, not the general proof.
metric=[]
eps=Q('2e-8')
for n in (2,10):
    m=n*n
    for count in sorted({math.ceil(m*Q('.225')),m//4,math.floor(m*Q('.275'))}):
        if not Q('.45')<=1-Q(2*count,m)<=Q('.55'):
            continue
        signs=[[(-1 if (j-i)%m<count else 1) for j in range(m)] for i in range(m)]
        B=[[I(Q('.999')/n,Q('1.001')/n) if s==1 else I(-Q('1.001')/n,-Q('.999')/n) for s in row] for row in signs]
        zz=[sum((b*u for b in row),I(0))/n for row in B]
        vv=[tanh_i(zi) for zi in zz]
        qq=[1-vi.square() for vi in vv]
        ga=[vi/m for vi in vv]
        gB=[[a*qq[i]*u/(m*n) for _ in range(m)] for i in range(m)]
        gc=[r*sum((a*qq[i]*B[i][j] for i in range(m)),I(0))/(m*n) for j in range(m)]
        actual_kernel=m*sum((g.square() for g in ga+[x for row in gB for x in row]+gc),I(0))
        assert actual_kernel.lo>34 and actual_kernel.hi<43
        # Two arbitrary tail gradients: interval multiplication retains
        # potentially negative hidden-coordinate products.
        ta=I(-18,18)
        tu=I('.66',1)
        tq=I(0,eps)
        tv=I(-1,-1+eps)
        tb=I(-Q(30,n),-Q(15,n))
        tgA=tv/m
        tgB=ta*tq*tu/(m*n)
        tgC=I(0,1)*(m*ta*tq*tb)/(m*n)
        tail_cross=m*(m*tgA*tgA+m*m*tgB*tgB+m*tgC*tgC)
        assert tail_cross.lo>1-Q('1e-6') and tail_cross.hi<1+Q('1e-6')
        S=Q('1.1')*Q('6.9')/(1-Q(1,8))
        movements=[m*S*tgA.absmax(),n*m*S*tgB.absmax(),m*S*tgC.absmax()]
        assert Q('6.9')+movements[0]<18
        assert -29-movements[1]>-30 and -16+movements[1]<-15
        assert Q('.84')-movements[2]>Q('.8')
        assert max(1-Q('.9')*tail_cross.lo,Q('1.1')*tail_cross.hi-1)<Q(1,8)
        metric.append(dict(width=m,negative_count=count,m_kernel0=actual_kernel.pair(),
                           tail_cross=tail_cross.pair(),tail_coordinate_movements=list(map(float,movements))))

# Exact binomial tails at m=20,000. All terms have denominator 4^m.
# K has success probability 3/4; bad event is K<14500 or K>15500.
m=20000
t=1
lower=0
for k0 in range(14500):
    lower+=t
    numerator=t*(m-k0)*3
    assert numerator%(k0+1)==0
    t=numerator//(k0+1)
t=3**m
upper=0
for j in range(4500):
    upper+=t
    numerator=t*(m-j)
    assert numerator%(3*(j+1))==0
    t=numerator//(3*(j+1))
bad_row=Q(lower+upper,4**m)
exact_union=2*m*bad_row
assert exact_union<Q('2e-6')
assert Q('5.8')**2*(1-eps)/2>16

# Explicit failures of weakened deterministic hypotheses.
def initial_update(signs,h):
    m=len(signs)
    aa,cc=8.,2.
    uu=math.tanh(cc)
    vv=[math.tanh(uu*sum(row)/m) for row in signs]
    kk=[aa/math.cosh(uu*sum(row)/m)**2 for row in signs]
    ff=aa*sum(vv)/m
    Cj=[(1-uu*uu)*sum(kk[i]*signs[i][j] for i in range(m))/m for j in range(m)]
    return ff,min(cc-h*ff*x for x in Cj)

row_only=[[(-1 if j<10 else 1) for j in range(40)] for i in range(40)]
fr,cr=initial_update(row_only,1.1)
assert all(sum(row)/40==.5 for row in row_only)
assert cr<.84
row_u=tanh_point(Q(2))
row_v=tanh_i(row_u/2)
row_c1=2-Q('1.1')*(8*row_v)*(1-row_u.square())*(8*(1-row_v.square()))
assert row_c1.lo<Q(cr)<row_c1.hi<Q('.22')
# Centered support contains an exact zero-residual state. This is not a
# probabilistic obstruction to a centered-law theorem; it invalidates a
# blanket deterministic claim for every signed matrix.
balanced=[[(-1 if j<20 else 1) for j in range(40)] for i in range(40)]
fz,cz=initial_update(balanced,1.1)
assert fz==0 and cz==2

summary=dict(status='PASS',method='binomial-limit exponential brackets; direct signed extrema',
             all_event_intervals=dict(u=u.pair(),z=z.pair(),v=v.pair(),C=C.pair(),
                                      a1=a1.pair(),W1=W1.pair(),c1=c1.pair(),m_kernel0=mk.pair()),
             literal_metric_audits=metric,
             exact_binomial_union_at_20000=float(exact_union),
             exact_binomial_numerator_bits=exact_union.numerator.bit_length(),
             exact_binomial_denominator_bits=exact_union.denominator.bit_length(),
             row_only_counterexample=dict(F0=fr,min_c1=cr,rational_c1_interval=row_c1.pair()),
             balanced_zero_residual=dict(F0=fz,min_c1=cz),
             nice=os.getpriority(os.PRIO_PROCESS,0),
             max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
             seconds=time.monotonic()-started)
assert summary['max_rss_bytes']<1_000_000_000
with open('signed_audit.json','w') as f:
    json.dump(summary,f,indent=2)
print(json.dumps(summary,indent=2))
