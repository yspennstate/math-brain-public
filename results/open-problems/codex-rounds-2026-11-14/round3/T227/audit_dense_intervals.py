"""Second exact audit: literal Euclidean-coordinate interval computations.

Square widths make sqrt(m) rational. This checks the bound calculations by
directly summing every gradient coordinate, without width-cancelled formulas.
It supports the general-width proof; finite tested widths are not that proof.
"""
import json
import math
import os
import resource
import time
from fractions import Fraction as Q

resource.setrlimit(resource.RLIMIT_CPU, (120,120))
started=time.monotonic()
assert os.getpriority(os.PRIO_PROCESS,0)>=15

class I:
    def __init__(self,lo,hi=None):
        self.lo,self.hi=Q(lo),Q(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,y):
        if not isinstance(y,I): y=I(y)
        return I(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,y):
        if not isinstance(y,I): y=I(y)
        return self+-y
    def __rsub__(self,y): return -self+y
    def __mul__(self,y):
        if not isinstance(y,I): y=I(y)
        endpoints=[x*z for x in (self.lo,self.hi) for z in (y.lo,y.hi)]
        return I(min(endpoints),max(endpoints))
    __rmul__=__mul__
    def __truediv__(self,y):
        y=Q(y)
        assert y>0
        return I(self.lo/y,self.hi/y)
    def square(self):
        return I(0 if self.lo<=0<=self.hi else min(self.lo**2,self.hi**2),max(self.lo**2,self.hi**2))
    def absmax(self): return max(abs(self.lo),abs(self.hi))
    def pair(self): return [float(self.lo),float(self.hi)]

def exp_reduced(x):
    power=1
    while x>Q(1,8):
        x/=2
        power*=2
    term=total=Q(1)
    for k in range(1,13):
        term=term*x/k
        total+=term
    upper=total+term*x/13/(1-x/14)
    return total**power,upper**power

def tanh_positive(x):
    lo,hi=exp_reduced(2*x)
    lo,hi=(lo-1)/(lo+1),(hi-1)/(hi+1)
    scale=10**12
    # Outward rational rounding prevents huge denominators from entering
    # nested nonlinearities, and preserves rigorous containment.
    return I(Q((lo*scale).__floor__(),scale),Q((hi*scale).__ceil__(),scale))

def tanh_interval(x):
    assert x.lo>0
    return I(tanh_positive(x.lo).lo,tanh_positive(x.hi).hi)

def gradients(a,B,r,u,v,q,n):
    m=n*n
    ga=[x/m for x in v]
    gB=[[a[i]*q[i]*u[j]/(m*n) for j in range(m)] for i in range(m)]
    gc=[r[j]*sum((a[i]*q[i]*B[i][j] for i in range(m)),I(0))/(m*n) for j in range(m)]
    return ga,gB,gc

def flatgrad(ga,gB,gc): return ga+[x for row in gB for x in row]+gc

rows=[]
eps=Q('1e-10')
S=Q('1.1')*Q('6.6')/(1-Q(1,8))
for n in (1,2,3,8):
    m=n*n
    a=[I('7.99','8.01') for _ in range(m)]
    B=[[I(Q('.499')/n,Q('.501')/n) for _ in range(m)] for _ in range(m)]
    c=[I('1.999','2.001') for _ in range(m)]
    u=[tanh_interval(x) for x in c]
    r=[1-x.square() for x in u]
    z=[sum((b*x for b,x in zip(row,u)),I(0))/n for row in B]
    v=[tanh_interval(x) for x in z]
    q=[1-x.square() for x in v]
    F=sum((x*y for x,y in zip(a,v)),I(0))/m
    ga,gB,gc=gradients(a,B,r,u,v,q,n)
    kernel=m*sum((g.square() for g in flatgrad(ga,gB,gc)),I(0))
    eta=m*I('.9','1.1')
    a1=[x-eta*F*g for x,g in zip(a,ga)]
    B1=[[x-eta*F*g for x,g in zip(row,grow)] for row,grow in zip(B,gB)]
    c1=[x-eta*F*g for x,g in zip(c,gc)]
    W1=[n*x for row in B1 for x in row]
    assert all(x.lo>Q('6.2') and x.hi<Q('6.6') for x in a1)
    assert all(x.lo>-25 and x.hi<-19 for x in W1)
    assert all(x.lo>Q('1.07') for x in c1)
    assert kernel.lo>37 and kernel.hi<39
    assert (F.square()/2).hi<Q('6.5')

    # Independent intervals for two arbitrary tail states. Each factor
    # of a product may take either endpoint. Unlike a squared-norm bound,
    # the cross-gradient bound must include negative hidden contributions.
    ta=[I(-16,16) for _ in range(m)]
    tB=[[I(Q(-26,n),Q(-18,n)) for _ in range(m)] for _ in range(m)]
    tr=[I(0,1) for _ in range(m)]
    tu=[I(Q(3,4),1) for _ in range(m)]
    tv=[I(-1,-1+eps) for _ in range(m)]
    tq=[I(0,eps) for _ in range(m)]
    tga,tgB,tgc=gradients(ta,tB,tr,tu,tv,tq,n)
    gs=flatgrad(tga,tgB,tgc)
    cross=m*sum((g*g for g in gs),I(0))
    assert cross.lo>1-Q('1e-8') and cross.hi<1+Q('1e-8')
    da=m*S*max(g.absmax() for g in tga)
    dW=n*m*S*max(g.absmax() for row in tgB for g in row)
    dc=m*S*max(g.absmax() for g in tgc)
    assert Q('6.6')+da<16
    assert -25-dW>-26 and -19+dW<-18
    assert Q('1.07')-dc>1
    rows.append(dict(width=m,m_kernel0=kernel.pair(),a1=a1[0].pair(),
                     W1=W1[0].pair(),c1=c1[0].pair(),tail_cross=cross.pair(),
                     tail_movements=list(map(float,(da,dW,dc)))))

summary=dict(status='PASS',checked_widths=[r['width'] for r in rows],
             direct_interval_bounds=rows,process_nice=os.getpriority(os.PRIO_PROCESS,0),
             max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
             seconds=time.monotonic()-started)
assert summary['max_rss_bytes']<1_000_000_000
with open('interval_audit.json','w') as f:
    json.dump(summary,f,indent=2)
print(json.dumps(summary,indent=2))
